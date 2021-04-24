import requests
import json
import conv


def send_message(channel, message):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + conv.get_slack_token()
    }
    payload = {
        'channel': channel,
        'text': message
    }
    requests.post('https://slack.com/api/chat.postMessage', headers=headers, data=json.dumps(payload))
