document.addEventListener("DOMContentLoaded", function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    // Log socket connection status
    socket.on('connect', function() {
        console.log('Socket connected');
        
        // Emit a test status update event after connection
        socket.emit('status_update', { data: 'Test status update' });
    });

    // Listen for 'status_update' messages from the server
    socket.on('status_update', function (data) {
        console.log(data.data);  // Log the received message

        // Update the status container with the received message
        var statusContainer = document.getElementById('status-container');
        statusContainer.innerHTML += `<p>${data.data}</p>`;

        // Optionally, you can scroll to the bottom to always show the latest status
        statusContainer.scrollTop = statusContainer.scrollHeight;
    });

    // Log any socket errors
    socket.on('error', function (error) {
        console.error('Socket error:', error);
    });

    // Additional functions and logic for your application can go here
});


// Example JavaScript for interactivity (optional)
document.addEventListener('DOMContentLoaded', function () 
{
    // You can add JavaScript functionality here
    console.log('Website loaded successfully.');
});
