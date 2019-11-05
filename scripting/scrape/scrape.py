import requests
from bs4 import BeautifulSoup
import pprint

pages = [1, 2, 3]
res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")

soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")

links = soup.select(".storylink")
links2 = soup2.select(".storylink")
# print(links[2].getText())
subtext = soup.select(".subtext")
subtext2 = soup2.select(".subtext")

mega_links = links + links2
# print(mega_links)
mega_subtext = subtext + subtext2
# print(mega_subtext)


def sort_stories_by_vote(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "href": href, "votes": points})

    return sort_stories_by_vote(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
