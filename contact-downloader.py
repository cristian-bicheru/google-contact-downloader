from selenium import webdriver
from bs4 import BeautifulSoup
import pickle
import time

# By: Cristian Bicheru
# Requires Selenium and Chromewebdriver
# Downloads all users in directory
########################################

end = 297 #changeable
driver = webdriver.Chrome()
driver.get('https://www.google.com/contacts/u/1/?cplus=1#contacts/group/27/Directory')
print('Press enter once logged in:')
t = input()
print('starting')

with open('dsbemails.txt', 'a') as emails:
    driver.get('https://www.google.com/contacts/u/1/?cplus=1#contacts/group/27/Directory')
    print('w0')
    time.sleep(10)
    print('d0')
    html = driver.page_source
    html = BeautifulSoup(driver.page_source)
    stuff = html.findAll("span")
    emailList = []
    for i in stuff:
        i = str(i)
        if "email" in i:
            emailList.append((i.split(">")[1]).split('<')[0])
            emailList.append((i.split('email="')[1]).split('"')[0])
    
    base = 'https://www.google.com/contacts/u/1/?cplus=1#contacts/group/27/Directory/p'
    for x in range(1, end):
        print(x)
        check = len(emailList)
        currentUrl = base + str(x)
        driver.get(currentUrl)
        while True:
            print('w'+str(x))
            time.sleep(3)
            print('d'+str(x))
            html = BeautifulSoup(driver.page_source)
            stuff = html.findAll("span")
            for i in stuff:
                i = str(i)
                if "email" in i:
                    emailList.append((i.split(">")[1]).split('<')[0])
                    emailList.append((i.split('email="')[1]).split('"')[0])
            if check != len(emailList):
                break
    emails.write(str(emailList))
    emails.close()
emails.close()
    
