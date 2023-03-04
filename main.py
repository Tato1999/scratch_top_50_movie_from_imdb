from bs4 import BeautifulSoup
import requests

resp = requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')
page = resp.text

soup = BeautifulSoup(page, "lxml")
text = []
name = soup.select(".lister-item-header a")
rank = soup.select(".lister-item-header .lister-item-index")
rankCout = -1
with open("rank.csv", mode="a") as file:
    for i in name:
        rankCout += 1
        file.write(rank[rankCout].getText())
        file.write(f"{i.getText()} \n")








    







 


























































