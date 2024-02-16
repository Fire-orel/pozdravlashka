from PyQt6.QtWidgets import QMainWindow,QApplication,QPushButton,QWidget,QVBoxLayout,QHBoxLayout,QSpinBox,QLabel,QLineEdit,QGridLayout,QTableWidget,QFileDialog,QDialog
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
        self.form=QDialog()
        self.form.setModal(True)


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
        self.table_data.setColumnCount(2)
        self.table_data.setHorizontalHeaderLabels(["Название","Путь"])

        self.prizes_layout=QHBoxLayout()
        self.prizes_name=QLabel()
        self.prizes_name.setText("Название")
        self.prizes_name_edit=QLineEdit()

        self.prizes_put=QLabel()
        self.prizes_put.setText("Путь")
        self.prizes_put_edit=QLineEdit()
        self.bt_open_file=QPushButton()
        self.bt_open_file.setText("...")
        self.bt_open_file.clicked.connect(self.open_file)
        self.prizes_count=QLabel()
        self.prizes_count.setText("Количество")
        self.prizes_count_edit=QSpinBox()
        self.prizes_count_edit.setMinimum(1)

        # self.bt_delete_layout=QPushButton()
        # self.bt_delete_layout.setText("X")
        # self.bt_delete_layout.clicked.connect(self.delete_prizes)

        self.prizes_layout.addWidget(self.prizes_name)
        self.prizes_layout.addWidget(self.prizes_name_edit)
        self.prizes_layout.addWidget(self.prizes_put)
        self.prizes_layout.addWidget(self.prizes_put_edit)
        self.prizes_layout.addWidget(self.bt_open_file)
        self.prizes_layout.addWidget(self.prizes_count)
        self.prizes_layout.addWidget(self.prizes_count_edit)
        # self.prizes_layout.addWidget(self.bt_delete_layout)

        self.bt_add_prize=QPushButton()
        self.bt_add_prize.setText("Добавить призы")
        self.bt_add_prize.clicked.connect(self.add_prize)


        self.main_layout=QGridLayout()
        self.main_layout.addLayout(range_layout_text,0,0)
        self.main_layout.addLayout(range_layout,1,0)
        self.main_layout.addWidget(self.table_data,2,0)
        self.main_layout.addLayout(self.prizes_layout,3,0)
        self.main_layout.addWidget(self.bt_add_prize)

        central_widget=QWidget()
        central_widget.setLayout(self.main_layout)
        self.form.setLayout(self.main_layout)
        # self.form.setCentralWidget(central_widget)

    def form2_show(self):

        self.form.show()


    def open_file(self):
        name=QFileDialog.getOpenFileName(self,"Выбор папки","","Файлы изображений (*.png *.jpg *.bmp)")[0]
        self.prizes_put_edit.setText(name)

    def add_prize(self):
        name=self.prizes_name_edit.text()
        put=self.prizes_put_edit.text()
        count=self.prizes_count_edit.text()


        # print(name,put,count)



if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=window()
    ex.show()
    sys.exit(app.exec())
