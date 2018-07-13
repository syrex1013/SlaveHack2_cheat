from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import numpy as np
import time
import datetime
import random
import requests
import json
options = Options()
options.add_argument("user-data-dir=data-dir");
browser = webdriver.Chrome("chromedriver-dir",chrome_options=options)
browser.get('https://www.slavehack2.com/')
wait = WebDriverWait(browser, 5)
npc_list = []
players_list = []
new_players = []
def bot_sendtext(bot_message):
	
	### Send text message
	bot_token = ''
	bot_chatID = '443032595'
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

	requests.get(send_text)
def scrape_ip_on(ip):
    element1 = browser.find_element_by_xpath('//*[@id="icon-terminal"]')
    element1.click()
    element3 = browser.find_element_by_xpath('//*[@id="icon-logs"]')
    element3.click()
    element2 = browser.find_element_by_xpath('//*[@id="term_command"]')
    time.sleep(5)
    element2.send_keys("pulse "+ip)
    element2.send_keys(Keys.ENTER)
    time.sleep(12)
    element2.send_keys("pulse "+ip)
    element2.send_keys(Keys.ENTER)
    time.sleep(2)
    element2.send_keys("connect "+ip)
    element2.send_keys(Keys.ENTER)
    time.sleep(2)
    delete_logs(1)
    # 38.126.127.136
    count = 1
    new_ips = []
    time.sleep(2)
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=5)
    while True:
        while True:
                try:
                    xpath_string = '//*[@id="body-remote-logs"]/tr['+str(count)+']/td[1]/span[2]'
                    element = browser.find_element_by_xpath(xpath_string)
                    ip = element.text
                    if "[Click To View]" in ip:
                        print("CLICK")
                        xpath_string = '//*[@id="body-remote-logs"]/tr['+str(count)+']/td[1]/span[2]/span'
                        element222 = browser.find_element_by_xpath(xpath_string)
                        element222.click()
                        ip = element222.get_attribute('innerHTML')
                        if ip not in new_ips:
                            print(ip)
                            new_ips.append(ip)
                            count += 1
                            delete_logs(1)
                        else:
                            count += 1
                            delete_logs(1)
                    else:
                        count += 1
                        print(ip)
                        new_ips.append(ip)
                        delete_logs(1)
                except Exception as e:
                    count = 1
                    break;
        if datetime.datetime.now() >= endTime:
                    break;
    time.sleep(2)
    element2.send_keys("exit")
    element2.send_keys(Keys.ENTER)
    hackip(new_ips)
