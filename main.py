from selenium.webdriver.chrome.options import Options 
from datetime import datetime
from selenium import webdriver
from function import message
import time

y = 0
z = 0

while True:
	x = datetime.now()
	print(x)
	time.sleep(5)
	if y != 1:
		if "05-02" in str(x):
			message("Happy Easter!")
			time.sleep(5)
			y += 1
	else:
		continue
		

	if z != 1:
		if "12-25" in str(x):
			message("Merry Christmas!")
			time.sleep(5)
			z += 1
	else:
		break

#This is just for Easter and Christmas, feel free to add more! I sure won't!
#I've been working on this for 7 hours straight, I only wish for the sweet sweet relief of death!
#This is small brain code, it is the best i could come up with, i am not proud