# 1.Imports

import pkg_resources #to check for installed package

import getpass

import subprocess
from selenium import webdriver

# from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime
import time


# from pyvirtualdisplay import Display
import random

import os
import sys

#from flask import jsonify

import logging
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit


# Define the default GeckoDriver path
geckodriver_path = "/usr/local/bin/geckodriver"

# Specify the default path to the Firefox binary
firefox_binary_location = '/usr/bin/firefox'

# Move the definition of firefox_options outside of the function
firefox_options = FirefoxOptions()

app = Flask(__name__)



# Set logging level to DEBUG for more detailed logs
logging.basicConfig(level=logging.DEBUG)

CORS(app, resources={r"/socket.io/*": {"origins": "https://www.hongpage.com"}})

socketio = SocketIO(app, cors_allowed_origins="https://www.hongpage.com", async_mode='eventlet')










#log-in 
def attempt_login(driver, username, password):
    username_field_id = "username"  # Replace with the actual ID of the username field
    password_field_id = "password"  # Replace with the actual ID of the password field

    try:
        # WebDriverWait(driver, 1).until(
        #     EC.element_to_be_clickable((By.ID, username_field_id))
        # )
        username_field = driver.find_element(By.ID, username_field_id)
        username_field.send_keys(username)

        # WebDriverWait(driver, 1).until(
        #     EC.element_to_be_clickable((By.ID, password_field_id))
        # )
        password_field = driver.find_element(By.ID, password_field_id)
        password_field.send_keys(password)

        password_field.send_keys(Keys.ENTER)
    
        # Wait for navigation and check if the login was successfuld

        # WebDriverWait(driver, 5).until(EC.url_to_be("https://profile.intra.42.fr/"))
        return True  # Return True to indicate successful login

    except Exception as e:
        print("An error occurred:", e)
        return False  # Return False to indicate login failure
    
@app.route('/is_running')
def check_if_running():
  return jsonify({
    'is_running': True 
  })

@app.route('/hongbooking')
def index():
    return render_template('index.html')

@app.route('/hongbooking/handle_form', methods=['POST'])
def handle_form():
    user_id_from_app = request.form.get('user_id')
    password_from_app = request.form.get('password')
    project_name_from_app = request.form.get('project_name')
    #evaluation_day_from_app = request.form.get('evaluation_day')
    start_time_from_app = request.form.get('start_time')
    end_time_from_app = request.form.get('end_time')

    #This option runs Chrome in headless mode, 
    #it will not display a UI or open a browser window.
    firefox_options.add_argument('--headless')

    # Set the path to the Firefox binary
    firefox_options.binary_location = firefox_binary_location
    
    # Specify the path to the GeckoDriver executable using the executable_path property
    firefox_options.executable_path = geckodriver_path

    # Instantiate Firefox WebDriver using FirefoxOptions
    try:
        # Instantiate Firefox WebDriver using FirefoxOptions
        driver = webdriver.Firefox(options=firefox_options)
        login_url = "https://auth.42.fr/auth/realms/students-42/protocol/openid-connect/auth?client_id=intra&redirect_uri=https%3A%2F%2Fprofile.intra.42.fr%2Fusers%2Fauth%2Fkeycloak_student%2Fcallback&response_type=code&state=e510170b7adc7ed8fc39319b0c9896692df12a594087df4c"
        
        # Open the login URL
        driver.get(login_url)
        
        # Further actions with the WebDriver can be added here

    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        return jsonify({"error": "Error initializing WebDriver"})

    # Continue with the rest of your script after a successful login
    logged_in = False
    
    while not logged_in:
        username = user_id_from_app    
        password = password_from_app

        logged_in = attempt_login(driver, username, password)
        if logged_in:

            print("loged_in")
            
        else:
            
            login_response = {
            'message': 'Login failed. Please try again.',
            'step': 'login',
            'success': False
            }

            return jsonify({
                'login_response': login_response,
            })
            

    # Dynamically build the URL
    base_url = "https://projects.intra.42.fr/projects"

    full_url = f"{base_url}/{project_name_from_app}/slots?team_id=True"

    # Navigate to the specified slots page
    driver.get(full_url)



    current_day = datetime.now().weekday()
    
    


    # Select time 
    def is_valid_time(time_str):
        try:
            datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False

    def attempt_time(start_time, end_time):
        if is_valid_time(start_time) and is_valid_time(end_time):
            print("Successfully typed desired_eval_time")
            return True
        else:
            print("Invalid time format. Please use HH:MM format.")
            return False

    time_in = False
    while not time_in:

        start_time = start_time_from_app
        end_time = end_time_from_app

        time_in = attempt_time(start_time, end_time)
        if not time_in:
            print("time has not typed. Please try again.")

    # Set the desired time for the slot
    start_time_from_app = datetime.strptime(start_time, "%H:%M").time()  # 24-hour format
    end_time_from_app = datetime.strptime(end_time, "%H:%M").time()  # 24-hour format

    # Function to convert 12-hour format time to 24-hour format
    def convert_to_24hr_format(time_str):
        try:
            return datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M")
        except ValueError:
            print(f"Error converting time: {time_str}")
            return None

    # Function to check if the slot time is within the desired range
    def is_time_within_range(time_str, start_time_from_app, end_time_from_app):
        try:
            slot_time = datetime.strptime(time_str, "%H:%M").time()  # Expecting 24-hour format
            return start_time_from_app <= slot_time <= end_time_from_app
        except ValueError as e:
            print(f"Error parsing time: {time_str} - {e}")
            return False

    # This flag will indicate whether a slot has been successfully clicked
    slot_clicked = False
    max_retries = 10
    attempts = 0


    while not slot_clicked and attempts < max_retries:
        try:
            attempts += 1
            print(f"{attempts} of {max_retries}")
            
            available_slots_today = []                      
            xpath = f".//tr/td[{current_day + 2}]//div[contains(@class, 'fc-time')]"
            slots = driver.find_elements(By.XPATH, xpath)
            
            if (len(slots) == 0):
                time.sleep(10)
                driver.refresh()

                
            for slot in slots:
                
                print("(2)there is another available slot", slot.text)
                time_str = slot.get_attribute("data-full").split(" - ")[0]
                
                if is_time_within_range(convert_to_24hr_format(time_str), start_time_from_app, end_time_from_app):
                    print("30 : check time range")
                    available_slots_today.append(slot)

            for slot in available_slots_today:
                # WebDriverWait(driver, 1).until(EC.element_to_be_clickable(slot))
                slot.click()
                print("(4)Clicked on an available slot.")
                slot_clicked = True
                    
                try:
                    nextok = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
                    if nextok.text == "OK":
                        
                        # WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
                        #nextok.click()
                        print("Clicked 'OK' button.")
                
                             
                        slot_booking_response = {
                            'message': 'Slot booked successfully.',
                            'step': 'slot_booking',
                            'success': True
                        }
                        return jsonify({
                            'slot_booking_response': slot_booking_response
                        })
         
                
                except NoSuchElementException:
                    print("OK button not found.")
    
                    #break

        except TimeoutException:
            print("Timeout occurred while looking for slots. Refreshing and retrying...")
            driver.refresh()
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

    if attempts >= max_retries:
        print("Reached the maximum number of retries. Exiting.")

    driver.quit()
    return render_template('index.html')



if __name__ == '__main__':  
    # app.run(host='0.0.0.0', port=5000)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
