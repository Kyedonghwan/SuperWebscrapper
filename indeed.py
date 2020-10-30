import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}&vjk=84a541c104b5b24c"


def get_last_page():
    result = requests.get(URL)

    # indeed_result.text = 추출된 html

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    # class 속성이 pagination 인 div element를 추출

    links = pagination.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.find("span").string))
    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    if company:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
    else:
        company = None

    location = html.find("span", {"class": "location"}).string

    job_id = html["data-jk"]
    return {'title': title, 'company': company, 'location': location, "link": f"https://indeed.com/viewjob?jk={job_id}"}
    # 속성title의 값을 가져옴


def extract_jobs(last_page):

    jobs = []
    for page in range(last_page):
        #print(f"Scrapping page: {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
