import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "heidi2",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "heidi2.codeberg.page/",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Karla",
        body: "Karla",
        code: "Victor Mono",
      },
      colors: {
        lightMode: {
          light: "hsla(275, 38%, 98%, 1)",
          lightgray: "hsla(275, 37%, 92%, 1)",
          gray: "hsla(275, 37%, 70%, 1)",
          darkgray: "hsla(275, 28%, 40%, 1)",
          dark: "hsla(275, 54%, 17%, 1)",
          secondary: "hsla(178, 45%, 40%, 1)",
          tertiary: "hsla(178, 39%, 40%, 1)",
          highlight: "hsla(275, 37%, 70%, 0.15)",
          textHighlight: "hsla(42, 89%, 46%, 1)",
        },
        darkMode: {
          light: "hsla(275, 15%, 15%, 1)",
          lightgray: "hsla(275, 15%, 25%, 1)",
          gray: "hsla(275, 15%, 35%, 1)",
          darkgray: "hsla(275, 15%, 70%, 1)",
          dark: "hsla(275, 15%, 90%, 1)",
          secondary: "hsla(178, 55%, 65%, 1)",
          tertiary: "hsla(178, 39%, 40%, 1)",
          highlight: "hsla(275, 50%, 50%, 0.2)",
          textHighlight: "hsla(42, 89%, 46%, 1)",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false , mermaid: true}),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
