import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import re


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setMinimumSize(315, 350)
        #self.setContentsMargins(0, 0, 0, 0)

        widget = QWidget(self)
        layout = QGridLayout(widget)

        self.input_1 = QLineEdit()
        self.input_1.setText("0")
        self.input_1.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.input_1.setFixedSize(300, 50)  # Set fixed size instead of geometry
        self.input_1.setStyleSheet("background-color : 'lightgray'; border: 1px, solid, black; font: 26px bold;")
        layout.addWidget(self.input_1, 0, 0, 2, 4)  # Span across 4 columns


        buttons = [
            ('%', 1, 0), ('C', 1, 1), ('⌫', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),
        ]

        operators = ['*', '+', '-', '/', '%']

        for text,row,column in buttons:
            button = QPushButton(text)
            button.setFixedSize(75, 45)
            #percent_button.clicked.connect(self.add_percent)
            layout.addWidget(button, row, column)

            if text == '%':
                button.clicked.connect(self.add_percent)
                
            elif text == '.':
                button.clicked.connect(self.add_decimal)
                
            elif text == 'C':
                button.clicked.connect(self.add_cancel)
                
            elif text == '⌫':
                button.clicked.connect(self.add_backspace)
                QShortcut(QKeySequence('Backspace'), self).activated.connect(button.click)

            elif text == '=':
                button.clicked.connect(self.add_calculate)
                QShortcut(QKeySequence('Return'), self).activated.connect(button.click)

                
            elif text in operators:

                button.clicked.connect(self.add_operator)
            elif text == '+/-':
                button.clicked.connect(self.add_p_m)
            else:
                button.clicked.connect(self.add_number)





        ''' percent_button = QPushButton("%")
        percent_button.setFixedSize(75, 45)
        percent_button.clicked.connect(self.add_percent)
        layout.addWidget(percent_button, 1, 0)

        cancel_button = QPushButton("C")
        cancel_button.setFixedSize(75, 45)
        cancel_button.clicked.connect(self.add_cancel)
        layout.addWidget(cancel_button, 1, 1)

        back_button = QPushButton("⌫")
        back_button.setFixedSize(75, 45)
        back_button.clicked.connect(self.add_backspace)
        layout.addWidget(back_button, 1, 2)

        divide_button = QPushButton("/")
        divide_button.setFixedSize(75, 45)
        divide_button.clicked.connect(self.add_operator)
        layout.addWidget(divide_button, 1, 3)

        seven_button = QPushButton("7")
        seven_button.setFixedSize(75, 45)
        seven_button.clicked.connect(self.add_number)
        layout.addWidget(seven_button, 2, 0)

        eight_button = QPushButton("8")
        eight_button.setFixedSize(75, 45)
        eight_button.clicked.connect(self.add_number)
        layout.addWidget(eight_button, 2, 1)

        nine_button = QPushButton("9")
        nine_button.setFixedSize(75, 45)
        nine_button.clicked.connect(self.add_number)
        layout.addWidget(nine_button, 2, 2)

        multiply_button = QPushButton("*")
        multiply_button.setFixedSize(75, 45)
        multiply_button.clicked.connect(self.add_operator)
        layout.addWidget(multiply_button, 2, 3)

        four_button = QPushButton("4")
        four_button.setFixedSize(75, 45)
        four_button.clicked.connect(self.add_number)
        layout.addWidget(four_button, 3, 0)

        five_button = QPushButton("5")
        five_button.setFixedSize(75, 45)
        five_button.clicked.connect(self.add_number)
        layout.addWidget(five_button, 3, 1)

        six_button = QPushButton("6")
        six_button.setFixedSize(75, 45)
        six_button.clicked.connect(self.add_number)
        layout.addWidget(six_button, 3, 2)

        sub_button = QPushButton("-")
        sub_button.setFixedSize(75, 45)
        sub_button.clicked.connect(self.add_operator)
        layout.addWidget(sub_button, 3, 3)

        one_button = QPushButton("1")
        one_button.setFixedSize(75, 45)
        one_button.clicked.connect(self.add_number)
        layout.addWidget(one_button, 4, 0)

        two_button = QPushButton("2")
        two_button.setFixedSize(75, 45)
        two_button.clicked.connect(self.add_number)
        layout.addWidget(two_button, 4, 1)

        three_button = QPushButton("3")
        three_button.setFixedSize(75, 45)
        three_button.clicked.connect(self.add_number)
        layout.addWidget(three_button, 4, 2)

        add_button = QPushButton("+")
        add_button.setFixedSize(75, 45)
        add_button.clicked.connect(self.add_operator)
        layout.addWidget(add_button, 4, 3)

        p_m_button = QPushButton("+/-")
        p_m_button.setFixedSize(75, 45)
        p_m_button.clicked.connect(self.add_p_m)
        layout.addWidget(p_m_button, 5, 0)

        zero_button = QPushButton("0")
        zero_button.setFixedSize(75, 45)
        zero_button.clicked.connect(self.add_number)
        layout.addWidget(zero_button, 5, 1)

        decimal_button = QPushButton(".")
        decimal_button.setFixedSize(75, 45)
        decimal_button.clicked.connect(self.add_decimal)
        layout.addWidget(decimal_button, 5, 2)

        equal_button = QPushButton("=")
        equal_button.setFixedSize(75, 45)
        equal_button.clicked.connect(self.add_calculate)
        layout.addWidget(equal_button, 5, 3)   '''

        layout.setSpacing(2)

        self.setCentralWidget(widget)
    
    def add_percent(self):
        button = self.sender()

        button_text = button.text()

        self.input_1.setText(self.input_1.text() + button_text)

    def add_calculate(self):
        try:
            current_text = self.input_1.text()

            cal = eval(current_text)
            ## LineEdit only takes 

            self.input_1.setText(str(cal))
        except:
            self.input_1.setText("ERROR")

    def add_backspace(self):
        current_text  =  self.input_1.text()

        if len(current_text) > 1:
            self.input_1.setText(current_text[:-1])
        else:
            self.input_1.setText("0")


    def add_number(self):
        adding = self.sender()

        number_text = adding.text()
        ## adding number to zero, when you click it will displace 0

        if self.input_1.text() == "0":
            self.input_1.setText(number_text)
        ## adding number to already present values
        else:
            self.input_1.setText(self.input_1.text() + number_text)

    def add_cancel(self):
        self.input_1.setText("0")

    def add_operator(self):
        button = self.sender()
        current_text = self.input_1.text()
        operators = ['*', '+', '-', '/']
        if current_text[-1] in operators:
            self.input_1.setText(current_text + "")
        else:

            self.input_1.setText(current_text + button.text())

    def add_decimal(self):
        button = self.sender()
        decimal_text = button.text()
        current_text = self.input_1.text()
        #list = ['*', '+', '-', '/']

        split_text = re.split(r'(\+|\-|\*|/)', current_text)



        if '.' not in split_text[-1] and self.input_1.text()[-1] != '.':           
            self.input_1.setText(self.input_1.text() + decimal_text)

    def add_p_m(self):
        if self.input_1.text().startswith('-'):
            self.input_1.setText(self.input_1.text[1:])
        else:
            self.input_1.setText('-' + self.input_1.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
QPushButton{
            font : 18px;
            
            
            
            }
QMainWindow{
            background-color : '#72A0C1';
}


""")
    
    window = MainWindow()
    
    window.show()
    app.exec()
