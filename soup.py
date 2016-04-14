from BeautifulSoup import BeautifulSoup
import sys
import re

html_page = open('blah.html')
soup = BeautifulSoup(html_page)
target = open('hehe.txt', 'a')
episodes = []
count = 0
for link in soup.findAll('a'):
	if not str(link.get('href')) in episodes:
		episodes.append(str(link.get('href'))) 

for element in episodes:
	target.write(element + " ")