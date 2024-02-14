const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

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

// Start the server
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});
