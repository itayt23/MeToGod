import PySimpleGUI as sg

sg.theme('DarkBrown1')

layout = [[sg.Text("Hellow Bitchesssss")],
[sg.Text("name Here: "),sg.InputText()],
[sg.Button("Ok"), sg.Button("Cancel")]
]

window = sg.Window("CallerFinder", layout, margins=(300, 300))

while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('Your name ', values[0])

    window.close()