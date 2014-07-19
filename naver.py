#-*- coding:utf-8 -*-
import os
from urllib import urlopen
from bs4 import BeautifulSoup as BS
from string import punctuation

data = urlopen("http://openapi.naver.com/search?key=756c5583c04313bbe2086277c108de50&query=사자&target=news&start=1&display=20").read()
soup = BS(data)

if not os.path.exists('naver'): os.makedirs('naver')

items = soup.select('item')
for item in items:
	title = item('title')[0].text.replace('quot','').replace("b","")
	link = item("link")[0].text
	for p in punctuation:
		title = title.replace(p,'')
 	
 	link_data = urlopen(link).read()

 	title_path = 'naver\\'+str(title.encode('utf-8')+".html")	
 	with file(title_path.decode('utf-8'), 'w') as text:
 		text.write(link_data)

		text.close()