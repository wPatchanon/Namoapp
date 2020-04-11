import json


# def get_json(paresed_data):
#     with open('test.json', 'w') as fp:
#         json.dump(paresed_data, fp)

def gen_news_message(news_list, altText):
    res = {
        "type": "template",
        "altText": altText,
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

    # get_json(res)
    return res
