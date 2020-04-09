import json


def get_json(paresed_data):
    with open('test.json', 'w') as fp:
        json.dump(paresed_data, fp)


def gen_mind_message(news_list):
    res = {
        "type": "template",
        "altText": "this is a carousel template",
        "template": {
            "type": "carousel",
            "actions": [],
            "columns": [
            ]
        }
    }
    
    for new in news_list:
        body = {
            "thumbnailImageUrl": new['image'],
            "text": new['title'],
            "actions": [
                {
                    "type": "uri",
                    "label": "อ่านข่าว",
                    "uri":  new['link']
                }
            ]
        }
        res["template"]["columns"].append(body)
    
    get_json(res)
    return res