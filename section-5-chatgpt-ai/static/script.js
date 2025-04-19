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


// Fetch solar activity data
fetch("/donki")
  .then(res => res.json())
  .then(data => {
    document.getElementById("solar-cmes").textContent = data.cme.length;
    document.getElementById("solar-flares").textContent = data.flares.length;
    document.getElementById("solar-storms").textContent = data.storms.length;
  })
  .catch(err => console.error("DONKI fetch error:", err));

// Fetch Mars weather data
fetch("/mars")
  .then(res => res.json())
  .then(data => {
    document.getElementById("mars-temp").textContent = data.temperature?.toFixed(1) ?? '--';
    document.getElementById("mars-wind").textContent = data.wind?.toFixed(1) ?? '--';
    document.getElementById("mars-pressure").textContent = data.pressure?.toFixed(1) ?? '--';
  })
  .catch(err => console.error("Mars fetch error:", err));


// Fetch Astronomy Picture of the Day
fetch("/apod")
  .then(res => res.json())
  .then(data => {
    document.getElementById("apod-title").textContent = data.title;
    document.getElementById("apod-date").textContent = data.date;
    document.getElementById("apod-img").src = data.url;
    document.getElementById("apod-modal-title").textContent = data.title;
    document.getElementById("apod-modal-text").textContent = data.explanation;
  })
  .catch(err => console.error("APOD fetch error:", err));

// Modal toggle


document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("apod-card").addEventListener("click", () => {
    document.getElementById("apod-modal").classList.remove("hidden");
  });

  document.getElementById("apod-close").addEventListener("click", () => {
    document.getElementById("apod-modal").classList.add("hidden");
  });
});

// Universal AI explanation handler
function explain(type) {
  fetch(`/ai/${type}`, { method: 'POST' })
    .then(res => res.text())
    .then(markdown => {
      const output = document.getElementById(`${type}-explanation`);
      if (output) {
        output.innerHTML = marked.parse(markdown);
      }
    })
    .catch(err => {
      console.error("AI fetch error:", err);
    });
}
