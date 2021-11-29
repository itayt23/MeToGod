from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

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
        clients_df.to_excel(group_name+' לקוחות מקבוצת.xlsx')

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
            print( "Error found: %s" % str(e) )
            print("Error in oppening browser or reading Url")
            input('Press ENTER to exit') 
            sys.exit(1)

    
    def getClients(self, clients):
        browser = self.setBrowser()
        clients_dict = {}
        search_box =  WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/input")))
        try:
            for number in clients:
                search_box.send_keys(number)
                search_box_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/button")))
                search_box_button.click()
                client_name = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]"))).text
                clients_dict[client_name] = number
                search_box.clear()
            browser.close()
            return clients_dict
        except:
            self.writeFile()
            print("Problem accured during the data reading!! the patch close before it was finish")
            input('Press ENTER to exit') 
            sys.exit(1)



''''
    def pathFix(self):
        input_path = input("Drag input file")
        input_path = input_path.split('\\')
        input_path = input_path[-1]
        input_path = input_path[:-1]
        return input_path

        
    def readFile(input_path):
        try:
            clients_df = pd.read_excel(input_path)
            clients_df = clients_df[clients_df['Unnamed: 0'].notnull()]
            clients_df = clients_df.reset_index(drop=True)
            clients= []
            for  i in clients_df['Unnamed: 0']:
                if(type(i) == float):
                    number_string = str(i)
                    if(number_string[0]  == '5'):
                        number = "0" + number_string[0:9]
                        clients.append(number)
                elif(type(i) == int) :
                    number_string = str(i)
                    if(number_string[0]  == '5'):
                        number = "0" + number_string
                        clients.append(number)
                else:
                    if(i[0:2]  == '05' or  i[0] == '5'):
                        clients.append(i)
            return clients
        except Exception as e:
            print( "Error found: %s" % str(e) )
            input('Press ENTER to exit') 
            sys.exit(1)

'''