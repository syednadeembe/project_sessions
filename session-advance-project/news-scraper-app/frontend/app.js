const backendUrl = "http://localhost:8000";

function searchNews() {
  const topic = document.getElementById("searchInput").value;
  fetch(`${backendUrl}/search?topic=${topic}`)
    .then(res => res.json())
    .then(data => {
      const resultsDiv = document.getElementById("results");
      resultsDiv.innerHTML = `<h2>Results (${data.source})</h2>`;
      data.results.forEach(article => {
        resultsDiv.innerHTML += `<p><a href="${article.link}" target="_blank">${article.title}</a></p>`;
      });
    });
}

function getHistory() {
  fetch(`${backendUrl}/history`)
    .then(res => res.json())
    .then(data => {
      const historyDiv = document.getElementById("history");
      historyDiv.innerHTML = `<h2>Search History</h2>`;
      data.forEach(item => {
        historyDiv.innerHTML += `<p>${item.topic} — ${new Date(item.created_at).toLocaleString()}</p>`;
      });
    });
}
