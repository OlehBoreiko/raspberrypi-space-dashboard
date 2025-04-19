// Fetch live ISS position
fetch("/iss")
  .then(res => res.json())
  .then(data => {
    document.getElementById("iss-lat").textContent = data.latitude;
    document.getElementById("iss-lon").textContent = data.longitude;
  })
  .catch(err => console.error("ISS fetch error:", err));

// Fetch count of hazardous asteroids
fetch("/neo")
  .then(res => res.json())
  .then(data => {
    document.getElementById("asteroid-count").textContent = data.hazardous_asteroids.length;
  })
  .catch(err => console.error("NEO fetch error:", err));
