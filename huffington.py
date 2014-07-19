#-*- coding:utf-8 -*-
import os
from urllib import urlopen
from bs4 import BeautifulSoup as BS
data = urlopen("http://www.huffingtonpost.kr/the-news/2014/07/17/").read()
soup = BS(data)
# 7.17 폴더가 없으면 만들어죠
if not os.path.exists('7.17'): os.makedirs('7.17')

titles = soup.select('h3 a')
for title in titles:
	article_title = title.text.replace('!','').replace('?','').replace(':','').replace('\"','')
	save_path = '7.17\\'+article_title
	# Make file
	with file(save_path, "w") as text :
		h = title['href']
		data1 = urlopen(h)
		soup1 = BS(data1)
		contents = soup1.select('p')
		for content in contents:
		 	c = content.text
			text.write(c.encode('utf-8'))
		text.close()