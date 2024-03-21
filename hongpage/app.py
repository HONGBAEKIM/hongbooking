from flask import Flask, render_template, jsonify, session, send_from_directory, request
from datetime import datetime, timedelta, timezone
import hashlib
import random
import string


from apscheduler.schedulers.background import BackgroundScheduler
import os
import pytz

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





from datetime import datetime, timezone

def download_file(filename):
    # Check if the IP address is already in the session
    ip_address = request.remote_addr
    if 'downloads' not in session:
        session['downloads'] = {}
    if ip_address not in session['downloads']:
        session['downloads'][ip_address] = {'count': 0, 'last_download': datetime.now(timezone.utc)}

    # Check if the user has exceeded the download limit
    limit_per_hour = 5
    last_download_time = session['downloads'][ip_address]['last_download']
    current_time = datetime.now(timezone.utc)
    time_difference_seconds = (current_time - last_download_time).total_seconds()
    print("Time difference in seconds:", time_difference_seconds)
    if time_difference_seconds >= 8474 + 3600:
        session['downloads'][ip_address] = {'count': 0, 'last_download': current_time}
        print("Count reset for IP:", ip_address)
    if session['downloads'][ip_address]['count'] >= limit_per_hour:
        print("Download limit reached for IP:", ip_address)
        return "You have reached the maximum download limit for this hour."

    print("Count value before +1:", session['downloads'][ip_address]['count'])
    
    # Increment the download count
    session['downloads'][ip_address]['count'] += 1
    print("Count +1 value :", session['downloads'][ip_address]['count'])

    # Send the file for download
    response = send_from_directory(directory=directory, path=filename, as_attachment=True)
    
    # If download is successful, update last download time
    if response.status_code == 200:
        session['downloads'][ip_address]['last_download'] = current_time
        print("!!Count +1 value :", session['downloads'][ip_address]['count'])
    return response






# def download_file(filename):
#     # Check if the IP address is already in the session
#     ip_address = request.remote_addr
#     if 'downloads' not in session:
#         session['downloads'] = {}
#     if ip_address not in session['downloads']:
#         session['downloads'][ip_address] = {'count': 0, 'last_download': datetime.now(tz=utc_timezone)}
#     # Check if the user has exceeded the download limit
#     limit_per_hour = 5
#     last_download_time = session['downloads'][ip_address]['last_download']
#     print("last_download_time : ", last_download_time)
#     # time_difference = datetime.now(tz=utc_timezone) - last_download_time
#     # if time_difference.total_seconds() >= 3600:
#     #     session['downloads'][ip_address] = {'count': 0, 'last_download': datetime.now(tz=utc_timezone)}
#     #     print("Count reset for IP:", ip_address)
    
    
#     if session['downloads'][ip_address]['count'] >= limit_per_hour:
#         print("Download limit reached for IP:", ip_address)
#         return "You have reached the maximum download limit for this hour."


#     print("Count value before +1:", session['downloads'][ip_address]['count'])
#     # Increment the download count and update last download time
#     session['downloads'][ip_address]['count'] += 1
#     print("Count +1 value :", session['downloads'][ip_address]['count'])
#     session['downloads'][ip_address]['last_download'] = datetime.now(tz=utc_timezone)

#     # Send the file for download
#     response = send_from_directory(directory=directory, path=filename, as_attachment=True)
    
#     # If download is successful, update last download time
#     if response.status_code == 200:
#         session['downloads'][ip_address]['last_download'] = datetime.now(tz=utc_timezone)
#         print("!!Count +1 value :", session['downloads'][ip_address]['count'])
#     return response


@app.route('/download_student')
def download_student():
    return download_file('hongbooking19_student')

@app.route('/download_piscine')
def download_piscine():
    return download_file('hongbooking19_piscine')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
