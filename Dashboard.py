import os
import subprocess

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

#Nueva funcionalidad: muestra las estadística del archivo como número de líneas, funciones definidas, y tamaño en KB.
def estadisticas_script(ruta_script):
    try:
        with open(ruta_script, 'r') as archivo:
            lineas = archivo.readlines()
            funciones = [l for l in lineas if l.strip().startswith('def ')]
            tamano_kb = os.path.getsize(ruta_script) / 1024
            print(f"\n--- Estadísticas de {os.path.basename(ruta_script)} ---")
            print(f"Líneas totales       : {len(lineas)}")
            print(f"Funciones definidas  : {len(funciones)}")
            print(f"Tamaño del archivo   : {tamano_kb:.2f} KB\n")
    except Exception as e:
        print(f"Error al analizar el archivo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    actividades = {
        '1': 'ACTIVIDADES 1',
        '2': 'ACTIVIDADES 2',
        '3': 'ACTIVIDADES 3',
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key in actividades:
            print(f"{key} - {actividades[key]}")
        print("0 - Salir")

        eleccion_actividad = input("Elige una unidad o '0' para salir: ")
        if eleccion_actividad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_actividad in actividades:
            mostrar_sub_menu(os.path.join(ruta_base, actividades[eleccion_actividad]))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts - Selecciona un script para ver, ejecutar o analizar")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    #Nuevas opciones en el sub menú
                    while True:
                        print(f"\n--- Opciones para '{scripts[eleccion_script]}' ---")
                        print("1 - Ver código")
                        print("2 - Ejecutar script")
                        print("3 - Mostrar estadísticas")
                        print("0 - Regresar a la lista de scripts")
                        opcion = input("Selecciona una opción: ")

                        if opcion == '1':
                            mostrar_codigo(ruta_script)
                        elif opcion == '2':
                            ejecutar_codigo(ruta_script)
                        elif opcion == '3':
                            estadisticas_script(ruta_script)
                        elif opcion == '0':
                            break
                        else:
                            print("Opción no válida. Intenta de nuevo.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
