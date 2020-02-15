from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QLineEdit,\
    QLabel, QPushButton
from PySide2.QtCore import Slot, QRect   
import sys


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
      
        self.setWindowTitle('WeatherShow')
        self.resize(900,600)

        self.city_frame = QFrame(self)
        self.city_frame.setGeometry(QRect(0, 0, 200, 600))
        self.city_frame.setStyleSheet(u"background-color: rgb(254, 254, 254);")
        self.city_frame.setFrameShape(QFrame.Box)
        self.city_frame.setFrameShadow(QFrame.Sunken)
        self.city_frame.setLineWidth(2)
        
        self.choose_city_label = QLabel("<font color = green size=3>Please Enter city name</font>",self.city_frame)
        self.choose_city_label.setGeometry(QRect(20, 10, 150, 30))
        
        self.city_input = QLineEdit(self.city_frame)
        self.city_input.setGeometry(QRect(20, 35, 150,25))
        self.city_input.returnPressed.connect(self.city_input_action)

        self.current_button = QPushButton('Current',self)
        self.current_button.setGeometry(QRect(201, 2, 70, 28))
        self.current_button.clicked.connect(self.current_button_action)
        
        self.hourly_button = QPushButton('Hourly',self)
        self.hourly_button.setGeometry(QRect(271, 2, 70, 28))
        self.hourly_button.clicked.connect(self.hourly_button_action)

        self.daily_button = QPushButton('Daily',self)
        self.daily_button.setGeometry(QRect(341, 2, 70, 28))
        self.daily_button.clicked.connect(self.daily_button_action)


        self.data_frame = QFrame(self)
        self.data_frame.setGeometry(QRect(201, 100, 500, 500))
        self.data_frame.setStyleSheet(u"background-color: rgb(254, 254, 254);")
        self.data_frame.setFrameShape(QFrame.Box)
        self.data_frame.setFrameShadow(QFrame.Sunken)
        self.data_frame.setLineWidth(2)
    
    def city_input_action(self):
        print(self.city_input.text())
    
    def current_button_action(self):
        print('current button pressed')
   
    def hourly_button_action(self):
        print('hourly button pressed')
   
    def daily_button_action(self):
        print('daily button pressed')
        


app = QApplication()
mainwindow =MainWindow()
mainwindow.show()

sys.exit(app.exec_())


