# Accessibility Audit

Audit this product's user interface for accessibility against WCAG 2.2 level AA and fix what can be fixed safely. Focus on real barriers for real people: keyboard users, screen reader users, people with low vision or color blindness, people with motor or cognitive impairments, and people using zoom or small screens.

## Settings

- Mode: fix
- Scope: the whole user interface
- Report language: English

`report` mode changes nothing. `fix` mode also applies safe fixes as described under "Changes". Write code and comments in the project's existing language, whatever the report language.

## Working environment

- **With access to the project** (a coding agent such as Claude Code, Codex, Cursor, Gemini CLI or GitHub Copilot): inspect components, styles and templates yourself. If you can run the app and a browser (for example through Playwright or a browser tool), test the rendered pages, not just the source.
- **Without access** (a plain chat): ask me for what you need, most important first: the page URL or HTML, component code for navigation, forms, dialogs and other interactive elements, the design tokens or color palette, and screenshots. Work in `report` mode, give fixes as code, and mark everything you could not see as "Not verified".

## How to work

1. **Identify the UI technology** (web framework, component library, design tokens, native mobile or desktop toolkit) and the **key user flows**: signup, login, onboarding, the main task, checkout or payment, settings and error states. Prioritize those flows.
2. **Run automated checks that are already available**, such as axe, Lighthouse, pa11y, `eslint-plugin-jsx-a11y` or a Storybook accessibility addon. Do not install new tools without approval. Automated tools catch only some of the problems, so always review code and behavior manually too.
3. **Start with shared components** (buttons, links, inputs, dialogs, menus, tabs, toasts, tables): a fix there fixes every page that uses them.
4. **Go through the checklist.** Give every item a result: Pass, Fail, Partial, Not applicable or Not verified.

## Checklist

### Structure and semantics

1. **Semantic HTML**: native elements for their purpose (`button` for actions, `a href` for navigation, lists, tables for tabular data); no clickable `div` or `span` without a role, keyboard support and an accessible name.
2. **Landmarks and headings**: `header`, `nav`, `main` and `footer` landmarks; one `h1` per page; a heading hierarchy that reflects the content.
3. **Page title and language**: unique, descriptive page titles; a `lang` attribute on `html` and on passages in another language.
4. **Correct ARIA**: native elements are preferred over ARIA; roles, states and properties are valid and kept in sync (`aria-expanded`, `aria-selected`, `aria-current`); no `aria-hidden` on focusable content; custom widgets follow the WAI-ARIA Authoring Practices patterns.

### Text alternatives and media

5. **Images**: informative images have alt text that conveys their content or purpose; decorative images have `alt=""`; charts and other complex images have a text alternative; important text is not only inside images.
6. **Icons**: icon-only buttons and links have accessible names; decorative SVG icons are hidden from assistive technology.
7. **Audio and video**: captions for video, transcripts for audio, accessible player controls, and no sound that plays automatically.

### Keyboard and focus

8. **Keyboard access**: everything works with a keyboard alone (Tab, Shift+Tab, Enter, Space, Escape, and arrow keys inside composite widgets).
9. **Visible focus**: every focusable element has a clearly visible focus indicator with at least 3:1 contrast; no `outline: none` without a replacement.
10. **Focus order and management**: tab order is logical (no positive `tabindex`); focus moves into dialogs and returns to the trigger afterwards; focus is trapped only inside modal dialogs; focus is handled sensibly after route changes and deletions; focused elements are not hidden behind sticky headers or cookie banners.
11. **Skip link**: pages with repeated navigation have a link to skip to the main content.
12. **No traps or conflicting shortcuts**: there are no keyboard traps, and single-key shortcuts can be turned off or remapped.

### Visual design

