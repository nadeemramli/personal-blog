import { FullSlug } from "./path"
import { QuartzPluginData } from "../plugins/vfile"

export interface ArticleLinkResult {
  slug: FullSlug
  title: string
}

/**
 * Returns the sorted list of sibling articles in the same immediate folder,
 * excluding folder index pages. Sorted A-Z by slug (matches Obsidian order).
 *
 * All sort/filter logic for article ordering lives here.
 * To change ordering (e.g. by date or a frontmatter `order` field),
 * edit the sort comparator below — no other files need to change.
 */
function getSortedSiblings(
  currentSlug: FullSlug,
  allFiles: QuartzPluginData[],
): { siblings: QuartzPluginData[]; currentIndex: number } {
  const segments = currentSlug.split("/")

  if (segments.length <= 1) return { siblings: [], currentIndex: -1 }

  const folderPath = segments.slice(0, -1).join("/")

  const siblings = allFiles
    .filter((f) => {
      if (!f.slug) return false
      const fSegments = f.slug.split("/")
      if (fSegments.length <= 1) return false
      if (fSegments[fSegments.length - 1] === "index") return false
      const fFolder = fSegments.slice(0, -1).join("/")
      return fFolder === folderPath
    })
    .sort((a, b) => a.slug!.localeCompare(b.slug!))

  const currentIndex = siblings.findIndex((f) => f.slug === currentSlug)
  return { siblings, currentIndex }
}

/** Returns the next article in the same folder (A-Z), or null if last. */
export function getNextArticle(
  currentSlug: FullSlug,
  allFiles: QuartzPluginData[],
): ArticleLinkResult | null {
  const { siblings, currentIndex } = getSortedSiblings(currentSlug, allFiles)
  if (currentIndex === -1 || currentIndex >= siblings.length - 1) return null

  const next = siblings[currentIndex + 1]
  return { slug: next.slug!, title: next.frontmatter?.title ?? "Untitled" }
}

/** Returns the previous article in the same folder (A-Z), or null if first. */
export function getPreviousArticle(
  currentSlug: FullSlug,
  allFiles: QuartzPluginData[],
): ArticleLinkResult | null {
  const { siblings, currentIndex } = getSortedSiblings(currentSlug, allFiles)
  if (currentIndex <= 0) return null

  const prev = siblings[currentIndex - 1]
  return { slug: prev.slug!, title: prev.frontmatter?.title ?? "Untitled" }
}

/**
 * Returns the folder index slug for linking back to the section listing.
 * e.g. "1.-Karangan/1.-Pendek/2.-Life/Peace" → "1.-Karangan/1.-Pendek/2.-Life/index"
 */
export function getFolderSlug(slug: FullSlug): FullSlug | null {
  const segments = slug.split("/")
  if (segments.length <= 1) return null
  return (segments.slice(0, -1).join("/") + "/index") as FullSlug
}
