import socket
import subprocess
import time
import sys
import os
import warnings
warnings.filterwarnings('error')

path = os.getcwd()
packages = [
    "PySide6==6.6.1",
    "mysql-connector-python==8.2.0",
    "python-dotenv==1.0.0",
    "requests==2.31.0",
    "pyyaml==6.0.1"
]
checkPackages = [
    "PySide6",
    "mysql-connector-python",
    "python-dotenv",
    "requests",
    "pyyaml"
]
global notInstalled
notInstalled = []
print("""
 ___ ____   ____   ____             _             
|_ _| __ ) / ___| |  _ \  ___   ___| |_ ___  _ __ 
 | ||  _ \| |     | | | |/ _ \ / __| __/ _ \| '__|
 | || |_) | |___  | |_| | (_) | (__| || (_) | |   
|___|____/ \____| |____/ \___/ \___|\__\___/|_|   

""")

#GLOBAL KEYS
VERSION = "1.0.1"
HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(HOSTNAME)
LOGHOUR = time.localtime().tm_hour
LOGMINUTES = time.localtime().tm_min
SESION = 'INFORMACIÓN DEL LOG: ¡Se ha iniciado sesión desde un aplicación llave. No es necesario login manual!'
#FIN GLOBAL KEY

print(f"VERSIÓN: {VERSION}")
print(f"HOTNAME: {HOSTNAME}")
print(f"IP: {IP}")
print(f"LOG TIME: {LOGHOUR}:{LOGMINUTES}")
print(SESION)
print("""\n
SELECCIONE OPCIÓN:
1 - Instalación inicial (Setup)
2 - Comprobar paquetes necesarios
3 - Inicialización de base de datos (setup-database)
\n""")
#Descarga de paquetes
def setup(list):
    for i in range(101):
        sys.stdout.write("\rInicializando proceso: {}%".format(i))
        sys.stdout.flush()
        time.sleep(0.025)
    for a in list:
        try:
            print(f"\n**Instalando {a}**")
            comando = ["pip","install",a]
            subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("Paquete instalado correctamente\n")
            time.sleep(2)
        except Exception as e:
            print(e)
            notInstalled.append(a)
    new_file = path+"\main.py"
    bat_content = f"""@echo off
    python "{new_file}"
    """

            # Ruta al escritorio del usuario
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

            # Ruta completa del archivo por lotes en el escritorio
    bat_file_path = os.path.join(desktop_path, "ibcAplication.bat")

            # Guardar el contenido en el archivo por lotes
    with open(bat_file_path, "w") as bat_file:
        bat_file.write(bat_content)
    try:
        process = subprocess.run(['cd',bat_file_path], shell=False, check=True)
    except:
        print("Ocurrió un error al lanzar la aplicaión, contacte con su empresa más cercana")
def check(list):
    for i in range(101):
        sys.stdout.write("\rInicializando proceso: {}%".format(i))
        sys.stdout.flush()
        time.sleep(0.010)
    for a in list:
        print(f"\n**Comprobando {a}**")
        try:
            comando = ["pip","show",a]
            resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if ("WARNING: Package(s) not found:" in resultado.stderr):
                print(f"El paquete no está instalado.")
                notInstalled.append(a)
            else:
                print("El paquete está instalado")
            time.sleep(1.5)
        except Warning:
            print("El paquete no está instalado.")
            notInstalled.append(a)
            

opcion = int(input("Seleccione opción: "))
if(opcion == 1):
    setup(packages)
    print(f"\n*Paquetes no instalados*\n{notInstalled}")
    notInstalled.clear()
elif(opcion ==2):
    check(checkPackages)
    print(f"\n*Paquetes faltantes*\n{notInstalled}")
    notInstalled.clear()
elif(opcion==3):
    print("Si no se han instalado los paquetes necesarios, continuar por este camino podría ser fatal")
    afirmacion = input("¿Desea continuar? (s/n): ")
    if(afirmacion == "s"):
        for i in range(101):
            sys.stdout.write("\rInicializando proceso: {}%".format(i))
            sys.stdout.flush()
            time.sleep(0.010)
        new_file = path+"\config\database-setup.py"
        process = subprocess.run(['start', 'cmd.exe', '/k', 'python', new_file], shell=True, check=True)