from tkinter import *
from tkinter import ttk
from mysqlConnection.mysqlConnection import Connect
from pages.insurancePage import InsurancePage
from pages.depositsPage import DepositsPage


class MainScreen:
    def __init__(self):
        self.mysqlConnection = Connect()
        
        self.login()

    def login(self):
        def closeWindow():
            loginPage.destroy()

        def authenticateLogin():
            uInput = userInput.get()
            pInput = passwordInput.get()
            
            content = self.mysqlConnection.retrieveUsersData()
            if content == []:
                loginConfirm_textvar.set("No available records.")
            
            for i in content:
                if uInput in i and pInput in i:
                    loginConfirm_textvar.set("Credentials correct.\nSuccessful login.")
                    closeWindow()
                    self.homePage()
    
                else:
                    loginConfirm_textvar.set("Credentials wrong.\nTry again.")

        loginPage = Tk()
        loginPage.title("Login")

        appBarFrame = ttk.Frame(loginPage)
        appBarFrame.grid(row = 0)
        
        ttk.Label(appBarFrame, text = "LOG IN TO CONTINUE").grid(padx = 20, pady = 20)

        bodyFrame = ttk.Frame(loginPage)
        bodyFrame.grid(row = 1)
        
        ttk.Label(bodyFrame, text = "Username: ").grid(row = 0, column = 0, padx = 10, pady = 5)
        userInput = ttk.Entry(bodyFrame)
        userInput.grid(row = 0, column = 1, padx = 10)

        ttk.Label(bodyFrame, text = "Password: ").grid(row = 1, column = 0, padx = 10, pady = 5)
        passwordInput = ttk.Entry(bodyFrame)
        passwordInput.grid(row = 1, column = 1, padx = 10)

        loginConfirm_textvar = StringVar()
        ttk.Label(bodyFrame, text = "", textvariable = loginConfirm_textvar).grid(row = 2, column = 1)

        ttk.Button(bodyFrame, text = "Log In", command = authenticateLogin).grid(row = 3, column = 1, pady = 20)

        loginPage.mainloop()

    def homePage(self):
        def openInsurance():
            insurance = InsurancePage()

        def openDeposits():
            deposits = DepositsPage()
            
        homePage = Tk()
        homePage.geometry("600x300+0+0")

        ttk.Label(homePage, text = "Finance App").grid(row = 0, column = 1)
        choiceFrame = ttk.Frame(homePage).grid(padx = 125, pady = 50)
        ttk.Button(choiceFrame, text = "Insurance", command = openInsurance).grid(pady = 10, row = 2, column = 1)
        ttk.Button(choiceFrame, text = "Deposits", command = openDeposits).grid(row = 3, column = 1)

        homePage.mainloop()

if __name__ == "__main__":
    mainScreen = MainScreen()
