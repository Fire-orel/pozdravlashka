from PyQt6.QtWidgets import QMainWindow,QApplication,QPushButton,QWidget,QVBoxLayout,QHBoxLayout,QSpinBox,QLabel,QLineEdit,QGridLayout,QTableWidget
from PyQt6.QtGui import QPixmap
from PyQt6 import QtGui
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI_form1()
        self.initUI_form2()

    def initUI_form1(self):
        self.setWindowTitle("Рандомайзер подарков")
        self.showMaximized()
        self.setting_layout=QHBoxLayout(self)
        self.bt_settings=QPushButton("Настройки",self)
        self.setting_layout.addStretch()
        self.setting_layout.addWidget(self.bt_settings)
        self.bt_settings.clicked.connect(self.form2_show)

        main_layout=QVBoxLayout(self)
        main_layout.addLayout(self.setting_layout)
        main_layout.addStretch()

        central_widget=QWidget()
        central_widget.setLayout(main_layout)


        self.setCentralWidget(central_widget)



    def initUI_form2(self):
        self.form=QMainWindow()


        self.range_ot=QSpinBox()
        self.range_ot.setMinimum(1)
        self.range_do=QSpinBox()
        self.range_do.setMinimum(2)
        self.label_range=QLabel()

        self.label_range.setText("Диапазон участников")
        self.label_range_ot=QLabel()
        self.label_range_do=QLabel()
        self.label_range_ot.setText("От")
        self.label_range_do.setText("До")

        range_layout_text=QHBoxLayout()
        range_layout_text.addStretch()
        range_layout_text.addWidget(self.label_range)
        range_layout_text.addStretch()
        range_layout=QHBoxLayout()
        range_layout.addWidget(self.label_range_ot)
        range_layout.addWidget(self.range_ot)
        range_layout.addWidget(self.label_range_do)
        range_layout.addWidget(self.range_do)



        self.table_data=QTableWidget()



        self.main_layout=QGridLayout()
        self.main_layout.addLayout(range_layout_text,0,0)
        self.main_layout.addLayout(range_layout,1,0)
        self.main_layout.addWidget(self.table_data,2,0)

        central_widget=QWidget()
        central_widget.setLayout(self.main_layout)
        self.form.setCentralWidget(central_widget)

    def form2_show(self):
        self.form.show()


if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=window()
    ex.show()
    sys.exit(app.exec())
