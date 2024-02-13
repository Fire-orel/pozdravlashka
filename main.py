from PyQt6.QtWidgets import QMainWindow,QApplication,QPushButton,QWidget,QVBoxLayout,QHBoxLayout,QSpinBox,QLabel,QLineEdit,QGridLayout
from PyQt6.QtGui import QPixmap
from PyQt6 import QtGui
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Рандомайзер подарков")
        self.showMaximized()
        self.setting_layout=QHBoxLayout(self)
        self.bt_settings=QPushButton("Настройки",self)
        self.bt_settings.resize(200,200)
        self.setting_layout.addStretch()
        self.setting_layout.addWidget(self.bt_settings)
        self.bt_settings.clicked.connect(self.show_form2)

        self.photo=QPixmap("honor.jpg")
        self.label_photo=QLabel()
        self.label_photo.setPixmap(self.photo)
        self.label_photo.setScaledContents(True)
        self.label_photo.setFixedSize(500,500)



        self.photo_layout=QHBoxLayout(self)
        self.photo_layout.addWidget(self.label_photo)

        maim_layout=QVBoxLayout(self)
        maim_layout.addLayout(self.setting_layout)

        maim_layout.addLayout(self.photo_layout)
       

        central_widget=QWidget()
        central_widget.setLayout(maim_layout)


        self.setCentralWidget(central_widget)


    def show_form2(self):
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

        prizes_layout=QHBoxLayout()
        self.prizes_name=QLabel()
        self.prizes_name.setText("Название")
        self.prizes_text_edit=QLineEdit()

        self.bt_delete_layout=QPushButton()
        self.bt_delete_layout.setText("X")
        self.bt_delete_layout.clicked.connect(self.delete_prizes)

        self.bt_add_prize=QPushButton()
        self.bt_add_prize.setText("Добавить призы")
        self.bt_add_prize.clicked.connect(self.add_prizes)


        prizes_layout.addWidget(self.prizes_name)
        prizes_layout.addWidget(self.prizes_text_edit)
        # prizes_layout.addWidget(self.bt_delete_layout)





        self.main_layout=QGridLayout()
        self.main_layout.addLayout(range_layout_text,0,0)
        self.main_layout.addLayout(range_layout,1,0)
        self.main_layout.addWidget(self.bt_delete_layout,2,1)
        # self.main_layout.addWidget(self.prizes_name,2,0)
        # self.main_layout.addWidget(self.prizes_text_edit,2,1)
        # self.main_layout.addWidget(self.bt_delete_layout,2,2)
        self.main_layout.addLayout(prizes_layout,2,0)

        self.main_layout.addWidget(self.bt_add_prize,3,0)


        central_widget=QWidget()
        central_widget.setLayout(self.main_layout)
        self.form.setCentralWidget(central_widget)



        self.form.show()

    def add_prizes(self):
        btn=self.sender()
        ind=self.main_layout.indexOf(btn)
        prizes_layout=QHBoxLayout()
        self.prizes_name=QLabel()
        self.prizes_name.setText("Название")
        self.prizes_text_edit=QLineEdit()

        self.bt_delete_layout=QPushButton()
        self.bt_delete_layout.setText("X")
        self.bt_delete_layout.clicked.connect(self.delete_prizes)

        prizes_layout.addWidget(self.prizes_name)
        prizes_layout.addWidget(self.prizes_text_edit)
        # prizes_layout.addWidget(self.bt_delete_layout)
        self.main_layout.addWidget(self.bt_delete_layout,ind,1)

        # self.main_layout.addWidget(self.prizes_name,ind,0)
        # self.main_layout.addWidget(self.prizes_text_edit,ind,1)
        # self.main_layout.addWidget(self.bt_delete_layout,ind,2)

        self.main_layout.addLayout(prizes_layout,ind,0)

        self.main_layout.addWidget(self.bt_add_prize,ind+1,0)

    def delete_prizes(self):
        btn=self.sender()
        ind=self.main_layout.indexOf(btn)
        item=self.main_layout.itemAt(ind)

        print(item)

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=window()
    ex.show()
    sys.exit(app.exec())
