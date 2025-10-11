
// ===== TalentMatchAI Frontend Script =====

// Set your backend base URL (update if needed)
const API_BASE_URL = "https://talentmatchai.onrender.com";

// Handle upload (mock functionality for now)
document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const uploadStatus = document.getElementById("uploadStatus");
  uploadStatus.textContent = "Analyzing CVs... Please wait ⏳";

  // Normally, you'd send a file to the backend here.
  // For demo purposes, we simulate a short delay.
  setTimeout(() => {
    uploadStatus.textContent = "✅ Upload complete. Click 'Fetch Rankings' to see AI results.";
  }, 2000);
});

// Fetch ranked candidates
document.getElementById("fetchRankings").addEventListener("click", async () => {
  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "Fetching ranked candidates... 🔍";

  try {
    const response = await fetch(`${API_BASE_URL}/ranked_candidates`);
    if (!response.ok) throw new Error("Network error or endpoint unavailable.");

    const data = await response.json();
    displayResults(data);
  } catch (error) {
    resultsDiv.innerHTML = `<p class="error">❌ Error fetching data: ${error.message}</p>`;
  }
});

// Display ranked applicants dynamically
function displayResults(data) {
  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "";

  if (!Array.isArray(data) || data.length === 0) {
    resultsDiv.innerHTML = "<p>No results found.</p>";
    return;
  }

  data.forEach((candidate) => {
    const card = document.createElement("div");
    card.className = "candidate-card";
    card.innerHTML = `
      <h3>${candidate.name}</h3>
      <p><strong>Score:</strong> ${candidate.score}</p>
      <ul>
        ${candidate.reasons.map((r) => `<li>${r}</li>`).join("")}
      </ul>
    `;
    resultsDiv.appendChild(card);
  });
}