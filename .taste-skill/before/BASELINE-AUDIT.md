# Code&Colors Baseline Audit Report

**Date**: November 2026  
**Auditor**: Antigravity Studio Worker  
**Repository**: `C:\projects\Code&Colors\`  
**Target URL**: `http://localhost:8765/` (Production: `https://code-colors.vercel.app/`)

---

## 1. Technical Stack & Component Architecture

| Layer | Implementation |
|---|---|
| **Architecture** | Zero-build, browser-native ES modules and HTML5 |
| **Markup & DOM** | Single-page application in `index.html` with modular `<style>` and `<script>` blocks |
| **Styling** | Native CSS tokens, responsive flexbox and CSS grid |
| **Painting Engine** | Native Canvas 2D (48 algorithmic styles) + dynamic trajectory curves |
| **Relief & Normal Maps** | WebGL 2 Sobel gradient height synthesis & Blinn-Phong lighting shader |
| **3D Engine** | Three.js r160 (`viewer3d.js`) with OrbitControls and GLTF/OBJ/STL/PLY loaders |
| **Audio Processing** | Web Audio API 512-band FFT analyzer with 10 bundled demo tracks and live mic |
| **AI Vision** | MediaPipe Face Mesh WASM (`vision_wasm_internal.wasm` + TFLite models) |
| **Export Engines** | Standalone self-executing HTML, 8K Master PNG, SVG vector paths, WebCodecs MP4 |

---

## 2. Views, Modes, and Component Inventory

1. **Application Modes**:
   - **Easy Mode (`#easy`)**: 4-stage guided workflow (Source, Look/Style, Motion, Export).
   - **Full Console (`#uimode` -> `console`)**: Studio engineering instrument with full controls:
     - Source panel (file open, examples, live camera/mic/3D).
     - Style panel (48 styles, subject/background toggles, custom color swatches, lighting pad).
     - Brush panel (shape generator, caps, clean/stamped, performance quality).
     - Motion panel (draw, glide, sketch, ink, spiral, fall, pop, shard, pixel, hilite).
     - Path panel (free, one line, spiral, top-down order, outline controls).
     - Frame & Rim panel (aspect ratios 16:9, 9:16, 4:5, 1:1; geometry cuts; rim lighting).
     - Speed & Playlist deck (speed slider, 10-slot memory playlist, presets A-D).
     - Music deck (beat sensitivity knob, hits/flow/free triggers, frequency modulation).
     - Output deck (format selectors, resolution up to 8K, cover export).
2. **Display Views**:
   - `studio`: Full stage with original reference thumbnail and live algorithmic code streamer.
   - `simple`: Distraction-free reel mode (stage on top, reference and code underneath, no chrome).
   - `painting`: Pure artwork viewport maximized.
   - `duo`: Artwork with synchronized code streamer beneath.
   - `editor`: Side-by-side IDE layout with editable painting code and syntax line numbering.
3. **Aspect Ratios**:
   - `landscape` (16:9 - 1920×1080)
   - `vertical` (9:16 - 1080×1920 Reels/Shorts/TikTok)
   - `portrait` (4:5 - 1080×1350 Instagram Feed)
   - `square` (1:1 - 1080×1080)
4. **Theme Toggles**:
   - Dark Theme (`body[data-ui="dark"]`)
   - Light Theme (`body[data-ui="light"]`)

---

## 3. Baseline Performance & Quality Metrics

Captured using Playwright Chromium at standard desktop (1440×900) and mobile (390×844) viewports:

| Metric | Baseline Value | Standard / Target | Status |
|---|---|---|---|
| **Initial Load** | 5,495 ms | < 2,500 ms | ⚠️ Needs optimization |
| **DOM Content Loaded** | 4,226 ms | < 1,500 ms | ⚠️ Heavy inline assets |
| **First Contentful Paint (FCP)** | 4,068 ms | < 1,800 ms | ⚠️ Delayed initial paint |
| **Largest Contentful Paint (LCP)** | 4,232 ms | < 2,500 ms | ⚠️ Delayed canvas init |
| **Cumulative Layout Shift (CLS)** | 0.2925 | < 0.1000 | ❌ High layout shifts |
| **JavaScript Console Errors** | 0 | 0 | ✅ Zero errors |
| **JavaScript Console Warnings** | 0 | 0 | ✅ Zero warnings |
| **Test Suite (`npm test`)** | 26 / 26 Pass | 26 / 26 Pass | ✅ Clean pass |

---

## 4. Visual Inconsistencies & UX Failures Identified

1. **Aesthetic Misalignment & AI Cliché Colors**:
   - The UI relies heavily on harsh pitch black (`#080808` / `#121314`) and oversaturated neon green (`#00f59b`), reminiscent of generic terminal emulators.
   - Clashes with the mandated editorial design direction: **Porcelain (`#F7F5F2`), Deep Cherry (`#8F1738`), Soft Rose (`#E9B9C5`), Ink (`#191719`), Warm Grey (`#EFEBE7`), Muted Grey (`#898187`)**.
2. **Typographic Breakdown**:
   - Monospaced typography is applied everywhere—across navigation, headings, buttons, badges, descriptions.
   - Lacks an expressive editorial serif/display typeface for titles and clear humanist/modern sans-serif for controls.
   - Numbers and labels feel cramped and mechanical.
3. **Severe Mobile Responsiveness Failures**:
   - On viewports < 768px, horizontal overflow occurs in multiple control bars.
   - Style selection buttons (`pencil sketch`, `graffiti`, `watercolour`, `ink dr`) clip off the edge of the viewport.
   - Bottom helper text displays `"more controls: visit on your computer"`, failing to provide a touch-optimized mobile creative experience.
4. **Light Mode Disconnect**:
   - Switching to light mode inverts the navigation and sidebars to white/grey, but leaves the entire central canvas stage encased in an unstyled pitch-black rectangle with high-contrast borders.
5. **Legacy Branding Artifacts**:
   - The algorithmic code streamer footer still displays `"Code&Paint Studio"`.
   - The status bar prints `"Painting demo · Code&Paint — 1000 shapes."`.
6. **Easy Mode Discovery**:
   - The 48 artistic styles are compressed into a tiny "all 48 styles, palettes, outlines" link that switches to a confusing sub-menu rather than a modern, visual, categorized browsing experience.

---

## 5. Baseline Screenshots Archived

The following visual records are saved in `.taste-skill/before/`:
- `01_desktop_fullpage.png` — Full desktop layout
- `02_desktop_viewport.png` — Standard 1440×900 desktop viewport
- `03_creative_workspace.png` — Canvas darkroom stage and code streamer
- `04_header_controls.png` — Navigation bar, mode selector, transport controls
- `06_tablet_viewport.png` — Tablet viewport (820×1180)
- `07_mobile_viewport.png` — Mobile viewport (390×844)
- `08_mobile_fullpage.png` — Mobile full page scroll
- `09_full_console_desktop.png` — Full console layout (desktop)
- `10_full_console_viewport.png` — Full console viewport
- `11_light_mode_console.png` — Light mode console
- `12_light_mode_easy.png` — Light mode easy mode
