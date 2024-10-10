from tkinter import *
from tkinter import ttk
from sql.sqlFile import Connect
import pandas as pd
from datetime import date
from matplotlib import pyplot as plt
from tkcalendar import *


class InsuranceClass:
    def __init__(self) -> None:
        self.insurance()

    def insurance(self) -> None:
        def update():
            mysqlConnection = Connect()
            insuranceData = mysqlConnection.retrieveInsuranceInfo()
            trv.delete(*trv.get_children())

            for everyInsurance in insuranceData:
                trv.insert("", END, values = everyInsurance)
            insurancePage.after(1000, update)

        insurancePage = Toplevel()
        insurancePage.title("Insurance Page")
        insurancePage.geometry("850x400")

        # main Frame
        mainFrame = ttk.Frame(insurancePage)
        mainFrame.pack(fill = BOTH, expand = 1)

        # main Canvas
        mainCanvas = Canvas(mainFrame)
        mainCanvas.pack(side = BOTTOM, fill = BOTH, expand = 1) 

        # Scrollbar
        hScrlbar = ttk.Scrollbar(mainFrame, orient = HORIZONTAL, command = mainCanvas.xview)
        hScrlbar.pack(side = TOP, fill = X)

        # Configure canvas
        mainCanvas.configure(xscrollcommand = hScrlbar.set)
        mainCanvas.bind('<Configure>', lambda e: mainCanvas.configure(scrollregion = mainCanvas.bbox(ALL)))

        # other frames inside canvas
        otherFrame = ttk.Frame(mainCanvas)

        # add new frame to windwo in canvas
        mainCanvas.create_window((0, 0), window = otherFrame, anchor = 's')

        # treeview widget
        trv = ttk.Treeview(otherFrame, selectmode = 'browse')

        # vertical scrollbar
        vScrlbar = ttk.Scrollbar(otherFrame, orient = VERTICAL, command = trv.yview)
        vScrlbar.grid(row = 0, column = 1, sticky = NS)

        # treeview widget continues
        trv.grid(row = 0, column = 0)
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
        
        ttk.Button(otherFrame, text = "Download as CSV", command = self.downloadAsCSV).grid(row = 1, column = 0, padx = 10, pady = 10, ipadx = 50, sticky = E)
        ttk.Button(otherFrame, text = "Download as PDF", command = self.donwloadAsPDF).grid(row = 2, column = 0, padx = 10, pady = 10, ipadx = 50, sticky = E)

        ttk.Button(otherFrame, text = "Add More", command = self.addData_insurance).grid(row = 3, column = 0, padx = 10, pady = 10, ipadx = 63, sticky = E)

        update()

        insurancePage.mainloop()

    def downloadAsCSV(self):
        mysqlConnection = Connect()
        insuranceData = mysqlConnection.retrieveInsuranceInfo()

        insuranceProvider_csv = []
        policyNumber_csv = []
        policyName_csv = []
        policyHolder_csv = []
        lifeInsured_csv = []
        sumAssured_csv = []
        nominee_csv = []
        policyPaymentTerm_csv = []
        premiumPaymentFrequency_csv = []
        lastPremiumPaid_csv = []
        nextPremiumDue_csv = []
        maturityDate_csv = []
        maturityAmount_csv = []

        for insuranceProvider, policyNumber, policyName, policyHolder, lifeInsured, sumAssured, nominee, policyPaymentTerm, premiumPaymentFrequency, lastPremiumPaid, nextPremiumDue, maturityDate, maturityAmount in insuranceData:
            insuranceProvider_csv.append(insuranceProvider)
            policyNumber_csv.append(policyNumber)
            policyName_csv.append(policyName)
            policyHolder_csv.append(policyHolder)
            lifeInsured_csv.append(lifeInsured)
            sumAssured_csv.append(sumAssured)
            nominee_csv.append(nominee)
            policyPaymentTerm_csv.append(policyPaymentTerm)
            premiumPaymentFrequency_csv.append(premiumPaymentFrequency)
            lastPremiumPaid_csv.append(lastPremiumPaid)
            nextPremiumDue_csv.append(nextPremiumDue)
            maturityDate_csv.append(maturityDate)
            maturityAmount_csv.append(maturityAmount)
        
        dict_csv = {'Insurance Provider': insuranceProvider_csv,
                    'Policy Number': policyNumber_csv,
                    'Policy Name': policyName_csv,
                    'Policy Holder': policyHolder_csv,
                    'Life Insured': lifeInsured_csv,
                    'Sum Assured': sumAssured_csv,
                    'Nominee': nominee_csv,
                    'Policy Payment Term': policyPaymentTerm_csv,
                    'Premium Payment Frequency': premiumPaymentFrequency_csv,
                    'Last Premium Paid': lastPremiumPaid_csv,
                    'Next Premium Due': nextPremiumDue_csv,
                    'Maturity Date': maturityDate_csv,
                    'Maturity Amount': maturityAmount_csv}
        
        df = pd.DataFrame(dict_csv)
        now = date.today()
        df.to_csv(f"insurance_{now}_csv.csv")

    def donwloadAsPDF(self):
        mysqlConnection = Connect()
        data = pd.read_sql(mysqlConnection.INSURANCE_QUERY, con=mysqlConnection.cnx)

        # Generating a PDF table using Matplotlib
        plt.figure(figsize=(14, 10))
        ax = plt.subplot(111, frame_on=False)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        table = plt.table(cellText=data.values, colLabels=data.columns, loc='center')
        plt.title('Insurance Portfolio', fontsize = 15, pad = 50)
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(2, 2)

        # Save the table to a PDF file
        now = date.today()
        plt.savefig(f'insurance_{now}_pdf.pdf', bbox_inches='tight', pad_inches=0.3)
        plt.close()

    def addData_insurance(self):
        mysqlConnection = Connect()

        popup_insurance = Toplevel()
        popup_insurance.title("Add More (Insurance)")
        popup_insurance.geometry('650x650')
        addData_textvar = StringVar()

        # scrollbar
        mainFrame = ttk.Frame(popup_insurance)
        mainFrame.pack(fill = BOTH, expand = 1)

        mainCanvas = Canvas(mainFrame)
        mainCanvas.pack(side = LEFT, fill = BOTH, expand = 1)

        scrlbar = ttk.Scrollbar(mainFrame, orient = VERTICAL, command = mainCanvas.yview)
        scrlbar.pack(side = RIGHT, fill = Y)

        mainCanvas.configure(yscrollcommand = scrlbar.set)
        mainCanvas.bind('<Configure>', lambda e: mainCanvas.configure(scrollregion = mainCanvas.bbox("all")))

        sideFrame = ttk.Frame(mainCanvas)
        mainCanvas.create_window((0, 0), window = sideFrame, anchor = 'nw')

        # Insurance Provider goes here
        ttk.Label(sideFrame, text = "Insurance Provider: ").grid(row = 0, column = 0, padx = 30, pady = 40, sticky = W)
        addData_combobox = ttk.Combobox(sideFrame, textvariable = addData_textvar)
        addData_combobox.grid(row = 0, column = 1, ipadx = 80)
        addData_combobox['values'] = ('TATA AIA', 'LIC', 'EDELWEISS TOKIO', 'SBI', 'HDFC LIFE', 'ICICI PRUDENTIAL', 'ADITYA BIRLA SUNLIFE')
        addData_combobox.state(['readonly'])
        
        ttk.Label(sideFrame, text = "Policy Number: ").grid(row = 1, column = 0, padx = 30, pady = 40, sticky = W)
        policyNo_str = StringVar() 
        policyNo_entry = ttk.Entry(sideFrame, textvariable = policyNo_str)
        policyNo_entry.grid(row = 1, column = 1, ipadx = 80)
        
        # Make new column - Policy Name - VARCHAR
        ttk.Label(sideFrame, text = "Policy Name: ").grid(row = 2, column = 0, padx = 30, pady = 40, sticky = W)
        policyName_entry = ttk.Entry(sideFrame)
        policyName_entry.grid(row = 2, column  = 1, ipadx = 80)
        
        # Make new column - Policy Holder - VARCHAR
        ttk.Label(sideFrame, text = "Policy Holder: ").grid(row = 3, column = 0, padx = 30, pady = 40, sticky = W)
        policyHolder_entry = ttk.Entry(sideFrame)
        policyHolder_entry.grid(row = 3, column = 1, ipadx = 80)
        
        # Make new column - Life Insured - VARCHAR
        ttk.Label(sideFrame, text = "Life Insured: ").grid(row = 4, column = 0, padx = 30, pady = 40, sticky = W)
        lifeInsured_entry = ttk.Entry(sideFrame)
        lifeInsured_entry.grid(row = 4, column = 1, ipadx = 80)
        
        # Make new column - Sum Assured - INT
        ttk.Label(sideFrame, text = "Sum Assured: ").grid(row = 5, column = 0, padx = 30, pady = 40, sticky = W)
        sumAssured_var = IntVar()
        sumAssured_entry = ttk.Entry(sideFrame, textvariable = sumAssured_var)
        sumAssured_entry.grid(row = 5, column = 1, ipadx = 80)
        
        # Make new Column - Nominee - VARCHAR --MORE[ALL NOMINEES, PERCENTAGE OF SHARE ACROSS NOMINEES - [BUTTON, NEW TOPLEVEL]]
        ttk.Label(sideFrame, text = "Nominee: ").grid(row = 6, column = 0, padx = 30, pady = 40, sticky = W)
        nominee_entry = ttk.Entry(sideFrame)
        nominee_entry.grid(row = 6, column = 1, ipadx = 80)
        
        # Make new column - Policy Payment Term - INT
        ttk.Label(sideFrame, text = "Policy Payment Term: ").grid(row = 7, column = 0, padx = 30, pady = 40, sticky = W)
        policyPaymentTerm_entry = ttk.Entry(sideFrame)
        policyPaymentTerm_entry.grid(row = 7, column = 1, ipadx = 80)
        
        # Make new column - Premium Payment Freuqency - Annual/Half-yearly/QUarterly/Monthly [dropdown]
        ttk.Label(sideFrame, text = "Premium Payment Frequency: ").grid(row = 8, column = 0, padx = 30, pady = 40, sticky =  W)
        premiumPaymentFrequency_entry = ttk.Entry(sideFrame)
        premiumPaymentFrequency_entry.grid(row = 8, column = 1, ipadx = 80)
        
        ttk.Label(sideFrame, text = "Last Premium Paid: ").grid(row = 9, column = 0, padx = 30, pady = 40, sticky = W)
        lastPremiumPaid_entry = DateEntry(sideFrame, selectmode = 'day', date_pattern = 'y-mm-dd')
        lastPremiumPaid_entry.grid(row = 9, column = 1, ipadx = 90)
        
        ttk.Label(sideFrame, text = "Next Premium Due: ").grid(row = 10, column = 0, padx = 30, pady = 40, sticky = W)
        nextPremiumDue_entry = DateEntry(sideFrame, selectmode = 'day', date_pattern = 'y-mm-dd')
        nextPremiumDue_entry.grid(row = 10, column = 1, ipadx = 90)
        
        # Make new column - Maturity Date - DATE
        ttk.Label(sideFrame, text = "Maturity Date: ").grid(row = 11, column = 0, padx = 30, pady = 40, sticky = W)
        maturityDate_entry = DateEntry(sideFrame, selectmode = 'day', date_pattern = 'y-mm-dd')
        maturityDate_entry.grid(row = 11, column = 1, ipadx = 90)
        
        ttk.Label(sideFrame, text = "Maturity Amount: ").grid(row = 12, column = 0, padx = 30 , pady = 40, sticky = W)
        maturityAmount_var = IntVar()
        maturityAmount_entry = ttk.Entry(sideFrame, textvariable = maturityAmount_var)
        maturityAmount_entry.grid(row = 12, column = 1, ipadx = 80)
        
        def addData():
            insuranceProvider = addData_combobox.get()
            policyNo = policyNo_str.get()
            policyName = policyName_entry.get()
            policyHolder = policyHolder_entry.get()
            lifeInsured = lifeInsured_entry.get()
            sumAssured = int(sumAssured_entry.get())
            nominee = nominee_entry.get()
            policyPaymentTerm = policyPaymentTerm_entry.get()
            premiumPaymentFrequency = premiumPaymentFrequency_entry.get()
            lastPremiumPaid = lastPremiumPaid_entry.get_date()
            nextPremiumDue_date = nextPremiumDue_entry.get_date()
            nextPremiumDue = nextPremiumDue_date.isoformat()
            maturityDate = maturityDate_entry.get_date()
            maturityAmount = float(maturityAmount_entry.get())

            sql = '''INSERT INTO INSURANCE (InsuranceProvider, PolicyNumber, PolicyName, PolicyHolder, LifeInsured, SumAssured, Nominee,
            PolicyPaymentTerm, PremiumPaymentFrequency, LastPremiumPaid, NextPremiumDue, MaturityDate, MaturityAmount)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

            sqlValues = (insuranceProvider, policyNo, policyName, policyHolder, lifeInsured, sumAssured, nominee, policyPaymentTerm,
                        premiumPaymentFrequency, lastPremiumPaid, nextPremiumDue, maturityDate, maturityAmount)

            mysqlConnection.sendInsuranceInfo(sql, sqlValues)

            popup_insurance.destroy()

        ttk.Button(sideFrame, text = "Add", command = addData).grid(row = 13, column = 1, pady = 30)


if __name__ == "__main__":
    InsuranceClass()
