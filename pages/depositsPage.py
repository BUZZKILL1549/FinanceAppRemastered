from tkinter import *
from tkinter import ttk


class DepositsPage:
    def __init__(self):
        self.depositsPress()

    def depositsPress(self):
        depositsWindow = Tk()
        depositsWindow.geometry("850x400")
        depositsWindow.title("Deposits Window")

        mainFrame = ttk.Frame(depositsWindow)
        mainFrame.pack(fill = BOTH, expand = True)

        trv = ttk.Treeview(mainFrame, selectmode = 'browse')
        trv.grid(row = 0, column = 0, sticky = NSEW)
        trv["columns"] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14')
        trv['show'] = 'headings'

        trv.column("1", width = 150, anchor = 'c')
        trv.column("2", width = 180, anchor = 'c')
        trv.column("3", width = 150, anchor = 'c')
        trv.column("4", width = 150, anchor = 'c')
        trv.column("5", width = 150, anchor = 'c')
        trv.column("6", width = 150, anchor = 'c')
        trv.column("7", width = 150, anchor = 'c')
        trv.column("9", width = 150, anchor = 'c')
        trv.column("10", width = 150, anchor = 'c')
        trv.column("11", width = 150, anchor = 'c')
        trv.column("12", width = 150, anchor = 'c')
        trv.column("13", width = 150, anchor = 'c')
        trv.column("14", width = 150, anchor = 'c')

        trv.heading("1", text = "Financial Organization")
        trv.heading("2", text = "Name of Financial Institution")
        trv.heading("3", text = "Branch Address")
        trv.heading("4", text = "Type of Investment")
        trv.heading("5", text = "Investment Number")
        trv.heading("6", text = "Investment Holder")
        trv.heading("7", text = "Nominee")
        trv.heading("8", text = "Nominee Guardian")
        trv.heading("9", text = "Investment Amount")
        trv.heading("10", text = "Rate of Investment")
        trv.heading("11", text = "Investment Date")
        trv.heading("12", text = "Investment Duration")
        trv.heading("13", text = "Maturity Date")
        trv.heading("14", text = "Maturity Amount")

        trv.delete(*trv.get_children())

        # Create and configure the vertical scrollbar
        vScrlbar = ttk.Scrollbar(mainFrame, orient=VERTICAL, command=trv.yview)
        vScrlbar.grid(row=0, column=1, sticky=NS)
        trv.configure(yscrollcommand=vScrlbar.set)

        # Create and configure the horizontal scrollbar
        hScrlbar = ttk.Scrollbar(mainFrame, orient=HORIZONTAL, command=trv.xview)
        hScrlbar.grid(row=1, column=0, sticky=EW)
        trv.configure(xscrollcommand=hScrlbar.set)

        # Configure the main frame to expand properly
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)

        # Start the main loop
        depositsWindow.mainloop()

if __name__ == "__main__":
    x = DepositsPage()