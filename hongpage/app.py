from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hongbooking')
def hongbooking():
    return render_template('hongbooking.html')

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    # Handle form submission logic here
    # For example, you can access form data using request.form
    # Process the form data and return a response
    return render_template('hongbooking.html')
    #return 'Booking submitted successfully'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)





