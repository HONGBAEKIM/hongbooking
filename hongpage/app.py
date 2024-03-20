from flask import Flask, render_template, jsonify, session
from datetime import datetime, timedelta
import hashlib
import random
import string
import time
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.secret_key = 'bQHbgRtIv5PtkwRgMMwVQd4JzFeDFJqempwh48dUqHObo'

current_password = None

def generate_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(36))

def update_password():
    global current_password
    current_password = generate_password()
    print("New password generated:", current_password)

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(update_password, 'interval', minutes=30)
scheduler.start()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hongbooking')
def hongbooking():
    global current_password
    if current_password is None:
        current_password = generate_password()
        print("Initial password generated:", current_password)
    else:
        print("Password found:", current_password)
    return render_template('hongbooking.html', password=current_password)



@app.route('/get_password')
def get_password():
    global current_password
    return jsonify({'password': current_password})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
