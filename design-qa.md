# Design QA — Xinfeng Li academic profile

## Evidence

- Source visual truth: `https://chenyangsi.top/index.html`
- Source desktop capture: `/private/tmp/xinfeng-source-desktop-1280.png`
- Implementation desktop capture: `/private/tmp/xinfeng-local-desktop-1280.png`
- Desktop side-by-side comparison: `/private/tmp/xinfeng-design-comparison-desktop.png`
- Source mobile capture: `/private/tmp/xinfeng-source-mobile.png`
- Implementation mobile capture: `/private/tmp/xinfeng-local-mobile.png`
- Mobile side-by-side comparison: `/private/tmp/xinfeng-design-comparison-mobile.png`
- Desktop viewport/state: `1280 x 720`, light theme, homepage at top.
- Desktop source/implementation pixels: `1280 x 720` each. CSS viewport: `1280 x 720`; browser DPR reported `2`; screenshots were already normalized to CSS pixel dimensions.
- Mobile viewport/state: `390 x 844`, light theme, homepage at top with menu closed.
- Mobile source/implementation pixels: `390 x 844` each. CSS viewport: `390 x 844`; DPR `1`.

## Full-view comparison

The implementation preserves the reference site's core composition: compact white navigation, prominent identity block, left-aligned academic information, portrait on the right at desktop, and a single-column mobile hero. It intentionally adapts the reference's dark purple hero and serif display face into a lighter PolyU-oriented AI-safety identity while retaining the same information hierarchy.

## Focused comparison

The mobile comparison is the focused hero/navigation check. At `390 x 844`, the lockup, hamburger, title, affiliation, topic chips, actions, and portrait remain readable without horizontal overflow. The menu was also opened and closed successfully in the browser.

## Required fidelity surfaces

- Fonts and typography: The reference uses a serif display face; the implementation intentionally uses DM Sans for a more technical, contemporary profile. Hierarchy, line height, weights, wrapping, and small-label tracking remain consistent and readable.
- Spacing and layout rhythm: Desktop hero columns align cleanly and the tightened hero now transitions to About within the next viewport. Mobile spacing is compact enough for the core identity and primary actions to appear before the portrait.
- Colors and visual tokens: The deep reference purple is translated into a light lavender field, dark navy text, and focused violet accents. Contrast remains strong in both light and tested dark states.
- Image quality and asset fidelity: The implementation uses the verified Xinfeng Li portrait already present in the profile source; its crop is sharp and consistent on desktop and mobile. No reference-site logo, portrait, or decorative asset was copied.
- Copy and content: Biography, research directions, news, publications, affiliations, emails, and links are sourced from the supplied academic homepage and Google Scholar URL. Unverified citation metrics and missing publication links were not invented.

## Comparison history

1. Initial comparison found a P2 vertical-rhythm mismatch: the implementation hero left noticeably more empty space than the reference before the About section. The hero and section padding were reduced; the post-fix desktop capture shows a tighter transition while keeping the portrait card readable.
2. Functional review found a P2 publication-list issue: source ordering could repeat year headings, and a filtered search left empty year labels visible. Publications are now sorted before grouping, and empty year headings are hidden during search. Browser verification with `AudioTrust` returned one card and only the `2026` heading.

## Findings

- No actionable P0, P1, or P2 issues remain.
- Intentional adaptation: the implementation is not a pixel clone. Its light palette, sans-serif display type, card-based portrait, and CTA row distinguish the new profile while preserving the approved reference framework.

## Primary interactions and runtime checks

- Publication search: passed (`AudioTrust` yielded one matching publication and one visible year group).
- Mobile hamburger menu: passed (expanded and collapsed state verified).
- Dark-mode toggle: passed (`data-bs-theme="dark"` observed after click, then restored).
- Browser console warnings/errors: none observed on the tested local pages.

## Follow-up polish

- P3: Citation totals can be added later only after an accessible, verifiable source is available.
- P3: A supplied lab logo could replace the text-based `XL` monogram in a later branding pass.

final result: passed
