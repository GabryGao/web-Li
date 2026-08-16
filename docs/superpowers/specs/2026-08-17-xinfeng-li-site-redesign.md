# Xinfeng Li Academic Website Redesign

## Objective

Redesign the existing Jekyll academic website into a modern AI-safety research homepage while preserving its current build and GitHub Pages deployment. The visual language may take inspiration from `https://chenyangsi.top/index.html`, but its unlicensed source code and assets must not be copied.

## Source Policy

- `https://letterligo.netlify.app/` is the primary factual source for biography, affiliation, research interests, news, publications, professional services, honors, recruiting text, email addresses, and external links.
- `https://scholar.google.com/citations?user=JC_UWyoAAAAJ&hl=en` is a secondary verification source for publications and citation-related metadata.
- Google Scholar metrics are shown only when they can be retrieved and verified. Otherwise they are omitted.
- Missing lab members, grants, funders, teaching, software, talks, institutional address, and official lab naming are not inferred. Sections with no verified content are hidden; a visible `Pending confirmation` marker is used only where the page structure would otherwise be misleading.

## Architecture

Keep the existing Jekyll structure, Liquid layouts, Sass pipeline, `jekyll-scholar`, and GitHub Pages deployment. Content remains in `_data`, `_pages`, and `assets/ref.bib`; presentation remains in `_layouts`, `_includes`, and `_sass`.

The redesign must not replace the project with React, Next.js, or a copied static page.

## Information Architecture

1. **Home**
   - Sticky navigation
   - Hero with verified portrait, name, role, PolyU affiliation, research tagline, email, Scholar, and ResearchGate
   - About section
   - Three verified research-direction cards
   - Recent news timeline
   - Selected publications
   - Recruiting callout

2. **Research**
   - Security and Privacy of Agentic AI Systems
   - Responsible AI in Social Contexts
   - Trustworthy AI for X

3. **Publications**
   - Verified publications grouped by year
   - Title, authors, venue, year, and only source-backed links
   - Search/filter only if supported cleanly by the current architecture

4. **News**
   - Full verified chronology from the primary source

5. **Team**
   - PI profile only
   - Recruiting information from the primary source
   - No invented students, alumni, or lab roster

Professional services and honors are placed on Home or a compact profile section rather than creating empty top-level pages.

## Visual Direction

- Recreate the reference site's overall rhythm with an original implementation: restrained navy/purple palette, generous whitespace, clear section hierarchy, rounded cards, subtle borders and shadows, compact chips, and a prominent recruiting panel.
- Use a readable academic typography pairing and maintain strong contrast.
- Desktop uses a wide centered container and multi-column card sections; mobile collapses to one column with a functional menu and comfortable touch targets.
- Reuse only Xinfeng Li's verified portrait and project-owned assets. Do not hotlink or copy PRLab photography, icons, or illustrations.
- Preserve light/dark mode only if both modes can be made coherent; otherwise prioritize a polished light theme and retain a non-broken dark fallback.

## Content Flow

Verified source content is normalized into Jekyll data files. Layouts render those records without silently generating descriptions or missing metadata. Publication links remain empty when unavailable. Generated `_site` output is never edited directly.

## Failure and Missing-Data Behavior

- Missing optional values are omitted from cards.
- Missing required structural values use `Pending confirmation` / `待确认`, never plausible filler.
- Broken or unverifiable external links are removed or explicitly marked unavailable.
- Scholar throttling must not block the build; the site uses already verified source data and treats Scholar enrichment as optional.

## Verification

- Run the Jekyll production build locally and fix all errors.
- Search the source and rendered site for leftover Feynman/demo identity and unrelated demo content.
- Inspect Home, Publications, News, Research, and Team on desktop and mobile.
- Check navigation, external links, dark mode behavior if retained, and GitHub Pages `baseurl` handling.
- Do not deploy until the local rendered result has been reviewed.

## Non-Goals

- No new lab name unless the source establishes one.
- No invented people, grants, funders, courses, awards, publications, or citation counts.
- No migration away from Jekyll.
- No direct copy of the PRLab repository's unlicensed code or assets.
