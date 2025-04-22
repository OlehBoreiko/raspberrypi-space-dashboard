# 🛰️ Live ISS Trajectory on Leaflet Maps with Smooth Animation

This lecture enhances your Space Dashboard with a real-time animated map showing the current trajectory of the International Space Station (ISS). The data is fetched from your local `/iss` API and visualized using Leaflet.js in a modal popup.

---

## ✅ Features Implemented

- Live Leaflet map rendered in a modal (`#map-modal`)
- Custom SVG ISS marker that moves every 5 seconds
- Animated trajectory trail using `L.polyline`
- Smooth map movement with `map.panTo(...)`
- Close button styled to stay visible above the map
- ISS Trajectory button in ISS Tracker block

---

## 🛠 Files Updated

- `index.html`
  - Added Leaflet CDN
  - Injected modal HTML for `#map-modal`
  - Added button: 🔭 View ISS Trajectory
- `script.js`
  - `openTrajectoryMap()`, `initMap()`, `updateMapISS()`
  - Map logic initializes only once

---

## 🚀 How to Use

1. Launch your Flask server with `/iss` endpoint
2. Visit your dashboard in the browser
3. Click 🔭 View ISS Trajectory

---

## 💡 Bonus Ideas

- Add orbital predictions with TLE data
- Switch between light/dark map themes
- Show ISS altitude and speed

---

Enjoy your upgraded, real-time space dashboard!