document.getElementById("recommendation-form").addEventListener("submit", function(event) {
    event.preventDefault();

    let ph = parseFloat(document.getElementById("ph").value);
    let temperature = parseFloat(document.getElementById("temperature").value);
    let humidity = parseFloat(document.getElementById("humidity").value);

    // Send input values to backend
    fetch('/recommend-crop', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ph: ph,
            temperature: temperature,
            humidity: humidity
        })
    })
    .then(response => response.json())
    .then(data => {
        // Display recommendation on the frontend
        document.getElementById("recommendation-result").innerText = "Recommended Crop: " + data.crop;
    })
    .catch(error => console.error('Error:', error));
});
