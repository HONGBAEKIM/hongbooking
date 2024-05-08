#!/usr/bin/env python3


#program runs with argv[1] password
#ex)
#hongbooking19 *****




import sys
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime
#from webdriver_manager.chrome import ChromeDriverManager
#from undetected_chromedriver import Chrome
#import undetected_chromedriver as uc 

from seleniumbase import Driver


import time
import random


from pyotp import TOTP



import requests


#log-in 
def attempt_login(driver, username, password):
    username_field_id = "username"  # Replace with the actual ID of the username field
    password_field_id = "password"  # Replace with the actual ID of the password field
    login_url = "https://auth.42.fr/auth/realms/students-42/protocol/openid-connect/auth?client_id=intra&redirect_uri=https%3A%2F%2Fprofile.intra.42.fr%2Fusers%2Fauth%2Fkeycloak_student%2Fcallback&response_type=code&state=e510170b7adc7ed8fc39319b0c9896692df12a594087df4c"

    driver.get(login_url)
    time.sleep(1)

    try:
        # WebDriverWait(driver, 1).until(
        #     EC.element_to_be_clickable((By.ID, username_field_id))
        # )
        
        # EC.element_to_be_clickable(By.ID, username_field_id)
        
        username_field = driver.find_element(By.ID, username_field_id)
        username_field.send_keys(username)

        # WebDriverWait(driver, 1).until(
        #     EC.element_to_be_clickable((By.ID, password_field_id))
        # )
        # EC.element_to_be_clickable(By.ID, password_field_id)
        password_field = driver.find_element(By.ID, password_field_id)
        password_field.send_keys(password)

        password_field.send_keys(Keys.ENTER)
        
        # Wait for navigation and check if the login was successful
        WebDriverWait(driver, 0.5).until(EC.url_to_be("https://profile.intra.42.fr/"))
        
        print("Successfully logged in")
        return True  # Return True to indicate successful login

    except Exception as e:
        print("An error occurred:", e)
        return False  # Return False to indicate login failure




def printsubject():
    #Select project
    print("Login script completed")
    print("project_names = bsq")
    print("                shell00")
    print("                shell01")
    print("                c00")
    print("                c01")
    print("                c02")
    print("                c03")
    print("                c04")
    print("                c05")
    print("                c06")
    print("                c07")
    print("                c08")
    print("                c09")
    print("                c10")
    print("                c11")
    print("                c12")
    print("                c13")
    print("check above projects name")

valid_project_names = {"c-piscine-bsq",
                 "c-piscine-shell-00",
                 "c-piscine-shell-01",
                 "c-piscine-c-00",
                 "c-piscine-c-01",
                 "c-piscine-c-02",
                 "c-piscine-c-03",
                 "c-piscine-c-04",
                 "c-piscine-c-05",
                 "c-piscine-c-06",
                 "c-piscine-c-07",
                 "c-piscine-c-08",
                 "c-piscine-c-09",
                 "c-piscine-c-10",
                 "c-piscine-c-11",
                 "c-piscine-c-12",
                 "c-piscine-c-13"        
}

project_name_mapping = {
    "bsq": "c-piscine-bsq",
    "shell00": "c-piscine-shell-00",
    "shell01": "c-piscine-shell-01",
    "c00": "c-piscine-c-00",
    "c01": "c-piscine-c-01",
    "c02": "c-piscine-c-02",
    "c03": "c-piscine-c-03",
    "c04": "c-piscine-c-04",
    "c05": "c-piscine-c-05",
    "c06": "c-piscine-c-06",
    "c07": "c-piscine-c-07",
    "c08": "c-piscine-c-08",
    "c09": "c-piscine-c-09",
    "c10": "c-piscine-c-10",
    "c11": "c-piscine-c-11",
    "c12": "c-piscine-c-12",
    "c13": "c-piscine-c-13"
}

def attempt_project_name(project_name):
    
    mapped_name = project_name_mapping.get(project_name, project_name)
    if mapped_name in valid_project_names:
        
        print("Successfully typed project name")
        return True
    else:
        print("Invalid project name. Please check above project list.")
        return False



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



# Function to convert 12-hour format time to 24-hour format
def convert_to_24hr_format(time_str):
    try:
        return datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M")
    except ValueError:
        print(f"Error converting time: {time_str}")
        return None

# Function to check if the slot time is within the desired range
def is_time_within_range(time_str, start_time, end_time):
    try:
        slot_time = datetime.strptime(time_str, "%H:%M").time()  # Expecting 24-hour format
        return start_time <= slot_time <= end_time
    except ValueError as e:
        print(f"Error parsing time: {time_str} - {e}")
        return False

def get_current_password():
    response = requests.get('https://www.hongpage.com/get_password')
    data = response.json()
    return data['password']

