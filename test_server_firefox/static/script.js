// // Define a global variable to store the value of attempts
// let attempts = 0;
// let maxRetries = 0;

// // Function to fetch status information from the server
// function getStatus() {
//     fetch('/hongbooking/status')
//         .then(response => response.json())
//         .then(data => {
//             // Update the attempts variable with the latest attempt count from the server
//             attempts = data.attempts;
//             maxRetries = data.maxRetries;

//             // Update the status display
//             updateStatus();
//         })
//         .catch(error => console.error('Error fetching status:', error));
// }

// // Function to update the status display
// function updateStatus() {
//     document.getElementById('attemptCount').innerText = attempts;
//     document.getElementById('maxRetries').innerText = maxRetries;
// }

// // Call getStatus function initially to fetch status when the page loads
// getStatus();

// // Example of how you might call getStatus periodically to update the attempt count
// setInterval(getStatus, 5000); // Update every 5 seconds (adjust as needed)

// Request attempt count from the server
socket.emit('attempt_count_request');

// Listen for the response from the server
socket.on('attempt_count', function(data) {
    console.log('Attempt count:', data.attempt);
    // Update the UI with the attempt count
});