def do_mission_medium(loop_times):
    bot_sendtext("Started doing mission medium")
    element1 = browser.find_element_by_xpath('//*[@id="icon-terminal"]')
    element1.click()
    element3 = browser.find_element_by_xpath('//*[@id="icon-logs"]')
    element3.click()
    element2 = browser.find_element_by_xpath('//*[@id="term_command"]')
    time.sleep(5)
    element11 = browser.find_element_by_xpath('//*[@id="icon-start"]')
    element11.click()
    time.sleep(2)
    element12 = browser.find_element_by_xpath('//*[@id="tb-missions"]')
    element12.click()
    time.sleep(2)
    element11 = browser.find_element_by_xpath('//*[@id="icon-start"]')
    element11.click()
    time.sleep(2)
    element12 = browser.find_element_by_xpath('//*[@id="tb-slavelist"]')
    element12.click()
    time.sleep(2)
    for x in range(loop_times):
        time.sleep(5)
        element13 = browser.find_element_by_xpath('//*[@id="body-missions"]/table[17]/tbody/tr')
        element13.click()
        time.sleep(5)
        element14 = browser.find_element_by_xpath('//*[@id="mission_accept"]')
        element14.click()
        time.sleep(5)
        element15 = browser.find_element_by_xpath('//*[@id="body-missions"]/table/tbody/tr/td[2]/small/b[3]')
        element16 = browser.find_element_by_xpath('//*[@id="body-missions"]/table/tbody/tr/td[2]/small/b[1]')
        element17 = browser.find_element_by_xpath('//*[@id="body-missions"]/table/tbody/tr/td[1]/small/b[1]')
        file = element15.get_attribute('innerHTML')
        ip = element16.get_attribute('innerHTML')
        employer = element17.get_attribute('innerHTML')
        time.sleep(2)
        element2.send_keys("pulse "+ip)
        time.sleep(1)
        element2.send_keys(Keys.ENTER)
        time.sleep(12)
        element2.send_keys("pulse "+ip)
        time.sleep(1)
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        element2.send_keys("connect "+ip)
        time.sleep(1)
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        delete_logs(1)
        element2.send_keys("connect "+ip)
        time.sleep(1)
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        delete_logs(1)
        element2.send_keys("download "+file)
        time.sleep(1)
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        while True:
            try:
                element5 = browser.find_element_by_class_name('done')
                time.sleep(2)
                element5.click()
                break;
            except Exception as e:
                print("Waiting for task to complete")
                try:
                    time.sleep(2)
                    element18 = browser.find_element_by_xpath('//*[@id="process_network"]/div')
                    element18.click()
                except Exception as e:
                    print("No need for waiting")
                    break;
        time.sleep(2)
        delete_logs(1)
        time.sleep(4)
        element2.send_keys("exit")
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        count = 1
        ip2 = ('1.1.1.1')
        while True:
            try:
                xpath_string = '//*[@id="slaves_npcs"]/tr['+str(count)+']/td[1]/span'
                element = browser.find_element_by_xpath(xpath_string)
                employer_selected = element.text
                print("Employer selected: "+employer_selected+" Employer: "+employer)
                if employer in employer_selected:
                    print("FOUND")
                    element44 = browser.find_element_by_xpath('//*[@id="slaves_npcs"]/tr['+str(count)+']/td[1]/a')
                    ip2 = element44.get_attribute('innerHTML')
                    break;
                count += 1
            except Exception as e:
                print("Error")
                break;
        
        time.sleep(2)
        element2.send_keys("connect "+ip2)
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        delete_logs(1)
        element2.send_keys("connect "+ip2)
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        delete_logs(1)
        element2.send_keys("upload "+file)
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        while True:
            try:
                element5 = browser.find_element_by_class_name('done')
                time.sleep(2)
                element5.click()
                break;
            except Exception as e:
                print("Waiting for task to complete")
                try:
                    time.sleep(2)
                    element18 = browser.find_element_by_xpath('//*[@id="process_network"]/div')
                    element18.click()
                except Exception as e:
                    print("No need for waiting")
                    break;
        time.sleep(3)
        delete_logs(1)
        time.sleep(2)
        element2.send_keys("exit")
        element2.send_keys(Keys.ENTER)
        time.sleep(4)
        element17 = browser.find_element_by_xpath('//*[@id="body-missions"]/table/tbody/tr/td[1]/div/button[1]')
        element17.click()
        time.sleep(4)
        element2.send_keys("rm "+file)
        element2.send_keys(Keys.ENTER)
        time.sleep(4)
        while True:
            try:
                element5 = browser.find_element_by_class_name('done')
                time.sleep(2)
                element5.click()
                break;
            except Exception as e:
                print("Waiting for task to complete")
                try:
                    time.sleep(2)
                    element18 = browser.find_element_by_xpath('//*[@id="process_cpu"]/div')
                    element18.click()
                except Exception as e:
                    print("No need for waiting")
                    break;
        time.sleep(4)
        delete_logs(1)
        time.sleep(2)
        bot_sendtext("Done mission "+str(x)+"/"+str(loop_times))
        time.sleep(5)
