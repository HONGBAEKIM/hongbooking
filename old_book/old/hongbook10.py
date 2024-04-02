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



print("Let's book evaluation slot automatically")
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

#3.Initialize WebDriver:
#This line initializes a new instance of Chrome with the specified options.
driver = webdriver.Chrome(options=chrome_options)


username_field_id = "username"  # Replace with the actual ID of the username field
password_field_id = "password"  # Replace with the actual ID of the password field

# Replace with the actual login URL
login_url = "https://auth.42.fr/auth/realms/students-42/protocol/openid-connect/auth?client_id=intra&redirect_uri=https%3A%2F%2Fprofile.intra.42.fr%2Fusers%2Fauth%2Fkeycloak_student%2Fcallback&response_type=code&state=ae365667127c864fe9576c8eb3f4285649467e597d498f6f"

# Navigate to the login page
driver.get(login_url)

time.sleep(2)

try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, username_field_id))
    )
    username_field = driver.find_element(By.ID, username_field_id)
    username_field.send_keys(username)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, password_field_id))
    )
    password_field = driver.find_element(By.ID, password_field_id)
    password_field.send_keys(password)

    password_field.send_keys(Keys.ENTER)

except Exception as e:
    print("An error occurred:", e)


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
project_name = input("Please type project name: ")

project_name_mapping = {
    "ftprintf": "ft_printf",
    "gnl": "get_next_line",
    "solong": "so_long",
    "fractol": "fract-ol",
    "pushswap": "push_swap",
    "philo": "philosophers",
    "netp": "netpractice",
    "inc": "inception",
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

project_name = project_name_mapping.get(project_name, project_name)

# if project_name == "cpp06":
#     project_name = "cpp-module-06"
# if project_name == "cpp07":
#     project_name = "cpp-module-07"
# if project_name == "cpp08":
#     project_name = "cpp-module-08"
# if project_name == "cpp09":
#     project_name = "cpp-module-09"



# Navigate to the slots page
#5.Navigate to Slots Page:
#After logging in, the script navigates to the slots page where the available slots are listed.


time.sleep(2)
# Dynamically build the URL
base_url = "https://projects.intra.42.fr/projects"

#########################################################
#########################################################
#########################################################
#everyone has different team_id
#forexample 
#hongbae has "5374260"
#Ramesh has  "5395823"
team_id = "5374260"  # Replace with the actual team ID 
#########################################################
#########################################################
#########################################################






# project_names = ["libft",
#                  "Born2beroot"
#                  "ft_printf",
#                  "get_next_line",
#                  "so_long",
#                  "fdf",
#                  "fract-ol",
#                  "push_swap",
#                  "minitalk",
#                  "pipex",
#                  "philosophers",
#                  "minishell",
#                  "minirt",
#                  "cub3d",
#                  "netPractice",
#                  "inception",
#                  "webserv",
#                  "ft_irc",
#                  "cpp-module-00",
#                  "cpp-module-01",
#                  "cpp-module-02",
#                  "cpp-module-03",
#                  "cpp-module-04",
#                  "cpp-module-05",
#                  "cpp-module-06",
#                  "cpp-module-07",
#                  "cpp-module-08",
#                  "cpp-module-09",
#                  "ft_transcendence"]


#project_name = "cpp-module-09"  # Replace with the actual project name

full_url = f"{base_url}/{project_name}/slots?team_id={team_id}"

# Navigate to the specified slots page
driver.get(full_url)

# for input_project_name in project_names:
#     full_url = f"{base_url}/{input_project_name}/slots?team_id={team_id}"
#     driver.get(full_url)
#     if driver.get(full_url):
#         print("found what project you want to get evaluated ")
#         break
#     else:
#         print("Project URL for", input_project_name, ":", full_url)
#         continue

time.sleep(2)



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

#########################################################
#########################################################
#########################################################
# Set the desired time for the slot
desired_start_time = datetime.strptime("13:00", "%H:%M").time()  # 24-hour format
desired_end_time = datetime.strptime("23:45", "%H:%M").time()  # 24-hour format
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
        print(f"Attempt {attempts} of {max_retries}")
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
            print("15")
            
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



