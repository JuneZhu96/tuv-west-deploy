---
name: TÜV Rheinland BS.A West China
description: Professional certification and training brand. Blue-anchored, clean, technical, trustworthy. German engineering rigor expressed through restrained typography, a single authoritative blue, and precise green accents. No gradients, no glass, no AI-template aesthetic.
colors:
  # Source: TÜV Rheinland Standard Color (Pantone → RGB)
  # All values derived from official brand color spec

  # === Blue (Pantone 300) ===
  blue-100: "#0071B9"              # 0·113·185 — Primary brand blue: CTAs, headings, rules, logo
  blue-30: "#BDCEE9"               # 189·206·233 — Tinted backgrounds, table headers
  blue-10: "#EAEEF8"               # 234·238·248 — Subtle card fills, callout boxes

  # === Black ===
  black-100: "#000000"             # 0·0·0 — Body text, headings
  black-30: "#C3C5C7"              # 195·197·199 — Secondary text, captions, metadata
  black-10: "#ECECEC"              # 236·236·236 — Borders, dividers, disabled backgrounds

  # === Green (Pantone 355) ===
  green-100: "#009537"             # 0·149·55 — Success states, structural accents, data highlights
  green-60: "#7EBD80"              # 126·189·128 — Success backgrounds
  green-30: "#C4E0C1"              # 196·224·193 — Soft green callouts

  # === Orange (Pantone 151) ===
  orange-100: "#EB971B"            # 235·151·27 — Warning states, attention markers
  orange-60: "#F4C17A"             # 244·193·122 — Warning backgrounds
  orange-30: "#FAE1BE"             # 250·225·190 — Soft warning callouts

  # === Red (Pantone 186) ===
  red-100: "#D20033"               # 210·0·51 — Error / critical / delete actions

  # === Gray (Pantone 429) ===
  gray-100: "#BBBFC2"              # 187·191·194 — Neutral UI chrome, disabled states

  # === Semantic Aliases ===
  primary: "{colors.blue-100}"
  primary-pale: "{colors.blue-30}"
  primary-soft: "{colors.blue-10}"
  ink: "{colors.black-100}"
  muted: "{colors.black-30}"
  line: "{colors.black-10}"
  success: "{colors.green-100}"
  success-bg: "{colors.green-30}"
  warning: "{colors.orange-100}"
  warning-bg: "{colors.orange-30}"
  danger: "{colors.red-100}"

  # === Surfaces ===
  paper: "#ffffff"

  # === Hero Gradient (derived from blue-100, not in standard color spec) ===
  hero-start: "#0A1628"
  hero-end: "rgba(0, 113, 185, 0.85)"

typography:
  # Per TÜV Standard Front: Arial (Regular/Bold) + Times New Roman (Regular/Bold)
  # === Primary Sans (Arial) ===
  display:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "45px"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "0"
  headline:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "25px"
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: "0"
  title:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "16px"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "0"
  body:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.58
    letterSpacing: "0"
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "11px"
    fontWeight: 400
    lineHeight: 1.42
    letterSpacing: "0"
  eyebrow:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "13px"
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: "0"

  # === Serif (Times New Roman — formal documents only) ===
  serif-display:
    fontFamily: "'Times New Roman', Georgia, serif"
    fontSize: "45px"
    fontWeight: 700
    lineHeight: 1.08
  serif-body:
    fontFamily: "'Times New Roman', Georgia, serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.5

rounded:
  none: "0"
  xs: "2px"
  sm: "4px"
  md: "6px"
  lg: "8px"
  xl: "12px"
  pill: "999px"

spacing:
  xs: "4mm"
  sm: "8mm"
  md: "12mm"
  lg: "17mm"
  xl: "24mm"

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.paper}"
    typography: "{typography.title}"
    rounded: "{rounded.sm}"
    padding: "12px 28px"
    minHeight: "44px"
  button-primary-hover:
    backgroundColor: "{colors.blue-100}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "12px 28px"
  card:
    backgroundColor: "{colors.blue-30}"
    textColor: "{colors.ink}"
    borderTop: "4px solid {colors.success}"
    rounded: "{rounded.none}"
    padding: "5.5mm"
  page:
    width: "210mm"
    minHeight: "297mm"
    backgroundColor: "{colors.paper}"
    padding: "17mm"
  section-header:
    borderTop: "3px solid {colors.primary}"
  table-header:
    backgroundColor: "{colors.blue-30}"
    textColor: "{colors.primary}"
    borderBottom: "1px solid {colors.line}"
  footer:
    borderTop: "2px solid {colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
