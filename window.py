from queue import Empty
import PySimpleGUI as sg
from WhatsAppScrap import WhatsAppScrap
from MeScrap import MeScrap
from ExcelRead import ExcelReader 
import sys


progress = 0
sg.theme("DarkAmber")


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
        [sg.ProgressBar(max_value=5, orientation='h', size=(30,20), key="-PROG-")],
        [sg.Button("Exit",size=(8,1),button_color=('red','black'))]]

layout_whatsapp = [[sg.T("")],
        [sg.Text("Please enter the exact Group name: "), sg.Input(key="-GROUP_NAME-" ,change_submits=True), sg.Button("Search")],
        [sg.T("")],
        [sg.ProgressBar(max_value=5, orientation='h', size=(30,20), key="-PROG-")],
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
        window.close()
    elif event == "Read from WhatsApp":
        window.close()
        window = sg.Window('Caller Finder',layout_whatsapp, size=(750,500),element_justification='c')
        
        

window.close()