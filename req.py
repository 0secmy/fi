# -*- coding: utf-8 -*-
# @Author:varcer
import requests
import login
import conf
def req(url,data=''):
    if conf.conf['-a']:
        login.login()
        re=login.session.get(url,data=data)
    else:
        re=requests.get(url,data)
    if "Failed " not in re.text and "<b>Fatal error</b>" not in re.text:
        print(url)
    if conf.conf['-c']:
        f = open('./cmd.txt', 'w')
        f.write(re.content.decode('gbk'))
        f.close()
        f = open('./cmd.txt', 'r')
        for str in f:
            #print("\\".join(url.split('?')[0].split('//')[1].split("/")[1:])[0:-1])
            if "\\".join(url.split('?')[0].split('//')[1].split("/")[1:])[0:-1] in str:
                print(str)
        f.close()
    return re