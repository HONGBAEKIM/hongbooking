# 1.Imports

import pkg_resources #to check for installed package

import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime
import time
import random
import subprocess
import os
import sys

from flask import Flask, render_template, request, url_for, redirect
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/handle_form', methods=['POST'])
def handle_form():
    user_id_from_app = request.form.get('user_id')
    password_from_app = request.form.get('password')
    project_name_from_app = request.form.get('project_name')
    evaluation_day_from_app = request.form.get('evaluation_day')
    print("first: ", evaluation_day_from_app)

    start_time_from_app = request.form.get('start_time')
    end_time_from_app = request.form.get('end_time')

    # Process the form data as needed
    # For example, print the data to the console
    print(f'User ID: {user_id_from_app}')
    #print(f'User password: {password_from_app}')
    print(f'Project Name: {project_name_from_app}')
    print(f'Evaluation Day: {evaluation_day_from_app}')
    print(f'Start Time: {start_time_from_app}')
    print(f'End Time: {end_time_from_app}')

    #after clicking last step of booking icon, I should check if evaluation slot is booked

    #connected to my webpage







    # Retrieve parameters from command line arguments
    # user_id_from_app = sys.argv[1]
    # password_from_app = sys.argv[2]
    # project_name_from_app = sys.argv[3]
    # evaluation_day_from_app = sys.argv[4]
    # start_time_from_app = sys.argv[5]
    # end_time_from_app = sys.argv[6]

    # Process the parameters as needed
    # print(f'User ID: {user_id_from_app}')
    # print(f'Password: {password_from_app}')
    # print(f'Project Name: {project_name_from_app}')
    # print(f'Evaluation Day: {evaluation_day_from_app}')
    # print(f'Start Time: {start_time_from_app}')
    # print(f'End Time: {end_time_from_app}')

    # Set the environment variable
    os.environ["APP_PASSWORD"] = password_from_app


    #2.Setup Chrome WebDriver:
    #This line creates a ChromeOptions object, 
    #which allows you to set various options for the Chrome driver.
    chrome_binary_path = '/usr/bin/google-chrome'  # Adjust this path accordingly
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_binary_path
    #This option runs Chrome in headless mode, 
    #it will not display a UI or open a browser window.
    chrome_options.add_argument("--headless")
    
    
    localhost_number = random.randint(65536, 79999)
    chrome_options.add_experimental_option("debuggerAddress", f"localhost:{localhost_number}")

    driver = webdriver.Chrome()  # Add options=chrome_options if needed

    login_url = "https://auth.42.fr/auth/realms/students-42/protocol/openid-connect/auth?client_id=intra&redirect_uri=https%3A%2F%2Fprofile.intra.42.fr%2Fusers%2Fauth%2Fkeycloak_student%2Fcallback&response_type=code&state=e510170b7adc7ed8fc39319b0c9896692df12a594087df4c"

    driver.get(login_url)

    #log-in 
    def attempt_login(driver, username, password):
        username_field_id = "username"  # Replace with the actual ID of the username field
        password_field_id = "password"  # Replace with the actual ID of the password field

        try:
            WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.ID, username_field_id))
            )
            username_field = driver.find_element(By.ID, username_field_id)
            username_field.send_keys(username)

            WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.ID, password_field_id))
            )
            password_field = driver.find_element(By.ID, password_field_id)
            password_field.send_keys(password)

            password_field.send_keys(Keys.ENTER)
            
            # Wait for navigation and check if the login was successful
            WebDriverWait(driver, 1).until(EC.url_to_be("https://profile.intra.42.fr/"))

            print("Successfully logged in")
            return True  # Return True to indicate successful login

        except Exception as e:
            print("An error occurred:", e)
            return False  # Return False to indicate login failure


    print("Let's book an evaluation slot automatically")

    # Continue with the rest of your script after a successful login
    logged_in = False
    while not logged_in:
        username = user_id_from_app    
        password = password_from_app
        # print("Username is", username)
        # print("password is", password)

        logged_in = attempt_login(driver, username, password)
        if not logged_in:
            print("Login failed. Please try again.")


    # Dynamically build the URL
    base_url = "https://projects.intra.42.fr/projects"

    full_url = f"{base_url}/{project_name_from_app}/slots?team_id=True"

    # Navigate to the specified slots page
    driver.get(full_url)


    # valid_day_names = {"0",
    #                 "1"
    #                 "2",
    #                 "3"
    # }

    # project_day_mapping = {
    #     "today": "0",
    #     "tomorrow": "1",
    #     "2days": "2",
    #     "3days": "3"
    # }

    DAYS = {
        "today": 0,
        "tomorrow": 1,
        "2days": 2,
        "3days": 3
    }

    def attempt_day(evaluation_day):
        print("evaluation_day : ", evaluation_day)
        day_name = DAYS.get(evaluation_day, "invalid")
        if day_name == "invalid":
            print("Invalid day. Please check day list.")
            return False
        print("Successfully typed day")
        return True


    day_in = False
    while not day_in:
        evaluation_day = evaluation_day_from_app
        day_in = attempt_day(evaluation_day)
        if not day_in:
            print("day has not typed. Please try again.")

    int_evaluation_day = DAYS[evaluation_day]
    current_day = datetime.now().weekday()
    specialcase = 0
    #today is sunday
    if int_evaluation_day == 1 and current_day == 6:
        specialcase = 1
    elif int_evaluation_day == 2 and current_day == 6:
        specialcase = 2
    elif int_evaluation_day == 3 and current_day == 6:
        specialcase = 3
    #today is saturday   
    elif int_evaluation_day == 2 and current_day == 5:
        specialcase = 2
    elif int_evaluation_day == 3 and current_day == 5:
        specialcase = 3
    #today is friday 
    elif int_evaluation_day == 3 and current_day == 4:
        specialcase = 3
    else:
        specialcase = 0


    try:
        # just for test click next page is working or not
        #if (int_evaluation_day == 1):
        

        if not specialcase == 0:
            #I should click next page 
            try:
                wait = WebDriverWait(driver, 1)
                next_page_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-next-button.fc-button.fc-state-default.fc-corner-left.fc-corner-right")))       
                print("next page is ready?")
                next_page_button.click()
                print("Clicked next page")
                specialcase = 1

            except Exception as e:  # Consider catching specific exceptions
                print(f"Exception occurred: {str(e)}")
                # Additional error handling code here
            
    except TimeoutException:
            print("Timeout occurred while looking for slots. Refreshing and retrying...")
            driver.refresh()
            if not specialcase == 0:
            #I should click next page 
                try:
                    wait = WebDriverWait(driver, 1)
                    next_page_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-next-button.fc-button.fc-state-default.fc-corner-left.fc-corner-right")))       
                    print("next page is ready?")
                    next_page_button.click()
                    print("Clicked next page")
                    int_evaluation_day = 0  
                except Exception as e:  # Consider catching specific exceptions
                    print(f"Exception occurred: {str(e)}")
                    # Additional error handling code here 
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



    #Select time 
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
    max_retries = 100000
    attempts = 0






    while not slot_clicked and attempts < max_retries:
        try:
            attempts += 1
            print(f"{attempts} of {max_retries}")
            time.sleep(1)

            try:         
                available_slots_today = []                      
                #current_day = datetime.now().weekday()
                if not specialcase == 0:
                    xpath = f".//tr/td[{current_day + 2 + int_evaluation_day - specialcase}]//div[contains(@class, 'fc-time')]"
                else:
                    xpath = f".//tr/td[{current_day + 2 + int_evaluation_day}]//div[contains(@class, 'fc-time')]"
                slots = driver.find_elements(By.XPATH, xpath)

                if (len(slots) == 0):
                    driver.refresh()
                    if not specialcase == 0:
                        try:
                            wait = WebDriverWait(driver, 1)
                            next_page_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-next-button.fc-button.fc-state-default.fc-corner-left.fc-corner-right")))       
                            next_page_button.click()
                        except Exception as e:  # Consider catching specific exceptions
                            print("Exception occurred: ", str(e))
                            # Additional error handling code here 
                    time.sleep(1)
                    print("Grab a coffee and tea or watch a youtube video")
                    print("https://youtu.be/FClqKwgo5Bw?feature=shared")

                for slot in slots:
                    print("there is another available slot", slot.text)
                    time_str = slot.get_attribute("data-full").split(" - ")[0]
                    # Debugging: Check the type and value of time_str
                    #print("21 : time_str:", time_str, "Type:", type(time_str))

                    if is_time_within_range(convert_to_24hr_format(time_str), start_time_from_app, end_time_from_app):
                        print("30 : check time range")
                        available_slots_today.append(slot)

                if not available_slots_today:
                    print("No slots available within the desired time range.")
                    driver.refresh()
                    if not specialcase == 0:
                        try:
                            wait = WebDriverWait(driver, 1)
                            next_page_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-next-button.fc-button.fc-state-default.fc-corner-left.fc-corner-right")))       
                            next_page_button.click()
                        except Exception as e:  # Consider catching specific exceptions
                            print("Exception occurred: ", str(e))
                            # Additional error handling code here 
                    time.sleep(1)
                    continue

                
                
                for slot in available_slots_today:
                    print("40")
                    WebDriverWait(driver, 1).until(EC.element_to_be_clickable(slot))
                    print("41")
                    slot.click()
                    print("Clicked on an available slot.")
                    slot_clicked = True
                    
                    time.sleep(1)
                    # Find the "OK" button. Adjust the selector as per your page's structure
                    try:
                        nextok = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
                        if nextok.text == "OK":
                            
                            
                            #nextok.click()
                            time.sleep(2000)
                            
                            print("Clicked 'OK' button.")
                    except NoSuchElementException:
                        print("OK button not found.")
    
                    #break

            except NoSuchElementException:
                print("Today's column is not found or not highlighted.")
                driver.refresh()
                if not specialcase == 0:
                    try:
                        wait = WebDriverWait(driver, 1)
                        next_page_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-next-button.fc-button.fc-state-default.fc-corner-left.fc-corner-right")))       
                        next_page_button.click()
                    except Exception as e:  # Consider catching specific exceptions
                        print("Exception occurred: ", str(e))
                        # Additional error handling code here 
                time.sleep(1)

        except TimeoutException:
            print("Timeout occurred while looking for slots. Refreshing and retrying...")
            driver.refresh()
            if not specialcase == 0:
                try:
                    wait = WebDriverWait(driver, 1)
                    next_page_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-next-button.fc-button.fc-state-default.fc-corner-left.fc-corner-right")))       
                    next_page_button.click()
                except Exception as e:  # Consider catching specific exceptions
                    print("Exception occurred: ", str(e))
                    # Additional error handling code here 
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

    if attempts >= max_retries:
        print("Reached the maximum number of retries. Exiting.")


    time.sleep(1000)
    # Close the WebDriver
    #8.Close the WebDriver:
    #This line closes the browser and ends the WebDriver's session. 
    # It's important to include this to free up resources and not leave the browser running in the background.
    driver.quit()

    return "Form submitted successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
