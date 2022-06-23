import requests

response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=932037e00c2b5a6af5195f8ad77b66ba&language=en-US&page'
             '=1&include_adult=false&query=Spiderman no way home').json()
data = response['results'][0]
print(data)
title = data['title']
description = data['overview']
year = data['release_date'].split('-')[0]
print(year)
img_url = data['poster_path']
