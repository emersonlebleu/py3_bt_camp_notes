#https://www.rithmschool.com/blog
import requests 
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog").text
soup =BeautifulSoup(response, "html.parser")
articles = soup.find_all("article")

with open("rsdata.csv", "w", newline="") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["Title", "URL", "Date"])
    
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        href = a_tag["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, href, date])
