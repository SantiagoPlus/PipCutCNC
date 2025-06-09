#Menu superior "Acá estará el menú superior y el pie de páguina"
  #Menú o barra superior con los menús: 
    #PipCut(Directo a Ventana de bienvenida)
    # Archivo (Abrir proyecto,Guardar Proyecto, Cerrar proyecto, 
    # Configuración
        # Esta configuración es GLOBAL y afecta a todo el programa
        # Aquí se definen valores modificables por el usuario, sin alterar el código fuente
        # como el idioma, la unidad de medida
        # y otras preferencias generales.

#pie de páguina

# Aquí se implementará la lógica de la interfaz gráfica global

import tkinter as tk

class VisualGlobal(tk.Frame):
    """
    Barra superior y pie de página global para la aplicación PipCut CNC.
    Incluye menú superior (PipCut, Archivo, Configuración) y pie de página con ruta de proyecto abierto.
    """
    def __init__(self, master=None, callback_ventana_bienvenida=None, callback_abrir=None, callback_guardar=None, callback_cerrar=None, callback_config=None, ruta_proyecto=""):
        super().__init__(master)
        # Colores fijos para tema oscuro
        self.tema = {
            "fondo": "#353535",
            "texto": "#ffffff"
        }
        self.callback_ventana_bienvenida = callback_ventana_bienvenida
        self.callback_abrir = callback_abrir
        self.callback_guardar = callback_guardar
        self.callback_cerrar = callback_cerrar
        self.callback_config = callback_config
        self.ruta_proyecto = ruta_proyecto
        self.pack(fill=tk.BOTH, expand=False)
        self._crear_menu()
        self._crear_pie_pagina()

    def _crear_menu(self):
        menubar = tk.Menu(self.master)
        # Menú PipCut como acción directa
        menubar.add_command(label="PipCut", command=self.callback_ventana_bienvenida)
        # Menú Archivo
        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Abrir proyecto", command=self.callback_abrir)
        archivo_menu.add_command(label="Guardar proyecto", command=self.callback_guardar)
        archivo_menu.add_command(label="Cerrar proyecto", command=self.callback_cerrar)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)
        # Menú Configuración (sin opciones de tema)
        config_menu = tk.Menu(menubar, tearoff=0)
        config_menu.add_command(label="Configuración global", command=self.callback_config)
        menubar.add_cascade(label="Configuración", menu=config_menu)
        # Asignar menú a la ventana principal
        self.master.config(menu=menubar)

    def _crear_pie_pagina(self):
        self.pie = tk.Label(self.master, anchor="e", bg=self.tema["fondo"], fg=self.tema["texto"])
        self.pie.pack(side=tk.BOTTOM, fill=tk.X)
        self.actualizar_ruta(self.ruta_proyecto)

    def actualizar_ruta(self, nueva_ruta):
        self.ruta_proyecto = nueva_ruta
        self.pie.config(text=f"Ruta proyecto: {self.ruta_proyecto}")

    def agregar_notebook(self):
        """
        Crea un widget Notebook (pestañas) en la interfaz global.
        Debe llamarse una vez después de crear VisualGlobal.
        """
        from tkinter import ttk
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill='both', expand=True)

    def agregar_pestana(self, frame, nombre):
        """
        Agrega una pestaña (tab) al notebook global.
        """
        if hasattr(self, 'notebook'):
            self.notebook.add(frame, text=nombre)