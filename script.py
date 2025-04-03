#!/usr/bin/env python3

import os
import sys
import re

def main():
    # Lista de información adicional a agregar al inicio de cada fichero
    info_lines = [
        "<!-- Autor: Daniel Benjamin Perez Morales -->",
        "<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->",
        "<!-- Correo electrónico: danielperezdev@proton.me -->"
    ]
    
    # Obtener la lista de ficheros en el directorio actual, excepto el propio script
    files = os.listdir(".")
    # files.remove(sys.argv[0])  # Remove the script itself from the list
    
    files.remove("script.py")
    
    # Iterar sobre cada fichero encontrado
    for filename in files:
        # Construir el nuevo nombre del fichero con extensión .md y título capitalizado
        new_filename = f"{filename[:-3].title()}.md"

        # # Agregar información adicional al inicio del fichero
        # for line in info_lines:
        #     os.system(f'echo "{line}" >> "{filename}"')

        # Intentar renombrar el fichero
        try:
            os.rename(filename, new_filename)
        except FileNotFoundError:
            print(f"Error: El fichero '{filename}' no existe.")
        except FileExistsError:
            print(f"Error: Ya existe un fichero con el nombre '{new_filename}'.")
        except Exception as e:
            print(f"Error al renombrar '{filename}' a '{new_filename}': {str(e)}")

def second():

    # Ruta al directorio que contiene los ficheros
    directorio = '.'

    # Obtener la lista de ficheros ordenados
    ficheros = sorted(os.listdir(directorio))

    # Expresión regular para encontrar el número al inicio del nombre del fichero
    numero_regex = re.compile(r'^(\d+)')

    # Iterar sobre los ficheros
    for i, fichero in enumerate(ficheros):
        # Encontrar el número al inicio del nombre del fichero
        match = numero_regex.match(fichero)
        if match:
            numero_actual = int(match.group(1))
            
            # Solo modificar ficheros con números a partir de 15
            if numero_actual >= 1:
                # Calcular el nuevo número según la lógica especificada (incrementar en 1)
                nuevo_numero = numero_actual + 1
                
                # Crear el nuevo nombre de fichero
                nuevo_nombre = f"{nuevo_numero:02d} {fichero.split(maxsplit=1)[1]}"
                
                # Renombrar el fichero
                os.rename(os.path.join(directorio, fichero), os.path.join(directorio, nuevo_nombre))
                print(f"Renombrado: {fichero} -> {nuevo_nombre}")
            else:
                print(f"No se modificó el fichero: {fichero}")
        else:
            print(f"No se pudo encontrar un número al inicio en el fichero: {fichero}")

    print("Renombrado completado.")


if __name__ == "__main__":
    # main()
    second()