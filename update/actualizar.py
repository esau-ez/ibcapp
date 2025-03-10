import os
import sys
import time
import subprocess
from pathlib import Path
directorio_base = Path(__file__).resolve().parent
print("""
 ___ ____   ____   ____             _             
|_ _| __ ) / ___| |  _ \  ___   ___| |_ ___  _ __ 
 | ||  _ \| |     | | | |/ _ \ / __| __/ _ \| '__|
 | || |_) | |___  | |_| | (_) | (__| || (_) | |   
|___|____/ \____| |____/ \___/ \___|\__\___/|_|   

""")
for i in range(101):
    sys.stdout.write("\rInicializando proceso: {}%".format(i))
    sys.stdout.flush()
    time.sleep(0.025)
accept = input("\n\n¿Está seguro de actualizar la aplicación? (s/n): ")
if (accept == "s"):
    comando = f"rmdir /s /q C:\ibcapp"
    try:
        comando = "git clone https://github.com/esau-ez/ibcapp C:\ibcapp"
        subprocess.run(comando, shell=False)
        for i in range(101):
            sys.stdout.write("\rDescargando actualización: {}%".format(i))
            sys.stdout.flush()
            time.sleep(0.5)
        print("\nLa aplicación se ha actualizado correctamente")
        print("Por favor, ejecute el archivo setup.py para poder reestablecer la aplicación\n")
        directorio_ibcapp = directorio_base.parent
        new_file = directorio_ibcapp / 'main.py'
        process = subprocess.run(['python', new_file], shell=False, check=True)
        sys.exit()
    except Exception as e:
        print(f"Error: {e}")
else:
     print(f"\nSaliendo...")
     time.sleep(3)
     sys.exit()
