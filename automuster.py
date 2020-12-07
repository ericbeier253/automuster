import time

import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# only used if you want to drive a headless browser
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe' #set the path for your chromedriver

browser = webdriver.Chrome(executable_path=path) #initiate driver

browser.get('https://web.groupme.com/signin') #go to groupme

time.sleep(5)

#login
username = browser.find_element_by_id('signinUserNameInput')
userInput = input("Enter Username: ")
username.send_keys(userInput)

time.sleep(1)

password = browser.find_element_by_id('signinPasswordInput')
userInput = input("Enter Password: ")
password.send_keys(userInput)

time.sleep(1)


loginButton = browser.find_element_by_css_selector('button.btn.btn-success.btn-block')
loginButton.click()

time.sleep(3)

#enter Dual-factor-authentication pin
pin = browser.find_element_by_xpath("//form[@ng-submit='verifyPin()']/input[1]")
userInput = input("Enter Pin: ")
pin.send_keys(userInput)

time.sleep(1)

verifyPin = browser.find_element_by_xpath("//form[@ng-submit='verifyPin()']/div[1]/button[1]")
action = ActionChains(browser)
action.move_to_element(verifyPin)
action.click(verifyPin)
action.perform()

time.sleep(3)

#navigate to the IPBC 20060 chat log
IPBCWindow = browser.find_element_by_xpath("//span[@title='IPBC 20060']")
action = ActionChains(browser)
action.move_to_element(IPBCWindow)
action.click(IPBCWindow)
action.perform()

time.sleep(3)

while True:

	#check the sender of the last posted message
	lastSender = browser.find_element_by_xpath("//div[@class='page'][last()]/div[last()]/div[2]/div[2]").text

	print (lastSender) #check who the last sender was

	if lastSender == "Christiane Hidalgo":

		#find the UNLIKED heart by xpath, if latest message is liked, throw exception
		try:
			likeButton = browser.find_element_by_xpath("//div[@class='page'][last()]/div[last()]/div[@class='message-body clearfix']/div[1]/button[2][@aria-checked='false']/i[1]")

			action = ActionChains(browser)
			action.move_to_element(likeButton)
			action.click(likeButton)
			action.perform()

			print("Class leader's message liked")

		except:
			print("Class leader's latest message already liked")


	time.sleep(3)
