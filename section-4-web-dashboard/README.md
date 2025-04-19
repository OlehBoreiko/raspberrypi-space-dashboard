# Section 4 – APOD Photo of the Day with Metadata and Modal Popup

This step integrates NASA’s Astronomy Picture of the Day (APOD) directly into the bottom of your dashboard with a centered image and metadata.

---

## ✅ Fix in script.py

Ensure your `/apod` route returns a valid image URL:

```python
output = {
    "title": data["title"],
    "date": data["date"],
    "explanation": data["explanation"][:300],
    "url": data["url"]
}
```

---

## 🖼️ HTML Section at Bottom of Page

```html
<div class="bg-gray-800 p-4 rounded cursor-pointer" id="apod-card">
  <h2 class="text-xl font-semibold" id="apod-title">--</h2>
  <p id="apod-date">--</p>
  <div class="flex justify-center mt-2">
    <img id="apod-img" class="rounded max-h-96" src="" alt="APOD" />
  </div>
</div>

<div id="apod-modal" class="hidden fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50">
  <div class="bg-white text-black p-6 rounded max-w-xl">
    <button id="apod-close" class="float-right text-gray-500">✖</button>
    <h2 id="apod-modal-title" class="text-xl font-bold mb-2"></h2>
    <p id="apod-modal-text"></p>
  </div>
</div>
```

---

## 🚀 JS Fetch + Modal Toggle

```js
fetch("/apod")
  .then(res => res.json())
  .then(data => {
    document.getElementById("apod-title").textContent = data.title;
    document.getElementById("apod-date").textContent = data.date;
    document.getElementById("apod-img").src = data.url;
    document.getElementById("apod-modal-title").textContent = data.title;
    document.getElementById("apod-modal-text").textContent = data.explanation;
  });

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("apod-card").addEventListener("click", () => {
    document.getElementById("apod-modal").classList.remove("hidden");
  });
  document.getElementById("apod-close").addEventListener("click", () => {
    document.getElementById("apod-modal").classList.add("hidden");
  });
});
```

---

## 🎯 Final Result

- APOD image appears at the bottom of the dashboard
- Title and date are visible at a glance
- Full description opens in a clean modal popup
