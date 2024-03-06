from bs4 import BeautifulSoup
import requests

res = requests.get(url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
site = res.text

soup = BeautifulSoup(site, 'html.parser')

titles = soup.select('.article-title-description__text .title')

titles = [title.get_text() for title in titles]
titles = titles[::-1]

with open('Day 45/movies.txt',mode='w') as file:
  for title in titles:
    file.write(f"{title} \n")