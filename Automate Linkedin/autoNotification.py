from selenium import webdriver
from time import sleep

# open googleChrome, open facebook, click  on mail, enter mail, click on pass, enter pass, click sign in

user_id = input("Enter Email or Phone Number: ")
user_Password = input("Enter the Password: ")

ChromeDriverExeFilePath = "" #PAth to chromeDriver exe file
browserChrome = webdriver.Chrome(ChromeDriverExeFilePath)  #opens Chrome/Browser

browserChrome.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")  #gets the link to open in browser


get_id_email = browserChrome.find_element_by_id("username")    #go to the browser and finds the id in the web page present at the browser  #This clicks or get the email box clicking

get_id_email.send_keys(user_id)   #Sends value to that element or that tag or that object    #enters email id


#Similar fpr password
get_id_password = browserChrome.find_element_by_id("password")
get_id_password.send_keys(user_Password)

get_id_loginBtn = browserChrome.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')     #gets the id of login Button
get_id_loginBtn.click()

print("Logged In Succesfully")

getNotificationNumber = browserChrome.find_element_by_xpath("//*[@id='ember53']/span/span[1]").get_attribute("textContent")

print("Total Number of Notifications are", int(getNotificationNumber))

time.sleep(3)

get_id_notification = browserChrome.find_element_by_xpath('//*[@id="global-nav-icon--classic__notifications--active"]/path')
get_id_notification.click()