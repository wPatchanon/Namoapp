import os
from flask import Flask, request
from flask_restful import Resource, Api

from service.worker import requestPrayerByName, requestAllPrayer, requestTagPrayer, requestMindNews, requestHealthNews, requestDhammaNews, broadcast, notify, randomTeaching, randomPrayer


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Query(Resource):
    def post(self, ):
        req_body = request.get_json()
        intent_type = req_body['queryResult']['intent']['displayName']
        print(intent_type)
        if intent_type == 'ขอบทสวดมนต์' or intent_type == 'prayer - name - getname':
            return requestPrayerByName(req_body)
        elif intent_type == 'prayer - all':
            return requestAllPrayer(req_body)
        elif intent_type == 'prayer - benefit - getbenefit':
            return requestTagPrayer(req_body)
        elif intent_type == 'prayer - random':
            return randomPrayer(req_body)
        elif intent_type == 'news - mind':
            return requestMindNews(req_body)
        elif intent_type == 'news - all':
            return requestHealthNews(req_body)
        elif intent_type == 'news - dhamma':
            return requestDhammaNews(req_body)
        elif intent_type == 'teaching':
            return randomTeaching(req_body)

        return req_body


class Notify(Resource):
    def get(self):
        notify()
        return {"suscess": 'true'}

    def post(self,):
        req_body = request.get_json(force=True)
        broadcast(req_body['payload'])
        return {"suscess": 'true'}


api.add_resource(HelloWorld, '/')
api.add_resource(Query, '/query')
api.add_resource(Notify, '/notify')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(
        os.environ.get('PORT', 5000)))  # !!! Debug mode
    # app.run(debug=False, host='0.0.0.0')


""" DIALOGFLOW REQUEST
{
  "responseId": "response-id",
  "session": "projects/project-id/agent/sessions/session-id",
  "queryResult": {
    "queryText": "End-user expression",
    "parameters": {
      "param-name": "param-value"
    },
    "allRequiredParamsPresent": true,
    "fulfillmentText": "Response configured for matched intent",
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            "Response configured for matched intent"
          ]
        }
      }
    ],
    "outputContexts": [
      {
        "name": "projects/project-id/agent/sessions/session-id/contexts/context-name",
        "lifespanCount": 5,
        "parameters": {
          "param-name": "param-value"
        }
      }
    ],
    "intent": {
      "name": "projects/project-id/agent/intents/intent-id",
      "displayName": "matched-intent-name"
    },
    "intentDetectionConfidence": 1,
    "diagnosticInfo": {},
    "languageCode": "en"
  },
  "originalDetectIntentRequest": {}
}
"""

""" RESPONSE
{
  "fulfillmentText": "This is a text response",
  "fulfillmentMessages": [
    {
      "card": {
        "title": "card title",
        "subtitle": "card text",
        "imageUri": "https://example.com/images/example.png",
        "buttons": [
          {
            "text": "button text",
            "postback": "https://example.com/path/for/end-user/to/follow"
          }
        ]
      }
    }
  ],
  "source": "example.com",
  "payload": {
    "google": {
      "expectUserResponse": true,
      "richResponse": {
        "items": [
          {
            "simpleResponse": {
              "textToSpeech": "this is a simple response"
            }
          }
        ]
      }
    },
    "facebook": {
      "text": "Hello, Facebook!"
    },
    "slack": {
      "text": "This is a text response for Slack."
    }
  },
  "outputContexts": [
    {
      "name": "projects/project-id/agent/sessions/session-id/contexts/context-name",
      "lifespanCount": 5,
      "parameters": {
        "param-name": "param-value"
      }
    }
  ],
  "followupEventInput": {
    "name": "event name",
    "languageCode": "en-US",
    "parameters": {
      "param-name": "param-value"
    }
  }
}
"""
