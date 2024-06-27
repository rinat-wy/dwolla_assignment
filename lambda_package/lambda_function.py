from datetime import datetime
import json


def lambda_handler(event, context):
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

    response = { "currentTime": formatted_time }

    return response
