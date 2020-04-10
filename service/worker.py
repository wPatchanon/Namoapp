import service.GC_Client as gc
import random
from service.line_messager import all_prayer_msg


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

# print(requestAllPrayer(""))
