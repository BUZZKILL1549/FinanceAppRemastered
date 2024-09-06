import mysql.connector

class Connect:
    def __init__(self) -> None:
        try:
            self.cnx = mysql.connector.connect(
                host = "localhost",
                user = "buzzkill",
                password = "f00tball@143",
                database = "financedb"
            )

            self.cursor = self.cnx.cursor()
        
        except mysql.connector.Error as error:
            print(f"Error Encountered: {error}")

    def retrieveUsersData(self) -> list[tuple]:
        self.cursor.execute("SELECT * FROM users")
        content = self.cursor.fetchall()

        return content

    def closeConnection(self) -> None:
        self.cursor.close()
        self.cnx.close()
