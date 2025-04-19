# Section 4 – Web Dashboard with ISS and Asteroid Data

This folder contains the self-contained Flask project with the frontend dashboard and API server.

## 🚀 What Was Added in This Step

In this lecture, we added JavaScript fetch calls to display real-time space data.

### ✅ Live ISS Position

Updates these fields:

```html
<p>Latitude: <span id="iss-lat">--</span></p>
<p>Longitude: <span id="iss-lon">--</span></p>
```

In `static/script.js`:

```js
fetch("/iss")
  .then(res => res.json())
  .then(data => {
    document.getElementById("iss-lat").textContent = data.latitude;
    document.getElementById("iss-lon").textContent = data.longitude;
  });
```

### ✅ Asteroid Count

Updates:

```html
<p>Total hazardous: <span id="asteroid-count">--</span></p>
```

In `script.js`:

```js
fetch("/neo")
  .then(res => res.json())
  .then(data => {
    document.getElementById("asteroid-count").textContent = data.hazardous_asteroids.length;
  });
```

These values now update live whenever the page loads.

## 💡 Tip

Make sure Flask is running before opening the dashboard:

```bash
python script.py
```

Visit:
```
http://<your-raspberry-pi-ip>:5000
```