import threading
from win10toast import ToastNotifier
from sql.sqlFile import Connect

class Notify:
    def __init__(self, root) -> None:
        self.sqlConnection = Connect()
        self.root = root
        self.checkAndNotify()

    def checkAndNotify(self) -> None:
        threading.Thread(target = self._checkAndNotify, daemon = True).start()

    def _checkAndNotify(self) -> None:
        sqlConnection = Connect()
        cursor = sqlConnection.cursor

        insuranceDueDate = self.checkInsuranceDueDate(cursor)
        insuranceDueDate = sqlConnection.checkInsuranceDueDate()
        for insurance in insuranceDueDate:
            self.insuranceNotification(insurance)
            
        self.root.after(60000, self.checkAndNotify)

    def checkInsuranceDueDate(self, cursor) -> list[tuple]:
        query = '''SELECT InsuranceProvider, NextPremiumDue
                   FROM insurance
                   WHERE NextPremiumDue BETWEEN DATE("now", "-1 month") AND DATE("now")'''
        cursor.execute(query)
        insuranceDueDate = cursor.fetchall()
        return insuranceDueDate

    def insuranceNotification(self, insurance):
        insuranceProvider, nextPremiumDue = insurance
        n = ToastNotifier()
        n.show_toast(
            title = "FinanceApp",
            msg = f"{insuranceProvider} payment due by {nextPremiumDue}",
            duration = 5
        )


if __name__ == "__main__":
    x = Notify()
    