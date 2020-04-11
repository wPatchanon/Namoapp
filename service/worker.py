import service.GC_Client as gc
import service.news_fetcher as nf
import random
from service.line_messager import all_prayer_msg, news_msg


def requestPrayerByName(req):
    prayerName = req["queryResult"]["parameters"]["prayer_name"]
    text_variation = [
        ['บทสวดมนต์ "' + prayerName + '" อยู่ด้านล่างแล้วครับ'],
        ['บทสวดมนต์ "' + prayerName + '" ได้แล้วจ้า'],
    ]

    text_response = {'text': {
        'text': text_variation[random.randint(0, len(text_variation)-1)]
    }}
    print("Finding...")
    url_res = gc.get_prayer_image_url(prayerName)
    print("FINISH!!!")
    # Default img
    IMG_URL = [
        "https://storage.googleapis.com/namo-chatbot/not-found-image-15383864787lu.jpg"]
    if len(url_res):
        IMG_URL = url_res
    payload = []
    for url in IMG_URL:
        payload.append({
            "payload": {
                "line": {
                    "type": "image",
                    "originalContentUrl": url,
                    "previewImageUrl": url
                }
            }
        })
    res = {
        "fulfillmentMessages": [text_response]+payload
    }

    return res


def requestAllPrayer(req):
    print('Fetching')
    prayers = gc.get_all_prayer()
    print("Finish")
    body = all_prayer_msg.gen_message(prayers)
    res = {
        "fulfillmentMessages": [{
            "payload": {
                "line":
                {
                    "type": "flex",
                    "altText": "this is a flex message",
                    "contents": body,
                }
            }
        }
        ]
    }
    return res


def requestMindNews(req):
    print('Fetching')
    news_list = nf.get_mind_news()
    print("Finish")
    body = news_msg.gen_news_message(news_list, "อัพเดตข่าวสุขภาพจิต")
    text_variation = [
        ['ข่าวสุขภาพจิตอยู่ด้านล่างแล้วครับ'],
        ['อัพเดตสุขภาพจิตกันหน่อย'],
    ]

    text_response = {'text': {
        'text': text_variation[random.randint(0, len(text_variation)-1)]
    }}
    res = {
        "fulfillmentMessages": [text_response, {
            "payload": {
                "line": body
            }
        }
        ]
    }
    return res


def requestHealthNews(req):
    print('Fetching')
    news_list = nf.get_health_news()
    print("Finish")
    body = news_msg.gen_news_message(news_list, 'อัพเดตข่าวสุขภาพ')
    text_variation = [
        ['ข่าวสุขภาพอ่านด้านล่างได้เลยครับ'],
        ['สุขภาพดีเริ่มต้นได้ที่นี้เลยจ้า'],
    ]

    text_response = {'text': {
        'text': text_variation[random.randint(0, len(text_variation)-1)]
    }}
    res = {
        "fulfillmentMessages": [text_response, {
            "payload": {
                "line": body
            }
        }
        ]
    }
    return res


def requestTagPrayer(req):
    prayerTag = req["queryResult"]["parameters"]["prayer_benefit"]
    print('Fetching')
    prayers = gc.get_prayers_by_tag(prayerTag)
    print("Finish")
    body = all_prayer_msg.gen_message(prayers, prayerTag)
    res = {
        "fulfillmentMessages": [{
            "payload": {
                "line":
                {
                    "type": "flex",
                    "altText": "this is a flex message",
                    "contents": body,
                }
            }
        }
        ]
    }
    return res


def requestDhammaNews(req):
    print('Fetching')
    news_list = nf.get_dhamma_news()
    print("Finish")
    body = news_msg.gen_news_message(news_list, 'อัพเดตข่าวธรรมะ')
    text_variation = [
        ['ข่าวธรรมะเพื่อคุณ'],
        ['ธรรมะวันนี้'],
    ]

    text_response = {'text': {
        'text': text_variation[random.randint(0, len(text_variation)-1)]
    }}
    res = {
        "fulfillmentMessages": [text_response, {
            "payload": {
                "line": body
            }
        }
        ]
    }
    return res


# print(requestAllPrayer(""))
