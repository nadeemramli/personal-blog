import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { resolveRelative } from "../util/path"
import { getNextArticle, getPreviousArticle, getFolderSlug } from "../util/articleOrder"
import { classNames } from "../util/lang"
import style from "./styles/nextArticle.scss"

export default (() => {
  const NextArticle: QuartzComponent = ({
    fileData,
    allFiles,
    displayClass,
  }: QuartzComponentProps) => {
    const slug = fileData.slug!
    const folderSlug = getFolderSlug(slug)

    // Don't render on root-level pages (index, canvases, etc.)
    if (!folderSlug) return null

    const prev = getPreviousArticle(slug, allFiles)
    const next = getNextArticle(slug, allFiles)

    // If neither prev nor next exists and we're somehow here, show end state
    const hasPrev = prev !== null
    const hasNext = next !== null

    return (
      <nav class={classNames(displayClass, "article-nav")}>
        <div class="article-nav-row">
          {/* Previous — left side */}
          {hasPrev ? (
            <a href={resolveRelative(slug, prev.slug)} class="internal article-nav-card article-nav-prev">
              <span class="article-nav-arrow">←</span>
              <div class="article-nav-text">
                <span class="article-nav-label">Previous</span>
                <span class="article-nav-title">{prev.title}</span>
              </div>
            </a>
          ) : (
            <div class="article-nav-card article-nav-empty" />
          )}

          {/* Next — right side */}
          {hasNext ? (
            <a href={resolveRelative(slug, next.slug)} class="internal article-nav-card article-nav-next">
              <div class="article-nav-text">
                <span class="article-nav-label">Next</span>
                <span class="article-nav-title">{next.title}</span>
              </div>
              <span class="article-nav-arrow">→</span>
            </a>
          ) : (
            <div class="article-nav-card article-nav-empty" />
          )}
        </div>

        {/* End-of-section footer when no next article */}
        {!hasNext && (
          <div class="article-nav-end">
            <span class="article-nav-end-text">You've reached the end of this section</span>
            <a href={resolveRelative(slug, folderSlug)} class="internal article-nav-folder-link">
              ← Browse all in this folder
            </a>
          </div>
        )}
      </nav>
    )
  }

  NextArticle.css = style
  return NextArticle
}) satisfies QuartzComponentConstructor
