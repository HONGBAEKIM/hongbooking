

# Automatically booking evaluation slots  
  
I have developed a program that automates  
the process of booking evaluation slots,  
eliminating the need to manually refresh the evaluation page.  
  
Allow me to guide you on its usage:  
  
1.Start by logging in with your credentials (ID and password).  
2.Rest assured that your password remains confidential.  
3.Specify the project name that you wish to have evaluated.  
4.Enter '0' for today or '1' for tomorrow.  
5.Provide the desired start and end times for the evaluation.  
  
https://youtu.be/MWj3DeJTAtM  

[![Video Guide](https://img.youtube.com/vi/MWj3DeJTAtM/0.jpg)](https://www.youtube.com/watch?v=MWj3DeJTAtM)  
  
  
# 0. Run booking evaluation slots program  

python3 hongbook**.py  
  
  
  
# things to implement 

1. Server Management:  
I've set up an AWS EC2 server and am running the booking program 24/7 on the server.  
The challenge is managing multiple users simultaneously since each user requires a separate  Chrome browser instance.  
My goal is to enable access for all 42 students worldwide through a Flask application. 

2. Security Enhancement:  
I am going to replace the prompt input for ID and password with an API for improved security.  

3. Booking Verification:  
After a slot is booked, I'll implement a check in the program to ensure that the slot is  genuinely booked. Sometimes, despite successful automation, the booking may not be confirmed if  the program is terminated prematurely.  
  

  
# Test result  

<17/Jan>  
@rtimsina - cpp  
not working  
(error001) time delay between click button is shown and actually click button  
(error001) fixed: change time delay 5 sec to 1 sec to click icon  

<18/Jan>  
@ttaneski - cpp  
working  
(error002) I want to do everything with my code even installing "selenium" library  
(error002) fixed: installing selenium if there is no "selenium" library  

@mschaub - inception  
working  
(error003) when you force to close chrome page, error occurs.  
(error003) not fixed : not critical error. let's see.  

@dwilke - minishell  
not working  
(error004) Some project's name has + "42cursus-"  
(error004) fixed : fixed project_name_mapping  


<19/Jan>  
(error005) - random host number was 65536  
(error005) fixed ? : host number is going to be 65536 to 65999  

and 3 more people tested

(error001 - 2nd) after clicking last step of booking icon I should check if evaluation slot is booked
(error001 - 2nd) I will fix after I put this code in my homepage