13. **Text contrast**: at least 4.5:1, or 3:1 for large text (at least 24 px, or 18.66 px bold), including placeholder text, text over images or gradients, and dark mode.
14. **Non-text contrast**: input borders, icons and the states of interface components have at least 3:1 contrast.
15. **Not color alone**: errors, required fields, links in running text, chart series and statuses are not distinguished by color alone.
16. **Zoom and reflow**: usable at 200% zoom and at 320 CSS pixels wide without horizontal scrolling (except content such as tables and maps); no fixed heights that cut off text; increased text spacing does not break the layout.
17. **Motion**: `prefers-reduced-motion` is respected; nothing flashes more than three times per second; moving content such as carousels can be paused.
18. **Hover and focus content**: tooltips and popovers can be dismissed, can be hovered, and stay visible until dismissed.

### Forms

19. **Labels**: every input has a visible, programmatically associated label (a placeholder is not a label); related inputs are grouped with `fieldset` and `legend`; required fields are indicated in text.
20. **Errors**: errors are described in text, associated with their field (`aria-describedby`), announced to screen readers (focus moves to the first error or a summary, or a live region is used) and explain how to fix the problem; entered data is kept.
21. **Autocomplete**: personal data fields have correct `autocomplete` values (name, email, address, current or new password, one-time code).
22. **Accessible authentication**: login does not depend on memory or puzzles without an alternative; password managers and pasting work, and there are alternatives to puzzle CAPTCHAs.
23. **Redundant entry and error prevention**: users are not asked again for information they already gave in the same process; legal, financial and data-deleting actions can be reviewed, confirmed or undone.

### Interaction

24. **Target size**: interactive targets are at least 24 by 24 CSS pixels or have enough spacing around them; aim for about 44 to 48 pixels on touch screens.
25. **Dragging and gestures**: anything done by dragging or multi-finger gestures also works with a single tap or click.
26. **Status messages**: loading states, toasts, live search results and cart updates are announced through live regions (`role="status"` or `aria-live`) without moving focus.
27. **Time limits**: users are warned before a session times out and can extend it.
28. **Consistency**: navigation, labels and help options (such as contact or support) are consistent across pages.
29. **Link text**: links make sense out of context (not "click here" or a bare "read more"), and links that open a new window say so.

### Beyond the web page

30. **Documents and emails**: PDFs and HTML emails generated by the product are accessible (tagged PDFs, alt text, readable without images).
31. **Native apps**: platform accessibility APIs are used (labels, traits, content descriptions), text scales with the system font size, screen reader order is logical in VoiceOver and TalkBack, and touch targets are large enough.
32. **Accessibility statement**: if the product's markets require one (for example under EU rules for the public sector or the European Accessibility Act), it exists, is accurate, and offers a way to report barriers.

## Changes (`fix` mode only)

Safe fixes include adding missing alt text when the image content is clear from context (otherwise flag it for a human), labels and accessible names, `lang` attributes, semantic elements in place of clickable `div`s (keeping the styling), visible focus styles, a skip link, ARIA states in custom components, `autocomplete` attributes, live regions, and small contrast fixes through existing design tokens.

Propose, but do not apply, larger redesigns, changes to brand colors, replacement of component libraries, and content rewrites. Do not commit or push. Rerun the relevant tests, linters and automated accessibility checks after the changes.

## Report

1. **Summary**: overall assessment against WCAG 2.2 AA, the most serious barriers, which flows were covered, and how (automated tools, code review, rendered pages, screen reader).
2. **Findings**, most severe first. For each one:
   - The problem, and who is affected
   - WCAG success criterion: number and name
   - Location: component or file, and page
   - Fix
   - Status: Verified, Likely or Needs manual testing
   - Fixed: yes or no
3. **Checklist results**: every item with Pass, Fail, Partial, Not applicable or Not verified. Every item marked Fail or Partial must appear in at least one finding.
4. **Changes made** (`fix` mode) and the checks run afterwards.
5. **Manual test plan**: concrete steps to test the key flows with a keyboard only and with a screen reader (for example VoiceOver on macOS and iOS, NVDA on Windows and TalkBack on Android).

Severity levels:

- **Critical**: prevents a group of users from completing a key task, such as a checkout that cannot be completed by keyboard or a login form that screen readers cannot use.
- **High**: a WCAG A or AA failure on a key flow, or major difficulty.
- **Medium**: a WCAG failure on a secondary page, or significant friction.
- **Low**: minor issues and improvements beyond AA.
