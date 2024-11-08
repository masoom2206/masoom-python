import requests
from bs4 import BeautifulSoup
import pprint

def getData(url):
  page = 1
  links_data = []
  subtext_data = []
  while True:
    res = requests.get(f"{url}?p={page}")
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select(".titleline")
    subtext = soup.select(".subtext")
    if links:
      print(f"Page = {page}....")
      links_data = links_data + links
      subtext_data = subtext_data + subtext
      page += 1
    else:
      break
  parse_data = custom_hn(links_data, subtext_data)
  return parse_data

def sortByVote(hnList):
  # return sorted(hnList, key = lambda k:k['vote'])
  return sorted(hnList, key = lambda k:k['vote'], reverse=True)

def custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = links[idx].getText()
    # href = links[idx].select("href", None)
    href = links[idx].select("a")[0].get("href", None)
    vote = subtext[idx].select(".score")
    if  len(vote):
      point = int(vote[0].getText().replace(' points', ''))
      if point > 99:
        hn.append({
          'title': title,
          'href': href,
          "vote": point
        })
  return sortByVote(hn)

data = getData("https://news.ycombinator.com/news")
# print(data)
pprint.pprint(data)

