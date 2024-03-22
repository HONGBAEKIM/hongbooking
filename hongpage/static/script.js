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




// document.addEventListener('DOMContentLoaded', function() {
//     // Ensure the socket object is properly defined and initialized
//     var socket = io();
    
//     // Request attempt count from the server
//     socket.emit('attempt_count_request');
    
//     // Listen for the response from the server
//     socket.on('attempt_count', function(data) {
//         console.log('Attempt count:', data.attempt);
//         // Update the UI with the attempt count
//         var progressDiv = document.getElementById('progress');
//         progressDiv.innerHTML = '<p>' + data.attempt + ' / 3</p>'; // Append attempt count to existing content
//     });
// });


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


// document.addEventListener('DOMContentLoaded', function() {
//     // Initialize the SocketIO connection
//     var socket = io();

//     // Function to update the UI with the attempt count
//     function updateUI(attempt) {
//         var progressDiv = document.getElementById('progress');
//         progressDiv.innerHTML = '<p>' + attempt + ' / 3</p>';
//     }

//     // Listen for the attempt_count event from the server
//     socket.on('attempt_count', function(data) {
//         console.log('Attempt count:', data.attempt);
//         // Update the UI with the received attempt count
//         updateUI(data.attempt);
//     });

//     // Request the initial attempt count from the server upon page load
//     socket.emit('request_attempt_count');

//     // Print out every 3 seconds
//     setInterval(function() {
//         console.log('Printing every 3 seconds');
//     }, 3000); // 3000 milliseconds = 3 seconds
    
//     // Function to set a cookie
//     function setCookie(cname, cvalue, exdays) {
//         var d = new Date();
//         d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
//         var expires = "expires=" + d.toUTCString();
//         document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
//     }

//     // Function to check if the user has accepted cookies
//     function checkCookie() {
//         var consent = getCookie("cookieConsent");
//         if (consent === "") {
//             // Show cookie consent banner if consent cookie is not set
//             document.getElementById("cookieConsent").style.display = "block";
//         } else {
//             // Hide cookie consent banner if consent cookie is set
//             document.getElementById("cookieConsent").style.display = "none";
//         }
//     }

//     // Function to get a cookie by name
//     function getCookie(cname) {
//         var name = cname + "=";
//         var decodedCookie = decodeURIComponent(document.cookie);
//         var ca = decodedCookie.split(';');
//         for (var i = 0; i < ca.length; i++) {
//             var c = ca[i];
//             while (c.charAt(0) === ' ') {
//                 c = c.substring(1);
//             }
//             if (c.indexOf(name) === 0) {
//                 return c.substring(name.length, c.length);
//             }
//         }
//         return "";
//     }

//     // Function to accept cookies and hide the cookie consent banner
//     function acceptCookies() {
//         setCookie("cookieConsent", "accepted", 365); // Cookie expires in 365 days
//         document.getElementById("cookieConsent").style.display = "none";
//     }

//     // Check cookie consent when the page loads
//     window.onload = function () {
//         checkCookie();
//     };
// });



// // Connect to the server using Socket.IO
// var socket = io();

// // Listen for the 'user count' event from the server
// socket.on('user count', function(data) {
//     // Update the user count display with the count received from the server
//     document.getElementById('usersOnline').textContent = data.count;
// });
