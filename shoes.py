from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver

csv_file = open('shoes_scraped.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name','category','user_rating'])

for i in range (4):
	
	#inputting the url page by page using selenium
	driver = webdriver.Chrome()
	driver.get(f'http://myntra.com/shoes?p={i+1}')
	html = driver.page_source

	soup = BeautifulSoup(html,'html.parser')

	#iterating over the shoes
	for shoe in soup.find_all('li',class_='product-base'):
		name = shoe.find('h4',class_='product-product').text

		if("sneakers" in name.lower()):
			try:
				ratings = shoe.find('div',class_='product-ratingsContainer')
				ratings = ratings.find('span').text
				category = shoe.find('h3',class_='product-brand').text
			except Exception as e:
				ratings=None
			
			csv_writer.writerow([name,category,ratings])


csv_file.close()
