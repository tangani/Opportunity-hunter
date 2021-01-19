import bs4
import requests


def search_fun(keywords):
    link = "https://www.linkedin.com/jobs/search/" + "?keywords=" + keywords
    # link = 'https://www.linkedin.com/jobs/search/?geoId=104035573&keywords=data%20science' + fun + '/'
    print(link)
    data_science_jobs = requests.get(link)
    data_science_jobs.raise_for_status()

    linkedin_response = bs4.BeautifulSoup(data_science_jobs.content, "html.parser")

    all_jobs = [a_tag["href"] for a_tag in linkedin_response.find_all("a", href=True) if "/jobs/" in a_tag["href"]]

    return all_jobs
