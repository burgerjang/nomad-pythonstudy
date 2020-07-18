#!/usr/bin/python3

import os
import requests
from bs4 import BeautifulSoup


indeed_resul = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=devops&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&radius=25&l=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

#print(indeed_resul)
#print(indeed_resul.text)

indeed_soup = BeautifulSoup(indeed_resul.text, 'html.parser')
#print(indeed_soup)

pagination  = indeed_soup.find("div", {"class":"pagination"})
#print(pagination)

links = pagination.find_all('a')
#print(links)
############################################################

#for link in links:
#    print(link.find("span"))

pages=[]
#for link in links:
#    pages.append(link.find("span"))
#pages=pages[0:-1]

for link in links[:-1]:
    pages.append(int(link.find("span").string))
print(pages)
max_pages = pages[-1]

############################################################

for n in range(max_pages):
    print(f"start={ n*50 }")
