---
title: "In My Academic Era
"
aliases:
  - In My Academic Era
created: 2026-09-05
modified: 2026-09-05
tags:
  - obsidian
  - publish
  - zotero
---


All files can be found in this Github Repo: [GitHub - heidiwwang/academicera: Various templates and scripts to support me in my academic era · GitHub](https://github.com/heidiwwang/academicera)

## Disclaimers

Note that AI (Google Gemini) was used to generate initial templates and scripts that I used. I do then reviewed, test, and customize, but there's always a chance of bugs, issues, or inefficiency in the code that could be improved. Feel free to create an issue in the Github project, but I can't guarantee I will get around to fixing things in a timely way as all templates and scripts are meant to support my personal use only.

The instructions below assume the the reader has a baseline knowledge of how to configure and use the software referenced. While I can provide you some ideas of how I might fix things, I am not able to provide tutorials or troubleshooting. I encourage you to review the existing documentation from the actual software developers and ask for support via their channels.
## Managing Readings and Citations

### Required Software
1. [Zotero](https://www.zotero.org/) (free, open source)
	- plug-in: [Better BibTex for Zotero](https://retorque.re/zotero-better-bibtex/installation/)
2. [Obsidian.md](http://Obsidian.md) (free, open format)
	- plug-ins: [Zotero Integration - Obsidian Plugin](https://community.obsidian.md/plugins/obsidian-zotero-desktop-connector), [Templater - Obsidian Plugin](https://community.obsidian.md/plugins/templater-obsidian), [Dataview - Obsidian Plugin](https://community.obsidian.md/plugins/dataview)

I am using a fairly customized version of Obsidian that is integrated to Zotero for citation/annotation management. I have summarized the purpose of the tools below ​

1. Zotero + the [Better BibTex for Zotero](https://retorque.re/zotero-better-bibtex/installation/) plug-in allows you to import citation information from your university library and direct data entry where unavailable, PDF annotation, and the ability to create customized tags and collections. In the Zotero interface, PDF can be marked up and annotated with a tag or comment. 
<figure>
  <img src="/assets/Pasted image 20260905101049.png" alt="Screenshot of a PDF from Zotero showing highlights on text and a box to add either comment or tags">
  <figcaption>Screenshot of a PDF from Zotero showing highlights on text and a box to add either comment or tags</figcaption>
</figure>

 2. Ensure you have the Templater, Zotero Integration, and Dataview plug-ins set up and configured for your vault set up before proceding to the next step.
 <figure>
  <img src="/assets/Pasted image 20260905102739.png" alt="Screenshot of Zotero Integration settings from my vault">
  <figcaption>Screenshot of Zotero Integration settings from my vault</figcaption>
</figure>

 3. Download the [zotero-template](https://github.com/heidiwwang/academicera/blob/main/zotero-template.md) I shared in my Github project and put it into your template folder. Go into your Zotero Integration plug-in settings and set up an import format connected to the template. Run the Zotero Integration command in Obsidian and locate the document to import from Zotero.
 <img src="/assets/Pasted image 20260905103444.png" alt="Pasted image 20260905103444.png">
 4. **Note**: your output will not look exactly like mine as I have using a customized theme and additional CSS set up (if you would like to replicate this see [[obsidian_customization|My Obsidian Customizations]]). The output using my Zotero Template will include:
	 - YAML properties: Title, Type (e.g. Book Section, article, etc), Tags (any metadata tags), and Concepts (any tags applied to annotations within the PDF file itself, which I use to flag themes/concepts), and authors.
	 - Citation: An `[!info]` blockquote containing the citation in ALA (7th edition) format.
	<figure>
  <img src="/assets/Pasted image 20260905104155.png" alt="Screenshot of Obsidian file generated from a Zotero import with a Info blockquote containing citation information">
  <figcaption>Screenshot of Obsidian file generated from a Zotero import with a Info blockquote containing citation information</figcaption>
</figure>

	- Annotations: Any highlights you made in the PDF document will be pulled in as a `![note]` blockquote surrounded by single quotation marks with page number and any tags as `[[wikilinks]]` in the blockquote title. The wikilinks will automatically connect into your graph if Concept Page (more below) already exists.
<figure>
  <img src="/assets/Pasted image 20260905104501.png" alt="Screenshot of Obsidian file generated from a Zotero import with a Note blockquote containing the text that was highlighted in the PDF">
  <figcaption>Screenshot of Obsidian file generated from a Zotero import with a Note blockquote containing the text that was highlighted in the PDF</figcaption>
</figure>

5. You must have JavaScript enabled in the Dataview settings for the next step to work.
<figure>
  <img src="/assets/Pasted image 20260905105354.png" alt="Screenshot of Obsidian Dataview plug-in setting showing Javascript queries and inline Javascript queries are enabled">
  <figcaption>Screenshot of Obsidian Dataview plug-in setting showing Javascript queries and inline Javascript queries are enabled</figcaption>
</figure>

6. To see every annotation you've made across all readings related to a specific concept, you will need to set up concept pages. The DataviewJS codeblock in the [template_concept-page](https://github.com/heidiwwang/academicera/blob/main/template_concept-page.md) will automatically scan your vault for blockquotes with the tag that matches the **file name** and put into this page. The output will have sections with each reading as the title as a `[[wikilink]]` and only the relevant tagged quotes with the page number. If you have multiple tags, links will be created between multiple concept pages automatically (visualized in the graph on the top right of the screenshot).
 
<figure>
  <img src="/assets/Pasted image 20260905105513.png" alt="Screenshot of Obsidian showing a concept page, DataviewJS output and the connected graph on the top right hand side">
  <figcaption>Screenshot of Obsidian showing a concept page, DataviewJS output and the connected graph on the top right hand side</figcaption>
</figure>

