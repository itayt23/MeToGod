from queue import Empty
import PySimpleGUI as sg
from WhatsAppScrap import WhatsAppScrap
from MeScrap import MeScrap
from ExcelRead import ExcelReader 
import sys

sg.theme("DarkBrown")


layout_main = [[sg.T("")],
        [sg.Button("Read from WhatsApp", size=(20,4)), sg.Button("Read from Excel file", size=(20,4))],
        [sg.T("")],
        [sg.T("")],
        [sg.Button("Exit",size=(8,1),button_color=('red','black'))]]   


layout_excel = [[sg.T("")],
        [sg.Text("Please enter Group name: "), sg.Input(key="-FILE_NAME-" ,change_submits=True)],
        [sg.Text("Choose a folder: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FileBrowse(key="-FILE-", file_types=(("Excel Files", "*.xlsx"),("Excel Files", "*.xls")))],
        [sg.Button("Submit")],
        [sg.T("")],
        [sg.Text("Progress: "), sg.ProgressBar(max_value=5, orientation='h', size=(30,20), key="-PROG-")],
        [sg.Text(key='-OUT1-', size=(20, 1))],
        [sg.Button("Exit",size=(8,1),button_color=('red','black'))]]

layout_whatsapp = [[sg.T("")],
        [sg.Text("Please enter the exact group name: "), sg.Input(key="-GROUP_NAME-" ,change_submits=True), sg.Button("Search")],
        [sg.T("")],
        [sg.Text("Progress: "), sg.ProgressBar(max_value=7, orientation='h', size=(30,20), key="-PROG-")],
        [sg.Text("working....", key="-OUT2-", size=(20,1), justification='c')],
        [sg.Button("Exit",size=(8,1),button_color=('red','black'))]]          

window = sg.Window('Caller Finder',layout_main, size=(750,500),element_justification='c')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Read from Excel file":
        window.close()
        window = sg.Window('Caller Finder',layout_excel, size=(750,500),element_justification='c')
    elif event == "Submit" and values["-FILE_NAME-"] != "":
        window["-PROG-"].UpdateBar(1)
        file_path = values["-FILE-"]
        excel_reader = ExcelReader()
        clients_numbers = excel_reader.readFile(file_path)
        window["-PROG-"].UpdateBar(2)
        me_scraper = MeScrap(clients_numbers,values["-FILE_NAME-"])
        window["-PROG-"].UpdateBar(3)
        me_scraper.clients = me_scraper.getClients(clients_numbers)
        window["-PROG-"].UpdateBar(4)
        me_scraper.writeFile()
        window["-PROG-"].UpdateBar(5)
        break
    elif event == "Read from WhatsApp":
        window.close()
        window = sg.Window('Caller Finder',layout_whatsapp, size=(750,500),element_justification='c')
    elif event == "Search" and values["-GROUP_NAME-"] != "":
        window["-PROG-"].UpdateBar(1)
        whatsapp_scraper = WhatsAppScrap(values["-GROUP_NAME-"])
        window["-PROG-"].UpdateBar(2)
        numbers = whatsapp_scraper.searchNumbers()
        window["-PROG-"].UpdateBar(3)
        whatsapp_scraper.numbers = whatsapp_scraper.fixNumbers(numbers)
        window["-PROG-"].UpdateBar(4)
        me_scraper = MeScrap(whatsapp_scraper.numbers,values["-GROUP_NAME-"])
        window["-PROG-"].UpdateBar(5)
        me_scraper.clients = me_scraper.getClients(whatsapp_scraper.numbers)
        window["-PROG-"].UpdateBar(6)
        me_scraper.writeFile()
        window["-PROG-"].UpdateBar(7)
        break


window.close()





'''
from WhatsAppScrap import WhatsAppScrap
from MeScrap import MeScrap
from ExcelRead import ExcelReader 
import sys

def main():
    user_choose = input("press e for dropping excel file OR press w for whatsapp reading: ")
    if user_choose == 'w':
        group_name = input("Paste here the excactly Group name:")
        whatsapp_scraper = WhatsAppScrap(group_name)
        numbers = whatsapp_scraper.searchNumbers()
        whatsapp_scraper.numbers = whatsapp_scraper.fixNumbers(numbers)
        me_scraper = MeScrap(whatsapp_scraper.numbers,group_name)
        me_scraper.clients = me_scraper.getClients(whatsapp_scraper.numbers)
        me_scraper.writeFile()
    elif user_choose =='e':
        excel_reader = ExcelReader()
        file_path = excel_reader.pathFix()
        clients_numbers = excel_reader.readFile(file_path)
        group_name = input("please enter the group name: ")
        me_scraper = MeScrap(clients_numbers,group_name)
        me_scraper.clients = me_scraper.getClients(clients_numbers)
        me_scraper.writeFile()
    else:
        print("wrong input!")
        input('Press ENTER to exit')
        sys.exit(1)

    


if __name__ == "__main__":
    main()
    print("Application finished successfully :) ")
    input('Press ENTER to exit')

'''