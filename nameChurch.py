from bs4 import BeautifulSoup
import re
import os
from fbSearch import searchInfo

path = os.path.abspath('igreja – Resultados de pesquisa _ Facebook.html')

def nameChurch():
    with open(path,"r") as fp:
        soup = BeautifulSoup(fp, "html.parser")
        cont = 1 
        nome = []
        faceb = []
        email = []
        for i in soup.find_all(href=re.compile(r"^https://www.facebook.com/")):
            if i.text != "" and "Paróquia" not in i.text and "Escola" not in i.text and "Senhora" not in i.text:
                if cont > 11:
                    nome.append(i.text)
                    faceb.append(i['href'])
                    email.append(searchInfo(i['href'][24:]))
                print(cont)
                cont+=1
    return nome,faceb,email
    