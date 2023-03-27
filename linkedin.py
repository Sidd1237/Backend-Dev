from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from nameparser import HumanName



# Creating a webdriver instance
driver = webdriver.Chrome("Enter-Location-Of-Your-Web-Driver")
# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

# entering username
username = driver.find_element(By.ID, "username")
	

# Enter Your Email Address
username.send_keys("not_revealing@gmail.com")

# entering password
pword = driver.find_element(By.ID, "password")

pword.send_keys("not_revealing123")	


driver.find_element(By.XPATH, '//button[@type="submit"]').click()
.

profile_url = "https://www.linkedin.com/in/kunalshah1/"
 
driver.get(profile_url)

start = time.time()


initialScroll = 0
finalScroll = 1000

while True:
	driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
	initialScroll = finalScroll
	finalScroll += 1000


	time.sleep(3)

	end = time.time()
	if round(end - start) > 20:
		break

src = driver.page_source

# Now using beautiful soup
soup = BeautifulSoup(src, 'html.parser')

intro = soup.find('div', class_= 'mt2 relative')


name = intro.find("h1", class_='text-heading-xlarge inline t-24 v-align-middle break-words').text
name_parts = HumanName(name)	

first_name = name_parts.first
last_name = name_parts.last

print(first_name)
print(last_name)



experience = soup.find('div',class_='display-flex flex-column full-width')
work_loc = experience.find('span',class_='t-14 t-normal')
work = work_loc.text[:len(work_loc.text)//2]

position_loc = experience.find('div',class_='display-flex flex-wrap align-items-center full-height')
position = position_loc.text[:len(position_loc.text)//2]

print(work)
print(position)

# s = driver.find_element_by_css_selector("span[class='input_group_button']")
# s.click()
# t = s.text	
# This is going to be used to extract email from the apollo extension





