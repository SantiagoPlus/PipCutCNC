# services/gestor_proyectos.py

import os
import json
from datetime import datetime
from domain.proyecto import Proyecto

DATA_DIR = os.path.join("data", "proyectos")

def crear_proyecto(nombre, cliente, ruta=None):
    """
    Crea una nueva carpeta con el nombre del proyecto y guarda:
    - El archivo JSON con los datos del proyecto (usando el nombre del proyecto)
    - Un archivo notas.txt vacío (sin metadatos)
    Si ruta es None, usa la ruta por defecto (data/proyectos).
    """
    nombre_archivo = nombre.replace(" ", "_")
    if ruta is None:
        carpeta = os.path.join(DATA_DIR, nombre_archivo)
    else:
        carpeta = os.path.join(ruta, nombre_archivo)
    os.makedirs(carpeta, exist_ok=False)

    # Crear instancia del proyecto
    proyecto = Proyecto(nombre, cliente)
    datos = proyecto.a_dict()

    # Guardar JSON del proyecto con el nombre del proyecto
    path_json = os.path.join(carpeta, f"{nombre_archivo}.json")
    with open(path_json, 'w', encoding='utf-8') as f_json:
        json.dump(datos, f_json, ensure_ascii=False, indent=4)

    # Crear notas.txt con mensaje inicial
    path_txt = os.path.join(carpeta, f"{nombre_archivo}.txt")
    with open(path_txt, 'w', encoding='utf-8') as f_txt:
        f_txt.write("Notas del proyecto, escribí con libertad..\n")

    print(f"[LOG] Proyecto creado en: {carpeta}")
    return proyecto

def cargar_proyecto():
    """
    Abre un diálogo para seleccionar un archivo .json de proyecto y lo carga.
    Devuelve la instancia del proyecto cargado o None si se cancela o hay error.
    """
    from tkinter import filedialog, messagebox
    import os
    path = filedialog.askopenfilename(
        initialdir=os.path.abspath(DATA_DIR),
        title="Selecciona el archivo del proyecto",
        filetypes=[("Archivos de proyecto", "*.json")]
    )
    if not path:
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        proyecto = Proyecto(datos['nombre'], datos['cliente'])
        proyecto.fecha_creacion = datos['fecha_creacion']
        # TODO: cargar los productos, piezas y caños si están presentes en el JSON
        return proyecto, os.path.dirname(path)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None, None

def listar_proyectos_disponibles():
    """Devuelve una lista con los nombres de los proyectos guardados"""
    if not os.path.exists(DATA_DIR):
        return []
    return [nombre for nombre in os.listdir(DATA_DIR)
            if os.path.isdir(os.path.join(DATA_DIR, nombre))]

def crear_nuevo_proyecto_desde_interfaz(nombre, cliente, ruta_base=None):
    """
    Crea un nuevo proyecto en la ruta base indicada (o en la ruta por defecto), con el nombre y cliente dados.
    Devuelve (exito, mensaje, ruta_proyecto).
    """
    if not nombre or not cliente:
        return False, "Faltan datos para crear el proyecto.", None
    if ruta_base is None:
        ruta_base = DATA_DIR
    try:
        proyecto = crear_proyecto(nombre, cliente, ruta=ruta_base)
        ruta_proy = os.path.join(ruta_base, nombre.replace(" ", "_"))
        return True, f"Proyecto '{nombre}' creado correctamente en {ruta_proy}.", ruta_proy
    except FileExistsError:
        return False, "Ya existe un proyecto con ese nombre en la carpeta seleccionada.", None
    except Exception as e:
        return False, str(e), None
