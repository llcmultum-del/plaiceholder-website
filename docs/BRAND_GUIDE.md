# PlAIceholder Brand Guide

Version 1.1 · October 2026 · Taken from the live site, plaiceholder.io (style.css)

## 1. Name

**PlAIceholder**: capital P, lowercase "l", capital **AI**, then lowercase "ceholder".

- The AI in the middle is the point of the name: we fill the places in your week that are waiting for AI.
- Always one word with the AI capitalized. Never "Plaiceholder", "PlaiceHolder", "PLAICEHOLDER" or "Placeholder AI".
- Domain: **plaiceholder.io**, lowercase in URLs and email addresses.
- Legal entity: [Legal entity name, e.g. "Multum LLC d/b/a PlAIceholder"]. Use it in contracts and invoices only.

## 2. Logo

| Version | How it's built | Where |
|---|---|---|
| **Gradient wordmark** (primary) | "PlAIceholder" in weight 800, filled with the brand gradient (blue → sea → green, 135°) | Navigation bar and any white or mint background |
| **White wordmark** | The same, in solid white | Dark navy footer, gradient banners, photos |
| **Icon / favicon** | A gradient circle with a white "A" in weight 800 | Favicon, app icon, social avatar |

Rules:
- The whole word takes the gradient. Don't color the "AI" separately.
- Clear space equals the height of the "A" on every side. Minimum width is 96 px.
- Don't stretch it, add shadows, glows or outlines, use all caps, or put the gradient wordmark on the gradient, a photo or a busy background. Use the white version there.

## 3. Color

### Core palette (CSS variables on the site)

| Token | Hex | Use |
|---|---|---|
| `--blue` Blue | `#1A6EF5` | Primary accent: links, active nav, tier badges, button text on white |
| `--sea` Sea | `#3EC9C9` | Middle of the gradient; borders at 18% |
| `--green` Green | `#2ECC71` | End of the gradient; "ready" badges at 12% |
| `--dark` Navy | `#0D1B2A` | Headings, footer and dark sections, dark buttons |
| `--ink` Ink | `#1A2E20` | Body text (a deep green-black) |
| `--muted` Muted | `#5A7A65` | Secondary text, sub-headlines, area badges |
| `--light` Mint | `#F4FDF8` | Page background |
| White | `#FFFFFF` | Cards, navigation bar, light sections |
| `--border` Border | Sea at 18% (`rgba(62,201,201,.18)`, about `#DCF5F5` on white) | Card, input and filter borders |

### Gradients

| Name | Value | Use |
|---|---|---|
| **Brand gradient** `--grad` | `linear-gradient(135deg, #1A6EF5 0%, #3EC9C9 50%, #2ECC71 100%)` | Hero and page banners (with a faint white dot pattern), primary buttons, the wordmark, icon squares, active filter pill |
| **Dark gradient** `--grad2` | `linear-gradient(135deg, #0D1B2A 0%, #1A3A5C 100%)` | Dark panels and feature blocks |

The hero and page banners lay a 40 px grid of small white dots (7% opacity) over the gradient.

### Badges (pills)

| Badge | Text | Background |
|---|---|---|
| Area (Sales, Back office…) | Muted `#5A7A65` | Mint `#F4FDF8` |
| Tier (Starter, Standard, Advanced) | Blue `#1A6EF5` | Blue at 8% |
| Ready now | Dark green `#1A7A45` | Green at 12% |
| Available | Dark teal `#1A6A6A` | Sea at 10% |

### Contrast rules (WCAG AA)
- **Sea and Green are never text colors** on white or mint (about 2:1). They're for the gradient, tints and borders only.
- **White text on the gradient** only when it's large and bold (headlines, button labels). The green end is too light for small white text.
- **Blue text** passes on white (4.6:1) but is borderline on mint (4.4:1) and on its own 8% tint (4.1:1). For small text there, use weight 700, or a darker blue such as `#1558C7`.
- Ink on mint (13.9:1), Navy on white (17.4:1) and Muted on white (4.8:1) all pass.

### Status colors (agent dashboards only)
The site has no red or amber. For risk levels and severity inside agent dashboards and reports, use Dark green `#1A7A45` (good or low), Amber `#9A6A00` (medium) and Red `#C0392B` (high). These are proposed, not yet on the site, and are kept out of marketing pages.

## 4. Type

