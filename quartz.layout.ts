import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import Canvas from "./quartz/components/Canvas"
import NextArticle from "./quartz/components/NextArticle"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [
    NextArticle(),
    Component.MobileOnly(Component.Explorer({
      title: "Explore",
      folderClickBehavior: "collapse",
      folderDefaultState: "collapsed",
      useSavedState: true,
    })),
  ],
  footer: Component.Footer({
    links: {
    },
  }),
}

// Function to determine if current page is a canvas page
const isCanvasPage = (slug: string) => slug.includes("canvases")

// components for pages that display a single page
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
    Canvas(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer()),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer()),
  ],
  right: [],
}

// Get the appropriate layout based on the page type
export function getLayout(slug: string): PageLayout {
  if (isCanvasPage(slug)) {
    return {
      ...defaultContentPageLayout,
      beforeBody: [Component.Breadcrumbs(), Canvas()],
      right: [],
    }
  }
  return defaultContentPageLayout
}
