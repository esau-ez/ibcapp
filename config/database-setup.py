import sys
import time
import mysql.connector
import yaml
import os
from pathlib import Path
global directorio_base
directorio_base = Path(__file__).resolve().parent
print("""
 ___ ____   ____   ____             _             
|_ _| __ ) / ___| |  _ \  ___   ___| |_ ___  _ __ 
 | ||  _ \| |     | | | |/ _ \ / __| __/ _ \| '__|
 | || |_) | |___  | |_| | (_) | (__| || (_) | |   
|___|____/ \____| |____/ \___/ \___|\__\___/|_|   

""")

def probar_conexion(user, password,host):
    try:
        # Configurar la conexión
        conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database="ibcapp"
        )

        # Comprobar si la conexión fue exitosa
        if conexion.is_connected():
            return "¡Conexión exitosa a la base de datos!"
            # Aquí puedes realizar más operaciones si es necesario
            # ...

    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")

    finally:
        # Cerrar la conexión al finalizar
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()

print("¡Bienvenido a la interfaz de inicio de base de datos!\n")
print("¡A continuación introduzca su usuario y contraseña proporcionadas\n")
user = input("user: ")
password = input("\npassword: ")
host = input("\nHost (IP): ")
for i in range(101):
    sys.stdout.write("\rComprobando credenciales: {}%".format(i))
    sys.stdout.flush()
    time.sleep(0.010)

print("\n")
resultado = probar_conexion(user, password,host)
if(resultado == "¡Conexión exitosa a la base de datos!"):
    # Ruta del archivo YAML
    directorio_ibcapp = directorio_base.parent
    ruta_del_archivo_yaml = directorio_ibcapp /'config'/'settings.yaml'

    # Cargar el contenido del archivo YAML
    with open(ruta_del_archivo_yaml, 'r') as archivo_yaml:
        datos = yaml.safe_load(archivo_yaml)

    # Modificar o agregar datos
    datos['databaseUser'] = f'{user}'
    datos['databasePassword'] = f'{password}'
    datos['host'] = f'{host}'
    # Guardar los cambios en el archivo YAML
    with open(ruta_del_archivo_yaml, 'w') as archivo_yaml:
        yaml.dump(datos, archivo_yaml, default_flow_style=False)
    print("\nTodo funcionó correctamente. Programa listo para ser ejecutado")
    time.sleep(3)
    sys.exit()
else:
    print("\nError ocurrido, revise dependencias")
    time.sleep(3)
    sys.exit()