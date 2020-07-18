#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=devops&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&radius=25&l=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&fromage=any&limit={LIMIT}&sort=&psf=advsrch&from=advancedsearch"

def extract_indeed_pages():
    result = requests.get(INDEED_URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs=[]
    ###################################################
    #for page in range(last_page):
    #print(f"&start={page*50}")
    result = requests.get(f"{INDEED_URL}&start={0*LIMIT}")
    #print(result.status_code)
####################################################
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    #print(results)
    for result in results:
        print(result.find("div", {"class": "title"}))
    return jobs
