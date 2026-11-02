# Code&Colors User Guide

<div align="center">

### Operational Guide & Studio Manual
**Version 1.0.0** · Where Art Meets Algorithm

</div>

---

## 1. Getting Started

### Launching the Studio
1. Open a terminal in the project directory:
   ```bash
   npm start
   ```
2. Navigate to `http://localhost:8765/` in your browser.
3. The studio automatically loads **The Starry Night** (Vincent van Gogh, 1889) as the default reference painting and begins generating artwork on the central canvas.

---

## 2. Interface Layout

The workspace is organized into three functional zones:

1. **Left: Creative Controls**
   - **Source Input**: Open custom images, videos, webcams, or 3D models.
   - **Style Selector**: Select across 48 styles in 5 suites (Paint, Draw, Graphic, Craft, 3D).
   - **Motion Controls**: Adjust stroke speed, trajectory path, and layer build-up.
   - **Export Panel**: Generate standalone HTML, 8K PNG, SVG, or MP4 video.

2. **Center: Creative Darkroom**
   - **Main Painting Canvas**: Displays live algorithmic stroke rasterization.
   - **3D Relief Shading**: Interactive lighting pad for real-time impasto and depth.
   - **Transport Bar**: Pause, restart, record, or clear the painting run.

3. **Right: Reference & Code Studio**
   - **Reference Preview**: Displays the original reference image or live feed.
   - **Live Code Streamer**: Displays synthesized JavaScript coordinates and color commands in real time.

---

## 3. Working with Audio Reactivity

1. Open the bottom deck by clicking the deck toggle or pressing `H`.
2. Select one of the 10 bundled demo tracks (or drop your own MP3/WAV file).
3. Toggle the **audio reactive** switch.
4. The brush strokes will dynamically expand on bass transients, while treble harmonics ignite luminous light flares.

---

## 4. 3D Model Studio

1. In the source panel, select **3D demo** (or drop a `.glb`, `.gltf`, `.obj`, `.stl`, or `.ply` file).
2. Use OrbitControls (left drag to rotate, right drag to pan, wheel to zoom) to position the model.
3. Toggle live painting to sample the 3D model stream directly onto the 2D canvas with relief shading.
