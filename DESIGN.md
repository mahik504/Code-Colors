# Code&Colors Design System

<div align="center">

### Porcelain × Cherry × Rose × Graphite
**Version 1.0.0** · Visual Design Language & Interface Tokens

</div>

---

## 1. Design Direction

Code&Colors rejects the generic dark-terminal aesthetic common in creative software, introducing an editorial light-first atelier identity. It blends physical materials (warm porcelain, polished cherry lacquer, soft rose blush) with technical precision (graphite typography, IBM Plex Mono code streams).

---

## 2. Color Palette & Tokens

### Core Brand Tokens
```css
:root {
  --bg-main:         #FAF7F5;  /* Warm porcelain base canvas */
  --surf-porcelain:  #FFFFFF;  /* High-refinement panel surface */
  --bg-warm:         #F2EBE8;  /* Secondary recesses, segment tracks */
  --primary-cherry:  #A8173B;  /* Primary identity accent */
  --deep-cherry:     #70132F;  /* Typographic headings & dark mode core */
  --soft-rose:       #E9A0B0;  /* Keylines, glows, and rim illumination */
  --blush-accent:    #F5DCE2;  /* Focus rings & gentle selection fills */
  --graphite:        #202024;  /* Deep high-contrast text & technical frames */
  --text-secondary:  #77717A;  /* Secondary metadata and captions */
  --border-subtle:   #E9DDE0;  /* 1px structural boundary lines */
  --success-mint:    #218B64;  /* Operational ledger & status green */
}
```

### Light & Dark Theming
- **Light Theme (Primary)**: Clean porcelain white surfaces (`#FFFFFF`), subtle rose borders (`#E9DDE0`), and graphite text (`#202024`) with bold cherry accents.
- **Dark Theme (Technical)**: Deep cherry-graphite slate (`#141216`), glowing soft rose indicators, and luminous cherry buttons.

---

## 3. Typography Hierarchy

- **Display**: Space Grotesk / Archivo Bold (`800` weight) for brand title and studio banners.
- **Body & Controls**: Inter / System Sans for legible controls and accessible navigation.
- **Technical Code Streamer**: IBM Plex Mono (`400`, `500`, `600`) for syntax-highlighted algorithmic stroke generation.

---

## 4. Atmospheric System & Motion

- **Ambient Gradient Mesh**: Subtle dual-radial gradient fields drifting on an organic timer and responding gently to mouse coordinates.
- **Interactive Parallax**: Smooth normalized mouse tracking with `requestAnimationFrame` interpolation.
- **Tactile Feedback**: Subtle button elevation on hover, mechanical depression on press, and accessible cherry focus rings.
- **Custom Desktop Cursor**: Ambient cherry glow dot with magnetic follower ring on fine pointer devices.
