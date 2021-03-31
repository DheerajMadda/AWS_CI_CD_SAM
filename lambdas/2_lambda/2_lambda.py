import json
import Crypto
import os

def lambda_handler(event,context):
    print(event)
    return {'statusCode':200, 'body': json.dumps({'data' : Crypto.__version__})}
