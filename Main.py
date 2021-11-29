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