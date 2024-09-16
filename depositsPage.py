from tkinter import *
from tkinter import ttk
from sqlFile import Connect
import pandas as pd
from datetime import date
from matplotlib import pyplot as plt
from tkcalendar import *


class DepositsClass:
    def __init__(self) -> None:
        self.depositsPress()

    def depositsPress(self) -> None:
        def update():
            mysqlConnection = Connect()
            depositsData = mysqlConnection.retrieveDepositsInfo()
            trv.delete(*trv.get_children())

            for everyDeposits in depositsData:
                trv.insert("", END, values = everyDeposits)
            depositsPage.after(1000, update)

        depositsPage = Toplevel()
        depositsPage.geometry("850x400")
        depositsPage.title("Term Deposits")

        # main Frame
        mainFrame = ttk.Frame(depositsPage)
        mainFrame.pack(fill = BOTH, expand = 1)

        # main Canvas
        mainCanvas = Canvas(mainFrame)
        mainCanvas.pack(side = BOTTOM, fill = BOTH, expand = 1)

        # Scrollbar
        scrlbar = ttk.Scrollbar(mainFrame, orient = 'horizontal', command = mainCanvas.xview)
        scrlbar.pack(side = BOTTOM, fill = X)

        # Configure canvas
        mainCanvas.configure(xscrollcommand = scrlbar.set)
        mainCanvas.bind('<Configure>', lambda e: mainCanvas.configure(scrollregion = mainCanvas.bbox("all")))

        # other frames inside canvas
        otherFrame = ttk.Frame(mainCanvas)

        # add new frame to windwo in canvas
        mainCanvas.create_window((0, 0), window = otherFrame, anchor = 's')

        ## MySQL shit
        trv = ttk.Treeview(otherFrame, selectmode = 'browse')
        trv.grid(row = 0, column = 0)
        trv["columns"] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14')
        trv['show'] = 'headings'

        trv.column("1", width = 150, anchor = 'c')
        trv.column("2", width = 180, anchor = 'c')
        trv.column("3", width = 150, anchor = 'c')
        trv.column("4", width = 150, anchor = 'c')
        trv.column("5", width = 150, anchor = 'c')
        trv.column("6", width = 150, anchor = 'c')
        trv.column("7", width = 150, anchor = 'c')
        trv.column("8", width = 150, anchor = 'c')
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

        ttk.Button(otherFrame, text = "Download as CSV", command = self.downloadAsCSV).grid(row = 1, column = 0, padx = 10, pady = 10, ipadx = 50, sticky = E)
        ttk.Button(otherFrame, text = "Download as PDF", command = self.donwloadAsPDF).grid(row = 2, column = 0, padx = 10, pady = 10, ipadx = 50, sticky = E)

        ttk.Button(otherFrame, text = "Add More", command = self.addData_deposits).grid(row = 3, column = 0, padx = 10, pady = 10, ipadx = 63, sticky = E)

        update()

        depositsPage.mainloop()

    def downloadAsCSV(self):
        mysqlConnection = Connect()
        depositsData = mysqlConnection.retrieveDepositsInfo()

        financialOrganization_csv = []
        NameOfFinancialInstitution_csv = []
        branchAddr_csv = []
        typeOfInvestment_csv = []
        investmentNumber_csv = []
        investmentHolder_csv = []
        nominee_csv = []
        nomineeGuardian_csv = []
        investmentAmount_csv = []
        rateOfInvestment_csv = []
        investmentDate_csv = []
        investmentDuration_csv = []
        maturityDate_csv = []
        maturityAmount_csv = []

        for FinancialOrganisation, NameOfFinancialInstitution, BranchAddress, TypeOfInvestment, InvestmentNumber, InvestmentHolder, Nominee, nomineeGuardian, InvestmentAmount, RateOfInvestment, InvestmentDate, InvestmentDuration, MaturityDate, MaturityAmount in depositsData:
            financialOrganization_csv.append(FinancialOrganisation)
            NameOfFinancialInstitution_csv.append(NameOfFinancialInstitution)
            branchAddr_csv.append(BranchAddress)
            typeOfInvestment_csv.append(TypeOfInvestment)
            investmentNumber_csv.append(InvestmentNumber)
            investmentHolder_csv.append(InvestmentHolder)
            nominee_csv.append(Nominee)
            nomineeGuardian_csv.append(nomineeGuardian)
            investmentAmount_csv.append(InvestmentAmount)
            rateOfInvestment_csv.append(RateOfInvestment)
            investmentDate_csv.append(InvestmentDate)
            investmentDuration_csv.append(InvestmentDuration)
            maturityDate_csv.append(MaturityDate)
            maturityAmount_csv.append(MaturityAmount)

        dict_csv = {'Financial Organisation': financialOrganization_csv,
                    'Name of Financial Institution': NameOfFinancialInstitution_csv,
                    'Branch Address': branchAddr_csv,
                    'Type of Investment': typeOfInvestment_csv,
                    'Investment Number': investmentNumber_csv,
                    'Investment Holder': investmentHolder_csv,
                    'Nominee': nominee_csv,
                    'Nominee Guardian': nomineeGuardian_csv,
                    'Investment Amount': investmentAmount_csv,
                    'Rate of Investment': rateOfInvestment_csv,
                    'Investment Date': investmentDate_csv,
                    'investment Duration': investmentDuration_csv,
                    'Maturity Date': maturityDate_csv,
                    'Maturity Amount': maturityAmount_csv}                                    

        df = pd.DataFrame(dict_csv)
        now = date.today()
        df.to_csv(f"termDeposits_{now}_csv.csv")

    def donwloadAsPDF(self):
        mysqlConnection = Connect()
        data = pd.read_sql(mysqlConnection.DEPOSITS_QUERY, con=mysqlConnection.cnx)

        # Generating a PDF table using Matplotlib
        plt.figure(figsize=(14, 10))
        ax = plt.subplot(111, frame_on=False)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        table = plt.table(cellText=data.values, colLabels=data.columns, loc='center')
        plt.title('Deposits Portfolio', fontsize = 15, pad = 50)
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(2, 2)

        # Save the table to a PDF file
        now = date.today()
        plt.savefig(f'deposits_{now}_pdf.pdf', bbox_inches='tight', pad_inches=0.3)
        plt.close()

    def addData_deposits(self):     # Change name - term deposits
        mysqlConnection = Connect()

        popup_deposits = Toplevel()
        popup_deposits.title("Add More (Term Deposits)")
        popup_deposits.geometry('650x650')
        addData_textvar = StringVar()

        # scrollbar
        mainFrame = ttk.Frame(popup_deposits)
        mainFrame.pack(fill = BOTH, expand = 1)

        mainCanvas = Canvas(mainFrame)
        mainCanvas.pack(side = LEFT, fill = BOTH, expand = 1)

        scrlbar = ttk.Scrollbar(mainFrame, orient = VERTICAL, command = mainCanvas.yview)
        scrlbar.pack(side = RIGHT, fill = Y)

        mainCanvas.configure(yscrollcommand = scrlbar.set)
        mainCanvas.bind('<Configure>', lambda e: mainCanvas.configure(scrollregion = mainCanvas.bbox("all")))

        sideFrame = ttk.Frame(mainCanvas)
        mainCanvas.create_window((0, 0), window = sideFrame, anchor = 'nw')

        # Deposits stuff
        ttk.Label(sideFrame, text = "Financial Organisation: ").grid(row = 0, column = 0, padx = 30, pady = 40, sticky = W)
        finOrg_combobox = ttk.Combobox(sideFrame, textvariable = addData_textvar)
        finOrg_combobox.grid(row = 0, column = 1, ipadx = 80)
        finOrg_combobox['values'] = ('Bank', 'Post Office', 'Other')
        finOrg_combobox.state(['readonly'])

        ttk.Label(sideFrame, text = "Name of Financial Institution: ").grid(row = 1, column = 0, padx = 30, pady = 40, sticky = W)
        finInst_entry = ttk.Entry(sideFrame)
        finInst_entry.grid(row = 1, column = 1, ipadx = 80)

        ttk.Label(sideFrame, text = "Branch Address: ").grid(row = 2, column = 0, padx = 30, pady = 40, sticky = W)
        branchAddr_entry = ttk.Entry(sideFrame)
        branchAddr_entry.grid(row = 2, column = 1, ipadx = 80)

        ttk.Label(sideFrame, text = "Type of Investments: ").grid(row = 3, column = 0, padx = 30, pady = 40, sticky = W)
        typeOfInvestments_entry = ttk.Entry(sideFrame)
        typeOfInvestments_entry.grid(row = 3, column = 1, ipadx = 80)

        ttk.Label(sideFrame, text = "Investment Number: ").grid(row = 4, column = 0, padx = 30, pady = 40, sticky = W)
        investmentNo_entry = ttk.Entry(sideFrame)
        investmentNo_entry.grid(row = 4, column = 1, ipadx = 80)

        ttk.Label(sideFrame, text = "Investment Holder: ").grid(row = 5, column = 0, padx = 30, pady = 40, sticky = W)
        investmentHolder_entry = ttk.Entry(sideFrame)
        investmentHolder_entry.grid(row = 5, column = 1, ipadx = 80)

        ttk.Label(sideFrame, text = "Nominee: ").grid(row = 6, column = 0, padx = 30, pady = 40, sticky = W)
        nominee_entry = ttk.Entry(sideFrame)
        nominee_entry.grid(row = 6, column = 1, ipadx = 80)

        ttk.Label(sideFrame, text = "Guarian of Nominee (if nominee is a minor): ").grid(row= 7, column = 0, padx = 30, pady = 40, sticky = W)
        nomineeGuardian_entry = ttk.Entry(sideFrame)
        nomineeGuardian_entry.grid(row = 7, column = 1, ipadx = 80)

        # Make new column - Amount Invested - INT
        ttk.Label(sideFrame, text = "Investment Amount: ").grid(row = 8, column = 0, padx = 30, pady = 40, sticky = W)
        investmentAmount_entry = ttk.Entry(sideFrame)
        investmentAmount_entry.grid(row = 8, column = 1, ipadx = 80)

        ttk.Label(sideFrame, text = "Rate of Interest: ").grid(row = 9, column = 0, padx = 30, pady = 40, sticky = W)
        rateOfInterest_entry = ttk.Entry(sideFrame)
        rateOfInterest_entry.grid(row = 9, column = 1, ipadx = 80)

        ttk.Label(sideFrame, text = "Investment Date: ").grid(row = 10, column = 0, padx = 30, pady = 40, sticky = W)
        investmentDate_entry = DateEntry(sideFrame, selectmode = 'day', date_pattern = 'y-mm-dd')
        investmentDate_entry.grid(row = 10, column = 1, ipadx = 80)

        ttk.Label(sideFrame, text = "Duration of Investment: ").grid(row = 11, column = 0, padx = 30, pady = 40, sticky = W)
        durationOfInvestment_entry = ttk.Entry(sideFrame)
        durationOfInvestment_entry.grid(row = 11, column = 1, ipadx = 80)

        ttk.Label(sideFrame, text = "Maturity Date: ").grid(row = 12, column = 0, padx = 30, pady = 40, sticky = W)
        maturityDate_entry = DateEntry(sideFrame, selectmode = 'day', date_pattern = 'y-mm-dd')
        maturityDate_entry.grid(row = 12, column = 1, ipadx = 80)

        ttk.Label(sideFrame, text = "Maturity Amount: ").grid(row = 13, column = 0, padx = 30, pady = 40, sticky = W)
        maturityAmount_entry = ttk.Entry(sideFrame)
        maturityAmount_entry.grid(row = 13, column = 1, ipadx = 80)

        def addData():
            finOrg = finOrg_combobox.get()
            finInst = finInst_entry.get()
            branchAddr = branchAddr_entry.get()
            typeOfInvestments = typeOfInvestments_entry.get()
            investmentNo = investmentNo_entry.get()
            investmentHolder = investmentHolder_entry.get()
            nominee = nominee_entry.get()
            nomineeGuardian = nomineeGuardian_entry.get()
            investmentAmount = investmentAmount_entry.get()
            rateOfInterest = rateOfInterest_entry.get()
            investmentDate = investmentDate_entry.get()
            durationOfInvestment = durationOfInvestment_entry.get()
            maturityDate = maturityDate_entry.get()
            maturityAmount = maturityAmount_entry.get()

            sql = '''INSERT INTO deposits (FinancialOrganisation, NameOfFinancialInstitution, BranchAddress,
            TypeOfInvestment, InvestmentNumber, InvestmentHolder, Nominee, NomineeGuardian, InvestmentAmount, 
            RateOfInterest, InvestmentDate, InvestmentDuration, MaturityDate, MaturityAmount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''

            sqlValues = (finOrg, finInst, branchAddr, typeOfInvestments, investmentNo, investmentHolder, nominee, nomineeGuardian, investmentAmount,
                        rateOfInterest, investmentDate, durationOfInvestment, maturityDate, maturityAmount)
            
            mysqlConnection.sendDepositsInfo(sql, sqlValues)
            
            popup_deposits.destroy()

        ttk.Button(sideFrame, text = "Add", command = addData).grid(row = 14, column = 1, padx = 30)


if __name__ == "__main__":
    x = DepositsClass()