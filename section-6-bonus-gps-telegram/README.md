# Parallax Starfield & Collapsible Sections

In this lecture, we upgraded the visual experience of the Space Dashboard by adding two key front-end enhancements:

## 🌌 Starfield Background (Parallax)

- Added a full-screen animated SVG background using randomly placed stars.
- The background is animated using `@keyframes` in CSS (`panStars`) to simulate motion and depth.
- The CSS is embedded in `style.css` and applied using `body::before`.

## 🔽 Collapsible Sections

- Each section header (`h2`) is now clickable and includes a toggle icon (🔽 / 🔼).
- The content below each header is wrapped in a `<div class="section-content">`.
- JavaScript toggles the `.collapsed` class with smooth transitions defined in `style.css`.

### Updated Files

- `index.html` – Added toggle icons and wrapped content in `.section-content` divs.
- `script.js` – Added click listeners to toggle section visibility and arrow direction.
- `style.css` – Added collapsible logic using `max-height` and transitions. Also includes starfield background animation.

---

This improves both the usability and visual experience, especially on mobile devices. All blocks (ISS, Asteroids, Solar Activity, Mars Weather) now support collapsible UI.