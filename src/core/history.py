import requests

def view_personal_appointments(token, payload):
    url = "https://aiot.fzu.edu.cn/api/ibs/spaceAppoint/app/queryMyAppoint"

    headers = {
        "token": token,
    }
    
    return requests.post(url, json=payload, headers=headers)
        
