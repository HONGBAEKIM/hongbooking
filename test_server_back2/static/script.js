


// Example JavaScript for interactivity (optional)
document.addEventListener('DOMContentLoaded', function () 
{
    // You can add JavaScript functionality here
    console.log('Website loaded successfully.');
});


var socket = new WebSocket('wss://www.hongpage.com/socket.io/?EIO=4&transport=websocket');

// Listen for 'open' event
socket.addEventListener('open', function(event) {
    console.log('WebSocket connection opened:', event);
});

// Listen for 'message' event
socket.addEventListener('message', function(event) {
    console.log('WebSocket message received:', event.data);
});

// Listen for 'close' event
socket.addEventListener('close', function(event) {
    console.log('WebSocket connection closed:', event);
});

// Listen for 'error' event
socket.addEventListener('error', function(error) {
    console.error('WebSocket error:', error);
});

