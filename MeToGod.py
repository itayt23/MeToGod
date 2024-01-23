import PySimpleGUI as sg
from WhatsAppScrap import WhatsAppScrap
from MeScrap import MeScrap
from ExcelRead import ExcelReader 
from window import Layout
import pandas as pd
from pathlib import Path
from datetime import datetime 



layout = Layout()
window = layout.setWindow(layout.getMainLayout())

def split_excel(clients_numbers:list,row_per_file:int,file_name:str):
    size = len(clients_numbers)
    prog_jump = 10000/size
    if(prog_jump < 1): prog_jump = 1
    bar_update = prog_jump
    row_count = 1
    file_count = 1
    temp_df = pd.DataFrame(columns=['Numbers'])
    results_path = Path.cwd() / 'results'
    results_scrap_path = Path.cwd() / 'results' / datetime.now().strftime("%Y-%m-%d")
    if not results_path.exists():
        results_path.mkdir(parents=True)
    if not results_scrap_path.exists():
        results_scrap_path.mkdir(parents=True)
    try:
        for index, number in enumerate(clients_numbers):
            temp_df.loc[row_count,'Numbers'] = number
            row_count = row_count + 1
            if(row_count == row_per_file+1):
                file_name_final = file_name+str(file_count)+'.xlsx'
                temp_df.to_excel(results_scrap_path / file_name_final)
                temp_df = pd.DataFrame(columns=['Numbers'])
                row_count = 1
                file_count = file_count + 1
            window["-PROG-"].UpdateBar(bar_update)
            bar_update = bar_update + prog_jump
        if(not temp_df.empty):
            file_name_final = file_name+str(file_count)+'.xlsx'
            temp_df.to_excel(results_scrap_path / file_name_final)
    except Exception as e:
        print('Problem accured during scarp: '+str(e))
        print(f'the data was export to excel, scarp was stop at symbol No.{index}')

def split_excel(clients_numbers:list,row_per_file:int,file_name:str):
    size = len(clients_numbers)
    prog_jump = 10000/size
    if(prog_jump < 1): prog_jump = 1
    bar_update = prog_jump
    row_count = 1
    file_count = 1
    temp_df = pd.DataFrame(columns=['Numbers'])
    results_path = Path.cwd() / 'results'
    results_scrap_path = Path.cwd() / 'results' / datetime.now().strftime("%Y-%m-%d")
    if not results_path.exists():
        results_path.mkdir(parents=True)
    if not results_scrap_path.exists():
        results_scrap_path.mkdir(parents=True)
    try:
        for index, number in enumerate(clients_numbers):
            temp_df.loc[row_count,'Numbers'] = number
            row_count = row_count + 1
            if(row_count == row_per_file+1):
                file_name_final = file_name+str(file_count)+'.xlsx'
                temp_df.to_excel(results_scrap_path / file_name_final)
                temp_df = pd.DataFrame(columns=['Numbers'])
                row_count = 1
                file_count = file_count + 1
            window["-PROG-"].UpdateBar(bar_update)
            bar_update = bar_update + prog_jump
        if(not temp_df.empty):
            file_name_final = file_name+str(file_count)+'.xlsx'
            temp_df.to_excel(results_scrap_path / file_name_final)
    except Exception as e:
        print('Problem accured during scarp: '+str(e))
        print(f'the data was export to excel, scarp was stop at symbol No.{index}')


def split_dataframe(df: pd.DataFrame, row_per_file: int, file_name: str):
    size = len(df)
    prog_jump = 50000 / size
    if(prog_jump < 1):
        prog_jump = 1
    bar_update = prog_jump
    row_count = 1
    file_count = 1
    temp_df = pd.DataFrame(columns=df.columns)
    results_path = Path.cwd() / 'results'
    results_scrap_path = Path.cwd() / 'results' / datetime.now().strftime("%Y-%m-%d")
    if not results_path.exists():
        results_path.mkdir(parents=True)
    if not results_scrap_path.exists():
        results_scrap_path.mkdir(parents=True)
    try:
        df['טלפון ראשי'] = df['טלפון ראשי'].astype(str).str.zfill(10)
        for index, row in df.iterrows():
            temp_df = temp_df.append(row)
            row_count += 1
            if row_count == row_per_file + 1:
                file_name_final = f"{file_name}{file_count}.xlsx"
                # temp_df['טלפון ראשי'] = temp_df['טלפון ראשי'].astype(str)
                temp_df.to_excel(results_scrap_path / file_name_final, index=False)
                temp_df = pd.DataFrame(columns=df.columns)
                row_count = 1
                file_count += 1
                # Update progress bar
                window["-PROG-"].UpdateBar(bar_update)
                bar_update += prog_jump
        if not temp_df.empty:
            file_name_final = f"{file_name}{file_count}.xlsx"
            temp_df.to_excel(results_scrap_path / file_name_final, index=False)
    except Exception as e:
        print('Problem occurred during scraping: ' + str(e))
        print(f'The data was exported to Excel, scraping stopped at row No.{index}')


if __name__ == "__main__":

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        elif event == "Read from Excel File":
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
        elif event == "Split Excel File":
            window.close()
            window = sg.Window('Caller Finder',layout.get_split_layout(), size=(750,350),element_justification='c')
        elif event == "Split" and values["-FILE_NAME-"] != "" and values["-SPLIT_NUMBER-"] != "":
            file_path = values["-FILE-"]
            file_name = values["-FILE_NAME-"]
            row_per_file = int(values["-SPLIT_NUMBER-"])
            excel_reader = ExcelReader()
            # df = pd.read_excel(file_path)
            # split_dataframe(df,row_per_file,file_name)
            clients_numbers = excel_reader.readFile(file_path)
            split_excel(clients_numbers,row_per_file,file_name)
            # window.perform_long_operation(lambda: split_excel(clients_numbers,row_per_file,file_name), '-OPERATION DONE-')
            break

    window.close()
