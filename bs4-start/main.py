from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# find first article
articles = soup.find_all(name="a", class_="titlelink")
# print(first_article)
articles_text = []
articles_links= []
for article in articles:
    text = article.getText()
    link = article.get("href")
    articles_text.append(text)
    articles_links.append(link)
article_points = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(articles_text)
# print(articles_links)
print(article_points)
# split_points = article_points[0].split()
# point = int(split_points[0])
# print(point)
max_index = article_points.index(max(article_points))
max_atricle_title = articles_text[max_index]
max_article_link = articles_links[max_index]
print(max_atricle_title, max_article_link)



# with open("website.html", encoding='utf-8') as fp:
#     contents = fp.read()
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
#
# all_a_tags = soup.find_all(name="a")
# for tag in all_a_tags:
#     print(tag)
#     # get text associated with link
#     print(tag.text)
#     # get link
#     print(tag.get("href"))


