import math
import json

carousel = {
    "type": "carousel",
    "contents": []
}

bubble = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "บทสวด",
                "weight": "bold",
                "size": "xxl",
                "margin": "md",
                "decoration": "none",
                "align": "center",
                "color": "#FF8C00"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                ]
            }
        ]
    }
}

prayer_box = {
    "type": "box",
    "layout": "horizontal",
    "spacing": "sm",
    "contents": [
        {
            "type": "box",
            "layout": "vertical",
            "flex": 5,
            "contents": [
                {
                    "type": "text",
                    "size": "md",
                    "text": "บท1",
                    "align": "center",
                    "wrap": True,
                    "gravity": "center",
                    "offsetTop": "6px"
                }
            ]
        },
        {
            "type": "button",
            "flex": 3,
            "height": "sm",
            "gravity": "center",
            "style": "secondary",
            "action": {
                "type": "message",
                "label": "สวด",
                "text": "บท1"
            },
            "color": "#FFD700"
        }
    ],
    "borderWidth": "3px"
}


def gen_message(prayer_list):
    res = carousel
    if len(prayer_list) == 0:
        res['contents'].append(bubble)
        return res
    else:
        # 5 prayers per carousel
        num_carousel = math.ceil(len(prayer_list) / 5)
        for i in range(1, num_carousel):
            this_bubble = bubble.copy()
            for j in range((i-1)*5,i*5):
                this_prayer_box = prayer_box.copy()
                this_prayer_box["contents"][0]["contents"][0]["text"] = prayer_list[j]["name"]
                this_prayer_box["contents"][1]["action"]["text"] =  "ขอบท" + prayer_list[j]["name"]
                this_bubble["body"]["contents"][1]["contents"].append(prayer_box)
            res['contents'].append(this_bubble)
        # last carousel = the rest
        this_bubble = bubble.copy()
        for j in range((num_carousel-1)*5,len(prayer_list)):
            this_prayer_box = prayer_box.copy()
            this_prayer_box["contents"][0]["contents"][0]["text"] = prayer_list[j]["name"]
            this_prayer_box["contents"][1]["action"]["text"] =  "ขอบท" + prayer_list[j]["name"]
            this_bubble["body"]["contents"][1]["contents"].append(prayer_box)
        res['contents'].append(this_bubble)

        # with open('test.json', 'w') as fp:
        #     json.dump(res, fp)
        # return res



