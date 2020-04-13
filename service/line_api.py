import requests
import json
from etc.line_authen import LINE_TOKEN

# defining the api-endpoint
API_ENDPOINT = "https://api.line.me/v2/bot/message/broadcast"

TOKEN = "Bearer " + LINE_TOKEN
headers = {'Content-Type': 'application/json', 'Authorization': TOKEN}

payload = {
    "messages": [
        {
            "type": "text",
            "text": "สวัสดีตอนเช้า"
        },
    ]
}


def broadcast(payload=payload):
    # sending post request and saving response as response object
    requests.post(url=API_ENDPOINT, data=json.dumps(
        payload), headers=headers)

# # extracting response text
# pastebin_url = r.text
# print("The pastebin URL is:%s" % pastebin_url)
