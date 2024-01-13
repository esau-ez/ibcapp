import os
import sys
import time
import subprocess
print("""
 ___ ____   ____   ____             _             
|_ _| __ ) / ___| |  _ \  ___   ___| |_ ___  _ __ 
 | ||  _ \| |     | | | |/ _ \ / __| __/ _ \| '__|
 | || |_) | |___  | |_| | (_) | (__| || (_) | |   
|___|____/ \____| |____/ \___/ \___|\__\___/|_|   

""")
def crear_script_en_escritorio(nombre_script):
    # Obtener la ruta al escritorio
    escritorio = os.path.join(os.path.expanduser('~'), 'Desktop')

    # Crear el contenido del script
    contenido_script = """\
import os
import sys
import shutil
def borrar_todo_excepto_init(carpeta):
    for nombre_archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, nombre_archivo)

        if nombre_archivo != "__init__" and os.path.isfile(ruta_archivo):
            # Borrar archivo si no es la carpeta __init__
            os.remove(ruta_archivo)
        elif nombre_archivo != "__init__" and os.path.isdir(ruta_archivo):
            # Borrar directorio recursivamente si no es la carpeta __init__
            shutil.rmtree(ruta_archivo)

# Ejemplo de uso
carpeta_a_limpiar = "C:/ibcapp/"
borrar_todo_excepto_init(carpeta_a_limpiar)
"""

    # Ruta completa del nuevo archivo
    ruta_script = os.path.join(escritorio, nombre_script)

    # Escribir el contenido en el archivo
    with open(ruta_script, 'w') as archivo:
        archivo.write(contenido_script)

    print(f'Se ha creado el archivo {nombre_script} en el escritorio.')
    return ruta_script
for i in range(101):
    sys.stdout.write("\rInicializando proceso: {}%".format(i))
    sys.stdout.flush()
    time.sleep(0.025)
accept = input("¿Está seguro de actualizar la aplicación? (s/n): ")
if (accept == "s"):
    nombre_nuevo_script = "download.py"
    ruta = crear_script_en_escritorio(nombre_nuevo_script)
    try:
        # Abrir el nuevo script en una nueva consola
        subprocess.Popen(['start', 'cmd', '/k', 'python', ruta], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
        # Salir del script original
        sys.exit()
    except Exception as e:
        print(f"Error: {e}")
