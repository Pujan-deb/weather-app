import sys
import requests
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QLineEdit,QPushButton,
                             QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather: ",self)
        self.temp_level = QLabel("7",self)
        self.description_level = QLabel("sunny",self)
        self.city_input.setPlaceholderText("Enter city name")
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Weather app")
        self.setGeometry(800,250,400,500)
        self.city_input.setGeometry(0,0,300,90)

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_level)
        vbox.addWidget(self.description_level)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.description_level.setAlignment(Qt.AlignCenter)
        self.temp_level.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.description_level.setObjectName("description_level")
        self.temp_level.setObjectName("temp_level")

        self.setStyleSheet(""" 
        QLabel#city_label{
        font-family: calibri;
        font-size: 45px;
        font-weight: bold
        }
        QLabel#city_label{
        font-size: 34px;
        font-style: italic;
        }
        QLineEdit#city_input{
        font-size: 40px;
        padding:2px;
        font-style: italic
        }
        #get_weather_button{
        background-color: black;
        color: white;
        font-size: 32px;
        height: 100px;
        font-style: bold
        }
        #description_level{
        background-color: orange;
        padding: 4px;
        font-size: 40px;
        font-style: calibri;
        }
        #temp_level{
        background-color: #bf7034;
        padding: 4px;
        font-size: 40px ;
        font-style: calibri;
        }
        """)
        self.get_weather_button.clicked.connect(self.get_weather)
    def get_weather(self):
        api = "8323f30718f0d672af49d82b7e83ef0d"
        name = self.city_input.text()

        if name:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api}"
            try:
                data = requests.get(url)
                res = data.json()
                if res["main"]["temp"]:
                    value  = res["main"]["temp"]
                    celcious_value = int(value - 273.15)
                    self.temp_level.setText(str(f"{celcious_value}°C"))
                    self.description_level.setText(str(res["weather"][0]["main"]))
                else:
                    self.temp_level.setText(0)
            except requests.exceptions.HTTPError as Error:
                print(Error)
        else:
            self.city_input.setText("Enter city name")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())