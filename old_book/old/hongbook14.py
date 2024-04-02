
# 1st error - it saied booked but actually it was not
# so I changed WebDriverWait 5 to 0.5 sec
# let's see

#automatically install selenium if there is no selenium package.
# 1.Imports
import subprocess
import pkg_resources
import sys  # Import the sys module

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    # Try to import the selenium package
    pkg_resources.require("selenium")
    print("Selenium is already installed.")

except pkg_resources.DistributionNotFound:
    # If selenium is not installed, install it
    print("Selenium is not installed. Installing now...")
    install("selenium")
    print("Selenium installed successfully.")

except pkg_resources.VersionConflict as e:
    # Handle cases where the installed version does not match the required version
    print(f"A version conflict was detected: {e}")
    # Optionally, upgrade the package or handle the conflict as required
    # install("selenium --upgrade")

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

#2.Setup Chrome WebDriver:
#This line creates a ChromeOptions object, 
#which allows you to set various options for the Chrome driver.
#options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:65536")

#This option runs Chrome in headless mode, 
#it will not display a UI or open a browser window.
########################################################################
#options.add_argument("--headless")  # Run in headless mode, without a UI.
########################################################################

driver = webdriver.Chrome()  # Add options=chrome_options if needed


#log-in 
def attempt_login(driver, username, password):
    username_field_id = "username"  # Replace with the actual ID of the username field
    password_field_id = "password"  # Replace with the actual ID of the password field
    login_url = "https://auth.42.fr/auth/realms/students-42/protocol/openid-connect/auth?client_id=intra&redirect_uri=https%3A%2F%2Fprofile.intra.42.fr%2Fusers%2Fauth%2Fkeycloak_student%2Fcallback&response_type=code&state=e510170b7adc7ed8fc39319b0c9896692df12a594087df4c"

    driver.get(login_url)
    time.sleep(1)

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
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    logged_in = attempt_login(driver, username, password)
    if not logged_in:
        print("Login failed. Please try again.")


#Select project
print("Login script completed")
print("project_names = libft")
print("                ftprintf")
print("                gnl")
print("                solong")
print("                fdf")
print("                fractol")
print("                pushswap")
print("                minitalk")
print("                pipex")
print("                philo")
print("                minishell")
print("                minirt")
print("                cub3d")
print("                netp")
print("                inc")
print("                webser")
print("                ftirc")
print("                cpp00")
print("                cpp01")
print("                cpp02")
print("                cpp03")
print("                cpp04")
print("                cpp05")
print("                cpp06")
print("                cpp07")
print("                cpp08")
print("                cpp09")
print("                fttran")
print("check above projects name")

valid_project_names = {"libft",
                 "Born2beroot"
                 "ft_printf",
                 "get_next_line",
                 "so_long",
                 "fdf",
                 "fract-ol",
                 "push_swap",
                 "minitalk",
                 "pipex",
                 "philosophers",
                 "42cursus-minishell",
                 "minirt",
                 "cub3d",
                 "netPractice",
                 "inception",
                 "webserv",
                 "ft_irc",
                 "cpp-module-00",
                 "cpp-module-01",
                 "cpp-module-02",
                 "cpp-module-03",
                 "cpp-module-04",
                 "cpp-module-05",
                 "cpp-module-06",
                 "cpp-module-07",
                 "cpp-module-08",
                 "cpp-module-09",
                 "ft_transcendence"
}

project_name_mapping = {
    "libft": "libft",
    "Born2beroot": "Born2beroot",
    "ftprintf": "ft_printf",
    "gnl": "get_next_line",
    "solong": "so_long",
    "fdf": "fdf",
    "fractol": "fract-ol",
    "pushswap": "push_swap",
    "minitalk": "minitalk",
    "pipex": "pipex",
    "philo": "philosophers",
    "minishell": "42cursus-minishell",
    "minirt": "minirt",
    "cub3d": "cub3d",
    "netp": "netpractice",
    "inc": "inception",
    "webserv": "webserv",
    "ftirc": "ft_irc",
    "cpp00": "cpp-module-00",
    "cpp01": "cpp-module-01",
    "cpp02": "cpp-module-02",
    "cpp03": "cpp-module-03",
    "cpp04": "cpp-module-04",
    "cpp05": "cpp-module-05",
    "cpp06": "cpp-module-06",
    "cpp07": "cpp-module-07",
    "cpp08": "cpp-module-08",
    "cpp09": "cpp-module-09",
    "fttran": "ft_transcendence"
}

