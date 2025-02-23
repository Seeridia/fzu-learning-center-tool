import requests

url_signin = "https://aiot.fzu.edu.cn/api/ibs/station/app/signIn"

url_signout = "https://aiot.fzu.edu.cn/api/ibs/station/app/signOut"

url_cancel = "https://aiot.fzu.edu.cn/api/ibs/spaceAppoint/app/revocationAppointApp"

def operate(token, opration, id):

    headers = {
        "token": token,
    }

    data = {
        "id": id,
    }

    if opration == "signin":
        url = url_signin
    elif opration == "signout":
        url = url_signout
    elif opration == "cancel":
        url = url_cancel
    
    return requests.post(url, json=data, headers=headers)