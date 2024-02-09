
// var socket = new WebSocket('wss://www.hongpage.com/socket.io/?EIO=4&transport=websocket');

document.addEventListener('DOMContentLoaded', function () {
    var socket = io('https://www.hongpage.com'); // Replace with your actual server URL

    // Handle 'checking' event
    socket.on('checking', function (data) {
        updateMessage('Checking event: ' + data.data);
    });

    // Handle 'login_success' event
    socket.on('login_success', function (data) {
        updateMessage('Login success event: ' + data.data);
    });

    // Handle 'booked' event
    socket.on('booked', function (data) {
        updateMessage('Booked event: ' + data.data);
    });

    // Function to update the message container
    function updateMessage(message) {
        var messageContainer = document.getElementById('messageContainer');

        // Create a new paragraph element
        var newParagraph = document.createElement('p');

        // Set the text content of the paragraph
        newParagraph.textContent = message;

        // Append the new paragraph to the message container
        messageContainer.appendChild(newParagraph);
    }
});



// Example JavaScript for interactivity (optional)
document.addEventListener('DOMContentLoaded', function () 
{
    // You can add JavaScript functionality here
    console.log('Website loaded successfully.');
});