def do_mission_easy(loop_times):
    bot_sendtext("Started doing mission easy")
    element1 = browser.find_element_by_xpath('//*[@id="icon-terminal"]')
    element1.click()
    element3 = browser.find_element_by_xpath('//*[@id="icon-logs"]')
    element3.click()
    element2 = browser.find_element_by_xpath('//*[@id="term_command"]')
    time.sleep(5)
    element11 = browser.find_element_by_xpath('//*[@id="icon-start"]')
    element11.click()
    time.sleep(2)
    element12 = browser.find_element_by_xpath('//*[@id="tb-missions"]')
    element12.click()
    time.sleep(2)
    for x in range(loop_times):
        element13 = browser.find_element_by_xpath('//*[@id="body-missions"]/table[10]/tbody/tr')
        element13.click()
        time.sleep(2)
        element14 = browser.find_element_by_xpath('//*[@id="mission_accept"]')
        element14.click()
        time.sleep(5)
        element15 = browser.find_element_by_xpath('//*[@id="body-missions"]/table/tbody/tr/td[2]/small/b[3]')
        element16 = browser.find_element_by_xpath('//*[@id="body-missions"]/table/tbody/tr/td[2]/small/b[1]')
        file = element15.get_attribute('innerHTML')
        ip = element16.get_attribute('innerHTML')
        element2.send_keys("pulse "+ip)
        element2.send_keys(Keys.ENTER)
        time.sleep(12)
        element2.send_keys("pulse "+ip)
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        element2.send_keys("connect "+ip)
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        delete_logs(1)
        element2.send_keys("connect "+ip)
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        delete_logs(1)
        element2.send_keys("rm "+file)
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        while True:
            try:
                element5 = browser.find_element_by_class_name('done')
                time.sleep(2)
                element5.click()
                break;
            except Exception as e:
                print("Waiting for task to complete")
                try:
                    time.sleep(2)
                    element18 = browser.find_element_by_xpath('//*[@id="process_cpu"]/div')
                    element18.click()
                except Exception as e:
                    print("No need for waiting")
                    break;
        time.sleep(3)
        delete_logs(1)
        time.sleep(4)
        element2.send_keys("exit")
        element2.send_keys(Keys.ENTER)
        time.sleep(2)
        element17 = browser.find_element_by_xpath('//*[@id="body-missions"]/table/tbody/tr/td[1]/div/button[1]')
        element17.click()
        time.sleep(2)
        bot_sendtext("Done mission "+str(x)+"/"+str(loop_times))
def wait_for_login():
    timeout = 5
    while True:
        try:
            element_present = EC.presence_of_element_located((By.ID, 'sketcher_icon'))
            WebDriverWait(browser, timeout).until(element_present)
            break;
        except TimeoutException:
            print ("Not logged")
def get_npc_ips(count,npc_list):
    while True:
        try:
            xpath_string = '//*[@id="slaves_npcs"]/tr['+str(count)+']/td[1]/a'
            element = browser.find_element_by_xpath(xpath_string)
            print("IP:")
            print(element.get_attribute('innerHTML'))
            print("Count:")
            print(count)
            print("Xpath:")
            print(xpath_string)
            npc_list.append(element.get_attribute('innerHTML'))
            count += 1
        except Exception as e:
            print("All npc ips found")
            break;
def get_player_ips(count,players_list):
    while True:
        try:
            xpath_string = '//*[@id="slaves_players"]/tr['+str(count)+']/td[1]/a'
            element = browser.find_element_by_xpath(xpath_string)
            print("IP:")
            print(element.get_attribute('innerHTML'))
            print("Count:")
            print(count)
            print("Xpath:")
            print(xpath_string)
            players_list.append(element.get_attribute('innerHTML'))
            count += 1
        except Exception as e:
            print("All player ips found")
            break;
def delete_logs(count):
    try:
                xpath_string = '//*[@id="body-remote-logs"]/tr['+str(count)+']/td[2]/a'
                element = browser.find_element_by_xpath(xpath_string)
                element.click()
    except:
        print("All logs deleted")
def get_output():
    element = browser.find_element_by_xpath('//*[@id="term_dump"]')
    return element.get_attribute('innerHTML')

