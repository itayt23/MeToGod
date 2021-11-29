from WhatsAppScrap import WhatsAppScrap
from MeScrap import MeScrap

def main():
    group_name = input("Paste here the excactly Group name:")
    whatsapp_scraper = WhatsAppScrap(group_name)
    numbers = whatsapp_scraper.searchNumbers()
    whatsapp_scraper.numbers = whatsapp_scraper.fixNumbers(numbers)
    me_scraper = MeScrap(whatsapp_scraper.numbers,group_name)
    me_scraper.clients = me_scraper.getClients(whatsapp_scraper.numbers)
    me_scraper.writeFile()
    


if __name__ == "__main__":
    main()
    print("Application finished successfully :) ")
    input('Press ENTER to exit') 