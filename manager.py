import db
import PySimpleGUI as sg
import admin

#main screen shows all data of database and can add, delete, update and search clients in database 
def main_screen():
    layout = [[sg.Text('Welcome to the BANK')],
              [sg.Text('Name'), sg.Text('Surname'), sg.Text('Age'), sg.Text('Client number'), sg.Text('Password'), sg.Text('Balance')],
              [sg.Listbox(values=db.get_all_clients(), size=(30, 6), key='clients')],
              [sg.Text('Name: '), sg.Input(key='name')],
              [sg.Text('Surname: '), sg.Input(key='surname')],
              [sg.Text('Age: '), sg.Input(key='age')],
              [sg.Text('Client number: '), sg.Input(key='client_number')],
              [sg.Text('Password: '), sg.Input(key='password')],
              [sg.Text('Balance: '), sg.Input(key='balance')],
              [sg.Text('Search: ',key='search')],
              [sg.Button('Add client', key= 'add'), sg.Button('Delete client', key ='del'), sg.Button('Update client', key ='upd'), sg.Button('Search client', key='ser'), sg.Button('Exit')]]
    return sg.Window('Main screen', layout)

#main loop shows login window
def main():
    window = main_screen()
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        if event == 'log':
            window.close()
            window = main_screen()
        
        if event == 'add':
            admin.add_client(values['name'], values['surname'], values['age'], values['balance'])
            window['clients'].update(db.get_all_clients())
        if event == 'del':
            admin.delete_client(values['client_number'])
            window['clients'].update(db.get_all_clients())
        if event == 'upd':
            admin.update_client(values['name'], values['surname'], values['age'], values['client_number'], values['password'], values['balance'])
            window['clients'].update(db.get_all_clients())
        if event == 'ser':
            window['search'].update(admin.printable_search(values['client_number']))
    window.close()

if __name__ == '__main__':
    main()