from StringIO import StringIO
import requests
import json
import config


def send_message(content, message_type = "message"):
    data = { 'content': content, 'type': message_type }
    response = requests.post(config.SLACK_URL, data=json.dumps(data), headers=config.JSON_HEADER)
    print response.text
    return response

#send_message("Test message")
