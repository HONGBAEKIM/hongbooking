from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
from flasgger import Swagger


app = Flask(__name__)
swagger = Swagger(app)

# This dictionary will store generated licenses with their expiration times
licenses = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hongbooking')
def hongbooking():
    return render_template('hongbooking.html')

# @app.route('/submit_booking', methods=['GET', 'POST'])
@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    # Handle form submission logic here
    # For example, you can access form data using request.form
    # Process the form data and return a response
    # return render_template('hongbooking.html')
    return 'Booking submitted successfully'

@app.route('/generate_license', methods=['POST'])
def generate_license():
    user_id = request.json.get('user_id')
    expiration_time = datetime.now() + timedelta(hours=1)
    licenses[user_id] = expiration_time
    return jsonify({'message': 'License generated successfully'})

@app.route('/validate_license', methods=['POST'])
def validate_license():
    user_id = request.json.get('user_id')
    if user_id in licenses and licenses[user_id] > datetime.now():
        return jsonify({'valid': True})
    else:
        return jsonify({'valid': False})

@app.route('/update_expiration', methods=['POST'])
def update_expiration():
    user_id = request.json.get('user_id')
    new_expiration_time = datetime.now() + timedelta(hours=1)
    licenses[user_id] = new_expiration_time
    return jsonify({'message': 'Expiration time updated successfully'})

@app.route('/hello/<string:name>', methods=['GET'])
def hello(name):
    """
    This is an example endpoint that returns a greeting message.
    ---
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: The name to greet
    responses:
      200:
        description: A greeting message
    """
    return jsonify({'message': 'Hello, {}!'.format(name)})





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
