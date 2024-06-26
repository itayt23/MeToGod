import PySimpleGUI as sg

class Layout:
    def __init__(self):
        sg.theme("DarkBrown")
        self.layout_main = [[sg.T("")],
        [sg.T("     "),sg.Button("Read from WhatsApp", size=(20,4)),sg.T("                "), sg.Button("Read from Excel File", size=(20,4))],
        [sg.T("")],
        [sg.Button("Read from WhatsApp - Numbers Only", size=(30,4)),sg.T("      "),sg.Button("Split Excel File", size=(20,4))],
        [sg.T("")],
        [sg.T("")],
        [sg.Button("Exit",size=(8,1),button_color=('red','black'))]]  

        self.layout_excel = [[sg.T("")],
        [sg.Text("Please Enter Group Name: "), sg.Input(key="-FILE_NAME-" ,change_submits=True)],
        [sg.Text("Choose a folder: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FileBrowse(key="-FILE-", file_types=(("Excel Files", "*.xlsx"),("Excel Files", "*.xls")))],
        [sg.Button("Submit")],
        [sg.T("")],
        [sg.Text("Progress: "), sg.ProgressBar(max_value=5, orientation='h', size=(30,20), key="-PROG-")],
        [sg.Text(key='-OUT1-', size=(20, 1))],
        [sg.Button("Exit",size=(8,1),button_color=('red','black'))]]

        self.layout_whatsapp = [[sg.T("")],
        [sg.Text("Please Enter The Exact Group Name: "), sg.Input(key="-GROUP_NAME-" ,change_submits=True), sg.Button("Search",size=(8,1),button_color=('Green','White'))],   
        [sg.T("")],
        [sg.Text("Progress: "), sg.ProgressBar(max_value=7, orientation='h', size=(30,20), key="-PROG-")],
        [sg.Button("Exit",size=(8,1),button_color=('red','black'))]]          

        self.layout_whatsapp_numbers = [[sg.T("")],
        [sg.Text("Please Enter The Exact Group Name: "), sg.Input(key="-GROUP_NAME_2-" ,change_submits=True), sg.Button("Get Numbers",size=(12,1),button_color=('Green','White'))],   
        [sg.T("")],
        [sg.Text("Progress: "), sg.ProgressBar(max_value=5, orientation='h', size=(30,20), key="-PROG-")],
        [sg.Button("Exit",size=(8,1),button_color=('red','black'))]] 

        self.spliting_excel = [[sg.T("")],
        [sg.Text("Please Enter Group Name: "), sg.Input(key="-FILE_NAME-" ,change_submits=True)],
        [sg.Text("Please Enter Split Number: "), sg.Input(key="-SPLIT_NUMBER-" ,change_submits=True)],
        [sg.Text("Choose a Folder: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FileBrowse(key="-FILE-", file_types=(("Excel Files", "*.xlsx"),("Excel Files", "*.xls")))],
        [sg.Button("Split")],
        [sg.T("")],
        [sg.Text("Progress: "), sg.ProgressBar(max_value=10000, orientation='h', size=(30,20), key="-PROG-")],
        [sg.Text(key='-OUT1-', size=(20, 1))],
        [sg.Button("Exit",size=(8,1),button_color=('red','black'))]]

    def getWhatsAppLayout(self):
        return self.layout_whatsapp

    def getWhatsAppNumbersLayout(self):
        return self.layout_whatsapp_numbers

    def getMainLayout(self):
        return self.layout_main

    def getExcelLayout(self):
        return self.layout_excel
    
    def get_split_layout(self):
        return self.spliting_excel

    def getYad2Layout(self):
        return self.layout_yad2
    
    def setWindow(self, layout):
        return sg.Window('Caller Finder',layout, size=(750,350),element_justification='c')
    