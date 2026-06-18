#!/usr/bin/env python3
"""Build per-product Purchase Log sections from the PO ledger.

Usage:
    python os_purchase_logs.py "<Operating System path>"          # audit only
    python os_purchase_logs.py "<Operating System path>" --apply  # rewrite notes

The script is deliberately conservative. Direct PO wikilinks and the explicit
vendor-name map below are authoritative. Fuzzy matching is only accepted when
one candidate is clearly stronger than every other candidate.
"""

from __future__ import annotations

import argparse
import difflib
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

NON_PRODUCT_ROWS = {
    "flat rate shipping",
    "order level vouchers coins",
    "shipping",
    "shipping cost nov 2025 to april 2026",
    "shipping protection",
    "shop voucher",
    "subtotal",
    "total usd",
    "vigorous discount 10",
    "worldwide intl post 15 20 days",
    "your products",
    "your total",
}

# Vendor listing names and historical labels that are not safely inferable.
ITEM_TO_PRODUCT = {
    "99 ru58841 raw powder": "ru58841-99pct-raw-powder-lazada",
    "acarbose tablet": "acarbose-50mgx100tab-shopee-china",
    "anastrolin": "anastrozole-anastrolin-kohohpharma",
    "aspirin": "aspirin-100mgx60tab-shopee-china",
    "bcp tretinoin 0 025 cream 500g": "tretinoin-0-025pct-cream-bcp-500g-shopee",
    "clenbuterlin": "clenbuterol-40mcgx100tab-kohohpharma",
    "cytolin": "cytolin-25mcgx100tab-kohohpharma",
    "ell cranel alpha 0 025 topical": "ell-cranel-alpha-0-025pct-alfatradiol-100ml-shopee",
    "equibolone": "boldenone-undecanoate-250mg-ml-x10ml-kohohpharma",
    "ethanol 99 1l": "ethanol-99pct-carrier-1000ml-lazada",
    "gw501516": "cardarine-gw-501516-10mgx50tab-kohohpharma",
    "glycore tretinoin 0 1 moisturizer": "tretinoin-0-1pct-moisturizer-glycore-shopee",
    "indapamide": "indapamide-2-5mgx60tab-shopee-china",
    "irbesartan": "irbesartan-150mgx120tab-shopee-china",
    "lctc and minoxidil 5": "topical-minoxidil-5pct-plus-lctc-lazada",
    "levothyroxine sodium tablet": "levothyroxine-t4-50mcgx100tab-shopee-china",
    "minoxidil 5mg zontron hirsutin": "minoxidil-5mg-zontron-hirsutin-100tab-lazada",
    "mk677": "mk-677-10mgx50tab-kohohpharma",
    "nipro sterile insulin syringe": "insulin-syringe-30g-nipro-100pcs-shopee",
    "nizoral": "nizoral-ketoconazole-1pct-200ml-shopee",
    "nutricost acetyl l carnitine 500 mg 180 caps": "acetyl-l-carnitine-500mgx180tab-iherb",
    "nutricost magnesium 240 capsules 210 mg": "magnesium-glycinate-210mgx240tab-iherb",
    "nutricost p 5 p 240 capsules": "p5p-pyridoxal-5-phosphate-50mgx240cap-iherb",
    "nutricost tmg 750 mg 120 capsules": "tmg-betaine-750mgx120tab-iherb",
    "nutricost uridine 60 caps 300 mg": "uridine-monophosphate-300mgx60tab-iherb",
    "onthego pure protein isolate 1kg": "on-the-go-protein-isolate-otg-1000g-shopee",
    "oxandroline": "oxandrolone-anavar-10mgx100tab-kohohpharma",
    "oxandrolin": "oxandrolone-anavar-10mgx100tab-kohohpharma",
    "provilin": "proviron-25mgx50tab-kohohpharma",
    "pure creatine monohydrate": "creatine-monohydrate-1000g-shopee",
    "pure soy protein isolate hk spi": "spi-soy-protein-isolate-hk-1000g-shopee",
    "propylene glycol usp 1kg": "propylene-glycol-usp-carrier-1000g-lazada",
    "rosuvastatin": "rosuvastatin-10mgx28tab-shopee-china",
    "life extension bioactive b complex 60 caps": "methyl-b-complex-250mgx60tab-iherb",
    "tadalafil": "tadalafil-10mgx100tab-shopee-china",
    "testolone c": "testosterone-enanthate-cypionate-250mg-ml-x10ml-kohohpharma",
    "trazodone": "trazodone-50mgx40tab-shopee",
}

