import requests
import json


def loginCookie(username,password):
    url = "http://192.168.3.222:4002/request?rname=i_plc.Public.User.Login"
    data = {
        "username1": username,
        "password1": password,
        "loginDev": ""
    }

    response = requests.post(url, data=data)
    # print(response.headers)
    print(json.dumps(response.text))
    return response.cookies


def useCookie(cookie):
    url = "http://192.168.3.222:4002/request?rname=i_plc.Page.NcProgram.views.procedure_manage"
    data = {
        "funcType": "/nc/create_program",
        "type": "1",
        "name": "testtest1",
        "parentId": "6405",
        "code": "testfile",
        "info": "{\"graphicNo\":\"test\",\"graphicVersion\":\"\",\"procedureNo\":\"\",\"machType\":\"\",\"bucketCode\":\"\"}"
    }

    response = requests.post(url, data=data,cookies=cookie)

    print(response.text)

if __name__ == '__main__':
    cookie = loginCookie("admin","admin")
    # useCookie(cookie)