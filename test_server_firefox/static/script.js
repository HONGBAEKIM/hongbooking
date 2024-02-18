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


// Ensure the socket object is properly defined and initialized
var socket = io();

document.addEventListener('DOMContentLoaded', function() {
    // Request attempt count from the server
    socket.emit('attempt_count_request');

    // Listen for the response from the server
    socket.on('attempt_count', function(data) {
        console.log('Attempt count:', data.attempt);
        // Update the UI with the attempt count
        var progressDiv = document.getElementById('progress');
        progressDiv.innerHTML = '<p>' + data.attempt + ' / 3</p>';
    });
});


// document.addEventListener('DOMContentLoaded', function() {
//     var socket = io();
//     // Listen for the status update from the server
//     socket.on('status_update', function(data) {
//         console.log('Status update received:', data);
//         // Update the UI with the attempt count and max retries
//         document.getElementById('attemptCount').innerText = data.attempts;
//         document.getElementById('maxRetries').innerText = data.maxRetries;
//     });
// });

