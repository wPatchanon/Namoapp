import feedparser
import json
import re

NUM_NEWS = 5


# def get_json(paresed_data):
#     with open('test2.json', 'w') as fp:
#         json.dump(paresed_data, fp)


def remove_special_chars(sentence):
    res = re.sub('\ |\?|\.|\!|\/|\;|\:|\&|\#|\-|\“|\”|\(|\)', '', sentence)
    res = re.sub('8220|8221', '', res)
    return res


def get_mind_news():
    URL = "http://rssfeeds.sanook.com/rss/feeds/sanook/health.mind-brain.xml"
    d = feedparser.parse(URL)
    d = d['entries']
    res = []
    for i in range(NUM_NEWS):
        new = {}
        new['title'] = remove_special_chars(d[i]['title'])
        new['link'] = d[i]['links'][0]['href'].split("|")[1]
        new['image'] = d[i]['links'][1]['href']
        new['date'] = d[i]['published'][:-6]
        res.append(new)

    return res


def get_health_news():
    URL = "http://rssfeeds.sanook.com/rss/feeds/sanook/health.index.xml"
    d = feedparser.parse(URL)
    d = d['entries']
    res = []
    for i in range(NUM_NEWS):
        new = {}
        # new['title'] = d[i]['title']
        new['title'] = remove_special_chars(d[i]['title'])
        # print(new['title'])
        new['link'] = d[i]['links'][0]['href'].split("|")[1]
        new['image'] = d[i]['links'][1]['href']
        new['date'] = d[i]['published'][:-6]
        res.append(new)

    return res


def get_dhamma_news():
    URL = "https://www.posttoday.com/rss/src/dhamma.xml"
    d = feedparser.parse(URL)
    d = d['entries']

    plcholder_imgs = ['https://static.wixstatic.com/media/cc9374_522cbdb6480f46b793f3dd6588bc1828~mv2_d_2048_1366_s_2.jpg/v1/crop/x_110,y_0,w_1829,h_1366/fill/w_480,h_358,al_c,q_80,usm_0.66_1.00_0.01/cc9374_522cbdb6480f46b793f3dd6588bc1828~mv2_d_2048_1366_s_2.webp',
                      'https://www.khaosodenglish.com/wp-content/uploads/2019/02/49764919_280709632624104_3008619320923127808_o-e1549428853336.jpg',
                      'https://www.mindfulness-project.org/wp-content/uploads/2016/07/THA_9518-2000x1328.jpg',
                      'https://www.matichon.co.th/wp-content/uploads/2017/10/%E0%B8%A0%E0%B8%9B-%E0%B9%80%E0%B8%87%E0%B8%B4%E0%B8%99%E0%B8%97%E0%B8%AD%E0%B8%99%E0%B8%AA%E0%B8%87%E0%B8%86%E0%B9%8C.jpg']
    res = []
    for i in range(NUM_NEWS):
        new = {}
        new['title'] = d[i]['title']
        new['link'] = d[i]['links'][0]['href']
        new['image'] = plcholder_imgs[i % len(plcholder_imgs)]
        new['date'] = d[i]['published'][:-6]
        res.append(new)

    return res


# health http://rssfeeds.sanook.com/rss/feeds/sanook/health.index.xml
#  dhamma https://www.posttoday.com/rss/src/dhamma.xml
