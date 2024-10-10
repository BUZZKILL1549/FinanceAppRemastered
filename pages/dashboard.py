from tkinter import *
from tkinter import ttk
from sql.sqlFile import Connect
from toastNotifications import Notify

from insurancePage import InsuranceClass
from depositsPage import DepositsClass

class Dashboard:
    def __init__(self) -> None:
        self.mainPage = Tk()
        self.mainPage.title('Dashboard')
        
        Notify(self.mainPage)

        ttk.Label(self.mainPage, text = 'Finance App').grid(row = 0, column = 0, pady = 10)
        self.choiceFrame = ttk.Frame(self.mainPage)
        self.choiceFrame.grid(padx = 125, pady = 50)
        ttk.Button(self.choiceFrame, text = 'Insurance', command = lambda: InsuranceClass()).grid(row = 1, column = 1, pady = 5, ipadx = 20)
        ttk.Button(self.choiceFrame, text = 'Deposits', command = lambda: DepositsClass()).grid(row = 2, column = 1, pady = 5, ipadx = 20)

        self.mainPage.mainloop()
