from logging import ERROR
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import PySimpleGUI as sg
import time
import random


class MeScrap:
    numbers = []
    clients = {}
    group =""


    def __init__(self,numbers,group):
        self.numbers = numbers
        self.group = group

    def writeFile(self):
        clients_df = pd.DataFrame(data=self.clients,index=[self.group])
        clients_df = (clients_df.T)
        group_name = self.group.replace('"',"").replace(':',"").replace('?',"").replace('\\',"").replace('/',"").replace('<',"").replace('>',"").replace('*',"").replace('|',"")
        clients_df.to_excel(group_name+' לקוחות.xlsx')

    def loadCookies(self):
        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profile", "wpp")
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir={}".format(profile))
        return options

    def setBrowser(self):
        try:
            cookies = self.loadCookies()
            url = "https://web.me.app/"
            browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=cookies)
            browser.get(url)
            return browser
        except Exception as e:
            sg.popup_error(f"Oops!", e.__class__, "occurred.\n Error: Oppening browser or reading Url.")
            sys.exit(1)

    
    def ScrapClients(self):
        browser = self.setBrowser()
        clients_dict = {}
        search_box =  WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/input")))
        try:
            for index, number in enumerate(self.numbers):
                if(index % random.randint(10,15) == 0): time.sleep(random.uniform(2.5,6))
                search_box.send_keys(number)
                search_box_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/button")))
                if(index % random.randint(5,15) == 0): time.sleep(random.uniform(0.5,3))
                search_box_button.click()
                client_name = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]"))).text
                clients_dict[client_name] = number
                if(index % 20 == 0): time.sleep(10)
                search_box.clear()
            browser.quit()
            self.clients = clients_dict
            #return clients_dict
        except Exception as e:
            self.clients = clients_dict
            self.writeFile()
            sg.popup_error(f"Oops!", e.__class__, "occurred.\n Error: Problem accured during the data reading!! the patch close before it was finish.")
            sys.exit(1)