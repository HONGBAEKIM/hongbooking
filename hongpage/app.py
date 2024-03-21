from flask import Flask, render_template, jsonify, session, send_from_directory, request
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


# Directory where your files are located
directory = '/home/ubuntu/2booking/cgi-bin/downloadfiles'

@app.route('/download_student')
def download_file():
    # Check if the IP address is already in the session
    ip_address = request.remote_addr
    if 'downloads' not in session:
        session['downloads'] = {}
    if ip_address not in session['downloads']:
        session['downloads'][ip_address] = {'count': 0, 'last_download': datetime.now()}

    # Check if the user has exceeded the download limit
    limit_per_hour = 5
    time_difference = datetime.now() - session['downloads'][ip_address]['last_download']
    if time_difference.total_seconds() > 3600:
        session['downloads'][ip_address] = {'count': 0, 'last_download': datetime.now()}
    if session['downloads'][ip_address]['count'] >= limit_per_hour:
        return "You have reached the maximum download limit for this hour."

    # Increment the download count and update last download time
    session['downloads'][ip_address]['count'] += 1
    session['downloads'][ip_address]['last_download'] = datetime.now()

    # Specify the filename you want to download
    filename = 'hongbooking19_studente'
    return send_from_directory(directory=directory, path=filename, as_attachment=True)


@app.route('/download_piscine')
def download_piscine():
    # Check if the IP address is already in the session
    ip_address = request.remote_addr
    if 'downloads' not in session:
        session['downloads'] = {}
    if ip_address not in session['downloads']:
        session['downloads'][ip_address] = {'count': 0, 'last_download': datetime.now()}

    # Check if the user has exceeded the download limit
    limit_per_hour = 5
    time_difference = datetime.now() - session['downloads'][ip_address]['last_download']
    if time_difference.total_seconds() > 3600:
        session['downloads'][ip_address] = {'count': 0, 'last_download': datetime.now()}
    if session['downloads'][ip_address]['count'] >= limit_per_hour:
        return "You have reached the maximum download limit for this hour."

    # Increment the download count and update last download time
    session['downloads'][ip_address]['count'] += 1
    session['downloads'][ip_address]['last_download'] = datetime.now()

    # Specify the filename you want to download
    filename = 'hongbooking19_piscine'
    return send_from_directory(directory=directory, path=filename, as_attachment=True)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
