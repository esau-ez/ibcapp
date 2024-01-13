from PySide6.QtWidgets import QApplication, QMainWindow,QWidget
from PySide6.QtCore import Signal, Qt
#Interfaces
from interfaces.ui_main import Ui_MainWindow
from interfaces.ui_login import Ui_Form
from interfaces.ui_dialogo import Ui_Dialog
from interfaces.ui_dialogoexito import Ui_Dialog2
from interfaces.ui_dialogopregunta import Ui_Dialog3
from config.db_script import consulta, add

#Librerias extras
import sys
import os
import subprocess
import requests
import time
import re
class Dialogo(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
class DialogoExito(QWidget, Ui_Dialog2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
class DialogoPregunta(QWidget,Ui_Dialog3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.actualizar)
    def actualizar(self):
        path = os.getcwd()
        file = f"{path}/update/actualizar.py"
        try:
            subprocess.Popen(['start', 'cmd', '/k', 'python',file], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
            sys.exit()
        except Exception as e:
            print(f"Error al abrir la aplicación.")
class Login(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #interfaz principal
        self.home = MainWindow()
        self.dialogo = Dialogo()
        self.dialogoexito = DialogoExito()
        #declaracion de boton-funcion
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.register)
    def login(self):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        query=f"SELECT password FROM users WHERE email='{email}'"
        response = consulta(query)
        for tupla in response:
            for a in tupla:
                resultado = a
                
        if response:
            # Verificar si la contraseña coincide
            if password == resultado:
                query = f"SELECT authorization FROM users WHERE email='{email}'"
                response = consulta(query)
                for tupla in response:
                    for a in tupla:
                        self.authorization = a
                global authorization_level
                authorization_level = self.authorization
                self.home.label_9.setText(str(self.authorization))
                query = f"SELECT username FROM users WHERE email='{email}'"
                response = consulta(query)
                for tupla in response:
                    for a in tupla:
                        self.username = a
                self.home.label_11.setText(self.username)
                self.close()
                self.home.show()
                self.lineEdit.clear()
                self.lineEdit_2.clear()
            else:
                self.dialogo.label_2.setText("Usuario o contraseña incorrecto")
                self.dialogo.show()
                self.lineEdit.clear()
                self.lineEdit_2.clear()
        else:
            self.dialogo.label_2.setText("Usuario o contraseña incorrecto")
            self.dialogo.show()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
    def register(self):
        email = self.lineEdit_3.text()
        user = self.lineEdit_4.text()
        password = self.lineEdit_5.text()
        re_password = self.lineEdit_6.text()
        #condiciones y consultas
        if(password == re_password):
            consulta1 = f"SELECT * FROM users WHERE email = '{email}'"
            response1 = consulta(consulta1)
            consulta2 = f"SELECT * FROM users WHERE username = '{user}'"
            response2 = consulta(consulta2)
            if(len(response1) == 0 and len(response2) == 0):
                patron_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if re.match(patron_email, email):
                    add_setence = f"INSERT INTO users (username, password, email, authorization) VALUES ('{user}','{password}','{email}',1)"
                    add(add_setence)
                    self.lineEdit_3.clear()
                    self.lineEdit_4.clear()
                    self.lineEdit_5.clear()
                    self.lineEdit_6.clear()
                    self.dialogoexito.label_2.setText("Registro de usuario exitoso")
                    self.dialogoexito.show()
                else:
                    self.lineEdit_3.clear()
                    self.dialogo.label_2.setText("Email inválido")
                    self.dialogo.show()
            elif(len(response1) != 0):
                self.lineEdit_3.clear()
                self.dialogo.label_2.setText("El email ya existe")
                self.dialogo.show()   
            elif(len(response2) != 0):
                self.lineEdit_4.clear()
                self.dialogo.label_2.setText("El usuario ya existe")
                self.dialogo.show()
        else:
            self.dialogo.label_2.setText("La contraseña no coincide")
            self.dialogo.show()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Interfaces
        self.dialogo = Dialogo()
        self.dialogopregunta = DialogoPregunta()
        self.path = os.getcwd()
        self.log = ""
        self.time = time.localtime()
        self.time = time.strftime("%H:%M", self.time)
        #Inicio
        self.log += f"{self.time} - ¡Nuevo inicio de Sesión!\n"
        self.plainTextEdit.setPlainText(self.log)
        #Configuracion de botones.
        self.pushButton_5.clicked.connect(self.load)
        self.pushButton_2.clicked.connect(self.restart)
        self.pushButton.clicked.connect(self.loadIBC)
        self.pushButton_4.clicked.connect(self.actualizar)
    def actualizar(self):
        self.dialogopregunta.show()
    def loadIBC(self):
        if(authorization_level == 0):
            path = os.getcwd()
            new_file = path+"\lib\setup.py"
            subprocess.run(['start', 'cmd.exe', '/k', 'python', new_file], shell=True, check=True)
            self.log += f"{self.time} - Se ha ejecutado IBC Doctor\n"
            self.plainTextEdit.setPlainText(self.log)
        else:
            self.dialogo.label_2.setText("No tiene permisos de administrador")
            self.dialogo.show()
    def load(self):
        loader = self.path+"\__init__"
        os.chdir(loader)
        try:
            subprocess.Popen(['Proyektor.bat'], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
            self.log += f"{self.time} - Se ha iniciado la aplicación con éxito\n"
            self.plainTextEdit.setPlainText(self.log)
        except Exception:
            self.dialogo.label_2.setText("No se ha encontrado el archivo")
            self.dialogo.show()
    def restart(self):
        try:
            response = requests.get('http://localhost:7777/shutdown')
            self.log += f'{self.time} - Solicitud de cierre enviada. Respuesta del servidor: {response.status_code}\n'
            self.plainTextEdit.setPlainText(self.log)
        except requests.exceptions.RequestException as e:
            self.dialogo.label_2.setText("No se ha realizado la petición")
            self.dialogo.show()
        comando = f'taskkill /F /IM chrome.exe'
        try:
            subprocess.run(comando, shell=True, check=True)
            self.log += f'{self.time} - Servidor "chrome.exe" detenido correctamente.\n'
            self.plainTextEdit.setPlainText(self.log)
        except subprocess.CalledProcessError as e:
            self.dialogo.label_2.setText("Error al detener el servidor")
            self.dialogo.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = MainWindow()
    login = Login()
    login.show()
    sys.exit(app.exec())