def attempt_project_name(project_name):
    
    mapped_name = project_name_mapping.get(project_name, project_name)
    if mapped_name in valid_project_names:
        
        print("Successfully typed project name")
        return True
    else:
        print("Invalid project name. Please check above project list.")
        return False

project_name_in = False
while not project_name_in:
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


#Put date
#today or tomorrow

valid_day_names = {"today",
                 "tomorrow"
                 #"in_2_days",
                 #"in_3_days"
}

project_day_mapping = {
    "0": "today",
    "1": "tomorrow"
    #"2": "in_2_days",
    #"3": "in_3_days"
}

def attempt_day(evaluation_day): 
    day_name = project_day_mapping.get(evaluation_day, evaluation_day)
    if day_name in valid_day_names:
        print("Successfully typed day")
        return True
    else:
        print("Invalid day. Please check day list.")
        return False


day_in = False
while not day_in:
    print("date : 0      (today)")
    print("       1      (tomorrow)")
    #print("       2      (in 2 days)")
    #print("       3      (in 3 days)")

    evaluation_day = input("Enter your desired evaluation day (0 or 1) : ")
    day_in = attempt_day(evaluation_day)
    if not day_in:
        print("day has not typed. Please try again.")



#so let's just handle today and tomorrow first!!!!!
#Here manage if today() is sunday and you want to book tomorrow eval.
#eval page should be shown next week slot 
try:         
    int_evaluation_day = int(evaluation_day)
    
    # just for test click next page is working or not
    #if (int_evaluation_day == 1):
    current_day = datetime.now().weekday()

    if (int_evaluation_day == 1 and current_day == 6):
        #I should click next page 
        try:
            wait = WebDriverWait(driver, 5)
            next_page_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-next-button.fc-button.fc-state-default.fc-corner-left.fc-corner-right")))       
            print("next page is ready?")
            next_page_button.click()
            print("Clicked next page")
            int_evaluation_day = 0

        except Exception as e:  # Consider catching specific exceptions
            print("Exception occurred: ", str(e))
            # Additional error handling code here
        
except TimeoutException:
        print("Timeout occurred while looking for slots. Refreshing and retrying...")
        driver.refresh()        
    
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
    print("ex) 10:00 AM = 10:00")
    print("ex)  1:00 PM = 13:00")
    start_time = input("Enter your desired start time (24-hour format): ")
    end_time = input("Enter your desired end time (24-hour format): ")

    time_in = attempt_time(start_time, end_time)
    if not time_in:
        print("time has not typed. Please try again.")

# Set the desired time for the slot
desired_start_time = datetime.strptime(start_time, "%H:%M").time()  # 24-hour format
desired_end_time = datetime.strptime(end_time, "%H:%M").time()  # 24-hour format

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
            current_day = datetime.now().weekday()
            xpath = f".//tr/td[{current_day + 2 + int_evaluation_day}]//div[contains(@class, 'fc-time')]"
            slots = driver.find_elements(By.XPATH, xpath)

            if (len(slots) == 0):
                driver.refresh()
            print("Grab a coffee and tea or watch a youtube video")
            print("https://youtu.be/FClqKwgo5Bw?feature=shared")

            for slot in slots:
                print("there is another available slot", slot.text)
                time_str = slot.get_attribute("data-full").split(" - ")[0]
                # Debugging: Check the type and value of time_str
                #print("21 : time_str:", time_str, "Type:", type(time_str))

                if is_time_within_range(convert_to_24hr_format(time_str), desired_start_time, desired_end_time):
                    print("30 : check time range")
                    available_slots_today.append(slot)

            if not available_slots_today:
                print("No slots available within the desired time range.")
                driver.refresh()
                time.sleep(5)
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
                        
                        
                        nextok.click()
                        
                        
                        print("Clicked 'OK' button.")
                except NoSuchElementException:
                    print("OK button not found.")
 
                #break

        except NoSuchElementException:
            print("Today's column is not found or not highlighted.")
            driver.refresh()
            time.sleep(5)

    except TimeoutException:
        print("Timeout occurred while looking for slots. Refreshing and retrying...")
        driver.refresh()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        break

if attempts >= max_retries:
    print("Reached the maximum number of retries. Exiting.")

time.sleep(5)
# Close the WebDriver
#8.Close the WebDriver:
#This line closes the browser and ends the WebDriver's session. 
# It's important to include this to free up resources and not leave the browser running in the background.
driver.quit()

