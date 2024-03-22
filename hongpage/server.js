// const express = require('express');
// const bodyParser = require('body-parser');
// const http = require('http');
// const socketIo = require('socket.io');
// const fetch = require('node-fetch'); // Import fetch module

// const app = express();
// const PORT = process.env.PORT || 3000;

// // Set the server response timeout to 2 minutes (120,000 milliseconds)
// const serverTimeout = 1200000; // 20 minutes in milliseconds

// // Middleware to parse JSON and URL-encoded bodies
// app.use(bodyParser.json());
// app.use(bodyParser.urlencoded({ extended: true }));

// // Create HTTP server
// const server = http.createServer(app);

// // Set the server response timeout
// server.setTimeout(serverTimeout);

// const io = socketIo(server, {
//     // pingInterval: 1200000, // Check client connectivity every 20 minutes
//     // pingTimeout: 1200000,  // Consider the connection disconnected if no response after 20 minutes
//     pingInterval: 10000, // Check client connectivity every 10 sec
//     pingTimeout: 10000,  // Consider the connection disconnected if no response after 10 sec
//   });

// // Socket.IO event handlers
// io.on('connection', (socket) => {
//     console.log('A client connected');

//     socket.on('disconnect', () => {
//         console.log('A client disconnected');
//     });
// });

// // Endpoint to handle POST requests from the client
// app.post('/hongbooking', (req, res) => {
//     const formData = req.body;

//     // Process the form data here (e.g., save to database)
//     // For demonstration purposes, let's log the form data
//     console.log('Form data received:', formData);

//     // Check if form data is valid
//     if (formData && formData.username && formData.password) {
//         // Form data is valid
//         // You can perform additional processing or validation here
        
//         // Emit the attempt count to the client
//         io.emit('attempt_count', { attempt: session.get('attempts', 0) });

//         // Send a success response to the client
//         res.status(200).json({ message: 'Form data received successfully', success: true });
//     } else {
//         // Form data is invalid or incomplete
//         // Send an error response to the client
//         res.status(400).json({ message: 'Invalid form data', success: false });
//     }
// });

// // Endpoint to provide status information to the client
// // app.get('/hongbooking/status', (req, res) => {
// app.get('/hongbooking', (req, res) => {

//     // Assuming attempts is defined or retrieved from your Flask application
//     // You need to modify this part to fetch the attempt count from your Flask application
//     // For example, if your Flask application exposes an endpoint to provide the attempt count,
//     // you would make a request to that endpoint to get the attempt count
//     // fetch('/hongbooking/status')
//     fetch('/hongbooking/status')
//         .then(response => response.json())
//         .then(data => {
//             // Extract the attempt count and max retries from the response
//             const { attempts, maxRetries } = data;
//             // Send the status information to the client
//             res.json({ attempts, maxRetries });
//         })
//         .catch(error => {
//             console.error('Error fetching status:', error);
//             // In case of an error, send a response indicating the error
//             res.status(500).json({ error: 'Failed to fetch status' });
//         });
// });

// // Allow GET requests for /hongbooking/status
// app.get('/hongbooking/status', (req, res) => {
//     // Here you can provide the status directly or fetch from other sources
//     res.json({ attempts: 0, maxRetries: 5 }); // Example response, modify as needed
// });

// // Start the server
// server.listen(PORT, () => {
//     console.log(`Server is listening on port ${PORT}`);
// });



//this is for counting how many people are in my website
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

let userCount = 0;

io.on('connection', (socket) => {
    userCount++; // Increment user count
    io.emit('user count', { count: userCount }); // Update all clients

    socket.on('disconnect', () => {
        userCount--; // Decrement user count
        io.emit('user count', { count: userCount }); // Update all clients
    });
});

// Serve your static files (HTML, CSS, etc.)
app.use(express.static('/var/www/html/static'));  

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => console.log(`Server running on port ${PORT}`));

