import PySimpleGUI as sg
from WhatsAppScrap import WhatsAppScrap
from MeScrap import MeScrap
from ExcelRead import ExcelReader 
from window import Layout


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
        me_scraper.clients = me_scraper.getClients(clients_numbers)
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
    elif event == "Read from Yad2":
        window.close()
        window = sg.Window('Caller Finder',layout.getYad2Layout(), size=(750,350),element_justification='c')
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