def runcommand(command,list_of_targets,count):
    myarray = np.asarray(list_of_targets)
    element1 = browser.find_element_by_xpath('//*[@id="icon-terminal"]')
    element1.click()
    element3 = browser.find_element_by_xpath('//*[@id="icon-logs"]')
    element3.click()
    time.sleep(5)
    for x in range(len(list_of_targets)):
        element2 = browser.find_element_by_xpath('//*[@id="term_command"]')
        element2.send_keys("pulse "+myarray[x])
        element2.send_keys(Keys.ENTER)
        time.sleep(10)
        element2.send_keys("connect "+myarray[x])
        element2.send_keys(Keys.ENTER)
        time.sleep(2) #log sleep time
        delete_logs(count)
        element2.send_keys("connect "+myarray[x])
        element2.send_keys(Keys.ENTER)
        time.sleep(2) #log sleep time
        delete_logs(count)
        commands = command.split(',')
        for xx in range(len(commands)):
            try:
                time.sleep(5)
                element4 = browser.find_element_by_xpath('//*[@id="term_command"]')
                element4.send_keys(str(commands[xx]))
                element4.send_keys(Keys.ENTER)
                delete_logs(count)
                time.sleep(1)
                element2.send_keys("scan")
                element2.send_keys(Keys.ENTER)
                while True:
                    try:
                        element5 = browser.find_element_by_class_name('done')
                        time.sleep(2)
                        element5.click()
                        break;
                    except Exception as e:
                        print("Waiting for task to complete")
                        try:
                            time.sleep(2)
                            element14 = browser.find_element_by_xpath('//*[@id="process_network"]/div')
                            element14.click()
                        except Exception as e:
                            print("No need for waiting")
                            break;
                count = 1
                time.sleep(2)
                delete_logs(count)
            except Exception as e:
                print("Command cannot be executed")
                break;
        time.sleep(1)
        element4.send_keys(str("exit"))
        element4.send_keys(Keys.ENTER)
        time.sleep(2)
def mine(list_of_targets,count):
    bot_sendtext("Started collecting")
    myarray = np.asarray(list_of_targets)
    for x in range(len(list_of_targets)):
        element1 = browser.find_element_by_xpath('//*[@id="icon-terminal"]')
        element1.click()
        element3 = browser.find_element_by_xpath('//*[@id="icon-logs"]')
        element3.click()
        element2 = browser.find_element_by_xpath('//*[@id="term_command"]')
        element2.send_keys("connect "+myarray[x])
        element2.send_keys(Keys.ENTER)
        time.sleep(1) #log sleep time
        delete_logs(count)
        element2.send_keys("connect "+myarray[x])
        element2.send_keys(Keys.ENTER)
        time.sleep(1) #log sleep time
        delete_logs(count)
        element2.send_keys("mine")
        element2.send_keys(Keys.ENTER)
        time.sleep(1) #log sleep time
        delete_logs(count)
        time.sleep(1)
        element2.send_keys("scan")
        element2.send_keys(Keys.ENTER)
        time.sleep(1)
        element2.send_keys("exit")
        element2.send_keys(Keys.ENTER)
        time.sleep(1) #log sleep time
    print("All hosts mined")
    bot_sendtext("Done collecting")
def turnon(count):
    element11 = browser.find_element_by_xpath('//*[@id="icon-start"]')
    element11.click()
    time.sleep(2)
    element12 = browser.find_element_by_xpath('//*[@id="tb-slavelist"]')
    element12.click()
    while True:
        try:
            xpath_string = '//*[@id="slaves_npcs"]/tr['+str(count)+']/td[3]/a'
            element = browser.find_element_by_xpath(xpath_string)
            element.click()    
            count += 1
        except Exception as e:
            print("All npc running "+ element.get_attribute('innerHTML'))
            break;
def ip_ninja(list_of_targets):
    bot_sendtext("Started ip ninja")
    myarray = np.asarray(list_of_targets)
    for x in range(len(list_of_targets)):
        element1 = browser.find_element_by_xpath('//*[@id="icon-terminal"]')
        element1.click()
        element3 = browser.find_element_by_xpath('//*[@id="icon-logs"]')
        element3.click()
        element2 = browser.find_element_by_xpath('//*[@id="term_command"]')
        element2.send_keys("connect "+myarray[x])
        element2.send_keys(Keys.ENTER)
        time.sleep(2) #log sleep time
        delete_logs(1)
        time.sleep(1)
        element2.send_keys("scan")
        element2.send_keys(Keys.ENTER)
        t_end = time.time() + 60 * 10
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=10)
        while True:
            try:
                count = 1
                for x in range(10):
                    xpath_string = '//*[@id="body-remote-logs"]/tr['+str(count)+']/td[1]/span[2]/span'
                    element = browser.find_element_by_xpath(xpath_string)
                    element.click()
                    if element.get_attribute('innerHTML') not in new_players:
                        print("Found new ip: "+element.get_attribute('innerHTML'))
                        bot_sendtext("Found new ip!")
                        new_players.append(element.get_attribute('innerHTML'))              
                    delete_logs(1)
                    count +=1
            except Exception as e:
                pass
            if datetime.datetime.now() >= endTime:
                break;
        print("Connecting to new ip")
        element2.send_keys("exit")
        element2.send_keys(Keys.ENTER)
        time.sleep(2) #log sleep time
    print("Hacking new ips")
    hackip(new_players)
