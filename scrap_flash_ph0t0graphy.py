from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from PIL import Image
import os

x = 59
y = 59
cnt = 1

website = input("What image would you like to scrape (Copy and paste URL): ")
sav = input("What would you like to save the image as? {Please do not include any extentions, this script will automatically save the image in a .png format}: ")

if os.path.isfile(sav + ".png"):
	k = input("File already exists in directory, file " + sav + ".png will be overridden")

driver = webdriver.Firefox()
driver.get(website)
driver.implicitly_wait(.2)
elem = driver.find_element_by_id("imgLarge")
elem.click()
action = webdriver.common.action_chains.ActionChains(driver)
result = Image.new('RGB', (470, 610))

for c in range(7):
	y = 59 + 100 * c
	for r in range(5):
		x = 59 + 100 * r
		action.move_to_element_with_offset(elem, x, y)
		action.click()
		action.perform()
		name = str(cnt) + ".png"
		driver.get_screenshot_as_file(name)
		img = Image.open(name)
		img2 = img.crop((550, 58, 668, 176))
		result.paste(im=img2, box = (r * 102, c * 102))
		os.remove(name)
		cnt = cnt + 1
		
result.save(sav + ".png")
result.show()
