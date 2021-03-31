import json
import requests
import os

def lambda_handler(event,context):
    print(event)
    return {'statusCode':200, 'body': json.dumps({'data' : requests.__version__})}
