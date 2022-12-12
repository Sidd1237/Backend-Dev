from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver

csv_file = open('shoes_scraped.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name','category','user_rating'])

for i in range (4):

	driver = webdriver.Chrome()
	driver.get(f'http://myntra.com/shoes?p={i+1}')
	html = driver.page_source

	soup = BeautifulSoup(html,'html.parser')

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





#for shoe in soup.find_all('li',class_='product-base'):

# 	headline = article.a.text
# 	summary = article.find('div',class_='entry-content').p.text
	
# 	try:
# 		vid_src = article.find('iframe',class_='youtube-player')['src']
# 		vid_id = vid_src.split('/')[4].split('?')[0]
# 		yt_link = f'https://www.youtube.com/watch?v={vid_id}'
# 	except Exception as e:
# 		yt_link=None

# 	csv_writer.writerow([headline,summary,yt_link])

# csv_file.close()

	


