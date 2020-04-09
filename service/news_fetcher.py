import feedparser
import json




def get_json(paresed_data):
    with open('test.json', 'w') as fp:
        json.dump(paresed_data, fp)

def get_mind_news():
    URL = "http://rssfeeds.sanook.com/rss/feeds/sanook/health.mind-brain.xml"
    NUM_NEWS = 4
    d = feedparser.parse(URL)
    d = d['entries']
    res = []
    for i in range(NUM_NEWS):
        new = {}
        new['title'] = d[i]['title']
        new['link'] = d[i]['links'][0]['href'].split("|")[1]
        new['image'] = d[i]['links'][1]['href']
        new['date'] = d[i]['published'][:-6]
        res.append(new)

    return res


# health http://rssfeeds.sanook.com/rss/feeds/sanook/health.index.xml
#  dhamma https://www.posttoday.com/rss/src/dhamma.xml