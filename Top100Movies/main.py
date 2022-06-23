import requests
import json
from bs4 import BeautifulSoup

site = requests.get("https://www.imdb.com/list/ls091520106/")
website = site.text
soup = BeautifulSoup(website, "html.parser")

all_movies = soup.find_all(name="h3", class_="lister-item-header")

for movie in all_movies:
    name = movie.get_text("href")
    print(movie)
