const apiBase = "http://127.0.0.1:5000";
const predictionForm = document.getElementById("prediction-form");
const yearInput = document.getElementById("year");
const predictButton = document.getElementById("predict-button");
const resultTitle = document.getElementById("result-title");
const resultMessage = document.getElementById("result-message");

function formatNumber(value) {
  return new Intl.NumberFormat("en-IN", { maximumFractionDigits: 2 }).format(value);
}

function drawChart(chartId, years, valueName) {
  const chart = document.getElementById(chartId);
  const recentYears = years.slice(-8);
  const maximum = Math.max(...recentYears.map(function (item) { return item[valueName]; })) || 1;

  recentYears.forEach(function (item) {
    const row = document.createElement("div");
    row.className = "bar-row";

    const year = document.createElement("span");
    year.textContent = item.year;

    const track = document.createElement("div");
    track.className = "bar-track";

    const fill = document.createElement("div");
    fill.className = "bar-fill";
    fill.style.width = (item[valueName] / maximum * 100) + "%";
    track.appendChild(fill);

    const value = document.createElement("span");
    value.className = "bar-value";
    value.textContent = formatNumber(item[valueName]);

    row.append(year, track, value);
    chart.appendChild(row);
  });
}

async function loadEconomyData() {
  const status = document.getElementById("data-status");

  try {
    const response = await fetch(apiBase + "/data");
    const data = await response.json();

    if (!response.ok) {
      throw new Error("Could not load economy data.");
    }

    document.getElementById("gdp-value").textContent = formatNumber(data.gdp);
    document.getElementById("imports-value").textContent = formatNumber(data.imports);
    document.getElementById("exports-value").textContent = formatNumber(data.exports);
    drawChart("gdp-chart", data.years, "gdp");
    drawChart("imports-chart", data.years, "imports");
    status.textContent = "Economy data loaded";
  } catch (error) {
    status.textContent = "Could not load data. Start the Flask backend and refresh.";
  }
}

predictionForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  if (!predictionForm.reportValidity()) {
    return;
  }

  predictButton.disabled = true;
  resultTitle.textContent = "Calculating prediction";
  resultMessage.textContent = "Sending the year to the model...";

  try {
    const response = await fetch(apiBase + "/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ year: Number(yearInput.value) })
    });
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "The prediction request failed.");
    }

    resultTitle.textContent = "Prediction for " + yearInput.value;
    resultMessage.textContent = "Predicted Imports_Crore: " + formatNumber(data.prediction) + " Crore";
  } catch (error) {
    resultTitle.textContent = "Prediction unavailable";
    resultMessage.textContent = error.message || "Could not connect to the Flask API.";
  } finally {
    predictButton.disabled = false;
  }
});

loadEconomyData();