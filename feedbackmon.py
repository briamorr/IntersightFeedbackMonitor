import json
import requests
from datetime import datetime, timedelta

from intersight_auth import IntersightAuth

def getFeedback():
    #Determine the last X minutes, days, hours from now for how far back to return in the feedback filter
    timeDelta = datetime.utcnow() - timedelta(days=7)
    timeDelta = str(timeDelta.strftime("%Y-%m-%dT%H:%M:%SZ"))

    RESPONSE = requests.request(
        method="GET",
        url="https://www.intersight.com/api/v1/aaa/AuditRecords?$top=1000&$select=Email,CreateTime,Request&$filter=MoType eq 'feedback.FeedbackPost' and CreateTime gt " + timeDelta + "&$orderby=CreateTime desc",
        auth=AUTH
    )

    feedbacks = RESPONSE.json()["Results"]
    for r in feedbacks:
        try:
           print(r['CreateTime'],r['Email'],"\n",r['Request']['FeedbackData']['Comment'])
        except:
           print("")

#Configure Intersight API connection, requires minimum of "Audit Log Viewer" privilege        
AUTH = IntersightAuth(
    secret_key_filename='SecretKey.txt',
    api_key_id='xxxxxx/yyyyyy/zzzzzz'
    )

getFeedback()
