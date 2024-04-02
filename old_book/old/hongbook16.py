# 1.Install selenium library
import subprocess
import pkg_resources #to check for installed package
import sys  # Import the sys module

def install(library_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])

def is_library_installed(library_name):
    try:
        pkg_resources.get_distribution(library_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

library_name = "selenium"

if is_library_installed(library_name):
    print(f"{library_name} is already installed.")
else:
    print(f"{library_name} is not installed. Installing now...")
    install(library_name)
    print(f"{library_name} installed successfully.")


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



#2.Setup Chrome WebDriver:
#This line creates a ChromeOptions object, 
#which allows you to set various options for the Chrome driver.
#options = webdriver.ChromeOptions()
chrome_options = Options()

localhost_number = random.randint(65536, 65999)
chrome_options.add_experimental_option("debuggerAddress", f"localhost:{localhost_number}")

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
def login_process(driver):
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
print("                born")
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
print("                webserv")
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

valid_project_names = {"42cursus-libft",
                "42cursus-ft_printf",
                "42cursus-get_next_line",
                "born2beroot",
                "so_long",
                "42cursus-fdf",
                "42cursus-fract-ol",
                "42cursus-push_swap",
                "minitalk",
                "pipex",
                "42cursus-philosophers",
                "42cursus-minishell",
                "minirt",
                "cub3d",
                "netpractice",
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
    "libft": "42cursus-libft",
    "born": "born2beroot",
    "ftprintf": "42cursus-ft_printf",
    "gnl": "42cursus-get_next_line",
    "solong": "so_long",
    "fdf": "42cursus-fdf",
    "fractol": "42cursus-fract-ol",
    "pushswap": "42cursus-push_swap",
    "minitalk": "minitalk",
    "pipex": "pipex",
    "philo": "42cursus-philosophers",
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

def get_project_name():
    
    project_name_in = False
    while not project_name_in:
        project_name = input("Please type project name: ")

        
        project_name_in = attempt_project_name(project_name)
        if not project_name_in:
            print("Project name is invalid. Please try again.")
    return project_name_mapping.get(project_name, project_name)


def build_eval_page_url(project_name_input):
    base_url = "https://projects.intra.42.fr/projects"
    full_url = f"{base_url}/{project_name_input}/slots?team_id=True"
    return full_url

# Navigate to the specified slots page
#driver.get(full_url)



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

def get_evaluation_day():
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
    return evaluation_day


def handle_evaluation_day(driver):
    try:         
        int_evaluation_day = int(get_evaluation_day)
        current_day = datetime.now().weekday()
        if (int_evaluation_day == 1 and current_day == 6):
            try:
                wait = WebDriverWait(driver, 5)
                next_page_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-next-button.fc-button.fc-state-default.fc-corner-left.fc-corner-right")))       
                print("next page is ready?")
                next_page_button.click()
                print("Clicked next page")
                int_evaluation_day = 0
            except Exception as e:  
                print("Exception occurred: ", str(e))
            
    except TimeoutException:
            print("Timeout occurred while looking for slots. Refreshing and retrying...")
            driver.refresh()        
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


###########change it to 

    #Select evaluation time 
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














#check how many evaluation you already booked?
#and after click the booking, program should check how many evaluation is booked now.

#there is 3 options
# 1) there is 0 evaluation booked, after program runs 1 should be booked.
# 2) there is 1 evaluation booked, after program runs 2 should be booked.
# 3) there are 2 evaluation booked, after program runs 3 should be booked.
    
#if there is 0 evaluation booked, then check there is any new booking
# 
        








def run_eval_program(driver, full_url, int_evaluation_day, desired_start_time, desired_end_time):

   








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

                            #nextok.click()
                            print("Clicked 'OK' button.")
                            time.sleep(5)

                            
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













    
def get_data_scale_team_values(url_current_booking):
    # Set up the Selenium WebDriver (make sure you have the appropriate WebDriver for your browser)
    #driver = webdriver.Chrome()  # Change this line based on your browser choice and WebDriver installation

    try:
        # Open the URL in the browser
        driver.get(url_current_booking)

        # Find the elements with class 'project-item' and attribute 'data-scale-team'
        project_items_before = driver.find_elements(By.CSS_SELECTOR, '.project-item[reminder][data-scale-team]')
        number_project_items_before = len(project_items_before)
        print("How many booking has already booked : ", number_project_items_before)
        


        #values_before = set(item.get_attribute('data-scale-team') for item in project_items_before)

        # Run your program here
    

####################################################################




####################################################################




        # Reload the page to capture the changes
        driver.get(url_current_booking)

        # Find the elements again after running your program
        project_items_after = driver.find_elements(By.CSS_SELECTOR, '.project-item[reminder][data-scale-team]')
        #values_after = set(item.get_attribute('data-scale-team') for item in project_items_after)

        number_project_items_after = len(project_items_after)
        print("How many booking has already booked : ", number_project_items_after)

        # Identify newly generated values
        new_values = number_project_items_after - number_project_items_before

        return new_values

    except Exception as e:
        # Handle any exceptions that may occur
        print(f"Error: {e}")
        return None

    







time.sleep(50)
# Close the WebDriver
#8.Close the WebDriver:
#This line closes the browser and ends the WebDriver's session. 
# It's important to include this to free up resources and not leave the browser running in the background.
driver.quit()






def main():

    login_process(driver)
    project_name_input = get_project_name()
    full_url = build_eval_page_url(project_name_input)
    
    evaluation_day = get_evaluation_day()
    handle_evaluation_day(driver)
    





    url_current_booking = f"{base_url}/{project_name_input}/{username}"

    new_values = get_data_scale_team_values(url_current_booking)

    if new_values == 1:
        print("Successful. Do you want to book next evaluation?")
        #go back where you can put time and go back to while loop and run
    else:
        print("Try agian")
        #go back to while loop and run

if __name__ == "__main__":
    main()










