
from PySide6.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton, QComboBox
from Account import Account
from About import About

class BankApp(QWidget):

    def __init__(self):
        super().__init__()
        self.accounts = {}
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 480)
        self.setWindowTitle("🏦BankApp")




        label = QLabel("Open account:", self)
        label.setGeometry(200, 10, 200, 30)

        self.new_account = QLineEdit(self)
        self.new_account.setPlaceholderText("Enter ID")
        self.new_account.setGeometry(200, 40, 200, 40)

        enter = QPushButton("Enter", self)
        enter.setGeometry(200, 90, 200, 40)
        enter.clicked.connect(self.enter_clicked)


        self.message = QLabel("", self)
        self.message.setGeometry(200, 135, 200, 40)

        self.account_combo = QComboBox(self)
        self.account_combo.setPlaceholderText("Choose account")
        self.account_combo.setGeometry(200, 175, 200, 40)
  

        amount_label = QLabel("Amount:",self)
        amount_label.setGeometry(20, 250, 170, 30)

        self.amount_input = QLineEdit(self)
        self.amount_input.setGeometry(20, 280, 170, 40)
        self.amount_input.setPlaceholderText("Enter amount")

        deposit_button = QPushButton("Deposit", self)
        deposit_button.setGeometry(230, 250, 140, 40)
        deposit_button.setStyleSheet("background-color : #E0F2F1")
        deposit_button.clicked.connect(self.deposit_clicked)

        withdraw_button = QPushButton("Withdraw", self)
        withdraw_button.setGeometry(230, 300, 140, 40)
        withdraw_button.setStyleSheet("background-color : #E0F2F1")
        withdraw_button.clicked.connect(self.withdraw_clicked)
        

        balance_button = QPushButton("Balance", self)
        balance_button.setGeometry(230, 350, 140, 40)
        balance_button.setStyleSheet("background-color : #E0F2F1")
        balance_button.clicked.connect(self.balance_clicked)

        output_title = QLabel(self)
        output_title.setGeometry(400, 250, 180, 30)

        self.output = QLabel("", self)
        self.output.setGeometry(400, 280, 180, 110)
        self.output.setStyleSheet("border : 1px solid gray ; padding : 5px ; background : lightgray")
        self.output.setWordWrap(True)

        about_button = QPushButton("About", self)
        about_button.setGeometry(20, 10, 100, 35)
        about_button.setStyleSheet("background-color : lightgray")
        about_button.clicked.connect(self.about_clicked)


    def enter_clicked(self):
        id_number = self.new_account.text()
        if id_number in self.accounts:
            self.message.setText("The account already exists")
            return
        else:
            self.accounts[id_number] = Account(id_number)
            self.account_combo.addItem(id_number)
            self.message.setText(f' Account {id_number} created')
        self.new_account.clear() 
  

    def get_selected_account(self):
        id_number = self.account_combo.currentText()
        if id_number == "":
            self.output.setText("Please choose an account")
            return None
        else:
            return self.accounts[id_number]


    def get_amount(self):
        text = self.amount_input.text()
        if not text.isdigit() or int(text) == 0:
            self.output.setText("Please enter a positive number")
            return None
        else:
            return int(text)

    def deposit_clicked(self):
        account = self.get_selected_account()
        if account is None:
            return  
        amount = self.get_amount()
        if amount is None:
            return
        else:
            account.deposit(amount)
            self.output.setText(f"Deposited {amount} shekel. Balance: {account.balance} shekel")
            self.amount_input.clear()


    def withdraw_clicked(self):
        account = self.get_selected_account()
        if account is None:
            return
        amount = self.get_amount()
        if amount is None:
            return
        taken = account.withdraw(amount)
        if taken == 0:
            self.output.setText(f" Not enough money. balance: {account.balance} shekel")
        else:
            self.output.setText(f"Withdrew {taken} shekek. Balance : {account.balance} shekel")

    def balance_clicked(self):
        account = self.get_selected_account()
        if account is None:
            return
        else:
            self.output.setText(f"Account {account.id}: {account.balance} shekel")

    def about_clicked(self):
        self.about_window = About()
        self.about_window.show()




if __name__ == "__main__":
    app = QApplication()
    window = BankApp()
    window.show()
    app.exec()