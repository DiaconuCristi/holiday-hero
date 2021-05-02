from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import time

contact_list = ["'x'", "'y'", "'z'", "'w'"] #feel free to add as many contacts as you want!, be sure to write them like it's shown!

def message(text):
	options = Options()
	options.add_argument("--user-data-dir=")#the directory to your chromium user data!
	driver = webdriver.Chrome('', options=options)#directory to your chromium driver executable! (provided in the readme)
	driver.maximize_window()
	driver.get('https://web.whatsapp.com')
	time.sleep(15)
	for arraynumber in range(len(contact_list)):
		driver.find_element_by_xpath(f"//*[@title={contact_list[arraynumber]}]").click()
		driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(text)
		driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
	time.sleep(2)
	driver.quit()

	