---

# Design System: TÜV Rheinland BS.A West China

## 1. Overview: Rheinland Precision

**Creative North Star: "German engineering rigor, expressed through restraint."**

The system communicates authority through a single authoritative blue (`#0071B9`), generous white space, and precise green accents. It is professional, technical, and deliberate — a designed voice that says "we measure, we certify, we train" without a word of marketing copy.

This direction explicitly rejects the AI-template aesthetic: no purple gradients, no glassmorphism panels, no neon glow, no dark mesh hero backgrounds. The page should feel like a well-formatted technical document — dense with information but never cluttered, structured but never rigid.

**Key characteristics:**

- Rheinland Blue (`#0071B9`) as the sole brand anchor — CTAs, headings, rules, brand marks
- Rheinland Green (`#009537`) as the accent — section dividers, success states, data callouts
- Arial throughout — one typeface, weight-driven hierarchy, no decorative fonts
- Paper-white page ground — bright, clean, information-first
- Flat surfaces — tonal layering via `blue-30` (`#BDCEE9`) and `blue-10` (`#EAEEF8`), no decorative shadows
- Tight grids and tables — the system's natural vocabulary is structured data, not hero visuals
- Dual-language ready — Western/Chinese font stacks coexist, switch by context

## 2. Colors: One Blue, One Green, Measured Neutrals

### Brand Anchors

- **Rheinland Blue** (`#0071B9`): The system's only brand color. Used for primary CTAs, h2 section headers, the 3px top rule on section dividers, the 2px footer rule, and the brand logo area. Never used as a background fill for large surfaces — blue earns its presence through precision placement.
- **Rheinland Deep** (`#0071B9` (blue-100)): Hero grounds, footer backgrounds, heavy emphasis. Used sparingly — a full-width deep blue section signals "pay attention."
- **Rheinland Green** (`#009537` (green-100)): The accent. 4px top borders on content cards, 3px dividers between hero and body, data-highlight bars. Never a text color — green is structural, not typographic.

### Surfaces

- **Paper** (`#ffffff`): Default page ground. Pure white is acceptable here because the brand lives in a document/print tradition — PDFs, certificates, reports. Not a warm cream, not a cool gray.
- **Pale** (`#EAEEF8 (blue-10)`): Tinted card backgrounds, table headers, callout boxes. One shade from paper — enough to separate without creating a dark/light mode split.
- **Pale Deep** (`#EAEEF8 (blue-10)`): Alternating table rows, code blocks, page chrome behind the main content area. Used only when Pale isn't enough separation.

### Ink (Text)

- **Ink** (`#000000` (black-100 / ink)): Primary body text. Deep blue-black — warmer and more deliberate than `#000`.
- **Muted** (`#C3C5C7` (black-30 / muted)): Secondary text — captions, metadata, footer notes, table footnotes.
- **Faint** (`#C3C5C7 (black-30/muted)`): Disabled states, placeholder text, non-critical labels.

### Rules & Lines

- **Line** (`#ECECEC` (black-10 / line)): Default 1px borders on tables, cards, and content dividers.
- **Line Strong** (`#BBBFC2` (gray-100)): Card edges, input focus borders, structural separators.

### Named Rules

**The One-Blue Rule.** Rheinland Blue is the system's only brand color. Do not introduce teal, cyan, or alternate blues as secondary accents. The green accent exists for structure, not decoration.

**The White-Page Rule.** The default ground is paper white. Dark backgrounds are reserved for the hero and footer only. No dark mode toggle — the brand is light-first.

**The Green-Is-Structural Rule.** Rheinland Green appears only on structural elements: card top borders, section dividers, success badges. It is never a text color, never a button, never a page background.

## 3. Typography: One Typeface, Weight-Driven Hierarchy

**Primary Font:** Arial, Helvetica, sans-serif (Arial Regular for body, Arial Bold for headings)
**Serif Font (formal):** Times New Roman, Georgia, serif (Regular for body, Bold for headings)

The system uses a single typeface — Arial — across all content. Hierarchy is expressed through weight and size, not font changes. This is deliberate: certification and training materials must read as factual, not styled.

### Hierarchy (Western)

