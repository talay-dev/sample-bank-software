import PySimpleGUI as sg
import db
import admin
#create a windoe that will show login and register buttons and exit button with act
def login_window():
    layout = [[sg.Text('Welcome to the ATM')],
              [sg.Button('Login'), sg.Button('Register'), sg.Button('Exit')]]
    return sg.Window('Login', layout)

#function that will show account window with buttons for withdraw, deposit, transfer and exit buttons and show balance of the client and a entry for the amount to withdraw or deposit and a message that will show the result of the withdraw or deposit
def account_window(client_number):
    
    layout = [[sg.Text(client_number,key='cn')],
              [sg.Text('Account')],
              [sg.Text('Balance: '), sg.Text(admin.search_client(client_number)[5],key='balancenow')],
              [sg.Text('Amount: '), sg.Input(key='withdraw_amount')],
              [sg.Button('Withdraw', key='with')],
              [sg.Text(key='withdraw_message')],
              [sg.Text('Amount: '), sg.Input(key='deposit_amount')],
              [sg.Button('Deposit', key='dep')],
              [sg.Text(key='deposit_message')],
              [sg.Button('Exit')]]
    return sg.Window('Account', layout)



#create action for login button
def login_action():
    layout = [[sg.Text('Enter your client number')],
              [sg.Input(key='client_number')],
              [sg.Text('Enter your password')],
              [sg.Input(key='password')],
              [sg.Button('Login',key='logs'), sg.Button('Exit')]]
    return sg.Window('Login', layout)

#create action for register button
def register_action():
    layout = [[sg.Text('Enter your name')],
              [sg.Input(key='name')],
              [sg.Text('Enter your surname')],
              [sg.Input(key='surname')],
              [sg.Text('Enter your age')],
              [sg.Input(key='age')],
              [sg.Button('Register',key='reg'), sg.Button('Exit')]]
    return sg.Window('Register', layout)

def main():
    window = login_window()
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        if event == 'Login':
            window.close()
            window = login_action()
        if event == 'Register':
            window.close()
            window = register_action()
        if event == 'logs':
            if admin.login_parameters_true(values['client_number'], values['password']):
                window.close()
                window = account_window(values['client_number'])
        if event == 'with':
            window['withdraw_message'].update(admin.withdraw(window['cn'].get(), values['withdraw_amount']))
            window['balancenow'].update(admin.search_client(window['cn'].get())[5])
        if event == 'dep':
            window['deposit_message'].update(admin.deposit(window['cn'].get(), values['deposit_amount']))
            window['balancenow'].update(admin.search_client(window['cn'].get())[5])
        if event == 'reg':
            admin.add_client(values['name'], values['surname'], values['age'])
    window.close()

if __name__ == '__main__':
    main()