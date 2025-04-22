async function explain(type) {
    const output = document.getElementById(`${type}-explanation`);
    if (output) {
      output.innerHTML = "<p>Loading explanation...</p>";
      try {
        const res = await fetch(`/ai/${type}`, { method: "POST" });
        const data = await res.json();
        output.innerHTML = `<p>${data.text}</p>`;
      } catch (err) {
        output.innerHTML = "<p>Error getting explanation</p>";
      }
    }
  }
  
  async function loadISSTracker() {
    try {
      const res = await fetch("/iss");
      const data = await res.json();
      document.getElementById("iss-lat").textContent = data.latitude;
      document.getElementById("iss-lon").textContent = data.longitude;
    } catch (err) {
      document.getElementById("iss-lat").textContent = "Error";
      document.getElementById("iss-lon").textContent = "Error";
    }
    try {
      const res = await fetch("/iss-flyover");
      const data = await res.json();
  
      const rise = document.getElementById("iss-rise");
      const peak = document.getElementById("iss-peak");
      const set = document.getElementById("iss-set");
      const duration = document.getElementById("iss-duration");
  
      if (data.error) {
        rise.textContent = "Error";
        peak.textContent = "";
        set.textContent = "";
        duration.textContent = "";
      } else {
        rise.textContent = data.rise;
        peak.textContent = data.peak;
        set.textContent = data.set;
        duration.textContent = data.duration_seconds + " seconds";
      }
    } catch (err) {
      document.getElementById("iss-rise").textContent = "Error";
    }
  }
  
  async function loadNEO() {
    const counter = document.getElementById("asteroid-count");
    if (!counter) return;
  
    counter.textContent = "…";
    try {
      const res = await fetch("/neo");
      const data = await res.json();
      counter.textContent = data.hazardous_asteroids.length;
    } catch (err) {
      counter.textContent = "!";
    }
  }
  
  async function loadMars() {
    try {
      const res = await fetch("/mars");
      const data = await res.json();
      document.getElementById("mars-temp").textContent = data.temperature;
      document.getElementById("mars-wind").textContent = data.wind;
      document.getElementById("mars-pressure").textContent = data.pressure;
    } catch (err) {
      document.getElementById("mars-temp").textContent = "–";
      document.getElementById("mars-wind").textContent = "–";
      document.getElementById("mars-pressure").textContent = "–";
    }
  }
  
  async function loadSpaceWeather() {
    try {
      const res = await fetch("/donki");
      const data = await res.json();
      document.getElementById("solar-flares").textContent = data.flares.length;
      document.getElementById("solar-cmes").textContent = data.cme.length;
      document.getElementById("solar-storms").textContent = data.storms.length;
    } catch (err) {
      document.getElementById("solar-flares").textContent = "!";
      document.getElementById("solar-cmes").textContent = "!";
      document.getElementById("solar-storms").textContent = "!";
    }
  }
  
  async function loadAPOD() {
    try {
      const res = await fetch("/apod");
      const data = await res.json();
      document.getElementById("apod-title").textContent = data.title;
      document.getElementById("apod-date").textContent = data.date;
      document.getElementById("apod-img").src = data.url;
      document.getElementById("apod-modal-title").textContent = data.title;
      document.getElementById("apod-modal-explanation").textContent = data.explanation;
    } catch (err) {
      document.getElementById("apod-title").textContent = "Error";
    }
  }
  
  window.addEventListener("DOMContentLoaded", () => {
    loadISSTracker();
    document.getElementById("refresh-iss")?.addEventListener("click", loadISSTracker);
    loadNEO();
    loadMars();
    loadSpaceWeather();
    loadAPOD();
  
    // Handle APOD modal
    const apodImg = document.getElementById("apod-img");
    const apodModal = document.getElementById("apod-modal");
    const apodClose = document.getElementById("apod-close");
  
    if (apodImg && apodModal && apodClose) {
      apodImg.addEventListener("click", () => {
        apodModal.classList.remove("hidden");
      });
      apodClose.addEventListener("click", () => {
        apodModal.classList.add("hidden");
      });
    }
  });
  
  // 🌍 ISS Trajectory Map
  let mapInitialized = false;
  let map, marker, polyline, trajectory = [];
  
  function openTrajectoryMap() {
    document.getElementById("map-modal").classList.remove("hidden");
    if (!mapInitialized) {
      setTimeout(initMap, 100); // delay for modal render
    }
  }
  
  function closeTrajectoryMap() {
    document.getElementById("map-modal").classList.add("hidden");
  }
  
  function initMap() {
    map = L.map('map').setView([0, 0], 2);
  
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 5,
      minZoom: 2,
      attribution: ''
    }).addTo(map);
  
    const issIcon = L.icon({
      iconUrl: 'https://upload.wikimedia.org/wikipedia/commons/d/d0/International_Space_Station.svg',
      iconSize: [50, 32],
      iconAnchor: [25, 16]
    });
  
    marker = L.marker([0, 0], { icon: issIcon }).addTo(map);
    polyline = L.polyline([], { color: 'orange', weight: 2 }).addTo(map);
  
    mapInitialized = true;
    updateMapISS();
    setInterval(updateMapISS, 5000);
  }
  
  async function updateMapISS() {
    try {
      const res = await fetch("/iss");
      const data = await res.json();
      const lat = parseFloat(data.latitude);
      const lon = parseFloat(data.longitude);
  
      if (marker) marker.setLatLng([lat, lon]);
      trajectory.push([lat, lon]);
      if (polyline) polyline.setLatLngs(trajectory);
      if (map) map.panTo([lat, lon], { animate: true, duration: 1 });
  
    } catch (err) {
      console.error("Map ISS update failed:", err);
    }
  }
  
  // 🔽 Collapsible Sections Logic
  document.addEventListener("DOMContentLoaded", () => {
    const headers = document.querySelectorAll(".collapsible-header");
    headers.forEach(header => {
      header.addEventListener("click", () => {
        const content = header.nextElementSibling;
        const icon = header.querySelector(".toggle-icon");
  
        if (content && content.classList.contains("section-content")) {
          content.classList.toggle("collapsed");
          if (icon) {
            icon.textContent = content.classList.contains("collapsed") ? " 🔼" : " 🔽";
          }
        }
      });
    });
  });
  