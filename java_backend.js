function predict() {
    var emailSubject = document.getElementById('emailSubject').value;
    var emailBody = document.getElementById('emailBody').value;
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({subject: emailSubject, body: emailBody})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.result;
    });
}
