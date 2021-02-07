# Login to FB, see that how many has their birthdays, Go to Events, go to birthdays, find textbox for the birthday person, enters the message, send the message.
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



#LOGIN DONE----------------------------------------

# * means checking all the elements to check
getting_no_of_birthday_div = "//*[@id='home_birthdays']/div/div/div/div/a/div/div/span/span[2]"

find_no_of_birthdays = browserChrome.find_element_by_xpath(getting_no_of_birthday_div).get_attribute("textContent")     #This gives the value of that div which is containing no. of the other birthdays.


num_of_birthday = find_no_of_birthdays[0]
num_of_birthday = int(num_of_birthday)
print("Number of birthdays are: ", num_of_birthday)


openFacebookEventsBirthdays = browserChrome.get("https://facebook.com/events/birthdays/")


#all the birthdays list boxes of current future and past birthdays    #gets the text area for all the birthday boxes
bday_list = browserChrome.find_elements_by_xpath("//*[@class = 'enter_submit uiTextareaNoResize uiTextareaAutogrow uiSTreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")

#find the textbox for bday wishes
noOfBdayBlockWished = 0
for bdayBlock in bday_list:
    bdayBlockIDValue = str(bdayBlock.get_attribute('id'))    #gets the value of that attribute in each bday block
    XPAthForBirthdayBlock = '//*[@id ="' + bdayBlockIDValue + '"]'
    findCurrentBdayBlock = browserChrome.find_element_by_xpath(XPAthForBirthdayBlock)    #Get the Block for each bdayPerson in each loop
    findCurrentBdayBlock.send_keys("Happy Birthday")
    findCurrentBdayBlock.send_keys(Keys.RETURN)   #Sends the button by sending the wishes

    noOfBdayBlockWished += 1
    if noOfBdayBlockWished > num_of_birthday:
        break
