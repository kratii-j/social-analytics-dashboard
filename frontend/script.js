function analyzeSentiment() {
  const text = document.getElementById("textInput").value;

  fetch("http://127.0.0.1:8000/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text: text }) 
  })
  .then(response => response.json()) 
  .then(data => {

    document.getElementById("result").innerText = `Sentiment: ${data.sentiment}`;
  })
  .catch(error => {

    document.getElementById("result").innerText = 'Error analyzing sentiment.';
    console.error("Error:", error);
  });
}
