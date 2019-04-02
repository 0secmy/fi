# -*- coding: utf-8 -*-
# @Author:varcer
import requests
session=requests.session()
def login():
    res=session.get("http://127.0.0.1/DVWA/login.php")
    html=res.text
    f=open('./temp.txt','w')
    f.write(html)
    f.close()
    f=open('./temp.txt','r')
    token=""
    for i in f:
        if r"<input type='hidden' name='user_token'" in i:
            token=i.split("'")[5]
            f.close()
            break
    param={
        "username":"admin",
        "password":"password",
        "Login":"Login",
        "user_token":token
        }
    param1={
        "security":"medium",
        "seclev_submit":"Submit",
        "user_token":token
        }
    session.post('http://127.0.0.1/DVWA/login.php',data=param)
    session.post('http://127.0.0.1/DVWA/security.php',data=param1)

