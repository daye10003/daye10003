from urllib import urlopen
from bs4 import BeautifulSoup
data=urlopen("http://www.naver.com").read()
soup=BeautifulSoup(data)
print soup
