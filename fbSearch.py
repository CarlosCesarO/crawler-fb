import requests
from bs4 import BeautifulSoup
import re

class FBSearchScraper:

    def __init__(self, filtro, about):
        self.filtro = filtro
        self.about = about
        self.page_url = "https://mobile.facebook.com" + self.filtro + self.about
        self.page_content = requests.get(self.page_url).text

    def parseEmail(self):
        soup = BeautifulSoup(self.page_content, "html.parser")
        feed_container = soup.find_all(href=re.compile(r"^mailto:"))
        if feed_container == []:
            email = "E-mail não encontrado"
            return email
        for i in feed_container:
            email = i.text
            if email == "Enviar email":
                return searchInfo(self.filtro)
            return email

def searchInfo(fb):
    filtro =  fb
    about = "about"
    d = FBSearchScraper(filtro,about)
    return d.parseEmail()