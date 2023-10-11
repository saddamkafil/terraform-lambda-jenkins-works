import urllib
import urllib.request
import json


SLACK_URL = "https://hooks.slack.com/services/"

def lambda_handler(event, context):
    sns = event['Records'][0]['Sns']
    req = urllib.request.Request(
        SLACK_URL,
        data=json.dumps(
            {
                'channel': '#edevops',
                'attachments': [
                    {
                        "fallback": "Users withou MFA in AWS Account.",
                        "color": "#F35A00",
                        "title": sns['Subject'],
                        "text": sns['Message']
                    }
                ]
            }    
        ).encode('utf8'),
        headers={'content-type': 'application/json'}
    )
    urllib.request.urlopen(req)