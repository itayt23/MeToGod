import pandas as pd
import sys

from pandas.core.indexing import _iLocIndexer


class ExcelReader:

    def __init__(self) -> None:
        pass

    def pathFix(self,input_path):
            #input_path = input("Drag input file")
            input_path = input_path.split('\\')
            input_path = input_path[-1]
            input_path = input_path[:-1]
            return input_path


    def readFile(self, input_path):
        try:
            clients_df = pd.read_excel(input_path)
            clients_df = clients_df[clients_df.iloc[:,0].notnull()]
            clients_df = clients_df.reset_index(drop=True)
            clients= []
            for  i in clients_df.columns[0]:
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
                    if(i[0:2]  == '05' or  i[0] == '5'):
                        clients.append(i)
            return clients
        except Exception as e:
            print( "Error found: %s" % str(e) )
            input('Press ENTER to exit') 
            sys.exit(1)