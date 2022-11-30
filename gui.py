import PySimpleGUI as sg

#create a window function with a white background and a title of "Banking System" and a size of 500x500 pixels and a layout of 3 rows and 3 columns login, register and exit buttons
def create_window():
    sg.theme('LightGrey1')
    layout = [
        [sg.Button('Login', size=(10, 2), key='login'), sg.Button('Register', size=(10, 2), key='register'), sg.Button('Exit', size=(10, 2), key='exit')]
    ]
    return sg.Window('AUT BANK', layout, finalize=True)

#login function that takes the user to the login window
def login():
    layout = [
        [sg.Text('Client number: '), sg.Input(key='client_number')],
        [sg.Text('Password: '), sg.Input(key='password')],
        [sg.Button('Login', key='login'), sg.Button('Back', key='back')]
    ]
    return sg.Window('Login', layout, finalize=True)

#register function that takes the user to the register window
def register():
    layout = [
        [sg.Text('Name: '), sg.Input(key='name')],
        [sg.Text('Surname: '), sg.Input(key='surname')],
        [sg.Text('Age: '), sg.Input(key='age')],
        [sg.Button('Register', key='register'), sg.Button('Back', key='back')]
    ]
    return sg.Window('Register', layout, finalize=True)

#main function that runs the program
def main():
    window1, window2, window3 = create_window(), None, None
    while True:
        window, event, values = sg.read_all_windows()
        if window == window1 and event == sg.WIN_CLOSED or event == 'exit':
            break
        if window == window1 and event == 'login':
            window1.hide()
            window2 = login()
        if window == window2 and event == 'back':
            window2.hide()
            window1.un_hide()
        if window == window1 and event == 'register':
            window1.hide()
            window3 = register()
        if window == window3 and event == 'back':
            window3.hide()
            window1.un_hide()
    window1.close()
    window2.close()
    window3.close()

if __name__ == '__main__':
    main()