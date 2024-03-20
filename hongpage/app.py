from flask import Flask, render_template, request, jsonify
from datetime import datetime
import hashlib


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hongbooking')
def hongbooking():
    return render_template('hongbooking.html')


def generate_password():
    # Generate password based on current time
    current_time = datetime.datetime.now()
    password_str = str(current_time)
    password_hash = hashlib.sha256(password_str.encode()).hexdigest()
    return password_hash[:32]  # Return first 32 characters of the hash as the password




# @app.route('/submit_booking', methods=['GET', 'POST'])
@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    password = generate_password()
    # Handle form submission logic here
    # For example, you can access form data using request.form
    # Process the form data and return a response
    # return render_template('hongbooking.html')
    return f'Booking submitted successfully. Password: {password}'



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
