from tkinter import *
from tkinter import ttk

class InsurancePage:
    def __init__(self):
        self.insurancePress()

    def insurancePress(self):
        insuranceWindow = Tk()
        insuranceWindow.geometry("850x400")
        insuranceWindow.title("Insurance Window")

        # Main frame to hold the treeview and scrollbars
        mainFrame = ttk.Frame(insuranceWindow)
        mainFrame.pack(fill=BOTH, expand=True)

        # Create the Treeview widget with three columns
        trv = ttk.Treeview(mainFrame, selectmode = BROWSE)
        trv.grid(row=0, column=0, sticky=NSEW)
        trv["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
        trv['show'] = 'headings'

        trv.column("1", width = 150, anchor = 'c')
        trv.column("2", width = 150, anchor = 'c')
        trv.column("3", width = 150, anchor = 'c')
        trv.column("4", width = 150, anchor = 'c')
        trv.column("5", width = 150, anchor = 'c')
        trv.column("6", width = 150, anchor = 'c')
        trv.column("7", width = 150, anchor = 'c')
        trv.column("8", width = 150, anchor = 'c')
        trv.column("8", width = 180, anchor = 'c')
        trv.column("9", width = 150, anchor = 'c')
        trv.column("10", width = 150, anchor = 'c')
        trv.column("11", width = 150, anchor = 'c')
        trv.column("12", width = 150, anchor = 'c')
        trv.column("13", width = 150, anchor = 'c')

        trv.heading('1', text = "Insurance Provider")
        trv.heading('2', text = "Policy Number")
        trv.heading('3', text = "Policy Name")
        trv.heading('4', text = "Policy Holder")
        trv.heading('5', text = "Life Insured")
        trv.heading('6', text = "Sum Assured")
        trv.heading('7', text = "Nominee")
        trv.heading('8', text = "Policy Payment Term")
        trv.heading('9', text = "Premium Payment Frequency")
        trv.heading('10', text = "Last Premium Paid")
        trv.heading('11', text = "Next Premium Due")
        trv.heading('12', text = "Maturity Date")
        trv.heading('13', text = "Maturity Amount")
        
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
        insuranceWindow.mainloop()

if __name__ == "__main__":
    x = InsurancePage()