| Role | Font | Weight | Size (web) |
|---|---|---|---|
| Hero headline (H1) | Segoe UI / system-ui | 900 (Black) | 2.1 to 3.8 rem, line height 1.12 |
| Page banner H1 | Segoe UI / system-ui | 900 | 2 to 3.1 rem |
| Section headline (H2) | Segoe UI / system-ui | 800 | 1.6 to 2.4 rem, Navy |
| Card title (H3) | Segoe UI / system-ui | 700 | 1 rem |
| Body | Segoe UI / system-ui | 400 | 1 rem, line height 1.65, Ink |
| Eyebrow tag ("PRICING") | Segoe UI / system-ui | 700 | 0.72 rem, uppercase, 0.12em tracking, gradient text |
| Nav links | Segoe UI / system-ui | 500 | 0.88 rem |
| Buttons | Segoe UI / system-ui | 700 | 0.92 rem |

- The stack is `"Segoe UI", system-ui, sans-serif`, so each visitor's system font renders it (Segoe UI on Windows, San Francisco on Mac).
- Office files (Word, PowerPoint) use Segoe UI. On a Mac without it, Office substitutes a similar sans.
- Headlines are heavy (800 to 900) and short; body copy is regular and roomy.

## 5. Shapes and components

| Element | Spec |
|---|---|
| Buttons | Pill (fully rounded), 0.75 rem × 1.75 rem padding, weight 700. Four styles: **gradient** (white text), **white** (blue text, on gradient), **outline** (2 px white, on gradient), **dark** (navy). On hover they lift 2 px |
| Cards | White, 18 px corners, 1 px border in sea at 18%, 1.75 rem padding. On hover they lift 5 px with a soft blue shadow (`0 14px 36px` blue at 10%) |
| Icons | 46 px gradient square with 11 px corners, a single emoji or glyph inside |
| Badges and filters | Pills; the active filter takes the gradient, inactive filters are white with a sea border |
| Navigation | Sticky white bar (97% opacity, blurred), sea-tint bottom border, gradient "Book a Call" pill on the right |
| Sections | Alternate white, mint and navy. 5 rem vertical padding, 1,080 px content width |
| Footer | Navy, white wordmark, muted links, tagline under the logo |

## 6. Positioning and taglines

- **Primary:** "AI agents that do the busywork inside the tools you already use." (footer and taglines)
- **Hero:** "Your team's slowest weekly task, handed to a custom AI agent in two weeks."
- **Hero badge:** "Custom-built AI agents for growing companies"
- **Short:** "Installed. Tuned. Proven."
- **Positioning:** pre-built AI agents that do the busywork inside the tools a growing company already uses. Installed, tuned and proven in about two weeks.

### Proof points (in this order)
1. Works inside HubSpot, Salesforce, Apollo, Zendesk, Slack, QuickBooks and spreadsheets.
2. Works with the AI you already pay for: Claude, ChatGPT, Perplexity, Grok, Gemini or Copilot.
3. A 20-record pilot with a measured result before the full run.
4. Nothing is written or spent without a yes.
5. You own it.

## 7. Voice

Plain, calm, specific: a capable operator, not a hype machine.

| We say | We never say |
|---|---|
| "Built, tested, and running on sample data today." | "Revolutionary AI-powered solutions" |
| "Nothing is written or spent without a yes, one step at a time." | "Fully autonomous, set it and forget it" |
| "Your team sends emails, pays invoices, and makes hiring decisions." | "Replace your team with AI" |
| "Usually a few cents per record. We measure it in your pilot." | "Unlimited AI for one low price!" |

Rules:
- Sentences under 25 words. Lead with the task and the outcome, then the technology.
- Use numbers, names and dates instead of adjectives like "seamless" or "cutting-edge".
- No unmeasured claims: real numbers and quotes only, with client permission.
- Second person ("your team"), active voice, US English.

## 8. Imagery
- Show the product: dashboards, before-and-after tables, the 5-step diagram (Pull, Think, Check, Write back, Show and ask).
- Gradient banners with the dot pattern; emoji or simple glyphs in gradient icon squares.
- No stock robots, glowing brains, circuit boards or people pointing at screens.
- Label sample data: "Sample data. Companies shown are fictional."

## 9. Naming agents
- Pattern: function plus noun ("Signal Prospector", "Renewal Risk Radar", "Invoice Checker").
- No made-up words, no "-ify", no "GPT" in names. Start copy with the job: "Signal Prospector finds…".

## 10. Documents and deliverables
- Title pages: white wordmark on the brand gradient, title in navy or white, date.
- Tables: navy header row with white text, alternating mint rows, a sea-tint grid.
- Every client README ends with "Licensed to [Client] for internal use only. Built by PlAIceholder."
- File names: `client-agent-vN` (e.g. `acme-signal-prospector-v2.zip`).

## 11. Email signature
```
[Founder Name]
Founder, PlAIceholder
AI agents that do the busywork inside the tools you already use.
plaiceholder.io · [Booking Link]
```
