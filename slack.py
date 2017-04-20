from StringIO import StringIO
import requests
import json
import config


def send_message(message):
    data = { 'text': message }
    response = requests.post(config.SLACK_URL, data=json.dumps(data), headers=config.JSON_HEADER)
    print response.text
    return response

#send_message("Test message")
