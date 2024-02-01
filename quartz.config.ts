import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "Bro Cuba Menulis",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    baseUrl: "nadeemramli.com",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "created",
    theme: {
      typography: {
        header: "Poppins",
        body: "Poppins",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f8",
          lightgray: "#ADBAC7", 
          gray: "#1C2128",
          darkgray: "#1C2128",
          dark: "#1D1C28",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "#rgba(143, 159, 169, 0.15)",
        },
        darkMode: {
          light: "#1C2128",
          lightgray: "#313A46",
          gray: "#FFFFFF",
          darkgray: "#ADBAC7",
          dark: "#FFFFFF",
          secondary: "#ADC7C7",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.TableOfContents(),
      Plugin.CreatedModifiedDate({
        // you can add 'git' here for last modified from Git
        // if you do rely on git for dates, ensure defaultDateType is 'modified'
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.Latex({ renderEngine: "katex" }),
      Plugin.SyntaxHighlighting(),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources({ fontOrigin: "googleFonts" }),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
