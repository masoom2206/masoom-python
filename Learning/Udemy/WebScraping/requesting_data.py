# Beautiful Soup, allow us to scrape the website.
import requests
from bs4 import BeautifulSoup

# res = requests.get('https://news.ycombinator.com/news?p=10')
res = requests.get('https://www.ndtv.com/topic/api')
# print(res)
# print(res.status_code)
# print(res.content)
# with open('Learning/Udemy/WebScraping/res-text.html', mode='wt') as myFile:
#   myFile.write(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# with open('Learning/Udemy/WebScraping/res-soup.html', mode='wt') as myFile:
#   myFile.write(soup)
# print(soup.body.contents)
# print(soup.find_all("div"))
# print(soup.find_all("img")[1])
# print(soup.a)
# print(soup.find("img"))
# print(soup.find(id="score_42069646"))
# print(soup.find(id="score_42069646").text)
# print(soup.select('a'))
# print(soup.select('div'))
# print(soup.select('.score'))# Get data by the class
# print(soup.select('#score_42069646'))# Get data by the ID

# print(soup.select('.titleline'))# titleline
# print(soup.select('.titleline')[0])# titleline

# links = soup.select('.titleline')
# votes = soup.select('.score')

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
links = soup.select(".src_lst-li .src_lst-rhs .src_itm-ttl")
if links:
  print(links[0].getText())



