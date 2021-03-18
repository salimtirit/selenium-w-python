from os import link
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# this is going to be the line acturally
week = 3

# if the lesson is at 8.30 it means it is 17 and if the
# time is bigger or equal to 24 it will be %24 of pm
lessonTimes = [["8:30"], ["9:10", "9:50" , "10:30", "21", "22", "23"], ["3"], ["5"], ["7"]]

lessonTopic = [["FEN BİLİMLERİ 6A"], ["FEN BİLİMLERİ 7A", "FEN BİLİMLERİ 8A", "FEN BİLİMLERİ 9A", "FEN BİLİMLERİ 10A", "FEN BİLİMLERİ 11A", "FEN BİLİMLERİ 12A"], [
    "FEN BİLİMLERİ 13A"], ["FEN BİLİMLERİ 14A"], ["FEN BİLİMLERİ 15A"]]

options = webdriver.ChromeOptions()

options.add_argument(
    r'--user-data-dir=C:\Users\90506\AppData\Local\Google\Chrome\User Data')

# options.add_argument('--profile-directory=Profile 2')

browser = webdriver.Chrome(options=options)

browser.get('https://zoom.us/')

browser.execute_script("window.open('');")

# Switch to the new window
browser.switch_to.window(browser.window_handles[1])


#EBA OPENING PART
browser.get("http://www.eba.gov.tr/#/anasayfa")

def myClick(str):
    try:
        clck = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                 (By.XPATH, str))
        )
        clck.click()
    except:
        browser.quit()

def mySendKeys(str,keys):
    try:
        kys = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                 (By.XPATH, str))
        )
        kys.send_keys(keys)
    except:
        browser.quit()


myClick('/html/body/app-root/app-anasayfa-page/div[2]/div/div/div[1]/div[2]/div[3]/div[3]/a[3]')

myClick('//*[@id="teacher"]/div/button[1]/div[2]')

mySendKeys('//*[@id="txtKullaniciAd"]',"")

mySendKeys('//*[@id="txtSifre"]',"")

time.sleep(5)

myClick('//*[@id="btnGiris"]')

try:
    canliDersler = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH,    '//*[@id="vc-left-menu-item"]/a')) 
    )
    canliDersler[2].click()
except:
    browser.quit()

#this will be deleted
myClick('//*[@id="liveLessonList"]/div[2]/div/div[2]/div/button')

#come back
browser.switch_to.window(browser.window_handles[0])

#signIn
myClick('//*[@id="navbar"]/ul[2]/li[5]/a')

#with google
myClick('//*[@id="login"]/div/div[3]/div/div[4]/a[2]')

#e-mail
myClick('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div')

for i in range(5):
    for j in range(len(lessonTimes[i])):
        #shedule meeting
        myClick('//*[@id="btnScheduleMeeting"]')

        # TOPIC PART
        try:
            topic = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="topic"]'))
            )
            time.sleep(2)
            topic.send_keys(lessonTopic[i][j])
        except:
            browser.quit()

        # DATE PART
        myClick('//*[@id="mt_time"]/div[1]/div/button')

        # select date
        myClick('//*[@id="ui-datepicker-div"]/table/tbody/tr[' +str(week)+']/td['+str(i+1)+']')

        # select time
        mySendKeys('//*[@id="mt_time"]/div[1]/div/div[1]/div/div/div[1]/div/div/input',lessonTimes[i][j])

        """ am = True
        lessonTime = lessonTimes[i][j]
        if(lessonTime >= 24):
            lessonTime = lessonTime%24
            am = False
       
        try:
            b = '//*[@id="select-item-start_time-'+str(lessonTime)+'"]'
            
            timeOfMeeting0 = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, b)
                )
            )
            time.sleep(1)
            timeOfMeeting0.click()
        except:
            browser.quit() """

        # am / pm
        myClick('//*[@id="mt_time"]/div[1]/div/div[2]/div/div/div[1]/div/div/button/i')

        c = ""
        if(True):#change this
            c = '//*[@id="select-item-start_time_2-0"]'
        else:
            c = '//*[@id="select-item-start_time_2-1"]'
        # this is for pm //*[@id="select-item-start_time_2-1"]
        # this is for am //*[@id="select-item-start_time_2-0"]
        try:
            ampm0 = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, c))
            )
            time.sleep(1)
            ampm0.click()
        except:
            browser.quit()

        # DURATION PART
        myClick('//*[@id="mt_time"]/div[2]/div[2]/div[1]/div[1]/div/div[1]/div/div/button')

        try:
            duration0 = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="select-item-duration_hr-0"]'))
            )
            time.sleep(1)
            duration0.click()
        except:
            browser.quit()

        #duration minutes
        myClick('//*[@id="mt_time"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div/button')

        try:
            duration30 = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="select-item-duration_min-2"]'))
            )
            time.sleep(1)
            duration30.click()
        except:
            browser.quit()

        # MEETING ID
        """ try:
            meetingID = WebDriverWait(browser, 10).until(    
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="optionScheduleWithPMI"]'))
                )
            meetingID.click()
        except:
            browser.quit()
         """
        # SAVE
        myClick('//*[@id="meetingSaveButton"]')

        #invite link
        myClick('//*[@id="copyInvitation"]')
        
        text = ""
        try:
            invitation = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="invite_email"]'))
            )
            time.sleep(1)
            text = invitation.text
        except:
            browser.quit()

        list_of_words = text.split()

        link = ""
        p = list_of_words[len(list_of_words)-1]

        for x in list_of_words:
            if x.startswith("https"):
                link = x

        myClick('//*[@id="copyInviteDialog"]/div/div/div[3]/button[2]')

        print(link)
        print(p)

        browser.switch_to.window(browser.window_handles[1])

        mySendKeys('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/input',"FEN BİLİMLERİ")

        myClick('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/select/option[2]')
        
        myClick('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[3]/p/span/button')

        tarih = '//*[@id="datepicker-1773-6601-'+str((week-1)*7+i)+'"]/button'
        
        myClick(tarih)
        
        myClick('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[4]/div/div[2]/select')
        #//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[4]/div/div[2]
        
        #//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[4]/div/div[2]/select/option[2]
        #//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[4]/div/div[2]/select/option[3]
        time.sleep(100)
        #//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/select/option[3]

time.sleep(1000)

browser.close()
