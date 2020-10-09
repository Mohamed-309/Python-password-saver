import sqlite3
from PyQt5.uic import *
from PyQt5.QtWidgets import *
from os import path
import sys
conn = sqlite3.connect('database.sqlite')
cur = conn.cursor()
FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__), "app.ui"))
class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.handle_btns()
    def handle_btns(self):
        self.add_btn.clicked.connect(self.add_user)
        self.update_btn.clicked.connect(self.update_users)
        self.delete_btn.clicked.connect(self.delete_user)
    def add_user(self):
        username =  self.lineEdit.text()
        password = self.lineEdit_2.text()
        application = self.lineEdit_3.text()
        cur.execute('''INSERT INTO users(username, password, application)
        VALUES(?,?,?)''', (username, password, application))
        conn.commit()
        QMessageBox.about(self, "Done", "user added successfully")
    def update_users(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        application = self.lineEdit_3.text()
        cur.execute('''UPDATE users SET password = ?, application = ? WHERE username= ?''',
                    (password, application, username))
        conn.commit()
        QMessageBox.about(self, "Done", "user updated successfully")
    def delete_user(self):
        username = self.lineEdit.text()
        application = self.lineEdit_3.text()
        cur.execute('''DELETE FROM users WHERE username = ? AND application = ?''', (username, application))
        conn.commit()
        QMessageBox.about(self, "Done", "user deleted successfully")
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
        main()
