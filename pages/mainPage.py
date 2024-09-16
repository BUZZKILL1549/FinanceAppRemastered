from tkinter import *
from tkinter import ttk
from insurancePage import InsuranceClass
from depositsPage import DepositsClass

def main() -> None:
    mainPage = Tk()
    mainPage.title("Finance App")
    
    ttk.Label(mainPage, text = "Finance App").grid(row = 0, column = 0, pady = 10)
    choiceFrame = ttk.Frame(mainPage)
    choiceFrame.grid(padx = 125, pady = 50)
    ttk.Button(choiceFrame, text = "Insurance", command = lambda: InsuranceClass()).grid(row = 1, column = 1, pady = 5, ipadx = 20)
    ttk.Button(choiceFrame, text = "Deposits", command = lambda: DepositsClass()).grid(row = 2, column = 1, pady = 5, ipadx = 20)

    mainPage.mainloop()

if __name__ == "__main__":
    main()