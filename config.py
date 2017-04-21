import os


SLACK_URL = "https://ssqjqfgkj7.execute-api.us-west-2.amazonaws.com/prod"
JSON_HEADER = {'Content-type': 'application/json'}

current_path = os.path.dirname(os.path.realpath(__file__))
video_name = 'latest.h264'
video_path = os.path.join(current_path, video_name)

framerate = 160
