from selenium import webdriver

# open googleChrome, open facebook, click  on mail, enter mail, click on pass, enter pass, click sign in

user_id = input("Enter Email or Phone Number: ")
user_Password = input("Enter the Password: ")


ChromeDriverExeFilePath = "" #Path to chromeDriver exe file
browserChrome = webdriver.Chrome(ChromeDriverExeFilePath)  #opens Chrome/Browser

browserChrome.get("https://www.facebook.com")  #gets the link to open in browser

get_id_email = browserChrome.find_element_by_id("email")    #go to the browser and finds the id in the web page present at the browser  #This clicks or get the email box clicking
get_id_email.send_keys(user_id)   #Sends value to that element or that tag or that object    #enters email id

#Similar fpr password
get_id_password = browserChrome.find_element_by_id("pass")
get_id_password.send_keys(user_Password)

get_id_loginBtn = browserChrome.find_element_by_id("u_0_b")     #gets the id of login Button
get_id_loginBtn.click()

# Dont write that beacuse it will shut down the browser immediately
# browserChrome.quit()   #quits the browser