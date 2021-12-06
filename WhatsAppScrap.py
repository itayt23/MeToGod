from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import time
import PySimpleGUI as sg

class WhatsAppScrap:

    group =""
    numbers = []

    def __init__(self,group_name):
        self.group = group_name
    
    def getGroup(self):
        return self.group
    
    def getNumbers(self):
        return self.numbers


    def fixNumbers(self, numbers):
        numbers_fix =[]
        numbers = numbers.replace(" ","").replace("-","").replace("+972","0")
        numbers = numbers.split(',')
        for i in numbers:
            if(i[0:2] == '05'):
                numbers_fix.append(i)
        return numbers_fix

    def loadCookies(self):
        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profile", "wpp")
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir={}".format(profile))
        return options

    def setBrowser(self):
        cookies = self.loadCookies()
        url = "https://web.whatsapp.com/"
        browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=cookies)
        browser.get(url)
        return browser
    
    def searchNumbers(self):
        browser = self.setBrowser()
        search_box =  WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]")))
        try:
            search_box.send_keys(self.group)
            time.sleep(2)
            group_click = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[4]/div/div/div[2]")))
            group_click.click()
            time.sleep(2)
            group_numbers = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]/span"))).text
            search_box.clear()
            browser.close()
            print("WhatsApp looking for phones done successfully, please wait for MeScrapping...")
            return group_numbers
        except Exception as e:
            sg.popup_error(f"Oops!", e.__class__, "occurred.\n Error: Problem with reading file.")
            browser.close()
            sys.exit(1)



