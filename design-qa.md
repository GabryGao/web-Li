# Design QA — SPAIS Lab site refresh

## Evidence

- Approved visual direction: preserve the existing warm cream and burgundy academic-site style.
- Owner-supplied Home reference: `/Users/fara./Library/Containers/com.tencent.xinWeChat/Data/Documents/xwechat_files/wxid_5dji56bs0chf22_1df1/temp/RWTemp/2026-08/63b1f4a0a1ab5574a8933e81bd9ef27f/d4df6e943905d0577baa88e9cd5f2554.png`
- Supplied brand asset: `/Users/fara./Downloads/logo/SPAIS-Lab.png`
- Implementation Home capture: `/private/tmp/spais-home-desktop.png`
- Implementation About capture: `/private/tmp/spais-about-desktop-fixed.png`
- Implementation Team capture: `/private/tmp/spais-team-roster-desktop.png`
- Implementation Openings capture: `/private/tmp/spais-openings-desktop-ready.png`
- Implementation mobile captures: `/private/tmp/spais-home-mobile.png` and `/private/tmp/spais-team-mobile.png`
- Desktop viewport: `1280 x 720`, light theme.
- Mobile viewport: `390 x 844`, light theme.

## Full-view comparison

The refreshed Home keeps the approved structure from the supplied reference: personal information on the left, portrait/profile card on the right, compact topic tags, and restrained burgundy calls to action. The existing cream background, borders, typography, and spacing system remain in use. The separate duplicate About card was removed, and the verified career summary now fills the previously empty left-side area.

## Focused checks

- Branding: the supplied SPAIS Lab image renders proportionally in desktop and mobile navigation; a visible `SPAIS Lab@PolyU` affiliation line identifies the PolyU lab, and no `XL` monogram remains.
- Home/About separation: Home carries the third-person career history. About carries only a restrained third-person research summary plus the existing verified service and award sections.
- Publications: 51 cards render from the verified Google Scholar membership; existing richer metadata remains intact for matching records.
- Publications resilience: page content is visible without waiting for JavaScript or `IntersectionObserver`; the former all-page transparency failure is covered by a source regression check.
- Team: the roster uses the full content width and renders the five approved English names. Advising text appears only for Shunfa Zhao, Jiahe Chen, and Di Xu.
- Openings: the top-level route renders the existing verified recruiting text and two email actions.
- Responsive behavior: all tested pages reported `scrollWidth == innerWidth` at both `1280` and `390` CSS pixels. The mobile navigation opens and exposes all seven routes.
- Runtime: no browser console errors were observed on Home, About, Publications, Team, or Openings.

## Comparison history

1. Initial build failed because the repository's Sass version interpreted CSS `min(13rem, 100%)` as incompatible arithmetic. Replaced it with equivalent `width` and `max-width` declarations.
2. Initial About render exposed Markdown heading markers (`## About`) because this layout did not parse those headings as expected. Replaced the headings with explicit semantic HTML and recaptured the page.
3. Desktop and mobile rechecks found no horizontal overflow, clipped navigation, or unresolved page-transition state.
4. A user browser showed only the Publications navbar because `.fade-in-section` defaulted the entire page to `opacity: 0`. The page wrapper now defaults to visible, and the rebuilt local page renders all 51 cards immediately.

## Findings

- No actionable P0, P1, or P2 visual issues remain.
- The logo is intentionally scaled down from the supplied high-resolution source; its aspect ratio is preserved.
- Scholar-only publication records retain Scholar's visible abbreviated author and venue strings instead of inventing fuller metadata.

final result: passed
