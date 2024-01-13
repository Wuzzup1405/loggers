# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:56:14 2023

@author: POH
"""

import logging
import os
from datetime import datetime

def logger_gobierno(archivo_log):

    """Crea las carpetas en caso de no existir y guarda los 
    logs/inputs/outputs en las carpetas correspondientes """

    fecha_actual = datetime.now()

    # Obtener el directorio actual y dos niveles atrás
    directorio_base = os.path.dirname(os.path.dirname(os.getcwd()))
    directorio_registros = os.path.join(directorio_base, 'Registros')

    # Obtener el nombre del proyecto del último elemento de os.getcwd()
    nombre_proyecto = os.path.basename(os.path.dirname(os.getcwd()))

    # Crear el directorio base en caso de no existir
    os.makedirs(directorio_base, exist_ok=True)

    # Crea una subcarpeta adicional para la fecha y hora de ejecución
    directorio_fechado = fecha_actual.strftime('%Y-%m-%d %H%M%S')
    directorio_fechado = os.path.join(directorio_registros, nombre_proyecto, directorio_fechado)
    os.makedirs(directorio_fechado, exist_ok=True)

    # Crea la carpeta logs dentro de la carpeta con fecha
    directorio_logs = os.path.join(directorio_fechado, 'Logs')
    os.makedirs(directorio_logs, exist_ok=True)

    # Crea la carpeta inputs
    directorio_inputs = os.path.join(directorio_fechado, 'Inputs')
    os.makedirs(directorio_inputs, exist_ok=True)

    # Crea la carpeta outputs
    directorio_outputs = os.path.join(directorio_fechado, 'Outputs')
    os.makedirs(directorio_outputs, exist_ok=True)

    # Crear la instancia logger con el nombre escogido
    logger = logging.getLogger(nombre_proyecto)

    if not len(logger.handlers):
        # Establecer el nivel del logger a INFO
        logger.setLevel(logging.INFO)
    
        # Establecer el formato de los registros
        formatter = logging.Formatter('%(asctime)s [%(name)s][%(levelname)s] %(message)s')
    
        # Usar filehandler para guardar el log en archivo_log
        log_filename = os.path.join(directorio_logs, archivo_log)
    
        file_handler = logging.FileHandler(log_filename)
    
        # Especificar el formato que se enviará al archivo destino
        file_handler.setFormatter(formatter)

        # Se agrega el manejador de registro al archivo
        logger.addHandler(file_handler)
    
        # Especificar el nivel del logger en el archivo destino
        file_handler.setLevel(logging.INFO)
    
        logger.handler_set = True
    
        def guardar_archivo_input(contenido, nombre_archivo):
            ruta_input = os.path.join(directorio_inputs, nombre_archivo)
            with open(ruta_input, 'w', encoding='UTF-8') as archivo_input:
                archivo_input.write(contenido)
    
        def guardar_archivo_output(contenido, nombre_archivo):
            ruta_output = os.path.join(directorio_outputs, nombre_archivo)
            with open(ruta_output, 'w', encoding='UTF-8') as archivo_output:
                archivo_output.write(contenido)
    
        logger.guardar_archivo_input = guardar_archivo_input
        logger.guardar_archivo_output = guardar_archivo_output
    

    return logger