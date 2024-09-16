from tkinter import *
from tkinter import ttk
from sqlFile import Connect
from mainPage import main

def login() -> None:
    def performLogin():
        mysqlConnection = Connect()
        userData = mysqlConnection.retrieveUserInfo()

        uname = username.get()
        pwd = password.get()

        for users in userData:
            if not (uname in users and pwd in users):
                wrong.set("Incorrect username or password")
            else:
                wrong.set("Correct! Successful login.")
                login.destroy()
                main()

    login = Tk()
    login.title('Login')

    ttk.Label(login, text = 'Username: ').grid(row = 0, column = 0, padx = 30, pady = 50)
    username = ttk.Entry(login)
    username.grid(padx = 20, row = 0, column = 1, ipadx = 80)

    ttk.Label(login, text = 'Password: ').grid(row = 1, column = 0, padx = 30, pady = 50)
    password = ttk.Entry(login, show = '*')
    password.grid(padx = 20, row = 1, column = 1, ipadx = 80)

    wrong = StringVar()
    ttk.Label(login, text = "", textvariable=wrong).grid(row = 3, column = 1, padx = 15, pady = 30, sticky = W)

    ttk.Button(login, text = 'Login', command = performLogin).grid(row = 2, column = 1, ipadx = 50)

    login.mainloop()

if __name__ == "__main__":
    login()