- **Display / h1**: Arial, 45px, weight 700, line-height 1.08. Hero headlines and cover pages.
- **Headline / h2**: Arial, 25px, weight 700, line-height 1.18. Section titles. Always paired with a 3px blue top rule or a green divider.
- **Title / h3**: Arial, 16px, weight 700, line-height 1.25. Card headings, table captions, module labels.
- **Body**: Arial, 12px, weight 400, line-height 1.58. All running text, table cells, list items. Cap line length at 65–75 characters on full-width pages.
- **Caption**: Arial, 11px, weight 400, line-height 1.42. Metadata, footer text, source citations.
- **Eyebrow**: Arial, 13px, weight 700, line-height 1.35. Small markers above h2 sections.

### Typography Rules

**The One-Typeface Rule.** Arial carries everything — headlines, body, captions, buttons, nav. Times New Roman is reserved for formal certificate documents only. Do not introduce decorative or display fonts. Per TÜV Standard Front, only four font files are authorized: Arial Regular, Arial Bold, Times New Roman Regular, Times New Roman Bold.

**The Size-Over-Style Rule.** Emphasize through size and weight, never through italic (Arial italic reads poorly at small sizes), color (blue text is for links only), or letter-spacing tricks.

**The Bilingual Rule.** When mixing Chinese and English, use Arial for English runs. For Chinese-language documents targeting mainland China audiences, consult the local BS.A West team for the appropriate Chinese font stack — the TÜV Standard Front specifies only Western fonts (Arial + Times New Roman). The `lang` attribute on the HTML element controls font rendering behavior.

## 4. Elevation & Material

The system is flat by design. Depth is conveyed through:

- **Tonal layering**: `paper` (page) → `blue-30` (`#BDCEE9`) (cards) → `blue-10` (`#EAEEF8`) (alternating rows)
- **Hairline borders**: 1px `line` on every table cell, card edge, and content divider
- **Green structural accents**: 4px card top borders, 3px section dividers

### Material Rules

**The Flat-First Rule.** No box-shadows on cards, no elevation layers, no floating UI. If separation is needed, use a 1px border or a background tint.

**The No-Glass Rule.** Translucency, blur panels, and glassmorphism are absent from this system. The brand is solid, measurable, and precise.

## 5. Components

### Page Structure

- **Container**: 210mm × 297mm (A4) when used for PDF/flyer output. Responsive web uses max-width 1320px.
- **Padding**: 17mm (page edges), 12mm (internal sections).
- **Section Header**: 3px `blue-100` (`#0071B9`) top border, h2 headline, optional lead paragraph at 15px/1.65.

### Buttons

- **Primary**: `blue-100` (`#0071B9`) fill, white text, 4px radius, 12px 28px padding, min-height 44px. The only CTA style.
- **Secondary**: Transparent fill, `blue-100` (`#0071B9`) 1px border, `blue-100` (`#0071B9`) text. Used when primary is already present on the same view.
- **Hover**: Primary → `blue-100` fill. Secondary → `blue-100` (`#0071B9`) at 10% opacity background.
- **Disabled**: `faint` text, `line` border, no fill.

### Cards

- **Content Card**: `blue-30` (`#BDCEE9`) background, 4px `green-100` (`#009537`) top border, `5.5mm` padding. No shadow, no radius on the card itself. Internal elements may use `sm` (4px) radius.
- **Fact Card**: `blue-30` (`#BDCEE9`) background, left border in `blue-100` (`#0071B9`), large numeric value in `blue-100` (`#0071B9`) (22–30px), caption in `muted` (11px).

### Tables

- **Header Row**: `blue-30` (`#BDCEE9`) background, `blue-100` (`#0071B9`) text, weight 700, 1px `line` bottom border.
- **Data Row**: `paper` background, 1px `line` bottom border, 4mm 3mm padding. Alternating rows may use `blue-30` (`#BDCEE9`) on hover or for zebra striping.
- **First Column**: Keep-all word-break for labels. Other columns: normal overflow-wrap.

### Hero (Cover Page)

- **Background**: `#0A1628` to `rgba(0, 113, 185, 0.85)` gradient — deep maritime fading to `blue-100`. The only gradient in the system.
- **Content**: h1 in white (or champagne), eyebrow in `blue-100` (`#0071B9`), brand logo top-left.
- **Footer Rule**: 2px `blue-100` (`#0071B9`) at page bottom.

### Footer