def main():

 

    #Define the correct password
    correct_password = get_current_password()

    entered_password = sys.argv[1]

    print("Welcome to Hongbooking(my name is Hongbaekim)!")


    if entered_password != correct_password:
        print("Incorrect password. Access denied.")
        return


    # If the correct password is entered, continue with your program logic
    print("Access granted. Running the program...")


    

    #before make a.out file
    #before make a.out file
    #before make a.out file
    #if (len(sys.argv) != 2):
    # if (len(sys.argv) != 3):
    #     print("Usage: hongbooking19 <password>")
    #     try:
    #         driver.quit()
    #     except NameError:
    #         pass  # Ignore if the driver is not defined
    #     sys.exit(1)  # Terminate the program with a non-zero exit code
    


    #options = uc.ChromeOptions()
    #localhost_number = random.randint(65536, 65999)
    #options.add_experimental_option("debuggerAddress", f"localhost:{localhost_number}")    
    #chromedriver_path = '/home/hongbaki/bin/chromedriver'
    #driver = uc.Chrome(driver_executable_path=chromedriver_path ,options=options)
    
    
    
    #driver = Driver(uc=True, incognito=True)
    
    # options.add_argument("--headless")



    driver = Driver(uc=True)

    

    print("Let's book an evaluation slot automatically")

    # Continue with the rest of your script after a successful login
    logged_in = False
    while not logged_in:
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        logged_in = attempt_login(driver, username, password)
        if not logged_in:
            print("Login failed. Please try again.")
    

    project_name_in = False
    while not project_name_in:
        printsubject()
        project_name = input("Please type project name: ")

        
        project_name_in = attempt_project_name(project_name)
        if not project_name_in:
            print("Project name is invalid. Please try again.")

    project_name_input = project_name_mapping.get(project_name, project_name)

    # Dynamically build the URL
    base_url = "https://projects.intra.42.fr/projects"

    full_url = f"{base_url}/{project_name_input}/slots?team_id=True"

    # Navigate to the specified slots page
    driver.get(full_url)

    int_evaluation_day = 0


    time_in = False
    while not time_in:
        print("ex) 10:00 AM = 10:00")
        print("ex)  1:00 PM = 13:00")
        print("ex)  9:00 PM = 21:00")

        start_time = input("Enter your desired start time (24-hour format): ")
        end_time = input("Enter your desired end time (24-hour format): ")

        time_in = attempt_time(start_time, end_time)
        if not time_in:
            print("time has not typed. Please try again.")

    # Set the desired time for the slot
    desired_start_time = datetime.strptime(start_time, "%H:%M").time()  # 24-hour format
    desired_end_time = datetime.strptime(end_time, "%H:%M").time()  # 24-hour format


    # This flag will indicate whether a slot has been successfully clicked
    slot_clicked = False
    attempts = 0
    program_start_time = time.time()  # Get the current time in seconds
    previous_elapsed_time = time.time() - program_start_time - 1
    
    time_min_is_60 = 60
    ###################################################
    #################################################
    time_for_min = 20 #20min
    #################################################
    ###################################################
    setting_time = time_for_min * time_min_is_60 

    while not slot_clicked:
        elapsed_time = time.time() - program_start_time
        if elapsed_time > setting_time:
            
            print("Reached the " , setting_time ,"min. Exiting.")

            driver.quit()  # Close the WebDriver
            sys.exit()  # Terminate the program
        
        # Add code here to handle the situation when elapsed_time is not getting smaller
        if elapsed_time <= previous_elapsed_time:
            print("Elapsed time is not decreasing. Taking necessary action...")
            driver.quit()  # Close the WebDriver
            sys.exit()  # Terminate the program
            
        previous_elapsed_time = elapsed_time
        
        
        try:
        
            attempts += 1
            print(f"{attempts}, booking attempt")
            time.sleep(1)

            try:         
                available_slots_today = []                      
                current_day = datetime.now().weekday()
                xpath = f".//tr/td[{current_day + 2 + int_evaluation_day}]//div[contains(@class, 'fc-time')]"
                slots = driver.find_elements(By.XPATH, xpath)
                if (len(slots) == 0):
                    driver.refresh()
                print("Every 20 min, new password will be regenerated")
                print("New password is here")
                print("www.hongpage.com/hongbooking")

                for slot in slots:
                    print("there is another available slot", slot.text)
                    time_str = slot.get_attribute("data-full").split(" - ")[0]
                    # Debugging: Check the type and value of time_str
                    #print("21 : time_str:", time_str, "Type:", type(time_str))

                    if is_time_within_range(convert_to_24hr_format(time_str), desired_start_time, desired_end_time):
                        available_slots_today.append(slot)

                if not available_slots_today:
                    print("No slots available within the desired time range.")
                    driver.refresh()
                    #################################################
                    ###################################################
                    time.sleep(0.5)
                    #################################################
                    ###################################################
                    continue
                

                for slot in available_slots_today:

                    # WebDriverWait(driver, 1).until(EC.element_to_be_clickable(slot))
                    
                    EC.element_to_be_clickable(slot)

                    slot.click()
                    print("Clicked on an available slot.")
                    slot_clicked = True
                    
                    #time.sleep(1)
                    # Find the "OK" button. Adjust the selector as per your page's structure
                    try:
                        
                        nextok = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(nextok))
                        if nextok.text == "OK":
                            
                            
                            print("BEFORE: Clicking 'OK' button.")
                            nextok.click()
                            print("AFTER: Clicked 'OK' button.")
                    except NoSuchElementException:
                        print("OK button not found.")
    
                    #break

            except NoSuchElementException:
                print("Today's column is not found or not highlighted.")
                driver.refresh()
                time.sleep(15)

        except TimeoutException:
            print("Timeout occurred while looking for slots. Refreshing and retrying...")
            driver.refresh()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

    


    #time.sleep(50)
    # Close the WebDriver
    #8.Close the WebDriver:
    #This line closes the browser and ends the WebDriver's session. 
    # It's important to include this to free up resources and not leave the browser running in the background.
    driver.quit()



if __name__ == "__main__":
    main()


