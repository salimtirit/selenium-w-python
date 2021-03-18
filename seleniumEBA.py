from selenium import webdriver
import time
browser = webdriver.Chrome()

browser.get("http://www.eba.gov.tr/#/anasayfa")

#//*[@id="ebayaDevamEtButton"]

ebayaDevamEt = browser.find_element_by_xpath('/html/body/app-root/app-anasayfa-page/div[2]/div/div/div[1]/div[2]/div[3]/div[3]/a[3]')

time.sleep(5)

ebayaDevamEt.click()

mebbisIleGir = browser.find_element_by_xpath('//*[@id="teacher"]/div/button[1]/div[2]')

time.sleep(1)

mebbisIleGir.click()

time.sleep(5)
kullanıcıAdı = browser.find_element_by_xpath('//*[@id="txtKullaniciAd"]')

sifre = browser.find_element_by_xpath('//*[@id="txtSifre"]')

kullanıcıAdı.send_keys("")

sifre.send_keys("")

time.sleep(2)

girisYap = browser.find_element_by_xpath('//*[@id="btnGiris"]')

girisYap.click()

time.sleep(10)
#//*[@id="8a840e6a-b424-2f2f-c80c-e7c7c3a2e724"]/div[2]
#//*[@id="724b7835-6628-d10d-57a4-b18dc87e7eaa"]/div[2]/text()
canliDesler = browser.find_elements_by_xpath('//*[@id="vc-left-menu-item"]/a')

canliDesler[2].click()

time.sleep(2)

button  = browser.find_element_by_xpath('//*[@id="liveLessonList"]/div[2]/div/div[2]/div/button')

button.click()

time.sleep(1000)

browser.close()
