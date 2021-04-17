from bs4 import BeautifulSoup
import requests
# import lxml

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

largest_upvotes = max(article_upvotes)
largest_index = article_upvotes.index(largest_upvotes)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])





# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
#
# print(soup.title.string)