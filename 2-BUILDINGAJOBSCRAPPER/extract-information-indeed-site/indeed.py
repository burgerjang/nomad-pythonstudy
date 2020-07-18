#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&radius=25&l=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&fromage=any&limit={LIMIT}&sort=&psf=advsrch&from=advancedsearch"

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

def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    #print(title)
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        # print(str(company_anchor.string.split('\n')[-1])) -> my example
        company = str(company_anchor.string)
    else:
        # print(str(company.string.split('\n')[-1]))
        company = str(company.string)
    company = company.strip()
    #print(title, company)
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]

    #print(location)
    ################## Location ######################

    return {
        'title': title, 
        'company': company, 
        'location': location, 
        "link": f"https://kr.indeed.com/viewjob?jk={job_id}"
    }

def extract_indeed_jobs(last_page):
    jobs=[]
    ###################################################
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            # print(result.find("h2", {"class": "title"}))
            #title = result.find("h2", {"class": "title"})
            #anchor = title.find("a")["title"]
            job = extract_job(result)
            #print(job)
            jobs.append(job)
    return jobs
####################################################
    #
    #

    #print(results)
    # for result in results:
    #     print(result.find("div", {"class": "title"}))
    # 
