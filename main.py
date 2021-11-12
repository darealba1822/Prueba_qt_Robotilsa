import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import requests
import random

class VentanaPrincipal(QDialog):

    lista_global = []

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setWindowTitle("Postulante para ROBOTILSA S.A") 
        loadUi('Qt_Designer.ui', self)
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)
        self.ButtonRequest.setIcon(QIcon('edit.png'))
        self.ButtonRequest.clicked.connect(self.clickme) 
        self.listaItems.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.listaItems:
            menu = QMenu()
            menu.addAction('Información del personaje')
            if menu.exec_(event.globalPos()):
                item = source.itemAt(event.pos())

                #validacion
                item2 = ""
                for elem in lista_global:
                    if elem["name"]== item.text():
                        item2 = elem
                
                dlg = QDialog(self)
                dlg.setWindowTitle("Ventana secundaria - [Preview]")
                dlg.resize(250, 350)
                label_name = QLabel(dlg)
                label_name.setText("name: ")
                label_name.move(20, 40)
                label_name_value = QLabel(dlg)
                label_name_value.setText(item.text())
                label_name_value.move(126, 40)

                label_height = QLabel(dlg)
                label_height.setText("height: ")
                label_height.move(20, 60)
                label_height_value = QLabel(dlg)
                label_height_value.setText(item2["height"])
                label_height_value.move(126, 60)

                label_mass = QLabel(dlg)
                label_mass.setText("mass: ")
                label_mass.move(20, 80)
                label_mass_value = QLabel(dlg)
                label_mass_value.setText(item2["mass"])
                label_mass_value.move(126, 80)

                label_hair = QLabel(dlg)
                label_hair.setText("hair_color: ")
                label_hair.move(20, 100)
                label_hair_value = QLabel(dlg)
                label_hair_value.setText(item2["hair_color"])
                label_hair_value.move(126, 100)

                label_skin = QLabel(dlg)
                label_skin.setText("skin_color: ")
                label_skin.move(20, 120)
                label_skin_value = QLabel(dlg)
                label_skin_value.setText(item2["skin_color"])
                label_skin_value.move(126, 120)

                label_o = QLabel(dlg)
                label_o.setText("eye_color: ")
                label_o.move(20, 140)
                label_o_value = QLabel(dlg)
                label_o_value.setText(item2["eye_color"])
                label_o_value.move(126, 140)

                label_c = QLabel(dlg)
                label_c.setText("birth_year: ")
                label_c.move(20, 160)
                label_c_value = QLabel(dlg)
                label_c_value.setText(item2["birth_year"])
                label_c_value.move(126, 160)

                label_gender = QLabel(dlg)
                label_gender.setText("gender: ")
                label_gender.move(20, 180)
                label_gender_value = QLabel(dlg)
                label_gender_value.setText(item2["gender"])
                label_gender_value.move(126, 180)
                
                dlg.exec()

            return True
        return super().eventFilter(source, event)

    def clickme(self):
        self.listaItems.clear()
        temp = []
        for i in range(10):
            print("SOLICITANDO API REST: " + str(i))
            print("Request... ")
            URL = 'https://swapi.dev/api/people/'+str(random.randint(1, 83))
            print(URL)
            data = requests.get(URL)
            data = data.json()
            item = QListWidgetItem(data['name'])
            item.setTextAlignment(Qt.AlignCenter)
            self.listaItems.addItem(" ") 
            self.listaItems.addItem(item) 
            temp = temp + [data]
            print(data['name'])

        global lista_global
        lista_global = temp
        print(lista_global)

    def buildExamplePopup(self, item):
        name = item.text()
        self.exPopup = examplePopup(name)
        self.exPopup.setGeometry(100, 200, 100, 100)
        self.exPopup.show()

    def displayTime(self):
        currentTime = QTime.currentTime()
        currentData = QDate.currentDate()
        tiempo = currentTime.toString('hh:mm:ss')
        fecha =  currentData.toString('dd/MM/yyyy')
        self.reloj.setText(tiempo)
        self.fecha.setText(fecha)

class examplePopup(QWidget):
    def __init__(self, name):
        super().__init__()

        self.name = name

        self.initUI()

    def initUI(self):
        lblName = QLabel(self.name, self)

app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())