- **Rule**: 2px `blue-100` (`#0071B9`) top border.
- **Content**: Brand name (left), page/document identifier (right), `blue-100` (`#0071B9`) text, 10px caption weight.

## 6. Dual-Language Strategy

BS.A West China operates in both Chinese and English. The design system handles this through:

1. **HTML `lang` attribute**: Sets the primary language and triggers the correct font stack.
2. **Separate font stacks**: Western content uses Arial. Chinese content uses SimHei/SimSun, with "Microsoft YaHei" as a web-safe fallback.
3. **Bilingual headings**: H1/H2 with line-break-friendly `<br/>` between Chinese and English lines, often with the English at smaller size and lighter weight.
4. **Table content**: Chinese and English columns may coexist — each cell uses the font stack appropriate to its content language.

### Language-Specific Rules

**The Longer-English Rule.** English text is typically 2.5–4× longer than equivalent Chinese. Container `min-height` values must be increased for English versions. Remove `word-break: keep-all` and `overflow: hidden` from English variants.

**The No-CJK-Layout Rule.** CSS properties designed for CJK text (`word-break: keep-all`, `line-break: strict`, `text-wrap: balance`) must be removed or overridden in English-language documents.

## 7. Do's and Don'ts

### Do

- Do use `blue-100` (`#0071B9`) as the single brand anchor — CTAs, headings, rules.
- Do use `green-100` (`#009537`) only for structural accents — card borders, dividers, success states.
- Do keep the page ground white (`#ffffff`).
- Do use Arial for all text — one typeface, weight-driven hierarchy. Per TÜV Standard Front: Arial Regular/Bold only.
- Do use Times New Roman for formal certificate documents — Regular/Bold only.
- Do use tables and grids as the primary content vocabulary.
- Do separate sections with 3px blue rules or green dividers.
- Do include bilingual (CN/EN) headings for all external-facing content.
- Do set `lang="en"` on English documents and `lang="zh-CN"` on Chinese documents.

### Don't

- Don't introduce a second brand color — no teal, cyan, orange, or alternate blues.
- Don't use gradients except on the hero cover. No gradient text, no gradient buttons.
- Don't add box-shadows to cards, buttons, or surfaces.
- Don't use glassmorphism, neon glow, dark mesh backgrounds, or AI-template aesthetics.
- Don't use `word-break: keep-all`, `line-break: strict`, or `text-wrap: balance` on English content.
- Don't use `overflow: hidden` on `.page` containers — content must be visible, not clipped.
- Don't introduce decorative or display typefaces. Arial and Times New Roman are the complete type system per TÜV Standard Front.
- Don't use pure black (`#000`) — the ink color is `#000000` (black-100 / ink).

## 8. PPT Slide Layout System

> Source: Official TÜV Rheinland PPT templates — `Template.pptx` / `TUEV_Library_2020_03.pptx` / `TÜVR母板使用说明_2019.03.pptx`

### 8.1 Slide Specifications

| Property | Value |
|----------|-------|
| Aspect Ratio | 16:9 widescreen |
| Dimensions | 33.9cm × 19.1cm (13.3" × 7.5") |
| Content Area | 11.8cm × 30.8cm (fixed across all layouts) |
| Grid | 0.2cm, always activated |
| Theme Color Scheme | "TÜV Rheinland" (colors per §1) |
| Theme Font Scheme | "TÜV Rheinland" — Major: Arial, Minor: Arial |

### 8.2 Guide Lines

- **Red guide lines**: Locked to slide master. Cannot be moved or deleted. Define content boundaries.
- **Gray guide lines**: Draggable. Hold Ctrl while moving to duplicate.
- Content area marked by red guide lines on ALL layouts — outer edges always identical, only column spacing varies.

### 8.3 Layout Catalog (31 Official Layouts)

#### Title Family
| # | Layout Name | Use |
|---|-------------|-----|
| 1 | Title with picture | Cover slide with image |
| 2 | Only Title with picture | Cover variant |
| 3 | Title without picture | Text-only cover |
| 4 | Title white | White background cover |

#### Divider Family
| # | Layout Name | Use |
|---|-------------|-----|
| 5 | Divider with picture | Chapter/section transition with image |
| 6 | Divider without picture | Text-only chapter divider |
| 7 | Divider white | White background chapter divider |

