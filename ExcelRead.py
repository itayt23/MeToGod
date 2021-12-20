import pandas as pd
import sys
import PySimpleGUI as sg

from pandas.core.indexing import _iLocIndexer

class ExcelReader:

    def __init__(self) -> None:
        pass

    def pathFix(self,input_path):
            input_path = input_path.split('\\')
            input_path = input_path[-1]
            input_path = input_path[:-1]
            return input_path           
    
    def fixFile(self, file):
        try:
            print(file.iloc[0,0])
            if(file.iloc[0,0] == '0' or file.iloc[0,0] == 0):
                clients_df = file[file.iloc[:,1].notnull()]
                column = 1
            else:
                clients_df = file[file.iloc[:,0].notnull()]
                column = 0
            clients_df = clients_df.reset_index(drop=True)
            clients= []
            for  i in clients_df.iloc[:,column]:
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
                    elif (number_string[0:3] =='972'):
                        number = "0" + number_string[3:12]
                        clients.append(number)
                else:
                    if(i[0:2]  == '05' or  i[0] == '5' or i[0:3] == '972'):
                        clients.append(i)
            return clients
        except Exception as e:
            sg.popup_error(f"Oops!", e.__class__, "occurred.\n Error: Problem with reading the numbers in the file, check if the numbers are in column 0.")
            sys.exit(1)

    def readFile(self, input_path):
        try:
            clients_df = pd.read_excel(input_path)
        except Exception as e:
            sg.popup_error(f"Oops!", e.__class__, "occurred.\n Error: Problem with reading file.")
            sys.exit(1)
        return self.fixFile(clients_df)
