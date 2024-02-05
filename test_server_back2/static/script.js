


// Example JavaScript for interactivity (optional)
document.addEventListener('DOMContentLoaded', function () 
{
    // You can add JavaScript functionality here
    console.log('Website loaded successfully.');
});


// var socket = new WebSocket('wss://www.hongpage.com/socket.io/?EIO=4&transport=websocket');

var socket = io.connect('http://localhost:5000');

socket.on('connect', function() {
    console.log('Connected to server');
});

socket.on('message', function(data) {
    console.log('Server says:', data.data);
});

socket.on('progress', function(data) {
    document.getElementById('progress').innerText = data.data;
});

socket.on('process_complete', function(data) {
    console.log('Process completed:', data.data);
});

function startProcess() {
    socket.emit('start_process', { message: 'Start the process' });
}

