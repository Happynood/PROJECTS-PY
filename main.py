import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ex(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def encrypt(self):
        encrypted_text = self.lineEdit.text()
        encrypted_text_list = list(encrypted_text)
        number_en = len (encrypted_text_list)


        for x in range (number_en): #Тест абвгдеёжзийклмнопрстуфхцчшщъыьэюя
            if encrypted_text_list[x] == 'а':
                encrypted_text_list[x] = 'б'
                continue

            if encrypted_text_list[x] == 'б':
                encrypted_text_list[x] = 'в'
                continue

            if encrypted_text_list[x] == 'в':
                encrypted_text_list[x] = 'г'
                continue

            if encrypted_text_list[x] == 'г':
                encrypted_text_list[x] = 'д'
                continue

            if encrypted_text_list[x] == 'д':
                encrypted_text_list[x] = 'е'
                continue

            if encrypted_text_list[x] == 'е':
                encrypted_text_list[x] = 'ё'
                continue

            if encrypted_text_list[x] == 'ё':
                encrypted_text_list[x] = 'ж'
                continue

            if encrypted_text_list[x] == 'ж':
                encrypted_text_list[x] = 'з'
                continue

            if encrypted_text_list[x] == 'з':
                encrypted_text_list[x] = 'и'
                continue

            if encrypted_text_list[x] == 'и':
                encrypted_text_list[x] = 'й'
                continue

            if encrypted_text_list[x] == 'й':
                encrypted_text_list[x] = 'к'
                continue

            if encrypted_text_list[x] == 'к':
                encrypted_text_list[x] = 'л'
                continue

            if encrypted_text_list[x] == 'л':
                encrypted_text_list[x] = 'м'
                continue

            if encrypted_text_list[x] == 'м':
                encrypted_text_list[x] = 'н'
                continue

            if encrypted_text_list[x] == 'н':
                encrypted_text_list[x] = 'о'
                continue

            if encrypted_text_list[x] == 'о':
                encrypted_text_list[x] = 'п'
                continue

            if encrypted_text_list[x] == 'п':
                encrypted_text_list[x] = 'р'
                continue

            if encrypted_text_list[x] == 'р':
                encrypted_text_list[x] = 'с'
                continue
            if encrypted_text_list[x] == 'с':
                encrypted_text_list[x] = 'т'
                continue

            if encrypted_text_list[x] == 'т':
                encrypted_text_list[x] = 'у'
                continue

            if encrypted_text_list[x] == 'у':
                encrypted_text_list[x] = 'ф'
                continue

            if encrypted_text_list[x] == 'ф':
                encrypted_text_list[x] = 'х'
                continue

            if encrypted_text_list[x] == 'х':
                encrypted_text_list[x] = 'ц'
                continue

            if encrypted_text_list[x] == 'ц':
                encrypted_text_list[x] = 'ч'
                continue
            
            if encrypted_text_list[x] == 'ч':
                encrypted_text_list[x] = 'ш'
                continue

            if encrypted_text_list[x] == 'ш':
                encrypted_text_list[x] = 'щ'
                continue

            if encrypted_text_list[x] == 'щ':
                encrypted_text_list[x] = 'ъ'
                continue

            if encrypted_text_list[x] == 'ъ':
                encrypted_text_list[x] = 'ы'
                continue

            if encrypted_text_list[x] == 'ы':
                encrypted_text_list[x] = 'ь'
                continue

            if encrypted_text_list[x] == 'ь':
                encrypted_text_list[x] = 'э'
                continue

            if encrypted_text_list[x] == 'э':
                encrypted_text_list[x] = 'ю'
                continue

            if encrypted_text_list[x] == 'ю':
                encrypted_text_list[x] = 'я'
                continue

            if encrypted_text_list[x] == 'я':
                encrypted_text_list[x] = 'а'
                continue

            if encrypted_text_list[x] == '':
                encrypted_text_list[x] = ''
                continue
        
        print(encrypted_text_list)
        print(''.join(encrypted_text_list))
        self.lineEdit2.setText("")
        self.lineEdit2.insert(''.join(encrypted_text_list))

    def decrypt(self):
        decrypted_text = self.lineEdit.text()
        decrypted_text_list = list(decrypted_text)
        number_de = len (decrypted_text_list)

        for x in range (number_de): #Тест абвгдеёжзийклмнопрстуфхцчшщъыьэюя
            if decrypted_text_list[x] == 'а':
                decrypted_text_list[x] = 'я'
                continue

            if decrypted_text_list[x] == 'б':
                decrypted_text_list[x] = 'а'
                continue

            if decrypted_text_list[x] == 'в':
                decrypted_text_list[x] = 'б'
                continue

            if decrypted_text_list[x] == 'г':
                decrypted_text_list[x] = 'в'
                continue

            if decrypted_text_list[x] == 'д':
                decrypted_text_list[x] = 'г'
                continue

            if decrypted_text_list[x] == 'е':
                decrypted_text_list[x] = 'д'
                continue

            if decrypted_text_list[x] == 'ё':
                decrypted_text_list[x] = 'е'
                continue

            if decrypted_text_list[x] == 'ж':
                decrypted_text_list[x] = 'ё'
                continue

            if decrypted_text_list[x] == 'з':
                decrypted_text_list[x] = 'ж'
                continue

            if decrypted_text_list[x] == 'и':
                decrypted_text_list[x] = 'з'
                continue

            if decrypted_text_list[x] == 'й':
                decrypted_text_list[x] = 'и'
                continue

            if decrypted_text_list[x] == 'к':
                decrypted_text_list[x] = 'й'
                continue

            if decrypted_text_list[x] == 'л':
                decrypted_text_list[x] = 'к'
                continue

            if decrypted_text_list[x] == 'м':
                decrypted_text_list[x] = 'л'
                continue

            if decrypted_text_list[x] == 'н':
                decrypted_text_list[x] = 'м'
                continue

            if decrypted_text_list[x] == 'о':
                decrypted_text_list[x] = 'н'
                continue

            if decrypted_text_list[x] == 'п':
                decrypted_text_list[x] = 'о'
                continue

            if decrypted_text_list[x] == 'р':
                decrypted_text_list[x] = 'п'
                continue
            
            if decrypted_text_list[x] == 'с':
                decrypted_text_list[x] = 'р'
                continue

            if decrypted_text_list[x] == 'т':
                decrypted_text_list[x] = 'с'
                continue

            if decrypted_text_list[x] == 'у':
                decrypted_text_list[x] = 'т'
                continue

            if decrypted_text_list[x] == 'ф':
                decrypted_text_list[x] = 'у'
                continue

            if decrypted_text_list[x] == 'х':
                decrypted_text_list[x] = 'ф'
                continue

            if decrypted_text_list[x] == 'ц':
                decrypted_text_list[x] = 'х'
                continue

            if decrypted_text_list[x] == 'ч':
                decrypted_text_list[x] = 'ц'
                continue

            if decrypted_text_list[x] == 'ш':
                decrypted_text_list[x] = 'ч'
                continue

            if decrypted_text_list[x] == 'щ':
                decrypted_text_list[x] = 'ш'
                continue

            if decrypted_text_list[x] == 'ъ':
                decrypted_text_list[x] = 'щ'
                continue

            if decrypted_text_list[x] == 'ы':
                decrypted_text_list[x] = 'ъ'
                continue

            if decrypted_text_list[x] == 'ь':
                decrypted_text_list[x] = 'ы'
                continue

            if decrypted_text_list[x] == 'э':
               decrypted_text_list[x] = 'ь'
               continue

            if decrypted_text_list[x] == 'ю':
                decrypted_text_list[x] = 'э'
                continue

            if decrypted_text_list[x] == 'я':
                decrypted_text_list[x] = 'ю'
                continue

            if decrypted_text_list[x] == '':
                decrypted_text_list[x] = ''
                continue
        
        print(decrypted_text_list)
        print(''.join(decrypted_text_list))
        self.lineEdit2.setText("")
        self.lineEdit2.insert(''.join(decrypted_text_list))
          
    def initUI(self):
        self.resize(327, 150)
        self.setWindowTitle('Crypt')
        self.setWindowIcon(QIcon('icon.png'))
        
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(60, 20, 221, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit2.setGeometry(QtCore.QRect(60, 90, 221, 21))
        self.lineEdit2.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(80, 50, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText( "Зашифровать")
        self.pushButton.clicked.connect(self.encrypt)

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 50, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText( "Расшифровать")
        self.pushButton_2.clicked.connect(self.decrypt)

        self.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ex()
    sys.exit(app.exec_()) 