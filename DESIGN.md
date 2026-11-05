# Code&Colors Design System

<div align="center">

### Porcelain × Deep Cherry × Soft Rose × Ink
**Version 1.0.0** · Visual Design Language, Editorial Architecture & Interface Tokens

</div>

---

## 1. Design Philosophy & Atmosphere

Code&Colors marries contemporary generative algorithmic craftsmanship with refined neo-editorial aesthetics. Rejecting generic dark-terminal cliches and oversaturated neon blues/greens, it creates an atelier environment blending warm tactile materials (porcelain surfaces, deep cherry lacquer, soft rose rim accents) with surgical computational typography.

- **Atmosphere Spectrum**: Balanced Atelier (Density: 6, Variance: 6, Motion: 6)
- **Primary Interface**: Light editorial atelier (`#F7F5F2` porcelain canvas, `#FFFFFF` pure surfaces, `#191719` ink typography)
- **Work Surface / Darkroom**: Deep contrasting slate (`#141215`) for the creative canvas, WebGL relief stage, and live algorithmic code streamer

---

## 2. Color Calibration & Semantic Roles

```css
:root {
  /* Starting Design Tokens */
  --porcelain:       #F7F5F2;  /* Base editorial canvas */
  --deep-cherry:     #8F1738;  /* Primary brand identity & active accents */
  --soft-rose:       #E9B9C5;  /* Subtle keylines, glowing indicators, rims */
  --ink:             #191719;  /* Primary text and high-contrast darkroom */
  --warm-grey:       #EFEBE7;  /* Recesses, tracks, secondary wells */
  --muted-grey:      #898187;  /* Secondary captions, tooltips, inactive states */
  --blush-accent:    #F8E8EC;  /* Gentle selection fills & hover backgrounds */
  --border-subtle:   #E6DFD9;  /* 1px structural boundaries (Light) */
  --success-mint:    #218B64;  /* Operational ledger & recording green */
}

/* Light Editorial Theme (Atelier Standard) */
body[data-ui="light"], body:not([data-ui="dark"]) {
  --case:            #F7F5F2;
  --panel:           #FFFFFF;
  --line:            #E6DFD9;
  --key:             #FFFFFF;
  --keyon:           #F8E8EC;
  --keyline:         #E6DFD9;
  --keyshadow:       rgba(143, 23, 56, 0.08);
  --press:           rgba(143, 23, 56, 0.14);
  --text:            #191719;
  --muted:           #898187;
  --ledoff:          #D8D1CC;
  --knobtop:         #FFFFFF;
  --track:           #EFEBE7;
  --well:            #EFEBE7;
  --ink:             #191719;
  --inktext:         #F7F5F2;
  --accent:          #8F1738;
  --accent2:         #E9B9C5;
  --accent3:         #B9254D;
  --stage-bg:        #141215;
  --stage-border:    #E6DFD9;
}

/* Dark Technical Theme (Night Studio) */
body[data-ui="dark"] {
  --case:            #141215;
  --panel:           #1D1A1E;
  --line:            #2C262B;
  --key:             #252024;
  --keyon:           #3D1B24;
  --keyline:         #3C323A;
  --keyshadow:       #0A080C;
  --press:           rgba(143, 23, 56, 0.35);
  --text:            #F7F5F2;
  --muted:           #9E969D;
  --ledoff:          #3D343B;
  --knobtop:         #2D272C;
  --track:           #241F24;
  --well:            #100E11;
  --ink:             #F7F5F2;
  --inktext:         #141215;
  --accent:          #8F1738;
  --accent2:         #E9B9C5;
  --accent3:         #D63D66;
  --stage-bg:        #0E0C0F;
  --stage-border:    #2C262B;
}
```

---

## 3. Typographic Architecture

- **Editorial Display**: `Fraunces` / `Space Grotesk` (weights 600, 700, 800) for studio header, brand wordmark, and major stage titles.
- **Humanist Interface & Controls**: `Plus Jakarta Sans` / modern sans-serif system stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`) for buttons, badges, selectors, tabs, navigation links, and parameter labels.
- **Technical Code Streamer**: `IBM Plex Mono` (`400`, `500`, `600`) for the live algorithmic painting code streamer, canvas coordinates, shader metrics, and file exports.

---

## 4. Component Stylings & Interaction Design

- **Buttons (`.key`, `.ebtn`, `.ebig`)**: Flat, refined tactile elevation (-1px translate on active). Primary buttons dressed in Deep Cherry gradient (`#8F1738` → `#70132F`) with crisp white typography. Secondary buttons dressed in Porcelain/Keyline with gentle blush hover.
- **Segmented Controls (`.seg`, `.pseg`)**: Recessed pill track in Warm Grey (`#EFEBE7`) with smooth sliding pill states in Porcelain (`#FFFFFF`) with 1px border.
- **LED Indicators (`.led`)**: Micro-indicator rings with deep cherry and soft rose glowing states (`box-shadow: 0 0 6px var(--accent)`).
- **Stage Enclosure (`#stagewrap`, `main`)**: Deep darkroom canvas border with subtle rose rim lighting and smooth responsive aspect-ratio fitting.
- **Motion System**: Smooth CSS transitions (`0.14s - 0.2s cubic-bezier(0.2, 0, 0, 1)`). Reduced-motion support via `@media (prefers-reduced-motion: reduce)`.
- **Custom Cursor**: Desktop cherry dot with magnetic follower ring on fine pointer devices.

---

## 5. Banned Anti-Patterns (Anti-Slop Directives)

1. No generic neon green or purple button glows.
2. No pitch black `#000000` interfaces without warm tone calibration.
3. No monospace typography across primary interface labels and navigation.
4. No horizontal scrolling or button truncation on mobile.
5. No fake or unverified metrics.
6. No emoji icons in software controls.
