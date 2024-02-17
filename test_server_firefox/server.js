const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Set the server response timeout to 2 minutes (120,000 milliseconds)
const serverTimeout = 120000; // 2 minutes in milliseconds

// Middleware to parse JSON and URL-encoded bodies
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));



// Endpoint to handle POST requests from the client
app.post('/hongbooking', (req, res) => {
    
    const formData = req.body;

    // Process the form data here (e.g., save to database)
    // For demonstration purposes, let's log the form data
    console.log('Form data received:', formData);

    // Check if form data is valid
    if (formData && formData.username && formData.password) {
        // Form data is valid
        // You can perform additional processing or validation here
        
        // Send a success response to the client
        res.status(200).json({ message: 'Form data received successfully', success: true });
    } else {
        // Form data is invalid or incomplete
        // Send an error response to the client
        res.status(400).json({ message: 'Invalid form data', success: false });
    }
});

// Endpoint to provide status information to the client
app.get('/hongbooking/status', (req, res) => {
    // Assuming attempts is defined or retrieved from your Flask application
    // You need to modify this part to fetch the attempt count from your Flask application
    // For example, if your Flask application exposes an endpoint to provide the attempt count,
    // you would make a request to that endpoint to get the attempt count
    fetch('/hongbooking/status')
        .then(response => response.json())
        .then(data => {
            // Extract the attempt count and max retries from the response
            const { attempts, maxRetries } = data;
            // Send the status information to the client
            res.json({ attempts, maxRetries });
        })
        .catch(error => {
            console.error('Error fetching status:', error);
            // In case of an error, send a response indicating the error
            res.status(500).json({ error: 'Failed to fetch status' });
        });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});
