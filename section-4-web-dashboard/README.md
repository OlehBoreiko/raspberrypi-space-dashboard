# Section 4 – Dynamic Space Weather & Mars Climate Widgets

In this step, we extended our dashboard with two new data sources:

- 🔆 Space weather (solar flares, CMEs, geomagnetic storms)
- 🪐 Mars weather (temperature, wind, and pressure)

These are fetched via Flask endpoints and displayed live in the dashboard.

---

## 🌞 Space Weather (DONKI API)

New HTML:
```html
<p>Solar Flares: <span id="solar-flares">--</span></p>
<p>CMEs: <span id="solar-cmes">--</span></p>
<p>Storms: <span id="solar-storms">--</span></p>
```

Fetch code in `script.js`:
```js
fetch("/donki")
  .then(res => res.json())
  .then(data => {
    document.getElementById("solar-cmes").textContent = data.cme.length;
    document.getElementById("solar-flares").textContent = data.flares.length;
    document.getElementById("solar-storms").textContent = data.storms.length;
  });
```

---

## 🪐 Mars Weather (InSight API)

New HTML:
```html
<p>Mars Temp: <span id="mars-temp">--</span> °C</p>
<p>Mars Wind: <span id="mars-wind">--</span> m/s</p>
<p>Mars Pressure: <span id="mars-pressure">--</span> Pa</p>
```

Fetch code:
```js
fetch("/mars")
  .then(res => res.json())
  .then(data => {
    document.getElementById("mars-temp").textContent = data.temperature?.toFixed(1) ?? '--';
    document.getElementById("mars-wind").textContent = data.wind?.toFixed(1) ?? '--';
    document.getElementById("mars-pressure").textContent = data.pressure?.toFixed(1) ?? '--';
  });
```

---

## 🧪 Final Result

Now the dashboard includes:

- ✅ ISS Position
- ✅ Asteroids Near Earth
- ✅ Solar Activity
- ✅ Mars Weather

Everything is dynamic and updates automatically on load.