SPECIAL_EVENTS = {
    "copper-bisglycinate-2mgx100tab-iherb": [
        {
            "date": "2026-06-08",
            "event": "Gift",
            "source": "Personal gift",
            "change": "+200 mg acquired",
            "usage": "-",
            "note": "No purchase order required",
        }
    ],
    "glycerol-1000g-shopee": [
        {
            "date": "2026-07",
            "event": "Planned purchase",
            "source": "PO pending",
            "change": "+5 L planned",
            "usage": "-",
            "note": "Budget RM54; vendor and exact July date pending",
        },
        {
            "date": "2026-06-08",
            "event": "Gift",
            "source": "Personal gift",
            "change": "Current quantity not recorded",
            "usage": "-",
            "note": "No purchase order required",
        },
    ],
}


@dataclass
class Product:
    path: Path
    data: dict
    text: str

    @property
    def product_id(self) -> str:
        return str(self.data.get("product_id") or "")

    @property
    def filename(self) -> str:
        return self.path.stem


@dataclass
class Purchase:
    date: str
    po_name: str
    vendor: str
    item: str
    qty: str
    unit_cost: str
    total_cost: str
    remark: str


def norm(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = text.replace("×", "x").replace("—", " ").replace("–", " ")
    text = re.sub(r"\[\[([^]|]+)\|?([^]]*)\]\]", r"\1 \2", text)
    text = re.sub(r"[^a-zA-Z0-9]+", " ", text).lower()
    return re.sub(r"\s+", " ", text).strip()


def compact(value: object) -> str:
    return norm(value).replace(" ", "")


def frontmatter(text: str) -> dict:
    match = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    if not match:
        return {}
    data: dict[str, object] = {}
    active_list: str | None = None
    for line in match.group(1).splitlines():
        list_item = re.match(r"^\s+-\s+(.*)$", line)
        if list_item and active_list:
            value = list_item.group(1).strip().strip("\"'")
            current = data.setdefault(active_list, [])
            if isinstance(current, list):
                current.append(value)
            continue
        field = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not field:
            active_list = None
            continue
        key, raw = field.group(1), field.group(2).strip()
        if raw == "":
            data[key] = []
            active_list = key
            continue
        active_list = None
        value = raw.strip("\"'")
        if value.lower() in {"true", "false"}:
            data[key] = value.lower() == "true"
        elif re.fullmatch(r"-?\d+", value):
            data[key] = int(value)
        elif re.fullmatch(r"-?\d+\.\d+", value):
            data[key] = float(value)
        else:
            data[key] = value
    return data


def load_products(stock_dir: Path) -> list[Product]:
    products = []
    for path in sorted(stock_dir.rglob("*.md")):
        if path.name.startswith("0."):
            continue
        text = path.read_text(encoding="utf-8", errors="surrogateescape")
        data = frontmatter(text)
        if data.get("type") == "product":
            products.append(Product(path, data, text))
    return products


def parse_po(path: Path) -> list[Purchase]:
    text = path.read_text(encoding="utf-8", errors="surrogateescape")
    data = frontmatter(text)
    date = str(data.get("date") or "")
    vendor = str(data.get("vendor") or "")
    rows = []
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Item"):
            continue
        protected = re.sub(
            r"\[\[.*?\]\]",
            lambda match: match.group(0).replace("|", "<WIKILINK_PIPE>").replace("\\<WIKILINK_PIPE>", "<WIKILINK_PIPE>"),
            line,
        )
        cells = [
            cell.replace("<WIKILINK_PIPE>", "|").strip()
            for cell in protected.strip().strip("|").split("|")
        ]
        if len(cells) < 4 or "TOTAL" in cells[0].upper():
            continue
        item_key = norm(cells[0].replace("**", ""))
        if (
            item_key in NON_PRODUCT_ROWS
            or item_key.startswith("shipping ")
            or item_key.startswith("subtotal ")
            or item_key.startswith("vigorous discount ")
        ):
            continue
        while len(cells) < 5:
            cells.append("")
        rows.append(
            Purchase(
                date=date,
                po_name=path.stem,
                vendor=vendor,
                item=cells[0],
                qty=cells[1],
                unit_cost=cells[2],
                total_cost=cells[3],
                remark=cells[4],
            )
        )
    return rows


def direct_link_target(item: str) -> str | None:
    match = re.search(r"\[\[([^]|]+)(?:\|[^]]+)?\]\]", item.replace("\\|", "|"))
    return Path(match.group(1)).name if match else None


def product_terms(product: Product) -> list[str]:
    values = [
        product.filename.split(" — ")[0],
        product.data.get("compound"),
        product.data.get("name"),
    ]
    values.extend(product.data.get("aliases") or [])
    return sorted({norm(v) for v in values if norm(v)}, key=len, reverse=True)


def fuzzy_match(purchase: Purchase, products: list[Product]) -> Product | None:
    item = norm(purchase.item)
    item_compact = compact(purchase.item)
    purchase_vendor = norm(purchase.vendor)
    scored = []
    for product in products:
        product_vendors = {
            norm(product.data.get("vendor")),
            norm(product.data.get("source")),
        }
        if purchase_vendor not in product_vendors:
            continue
        best = 0.0
        for term in product_terms(product):
            term_compact = term.replace(" ", "")
            if len(term_compact) >= 4 and term_compact in item_compact:
                score = 0.92 + min(len(term_compact), 30) / 1000
            else:
                score = difflib.SequenceMatcher(None, item, term).ratio()
                item_tokens, term_tokens = set(item.split()), set(term.split())
                if term_tokens:
                    score = max(score, len(item_tokens & term_tokens) / len(term_tokens))
            best = max(best, score)
        scored.append((best, product))
    scored.sort(key=lambda row: row[0], reverse=True)
    if not scored:
        return None
    top = scored[0]
    runner_up = scored[1][0] if len(scored) > 1 else 0
    if top[0] >= 0.90 and top[0] - runner_up >= 0.05:
        return top[1]
    return None


def match_purchase(
    purchase: Purchase,
    products: list[Product],
    by_filename: dict[str, Product],
    by_id: dict[str, Product],
) -> Product | None:
    target = direct_link_target(purchase.item)
    if target and target in by_filename:
        return by_filename[target]
    explicit = ITEM_TO_PRODUCT.get(norm(purchase.item)) or ITEM_TO_PRODUCT.get(compact(purchase.item))
    if explicit:
        return by_id.get(explicit)
    return fuzzy_match(purchase, products)


def display_number(value: object) -> str:
    if value is None or value == "" or isinstance(value, (list, dict)):
        return "unknown"
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def purchase_change(purchase: Purchase, product: Product) -> str:
    delta_text = " ".join([purchase.remark, purchase.total_cost]).replace("\\|", "|").strip()
    explicit = re.search(r"([+-][\d,]+(?:\.\d+)?)\s*([A-Za-z]+)?", delta_text)
    if explicit:
        unit = explicit.group(2) or product.data.get("dose_unit") or product.data.get("size_unit") or ""
        return f"{explicit.group(1)} {unit}".strip()
    qty_match = re.search(r"[\d.]+", purchase.qty.replace(",", ""))
    qty = float(qty_match.group()) if qty_match else None
    package = product.data.get("package_size")
    base_dose = product.data.get("base_dose")
    size_unit = str(product.data.get("size_unit") or "")
    dose_unit = product.data.get("dose_unit") or ""
    if qty is not None and isinstance(package, (int, float)):
        normalized_size_unit = norm(size_unit)
        count_units = {"tab", "tabs", "cap", "caps", "capsule", "capsules", "softgel", "softgels"}
        if normalized_size_unit in count_units and isinstance(base_dose, (int, float)):
            amount = qty * float(package) * float(base_dose)
            return f"+{display_number(amount)} {dose_unit} purchased"
        if normalized_size_unit == "ml" and isinstance(base_dose, (int, float)) and dose_unit in {"mg", "mcg"}:
            amount = qty * float(package) * float(base_dose)
            return f"+{display_number(amount)} {dose_unit} purchased"
        amount = qty * float(package)
        return f"+{display_number(amount)} {size_unit} purchased".strip()
    return f"{purchase.qty or '1'} package(s) purchased"


def plain_item_label(item: str) -> str:
    text = item.replace("\\|", "|")
    text = re.sub(r"\[\[([^]|]+)\|([^]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^]]+)\]\]", r"\1", text)
    return text.replace("|", "/")


def usage_summary(product: Product) -> str:
    dose = display_number(product.data.get("daily_dose"))
    unit = product.data.get("dose_unit") or product.data.get("size_unit") or ""
    dosing = product.data.get("dosing") or "manual"
    if dose == "unknown":
        return f"usage not quantified; schedule {dosing}"
    return f"{dose} {unit}/{dosing}".strip()


def build_section(product: Product, purchases: list[Purchase]) -> str:
    stock_as_of = str(product.data.get("stock_as_of") or "date unknown")
    stock = display_number(product.data.get("stock_on_hand"))
    stock_unit = product.data.get("dose_unit") or product.data.get("size_unit") or "units"
    runout = product.data.get("runout_forecast")
    snapshot_note = "Latest recorded aggregate balance"
    if runout:
        snapshot_note += f"; forecast empty {runout}"

    rows = [
        "## Purchase Log",
        "",
        "> [!note] Stock is currently an aggregate balance, not a lot-level FIFO ledger. "
        "PO rows prove acquisition; exact surviving lots require a physical count or depletion entry.",
        "",
        "| Date | Event | PO / source | Change or balance | Usage at update | Note |",
        "|---|---|---|---|---|---|",
    ]

    special_events = SPECIAL_EVENTS.get(product.product_id, [])
    for event in special_events:
        if event["date"] > stock_as_of:
            rows.append(
                f"| {event['date']} | {event['event']} | {event['source']} | {event['change']} | "
                f"{event['usage']} | {event['note']} |"
            )

    rows.append(
        f"| {stock_as_of} | Stock update | Manual/model snapshot | {stock} {stock_unit} on hand | "
        f"{usage_summary(product)} | {snapshot_note} |"
    )

    for purchase in sorted(purchases, key=lambda row: (row.date, row.po_name), reverse=True):
        cost = purchase.total_cost.replace("**", "").strip()
        note_parts = [plain_item_label(purchase.item)]
        if cost:
            note_parts.append(f"line total {cost}")
        if purchase.remark:
            note_parts.append(purchase.remark.replace("\\|", "|"))
        note = "; ".join(note_parts).replace("|", "/")
        rows.append(
            f"| {purchase.date} | Purchase | [[{purchase.po_name}]] | "
            f"{purchase_change(purchase, product)} | - | {note} |"
        )

    for event in special_events:
        if event["date"] <= stock_as_of:
            rows.append(
                f"| {event['date']} | {event['event']} | {event['source']} | {event['change']} | "
                f"{event['usage']} | {event['note']} |"
            )

    if not purchases and not special_events:
        if str(product.data.get("stack") or "") == "Peptides":
            source = "INDEXA / peptide source record"
            note = "No personal PO expected; INDEXA-funded stock"
        else:
            source = "[[0. Reconciliation — Gaps]]"
            note = "No matching PO found; purchase provenance requires backfill"
        rows.append(
            f"| {stock_as_of} | Provenance gap | {source} | No PO-linked acquisition | - | {note} |"
        )

    rows.extend(
        [
            "",
            "> Append future events newest-first: `Purchase`, `Stock check`, `Usage change`, "
            "or `Depletion`. Every stock check must also update `stock_on_hand` and `stock_as_of`.",
        ]
    )
    return "\n".join(rows)


def replace_section(text: str, section: str) -> str:
    pattern = re.compile(r"\n## Purchase Log\n.*?(?=\n## |\Z)", re.S)
    if pattern.search(text):
        return pattern.sub("\n" + section + "\n", text).rstrip() + "\n"
    links = re.search(r"\n## Links\n", text)
    if links:
        return text[: links.start()] + "\n\n" + section + "\n" + text[links.start() + 1 :]
    return text.rstrip() + "\n\n" + section + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("os_path", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    products = load_products(args.os_path / "2. Catalog" / "Products" / "Stock")
    by_filename = {product.filename: product for product in products}
    by_id = {product.product_id: product for product in products}
    mapped: dict[str, list[Purchase]] = {product.product_id: [] for product in products}
    unmatched = []

    po_dir = args.os_path / "4. Management" / "Purchase Orders"
    for po_path in sorted(po_dir.glob("PO *.md")):
        for purchase in parse_po(po_path):
            product = match_purchase(purchase, products, by_filename, by_id)
            if product:
                mapped[product.product_id].append(purchase)
            else:
                unmatched.append(purchase)

    changed = 0
    with_po = 0
    with_special = 0
    for product in products:
        purchases = mapped[product.product_id]
        with_po += bool(purchases)
        with_special += bool(SPECIAL_EVENTS.get(product.product_id)) and not bool(purchases)
        updated = replace_section(product.text, build_section(product, purchases))
        if updated != product.text:
            changed += 1
            if args.apply:
                product.path.write_text(updated, encoding="utf-8", errors="surrogateescape")

    print(f"stock products: {len(products)}")
    print(f"products with matched POs: {with_po}")
    print(f"products with gift/planned provenance only: {with_special}")
    print(f"products with provenance gaps: {len(products) - with_po - with_special}")
    for product in products:
        if not mapped[product.product_id] and not SPECIAL_EVENTS.get(product.product_id):
            print(f"  GAP | {product.product_id}")
    print(f"notes needing rewrite: {changed}")
    print(f"unmatched PO product-like rows: {len(unmatched)}")
    for purchase in unmatched:
        print(f"  {purchase.date} | {purchase.vendor} | {purchase.item}")
    print("mode:", "APPLIED" if args.apply else "AUDIT ONLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
