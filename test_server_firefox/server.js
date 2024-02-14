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

    // Send a response to the client
    res.json({ message: 'Form data received successfully', success: true });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});