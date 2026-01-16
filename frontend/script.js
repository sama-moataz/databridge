const form = document.getElementById('upload-form');
const results = document.getElementById('results');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  results.textContent = "Uploading and analyzing...";

  const formData = new FormData();
  formData.append('file', document.getElementById('csv').files[0]);
  formData.append('gold_file', document.getElementById('gold').files[0]);

  const response = await fetch('https://YOUR_RENDER_URL/analyze-csv/', {
    method: 'POST',
    body: formData
  });
  const data = await response.json();
  results.textContent = JSON.stringify(data, null, 2);
});

