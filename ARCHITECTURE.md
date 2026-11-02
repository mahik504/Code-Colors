# Code&Colors Architecture

<div align="center">

### Technical Engine, Shader Pipeline & Audio-Reactive System
**Version 1.0.0** · Independent Creative Studio

</div>

---

## 1. System Overview

Code&Colors is structured as a zero-build, browser-native computational painting instrument. It operates without a virtual DOM, bundlers, or remote compilation, executing directly in standard evergreen browsers via native ES modules, HTML5 2D Canvas, WebGL 2, Web Audio API, and WebAssembly.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        PRESENTATION SHELL                              │
│   Left Panel: Controls    Center: Darkroom & Stage    Right: Code/Ref  │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
┌──────────────────────────────────▼─────────────────────────────────────┐
│                     ALGORITHMIC PAINTING ENGINE                        │
│   Stroke Generators (48 styles) · Dynamic Trajectories · Color Models  │
└───────┬──────────────────────────┬───────────────────────────┬─────────┘
        │                          │                           │
┌───────▼──────────────┐   ┌───────▼──────────────┐   ┌────────▼─────────┐
│   CANVAS 2D MASTER   │   │   WEBGL 2 RELIEF     │   │ THREE.JS STUDIO  │
│ Brush Dynamics &     │   │ Normal Maps, Height, │   │ 3D Viewport,     │
│ Impasto Raster       │   │ Impasto & Lighting   │   │ Models & Sampler │
└──────────────────────┘   └──────────────────────┘   └──────────────────┘
```

---

## 2. Rendering Engines

### 2.1 Canvas 2D Painting Engine
The core rendering pipeline executes 48 distinct aesthetic algorithms:
- **Paint Suite**: Oil (dual bristle displacement, drying tails), Acrylic, Palette Knife (impasto ridges), Gouache, Watercolour (pigment bleeding, edge granulation), Wet Watercolour, Sumi (ink wash diffusion), Ink, Calligraphy, Graffiti (stochastic spray droplets), Soft (airbrush).
- **Draw Suite**: Pencil, Charcoal, Pastel, Pen, Hatch, Marker.
- **Graphic Suite**: Flat, Geometric, Dots, Halftone, Scribble, String, Paper, Bokeh, Neon, Hylics, Linocut, Riso.
- **Craft Suite**: Thread, Cross-Stitch, Clay, Beads, Foam, Tape.
- **3D Surfaces**: Ceramic, Stone, Puffy, Metal, Molten, Pewter, Copper, Gold, Bronze, Glass, Lens, Crystal.

### 2.2 WebGL 2 Relief & Lighting Shader
A dedicated WebGL 2 pipeline synthesizes relief maps in real time:
- **Normal & Height Synthesis**: Computes Sobel derivatives across the luminance field to construct fine surface perturbation normals.
- **Lighting Shader**: Dynamic directional light controlled by the interactive lighting pad, calculating diffuse, Blinn-Phong specular, and ambient occlusion highlights.
- **Shader Pipeline**: Renders impasto thickness, metallic gloss, and glass refraction without impacting 2D stroke generation.

### 2.3 Audio-Reactive Engine
- **Web Audio Context**: Analyzes real-time audio streams from 10 bundled demonstration tracks or live microphone input.
- **Frequency Analysis**: 512-band Fast Fourier Transform (FFT) extraction.
- **Dynamic Modulation**: Low frequencies modulate brush width and impasto height; transients trigger burst splatters; mid-range harmonic peaks drive chromatic shifts and light flares.

### 2.4 MediaPipe Face & Landmark Detection
- Bundled in `vendor/mediapipe/`.
- Runs fully offline via WebAssembly (`vision_wasm_internal.wasm`) and lightweight TFLite models (`blaze_face_short_range.tflite`).
- Provides 468 landmark coordinates for real-time generative portraiture.

### 2.5 Three.js 3D Viewport
- Built with Three.js r160.
- Implements loaders for GLTF/GLB, OBJ, STL, and PLY files.
- Includes OrbitControls, studio environment presets, and dynamic mesh stream capture back into the 2D painting engine.

---

## 3. Master Export Architecture

1. **Standalone HTML**: Compiles the entire painting program, palette, and stroke instructions into an executable, zero-dependency HTML file that paints itself when opened.
2. **8K Master PNG**: Exports raster images up to 7680×4320 with embedded tEXt metadata storing complete painting reproduction recipes.
3. **SVG Vector**: Converts contour paths into standard SVG vectors for infinite scaling and physical plotter reproduction.
4. **WebCodecs MP4**: Hardware-accelerated H.264/AAC video recording at 60 FPS directly within compatible browsers.
5. **Syphon / Spout VJ Bridge**: Connects live canvas streams to external VJ software (Resolume) via local native bridge.
