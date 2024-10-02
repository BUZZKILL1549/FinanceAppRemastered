from sql.sqlFile import Connect
from tkinter import *
from tkinter import ttk

from dashboard import Dashboard


class Login:
    def __init__(self) -> None:
        self.sqlConnection = Connect()

        self.loginScreen = Tk()
        self.loginScreen.title('Login')

        self.appBarFrame = ttk.Frame(self.loginScreen)
        self.appBarFrame.grid(row = 0)
        
        ttk.Label(self.appBarFrame, text = 'LOGIN TO CONTINUE').grid(padx = 20, pady = 20)

        self.bodyFrame = ttk.Frame(self.loginScreen)
        self.bodyFrame.grid(row = 1)

        ttk.Label(self.bodyFrame, text = 'Username: ').grid(row = 0, column = 0, padx = 10, pady = 5)
        self.userInput = ttk.Entry(self.bodyFrame)
        self.userInput.grid(row = 0, column = 1, padx = 10)

        ttk.Label(self.bodyFrame, text = 'Password: ').grid(row = 1, column = 0, padx = 10, pady = 5)
        self.passwordInput = ttk.Entry(self.bodyFrame, show = '*')
        self.passwordInput.grid(row = 1, column = 1, padx = 10)

        self.loginConfirm_textVar = StringVar()
        ttk.Label(self.bodyFrame, text = '', textvariable = self.loginConfirm_textVar).grid(row = 2, column = 1)

        ttk.Button(self.bodyFrame, text = 'Login', command = self.authenticateLogin).grid(row = 3, column = 1, pady = 20)

        self.loginScreen.mainloop()

    def authenticateLogin(self):
        uInput = self.userInput.get()
        pInput = self.passwordInput.get()

        content = self.sqlConnection.retrieveUserInfo()
        if content == []:
            self.loginConfirm_textVar.set('No available records.')

        for i in content:
            if uInput in i and pInput in i:
                self.loginConfirm_textVar.set('Credentials correct.\nLogin Successful.')
                self.closeWindow()
                Dashboard()
            else:
                self.loginConfirm_textVar.set('Credentials wrong.\nLogin Unsuccessful.')

    def closeWindow(self):
        self.loginScreen.destroy()

if __name__ == '__main__':
    Login()