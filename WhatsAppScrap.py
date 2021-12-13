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
from difflib import SequenceMatcher


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
        numbers = numbers.replace(" ","").replace("-","").replace("+972","0").replace("\u2066","").replace('\u2069',"")
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
    
    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

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
            group_name = ""
            while(self.similar(group_name, self.group) < 0.5):
                group_name = WebDriverWait(browser, 25).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[1]/div/span"))).text
                if(self.similar(group_name, self.group) > 0.5):
                    time.sleep(3)
                    group_numbers = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]/span"))).text
                    print("WhatsApp looking for phones done successfully, please wait for MeScrapping...")
                    search_box.clear()
                    browser.close()
                    return group_numbers
                else:
                    sg.popup_error(f"Pay Attention!!""\n Error: the group name is not matching the group you choose!\n try again!.")

        except Exception as e:
            sg.popup_error(f"Oops!", e.__class__, "occurred.\n Error: Problem with reading the group numbers.")
            browser.close()
            sys.exit(1)



