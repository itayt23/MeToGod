import PySimpleGUI as sg
from WhatsAppScrap import WhatsAppScrap
from MeScrap import MeScrap
from ExcelRead import ExcelReader 
from window import Layout
import pandas as pd


layout = Layout()
window = layout.setWindow(layout.getMainLayout())

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Read from Excel file":
        window.close()
        window = sg.Window('Caller Finder',layout.getExcelLayout(), size=(750,350),element_justification='c')
    elif event == "Submit" and values["-FILE_NAME-"] != "":
        window["-PROG-"].UpdateBar(1)
        file_path = values["-FILE-"]
        excel_reader = ExcelReader()
        clients_numbers = excel_reader.readFile(file_path)
        window["-PROG-"].UpdateBar(2)
        me_scraper = MeScrap(clients_numbers,values["-FILE_NAME-"])
        window["-PROG-"].UpdateBar(3)
        me_scraper.ScrapClients()
        window["-PROG-"].UpdateBar(4)
        me_scraper.writeFile()
        window["-PROG-"].UpdateBar(5)
        break
    elif event == "Read from WhatsApp":
        window.close()
        window = sg.Window('Caller Finder',layout.getWhatsAppLayout(), size=(750,350),element_justification='c')
    elif event == "Search" and values["-GROUP_NAME-"] != "":
        window["-PROG-"].UpdateBar(1)
        whatsapp_scraper = WhatsAppScrap(values["-GROUP_NAME-"])
        window["-PROG-"].UpdateBar(2)
        whatsapp_scraper.searchNumbers()
        window["-PROG-"].UpdateBar(3)
        whatsapp_scraper.fixNumbers()
        window["-PROG-"].UpdateBar(4)
        me_scraper = MeScrap(whatsapp_scraper.getNumbers(), values["-GROUP_NAME-"])
        window["-PROG-"].UpdateBar(5)
        me_scraper.ScrapClients()
        window["-PROG-"].UpdateBar(6)
        me_scraper.writeFile()
        window["-PROG-"].UpdateBar(7)
        break
    elif event == "Read from WhatsApp - Numbers Only":
        window.close()
        window = sg.Window('Caller Finder',layout.getWhatsAppNumbersLayout(), size=(750,350),element_justification='c')
    elif event == "Get Numbers" and values["-GROUP_NAME_2-"] != "":
        window["-PROG-"].UpdateBar(1)
        whatsapp_scraper = WhatsAppScrap(values["-GROUP_NAME_2-"])
        window["-PROG-"].UpdateBar(2)
        whatsapp_scraper.searchNumbers()
        window["-PROG-"].UpdateBar(3)
        whatsapp_scraper.fixNumbers()
        window["-PROG-"].UpdateBar(4)
        whatsapp_scraper.writeFile()
        window["-PROG-"].UpdateBar(5)
        break

window.close()
