function predict() {
    const incident = document.getElementById("incident").value;

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ incident: incident })
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = "<h2>Predicted Sections:</h2>";
        data.results.forEach(item => {
            resultsDiv.innerHTML += `<div class="result-box">
                <strong>${item.section_number} - ${item.section_title}</strong><br>
                ${item.content}
            </div>`;
        });
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function startVoice() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-IN";
    recognition.start();

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById("incident").value = transcript;
    };
}
