# -*- coding: utf-8 -*-
# @Author:varcer
import random
encode_code={"backspace":"8%","A":"41%","a":"61%","§":"%A7","Õ":"%D5","tab":"9%","B":"42%","b":"62%","«":"%AB","Ö":"%D6","linefeed":"%0A","C":"43%","c":"63%","¬":"%AC","Ø":"%D8","creturn":"%0D","D":"44%","d":"64%","¯":"%AD","Ù":"%D9","space":"20%","E":"45%","e":"65%","º":"%B0","Ú":"%DA","!":"21%","F":"46%","f":"66%","±":"%B1","Û":"%DB","\"":"22%","G":"47%","g":"67%","ª":"%B2","Ü":"%DC","#":"23%","H":"48%","h":"68%",",":"%2C","Ý":"%DD","$":"24%","I":"49%","i":"69%","µ":"%B5","Þ":"%DE","%":"25%","J":"%4A","j":"%6A","»":"%BB","ß":"%DF","&":"26%","K":"%4B","k":"%6B","¼":"%BC","à":"%E0","'":"27%","L":"%4C","l":"%6C","½":"%BD","á":"%E1","(":"28%","M":"%4D","m":"%6D","¿":"%BF","â":"%E2",")":"29%","N":"%4E","n":"%6E","À":"%C0","ã":"%E3","*":"%2A","O":"%4F","o":"%6F","Á":"%C1","ä":"%E4","+":"%2B","P":"50%","p":"70%","Â":"%C2","å":"%E5","Q":"51%","q":"71%","Ã":"%C3","æ":"%E6","-":"%2D","R":"52%","r":"72%","Ä":"%C4","ç":"%E7",".":"%2E","S":"53%","s":"73%","Å":"%C5","è":"%E8","/":"%2F","T":"54%","t":"74%","Æ":"%C6","é":"%E9","0":"30%","U":"55%","u":"75%","Ç":"%C7","ê":"%EA","1":"31%","V":"56%","v":"76%","È":"%C8","ë":"%EB","2":"32%","W":"57%","w":"77%","É":"%C9","ì":"%EC","3":"33%","X":"58%","x":"78%","Ê":"%CA","í":"%ED","4":"34%","Y":"59%","y":"79%","Ë":"%CB","î":"%EE","5":"35%","Z":"%5A","z":"%7A","Ì":"%CC","ï":"%EF","6":"36%","ð":"%F0","7":"37%","?":"%3F","{":"%7B","Í":"%CD","ñ":"%F1","8":"38%","40%":"|","%7C":"Î","%CE":"ò","%F2":"9","[":"%5B","}":"%7D","Ï":"%CF","ó":"%F3",":":"%3A","\\":"%5C","~":"%7E","Ð":"%D0","ô":"%F4",";":"%3B","]":"%5D","¢":"%A2","Ñ":"%D1","õ":"%F5","<":"%3C","^":"%5E","£":"%A3","Ò":"%D2","ö":"%F6","=":"%3D","_":"%5F","¥":"%A5","Ó":"%D3","÷":"%F7",">":"%3E","`":"60%","|":"%A6","Ô":"%D4","ø":"%F8","ù":"%F9"}
def encodeurl(purl):
    if 'http://' not in purl and 'https://' not in purl:
        temp="/".join(purl.split('/')[1:])
        url=purl.split('/')[0]+'/'
    else:
        temp="/".join(purl.split('/')[3:])
        url ="/".join(purl.split('/')[:3])+'/'
    for i in temp:
        flag=random.randint(0,9)
        if flag%2==0 and i!='/' and i!='=':
            url+=encode_code[i]
        else:
            url+=i
    return url

def long_random_string(purl):
    if 'http://' not in purl and 'https://' not in purl:
        temp="/".join(purl.split('/')[1:])
        url=purl.split('/')[0]+'/'
    else:
        temp="/".join(purl.split('/')[3:])
        url ="/".join(purl.split('/')[:3])+'/'
    long_string=''
    ran=random.randint(1,20)
    for i in range(ran):
        while 1:
            number=random.randint(48,122)
            if number>=48 and number<=57:
                long_string+=chr(number)
                break
            elif number>=65 and number<=90:
                long_string += chr(number)
                break
            elif number>=97 and number<=122:
                long_string += chr(number)
                break
    muit=int(550/ran)
    return  url+long_string*muit+"/../"+temp

def upper_random_url(purl):
    if 'http://' not in purl and 'https://' not in purl:
        temp="/".join(purl.split('/')[1:])
        url=purl.split('/')[0]+'/'
    else:
        temp="/".join(purl.split('/')[3:])
        url ="/".join(purl.split('/')[:3])+'/'
    for i in temp:
        flag=random.randint(0,9)
        if flag%2==0 and i!='/' and i!='=':
            url+=i.upper()
        else:
            url+=i
    return url

