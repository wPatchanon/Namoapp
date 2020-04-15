from __future__ import print_function
import os
from googleapiclient.discovery import build


def event_fetcher(calendar_id, timeMin, timeMax):

    service = build('calendar', 'v3')

    # Call the Calendar API
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId=calendar_id, timeMin=timeMin, timeMax=timeMax,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    res = []
    if events:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            res.append(event['summary'])
    return res