#### Content Layouts
| # | Layout Name | Use |
|---|-------------|-----|
| 8 | Title Only | Minimal title slide |
| 9 | Empty | Blank canvas |
| 10 | Agenda overview | Course program / table of contents |
| 11 | Statement | Key message or quote |
| 12 | Title and Content | Standard text + bullet slide |
| 13 | Two Content | Side-by-side comparison |
| 14 | Three content | Three-column layout |
| 15 | Four content | Four-column grid |
| 16 | Eight content | Eight-item grid (icons/features) |
| 17 | Six content | Six-item grid |

#### Picture & Media
| # | Layout Name | Use |
|---|-------------|-----|
| 18 | Title and picture | Text + image combo |
| 19 | Wave picture with Text | Wave-shaped image + text overlay |
| 20 | Big picture (dark) | Full-bleed dark image background |
| 21 | Picture/Content | 50/50 split |
| 22 | 2/3 picture, 1/3 content | Image-dominant split |
| 23 | 1/3 picture, 2/3 content | Content-dominant split |
| 24 | Wave picture | Full wave-shaped image |
| 25 | Picture centered | Centered image |

#### Device Mockups
| # | Layout Name | Use |
|---|-------------|-----|
| 26 | Laptop Screen | Laptop device frame |
| 27 | Monitor Screen | Desktop monitor frame |
| 28 | Tablet Screen | Tablet device frame |
| 29 | Smartphone Screen | Phone device frame |

#### Closing
| # | Layout Name | Use |
|---|-------------|-----|
| 30 | Closing blue | Blue background end slide |
| 31 | Closing white | White background end slide |

### 8.4 Training-Specific Slide Patterns

Standard training deck structure derived from the official template:

| Sequence | Slide Type | Layout | Content |
|----------|-----------|--------|---------|
| 1 | Cover | Title with picture | TÜV Rheinland + Course Title + Training Master Template |
| 2 | Academy Intro | Title and Content | Academy & Life Care value proposition |
| 3 | Course Program | Agenda overview | Module listing / timeline |
| 4 | Chapter Divider | Divider with/without picture | "Module N" header |
| 5 | Learning Objectives | Title and Content | "The aim of this course is to understand and be able to:" → bullet list |
| 6 | Content Slides | Two/Three/Four Content | Topic × N per module |
| 7 | Q&A / Quiz | Statement or Title and Content | Question → answer |
| 8 | Coffee Break | Divider or Picture | "Coffeebreak" |
| 9 | Feedback | Title and Content | "We look forward to your feedback" |
| 10 | Closing | Closing blue/white | End slide |

### 8.5 PPT Usage Rules (from Official Guide)

**Colors:**
- Use ONLY theme colors (TÜV Rheinland scheme) and custom colors derived from the theme.
- Never use PowerPoint built-in "Standard Colors" — auto-generated, incompatible with corporate design.
- Charts default to coloring from the 5th theme color; manually recolor if needed.

**Typography & Bullets:**
- Font sizes, bullet styles, and line spacing are pre-set in each layout. Do not override manually.
- Use `SHIFT + ALT + →` / `SHIFT + ALT + ←` to adjust list indentation levels.
- **Never manually insert bullet characters** — use only the built-in list level system.
- Fonts: Arial for all Latin text. East Asian font slot is deliberately empty (inherits from OS).

**Images:**
- Use the Crop function to trim images.
- Resize using **corner handles only** — edge handles distort proportions.
- Hold `Ctrl + Shift` while dragging a corner handle to scale proportionally from center.
- Compress images before final save using the Compress Pictures command.

**Layout Discipline:**
- Stay within the content area (red guide lines). Do not place content outside these boundaries.
- Content area is always 11.8cm × 30.8cm — only column spacing varies between layouts.
- Keep the 0.2cm grid active at all times for alignment.

### 8.6 Relationship to Web/HTML Outputs

PPT templates inform HTML flyer design but are not 1:1 translatable:

- **A4 HTML flyers** follow the print-first spacing system (§3) rather than 16:9 slide dimensions.
- **PPT web versions** use the 16:9 slide ratio and theme color scheme.
- **Training slide patterns** (§8.4) apply to both PPT and web-based training materials.
- **Color tokens** (§1) are shared across all formats — PPT theme and DESIGN.md use identical accent1=#0071B9.
- PPT layout naming convention informs HTML section naming: Title → Hero, Divider → Section Break, Content → Card Grid, Closing → Footer CTA.
