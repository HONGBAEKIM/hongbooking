# 1.Imports
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
#import requests





# Set up the Chrome WebDriver

#2.Setup Chrome WebDriver:
#This line creates a ChromeOptions object, 
#which allows you to set various options for the Chrome driver.
#options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:65536")

#This option runs Chrome in headless mode, 
#it will not display a UI or open a browser window.


########options.add_argument("--headless")  # Run in headless mode, without a UI.


driver = webdriver.Chrome()  # Add options=chrome_options if needed


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

# Initialize WebDriver (make sure chrome_options is defined if you use it)


# Continue with the rest of your script after a successful login
logged_in = False
while not logged_in:
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    logged_in = attempt_login(driver, username, password)
    if not logged_in:
        print("Login failed. Please try again.")

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
                 "minishell",
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
    "minishell": "minishell",
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

time.sleep(1)

project_name_input = project_name_mapping.get(project_name, project_name)

# Dynamically build the URL
base_url = "https://projects.intra.42.fr/projects"



#########################################################
#########################################################
#########################################################

# # Replace with your actual access token
# access_token = "YOUR_ACCESS_TOKEN"

# # API endpoint
# url = "https://api.intra.42.fr/v2/projects_users/18"

# # Headers with authorization
# headers = {
#     "Authorization": f"Bearer {access_token}"
# }

# # Send a GET request to the API
# response = requests.get(url, headers=headers)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()
#     # Extract current_team_id
#     current_team_id = data['current_team_id']
#     print(f"Current Team ID: {current_team_id}")
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")

#everyone has different team_id
#forexample 
#hongbae has "5374260"
#Ramesh has  "5395823"

# def is_valid_team_id(team_id):
#     try:
#         team_id.isdigit() and len(team_id) == 7
#         return True
#     except ValueError:
#         return False

# def attempt_team_id(team_id):
#     if is_valid_team_id(team_id):
#         print("Successfully typed team_id")
#         return True
#     else:
#         print("Invalid team_id. Please fill out 7 digits of team_id.")
#         return False


# team_id = False
# while not team_id:
#     print("https://projects.intra.42.fr/projects/slots?team_id=XXXXXXX")
#     print("write down last 7 digits")

#     team_id = input("team_id : ")
#     team_id_in = attempt_team_id(team_id)
#     if not team_id_in:
#         print("time has not typed. Please try again.")


#team_id = "5374260"  # Replace with the actual team ID 
#########################################################
#########################################################
#########################################################



full_url = f"{base_url}/{project_name_input}/slots?team_id=True"

# Navigate to the specified slots page
driver.get(full_url)


time.sleep(1)



##
#
#
##
#
#
##
#
#
##
#
#
#
##
#
#
##
#
#
##
#
#
##
#
#
#

time.sleep(2)

#def attempt_time(driver, start_time, end_time):    


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

#########################################################
#########################################################
#########################################################
# Set the desired time for the slot
desired_start_time = datetime.strptime(start_time, "%H:%M").time()  # 24-hour format
desired_end_time = datetime.strptime(end_time, "%H:%M").time()  # 24-hour format
# desired_start_time = datetime.strptime("13:00", "%H:%M").time()  # 24-hour format
# desired_end_time = datetime.strptime("23:45", "%H:%M").time()  # 24-hour format


#########################################################
#########################################################
#########################################################

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

        todays_date_str = datetime.today().strftime("%Y-%m-%d")
        try:         
            #initialize today_colume with 'fc-state-highlight' from html
            today_column = driver.find_element(By.CSS_SELECTOR, f"td.fc-day.fc-widget-content.fc-today.fc-state-highlight[data-date='{todays_date_str}']")       
            html_of_element = today_column.get_attribute('outerHTML')
            available_slots_today = []

            time.sleep(1)
                       
            current_day = datetime.now().weekday()
            xpath = f".//tr/td[{current_day + 2}]//div[contains(@class, 'fc-time')]"
            slots = driver.find_elements(By.XPATH, xpath)

            if (len(slots) == 0):
                driver.refresh()
            print("Grab a coffee or tea")
            print("Hongbae is my name : Hungry baby")

            
            for slot in slots:
                print("20 : slot.text", slot.text)
                
                time_str = slot.get_attribute("data-full").split(" - ")[0]
                # Debugging: Check the type and value of time_str
                print("21 : time_str:", time_str, "Type:", type(time_str))

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
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable(slot))
                print("41")
                slot.click()
                print("Clicked on an available slot.")
                slot_clicked = True
                
                time.sleep(5)
                # Find the "OK" button. Adjust the selector as per your page's structure
                try:
                    nextok = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
                    if nextok.text == "OK":
                        
                        ###########last
                        ###########last
                        ###########last
                        #nextok.click()
                        ###########last
                        ###########last
                        ###########last
                        
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

    time.sleep(2)

if attempts >= max_retries:
    print("Reached the maximum number of retries. Exiting.")


time.sleep(20)

# Close the WebDriver
#8.Close the WebDriver:
#This line closes the browser and ends the WebDriver's session. 
# It's important to include this to free up resources and not leave the browser running in the background.
#driver.quit()

