# -*- coding: utf-8 -*-
#######################################################################
# FRIENDLY BOT 👾 TO AUTOMATE FOLLOWER BULK MESSAGE
# version   0.0 
# status:   not working yet
########################################################################
from selenium import webdriver #cant run this command
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import schedule

x = 0

def dmer():
    global x
    usrnames = [
'wd05031996',
'sasajenner',
'chefmarcusstoll',
'tuanicarvalho',
'goncalves.csf',
'iguana_garcia',
'___________beatrice',
'calliee7689',
'fedracaseiro0', 'psilva.pati',
'inesmatosg',
'mayraborowikoficial',
'ritameyer.hipnose',
'naturabrasilemportugal',
'yagmar.jovem',
'natashaguterres',
'mezcalorama',
'noussommesephemeres',
'barbbbbbs',
'mega_hair_pt',
'ka.zi6610',
'renatoarroyoo',
'isabellehogarth',
'boochy.boy',
'wd05031996',
'sasajenner',
'chefmarcusstoll',
'tuanicarvalho',
'goncalves.csf',
'iguana_garcia',
'___________beatrice',
'calliee7689',
'fedracaseiro',
'psilva.pati',
'inesmatosg',
'mayraborowikoficial',
'ritameyer.hipnose',
'naturabrasilemportugal',
'yagmar.jovem',
'natashaguterres,'
'mezcalorama,'
'noussommesephemeres',
'barbbbbbs']  # usernames to send dm

    chrome_options = Options()
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    browser = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    usrname_bar = browser.find_element_by_name('username')
    passwrd_bar = browser.find_element_by_name('password')

    username = 'user'  # username here
    password = 'pass'  # password here

    usrname_bar.send_keys(username)
    passwrd_bar.send_keys(password + Keys.ENTER)

    time.sleep(11)

    def send_msg(usrnames):
        browser.get('https://www.instagram.com/direct/new/')

        time.sleep(5) # avoid getting cout as spam

        to_btn = browser.find_element_by_name('queryBox')
        to_btn.send_keys(usrnames)

        time.sleep(8) # avoid getting cout as spam

        chk_mrk = browser.find_element_by_class_name('dCJp8')
        chk_mrk.click()

        time.sleep(3) # avoid getting cout as spam

        nxt_btn = browser.find_element_by_xpath('//div[@class="mXkkY KDuQp"]')
        nxt_btn.click()

        time.sleep(6)

        txt_box = browser.find_element_by_tag_name('textarea')
        txt_box.send_keys("Olá @{usrnames} Queriamos pessoalmente comunicar a todos os nossos queridos clientes que estamos finalmente abertos :) de quartas a domingos das 11.30am às 10pm. Cá vos esperamos, no lugar de sempre")

        time.sleep(2)

        snd_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF')
        snd_btnn = snd_btn[len(snd_btn)-1]
        snd_btnn.click()

        time.sleep(4)

    count = 0
    try:
        for usrnamee in usrnames:
            send_msg(usrnamee)
            count += 1

    except TypeError:
        print('Failed!')

    browser.quit()

    print('''
    Successfully Sent {count} Massages
    ''')

    x += 1


timee = "13:05"  # time for message

try:
    schedule.every().day.at(timee).do(dmer)
except TypeError:
    pass

try:
    while True and x != 1:
        schedule.run_pending()
        time.sleep(1)
except UnboundLocalError:
    pass
