import time
import sys
import pickle
from selenium import webdriver
from bs4 import BeautifulSoup

print('========== Instagram Follower Tracker ==========')

username = 'test'
print('UserName : '+username)
print('Password : ')

password = input()
while(len(password.strip())==0):
    print('Type at least 1 letter')
    password = input()

print('Password Input Complete')
print('Loading Instagram webpage')
time.sleep(0.5)

browser = webdriver.Chrome('C:/Users/WD2/PycharmProjects/pythonProject/chromedriver_win32/chromedriver')
username = 'hoo_pics'
browser.get('https://www.instagram.com/'+username)
browser.execute_script("document.querySelectorAll('.-nal3')[1].click();")

time.sleep(2)
username = 'jonghoo_bae'
#login
browser.find_element_by_name('username').send_keys(username)
browser.find_element_by_name('password').send_keys(password)
browser.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button').submit()

time.sleep(5)

browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

time.sleep(2)

browser.execute_script("document.querySelectorAll('.-nal3')[1].click();")

time.sleep(1)

oldHeight = -1
newHeight = -2
while oldHeight != newHeight:
    oldHeight = newHeight
    newHeight = browser.execute_script("return document.querySelectorAll('.jSC57')[0].scrollHeight")
    browser.execute_script("document.querySelectorAll('.isgrP')[0].scrollTo(0,document.querySelectorAll('.jSC57')[0].scrollHeight)")
    time.sleep(1.5)

soup = BeautifulSoup(browser.page_source, 'html.parser')
followers = soup.findAll('a',['FPmhX','notranslate','_0imsa'])
followers_text = []
for follower in followers:
    followers_text.append(follower.get_text())

print("Followers Count : " + str(len(followers_text)))

browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()

time.sleep(0.5)

browser.execute_script("document.querySelectorAll('.-nal3')[2].click();")

time.sleep(1)

oldHeight = -1
newHeight = -2
while oldHeight != newHeight:
    oldHeight = newHeight
    newHeight = browser.execute_script("return document.querySelectorAll('.jSC57')[0].scrollHeight")
    browser.execute_script("document.querySelectorAll('.isgrP')[0].scrollTo(0,document.querySelectorAll('.jSC57')[0].scrollHeight)")
    time.sleep(1.5)

soup = BeautifulSoup(browser.page_source, 'html.parser')
followings = soup.findAll('a',['FPmhX','notranslate','_0imsa'])
followings_text = []
for following in followings:
    followings_text.append(following.get_text())

print("Followings Count : " + str(len(followings_text)))

listUnfollower = []
for following in followings_text:
    cnt = 0
    for follower in followers_text:
        if following == follower:
            cnt += 1
            break
    if cnt == 0:
        listUnfollower.append(following)

print('Number of Unfollowers : '+str(len(listUnfollower)))
print('List of Unfollowers : '+str(listUnfollower))

listUnfollowing = []
for follower in followers_text:
    cnt = 0
    for following in followings_text:
        if follower == following:
            cnt += 1
            break
    if cnt == 0:
        listUnfollowing.append(follower)

print('Number of Unfollowings : '+str(len(listUnfollowing)))
print('List of Unfollowings : '+str(listUnfollowing))
#
#
# filePath = './20201203.txt'
# testList = ['123', '456', 'abc', 'def']
# with open(filePath, 'wb') as lf:
#     pickle.dump(testList, lf)
#
#
# with open(filePath, 'rb') as lf:
#     readList = pickle.load(lf)
#     print(readList)
#     # ['123', '456', 'abc', 'def']