def try_to_find_ip():
    for x in range(100):
        ip = ".".join(map(str, (random.randint(0, 255) 
                        for _ in range(4))))
        element1 = browser.find_element_by_xpath('//*[@id="icon-terminal"]')
        element1.click()
        element3 = browser.find_element_by_xpath('//*[@id="icon-logs"]')
        element3.click()
        element2 = browser.find_element_by_xpath('//*[@id="term_command"]')
        time.sleep(2)
        element2.send_keys("pulse "+ip)
        element2.send_keys(Keys.ENTER)
        time.sleep(1)
        element2.send_keys("exit")
        element2.send_keys(Keys.ENTER)
        time.sleep(1)
    print("Finished getting ips")
        
def hackip(ip_list):
        bot_sendtext("Started hacking ips")
        myarray = np.asarray(ip_list)
        for x in range(len(myarray)):
            element1 = browser.find_element_by_xpath('//*[@id="icon-terminal"]')
            element1.click()
            element3 = browser.find_element_by_xpath('//*[@id="icon-logs"]')
            element3.click()
            element2 = browser.find_element_by_xpath('//*[@id="term_command"]')
            element2.send_keys("pulse "+myarray[x])
            element2.send_keys(Keys.ENTER)
            time.sleep(10) #log sleep time
            element2.send_keys("connect "+myarray[x])
            element2.send_keys(Keys.ENTER)
            time.sleep(2) #log sleep time
            delete_logs(count)
            element2.send_keys("connect "+myarray[x])
            element2.send_keys(Keys.ENTER)
            time.sleep(2) #log sleep time
            delete_logs(count)
            element2.send_keys("scan")
            element2.send_keys(Keys.ENTER)
            time.sleep(2) #log sleep time
            element2.send_keys("exit")
            element2.send_keys(Keys.ENTER)
        bot_sendtext("All ips hacked")
wait_for_login()
print("LOGGED")
time.sleep(30)
count = 1
get_npc_ips(count,npc_list)
count = 1
get_player_ips(count,players_list)
count = 1
ans=True
while ans:
    count = 1
    print ("""
    1.Hack npc and do something
    2.Hack players and do something
    3.Mine coins on npc
    4.Mine coins on players
    5.Turn on mining
    6.Ip ninja
    7.Find random ips
    8.Do mission (easy)
    9.Do mission (medium)
    10.Scrape ip on
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
      print("\n Write command to run after hack: (To run multiple commands just type command,command,command)")
      input1 = input()
      runcommand(input1,npc_list,count)
    elif ans=="2":
      print("\n Write command to run after hack: (To run multiple commands just type command,command,command)")
      input2 = input()
      runcommand(input2,players_list,count)
    elif ans =="3":
      print("\n Collecting money")
      mine(npc_list,count)
    elif ans =="4":
      print("\n Collecting money")
      mine(players_list,count)
    elif ans =="5":
      print("\n Turning on mining")
      turnon(count)
    elif ans =="6":
      print("\n Turn on ip Ninja")
      ip_ninja(npc_list)
    elif ans =="7":
      print("\n Finding ips")
      try_to_find_ip()
    elif ans =="8":
      print("\n Doing mission easy")
      do_mission_easy(1000)
    elif ans =="9":
      print("\n Doing mission medium")
      do_mission_medium(1000)
    elif ans=="10":
      print("\n Type ip")
      input2 = input()
      scrape_ip_on(input2)
