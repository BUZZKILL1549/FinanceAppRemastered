import sqlite3
import sys


class Connect:
    def __init__(self) -> None:
        self.INSURANCE_QUERY = "SELECT * FROM insurance"
        self.DEPOSITS_QUERY = "SELECT * FROM deposits"

        try:
            self.cnx = sqlite3.connect("financedb.db")
            self.cursor = self.cnx.cursor()

            if self.cnx:
                self.cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                                        Uname                       varchar(60),
                                        Pwd                         varchar(60)
                                    )''')
                self.cursor.execute('''CREATE TABLE IF NOT EXISTS insurance(
                                        InsuranceProvider			varchar(60),
                                        PolicyNumber				varchar(60),
                                        PolicyName					varchar(60),
                                        PolicyHolder				varchar(60),
                                        LifeInsured					varchar(60),
                                        SumAssured					float,
                                        Nominee						varchar(60),
                                        PolicyPaymentTerm			int,
                                        PremiumPaymentFrequency		int,
                                        LastPremiumPaid				date,
                                        NextPremiumDue				date,
                                        MaturityDate				date,
                                        MaturityAmount				float
                                    )''')
                self.cursor.execute('''CREATE TABLE IF NOT EXISTS deposits(
                                        FinancialOrganization		varchar(60),
                                        NameOfFinancialOrganization	varchar(60),
                                        BranchAddress				text,
                                        TypeOfInvestment			varchar(60),
                                        InvestmentNumber			varchar(60),
                                        InvestmentHolder			varchar(60),
                                        Nominee						varchar(60),
                                        NomineeGuardian				varchar(60),
                                        InvestmentAmount			float,
                                        RateOfInterest  			float,
                                        InvestmentDate				date,
                                        InvestmentDuration			float,
                                        MaturityDate				date,
                                        MaturityAmount				float
                                    )''')
                
                self.cnx.commit()

                try:
                    if sys.argv[1] == "register":
                        self.registerUserInfo()
                    elif sys.argv[1] == "":
                        pass
                except IndexError:
                    pass
                
        except sqlite3.Error as error:
            print("Failed to connect to database: {}".format(error))

    # this function is only executed once for the whole program through the powershell script
    def registerUserInfo(self) -> None: 
        if len(sys.argv) != 4:
            print("Usage: sqlFile.py <username> <password>")
            sys.exit(1)

        username = sys.argv[2]
        password = sys.argv[3]

        self.cursor.execute("INSERT INTO users (Uname, Pwd) VALUES (?, ?)", (username, password))
        self.cnx.commit()

        print("Successfully registered data.")

    def retrieveUserInfo(self) -> list[tuple]:
        self.cursor.execute("SELECT * FROM users")
        userInfo = self.cursor.fetchall()

        return userInfo

    def retrieveInsuranceInfo(self) -> list[tuple]:
        self.cursor.execute("SELECT * FROM insurance")
        insuranceInfo = self.cursor.fetchall()

        return insuranceInfo

    def sendInsuranceInfo(self, query, values) -> None:
        try:
            self.cursor.execute(query, values)
            self.cnx.commit()

            print("Successfully added to Insurance")
        except sqlite3.Error as error:
            print("Unexpected error occured: {}".format(error))

    def retrieveDepositsInfo(self) -> list[tuple]:
        self.cursor.execute("SELECT * FROM deposits")
        depositsInfo = self.cursor.fetchall()

        return depositsInfo
    
    def sendDepositsInfo(self, query, values) -> None:
        try:
            self.cursor.execute(query, values)
            self.cnx.commit()

            print("Successfully added to deposits.")
        except sqlite3.Error as error:
            print("Unexpected error occured: {}".format(error))
        

if __name__ == "__main__":
    x = Connect()
    