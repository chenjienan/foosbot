from StringIO import StringIO
import requests
import json

SLACK_URL = "https://ssqjqfgkj7.execute-api.us-west-2.amazonaws.com/prod"
JSON_HEADER = {'Content-type': 'application/json'}

def slack_message( message ):
    data = { 'text': message }
    response = requests.post(SLACK_URL, data=json.dumps(data), headers=JSON_HEADER)
    print response.text
    return response

send_slack_message("Cosmin was here")
