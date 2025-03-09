import requests
from bs4 import BeautifulSoup


class Jobs:
    def __init__(self):
        self.base_url = "https://realpython.github.io/fake-jobs"
        self.jobs_data = []
    
    def scrape(self):
        main_page = requests.get(self.base_url)
        soup = BeautifulSoup(main_page.text,"html.parser")
        links = soup.find_all("a", string=lambda text: text and "Apply" in text)
        for link in links:
            response = requests.get(link["href"])
            job_soup = BeautifulSoup(response.text, "html.parser")
            job_title = job_soup.find(attrs={"class":"title is-2"}).text
            company = job_soup.find(attrs={"class":"subtitle is-4 company"}).text
            location = job_soup.find(attrs={"id":"location"}).text
            job_description = job_soup.find(attrs={"class":"content"}).find("p").text
            application_link = link["href"]
            job_info = (
                job_title,
                company,
                location,
                job_description,
                application_link
            )
            if job_title not in [job[0] for job in self.jobs_data] and company not in [job[1] for job in self.jobs_data] and location not in [job[2] for job in self.jobs_data]:
                self.jobs_data.append(job_info)
        print("Job details are scraped!")
    
    

    


base_url = "https://realpython.github.io/fake-jobs"
main_page = requests.get(base_url)
soup = BeautifulSoup(main_page.text,"html.parser")
print(soup.find_all("a", string=lambda text: text and "Apply" in text))

