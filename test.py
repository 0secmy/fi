# -*- coding: utf-8 -*-
# @Author:varcer
from splinter import Browser
def get_ip(page,page_number):
    browser = Browser(driver_name='chrome')
    for s in range(1,page):
        try:
            url='https://www.xicidaili.com/nn/%s'%s
            browser.visit(url)
            for i in range(2, page_number):
                ip=browser.find_by_xpath('/html/body/div[1]/div[2]/table/tbody/tr[%s]/td[2]'%i)
                port=browser.find_by_xpath('/html/body/div[1]/div[2]/table/tbody/tr[%s]/td[3]'%i)
                print(ip.value+":"+port.value)
        except:
            pass
if __name__=='__main__':
    get_ip(3,10)