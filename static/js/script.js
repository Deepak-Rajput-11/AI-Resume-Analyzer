const form = document.querySelector("form");
const resultsDiv = document.getElementById("results");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const resume = document.getElementById("resume").files[0];
  const jd_text = document.getElementById("jd_text").value;

  if (!resume) {
    resultsDiv.innerHTML = "<p>Please upload a resume.</p>";
    return;
  }

  if (!jd_text.trim()) {
    resultsDiv.innerHTML = "<p>Please enter a job description.</p>";
    return;
  }

  const formData = new FormData();

  formData.append("resume", resume);
  formData.append("jd_text", jd_text);

  fetch("/analyze", {
    method: "POST",
    body: formData,
  })
    .then((response) => {
      if (!response.ok) {
        return response.text().then((message) => {
          throw new Error(message);
        });
      }

      return response.json();
    })
    .then((data) => {
      resultsDiv.innerHTML = `
      <h2>Analysis Results</h2>
      <p>Skill Match: ${data.match_percentage}%</p>
      <p>Text Similarity: ${data.text_similarity}%</p>
      <p>Semantic Similarity: ${data.semantic_similarity}%</p>

      <h3>Matching Skills</h3>
      <p>${data.matching_skills.join(", ")}</p>

      <h3>Missing Skills</h3>
      <p>${data.missing_skills.join(", ")}</p>
    `;
    })
    .catch((error) => {
      resultsDiv.innerHTML = `<p>${error.message}</p>`;
    });
});
