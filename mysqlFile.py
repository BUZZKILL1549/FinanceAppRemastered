import mysql.connector

class Connect:
    def __init__(self) -> None:
        ## Consts
        self.INSURANCE_QUERY = "SELECT * FROM insurance"
        self.DEPOSITS_QUERY = "SELECT * FROM deposits"

        try:
            self.cnx = mysql.connector.connect(
                host = "localhost",
                user = "buzzkill",
                password = "f00tball@143",
                database = "financedb"
            )

            if self.cnx.is_connected():
                self.cursor = self.cnx.cursor()

        except mysql.connector.Error as error:
            print(f"Unexpected error occured: {error}")
    
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

            print("Successfully added to insurance")
        except mysql.connector.Error as error:
            print("Unexpected error occured: {}".format(error))    

    def retrieveDepositsInfo(self) -> list[tuple]:
        self.cursor.execute("SELECT * FROM deposits")
        depositsInfo = self.cursor.fetchall()

        return depositsInfo
    
    def sendDepositsInfo(self, query, values) -> None:
        try:
            self.cursor.execute(query, values)
            self.cnx.commit()

            print("Successfully added to deposits")
        except mysql.connector.Error as error:
            print("Unexpected error occured: {}".format(error))