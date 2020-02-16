from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QLineEdit,\
    QLabel, QPushButton
from PySide2.QtCore import Slot, QRect   
import sys
from get import get_city_ID, get_current_data, get_forecast_data


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
      
        self.city_name = ''
        
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
        self.city_name = self.city_input.text()
        self.current_data = get_current_data(self.city_name)
        self.forecast_data = get_forecast_data(self.city_name)
    
    def current_button_action(self):
        self.temp = QLabel('{:<15}{:<3}'.format('Temperature',self.current_data['temperature']),self.data_frame)
        self.temp.setGeometry(QRect(40, 30, 150, 20))
        self.temp.show()

        self.temp_feel = QLabel('{:<18}{:<3}'.format('Real_feel',self.current_data['temperature_feel']),self.data_frame)
        self.temp_feel.setGeometry(QRect(40, 60, 150, 20))
        self.temp_feel.show()

        self.humidity = QLabel('{:<18}{:<3}%'.format('Humidity',self.current_data['humidity']),self.data_frame)
        self.humidity.setGeometry(QRect(40, 90, 150, 20))
        self.humidity.show()

        self.weather = QLabel('{:<18}{:<3}'.format('Weather',self.current_data['weather_condition']),self.data_frame)
        self.weather.setGeometry(QRect(40, 120, 150, 20))
        self.weather.show()

        self.cloud = QLabel('{:<18}{:<3}%'.format('Cloud',self.current_data['clouds']),self.data_frame)
        self.cloud.setGeometry(QRect(40, 150, 150, 20))
        self.cloud.show()

        self.wind = QLabel('{:<18}{:<3}m/s'.format('Wind',self.current_data['wind']),self.data_frame)
        self.wind.setGeometry(QRect(40, 180, 150, 20))
        self.wind.show()

        self.perssure = QLabel('{:<18}{:<3}'.format('Perssure',self.current_data['pressure']),self.data_frame)
        self.perssure.setGeometry(QRect(40, 150, 150, 20))
        self.perssure.show()

        self.sunrise = QLabel('{:<18}{:<3}'.format('Sun Rise',self.current_data['sunrise']),self.data_frame)
        self.sunrise.setGeometry(QRect(40, 180, 150, 20))
        self.sunrise.show()

        self.sunset = QLabel('{:<18}{:<3}'.format('Sun Set',self.current_data['sunset']),self.data_frame)
        self.sunset.setGeometry(QRect(40, 210, 150, 20))
        self.sunset.show()




        
        
        
   
    def hourly_button_action(self):
        print(self.forecast_data)
   
    def daily_button_action(self):
        print(self.forecast_data)
        


app = QApplication()
mainwindow =MainWindow()
mainwindow.show()

sys.exit(app.exec_())


