import customtkinter as ctk
from tkinter import ttk
from editor.panel_accion.editor_notas import EditorNotas
import os

# Ventana de edición de proyectos
class EditorFrame(ctk.CTkFrame):
    def __init__(self, parent, ruta_proyecto=None, nombre_proyecto=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")  # Tema gris oscuro

        # --- MENÚ DE PESTAÑAS PARA BARRAS DE HERRAMIENTAS (solo espacio, sin vincular frames) ---
        self.notebook_herramientas = ttk.Notebook(self)
        self.notebook_herramientas.pack(side="top", fill="x")
        self.notebook_herramientas.add(ctk.CTkFrame(self.notebook_herramientas, height=90, fg_color="#2a2a2a"), text="Administrar proyectos")
        self.notebook_herramientas.add(ctk.CTkFrame(self.notebook_herramientas, height=90, fg_color="#2a2a2a"), text="Productos")
        self.notebook_herramientas.add(ctk.CTkFrame(self.notebook_herramientas, height=90, fg_color="#2a2a2a"), text="Pieza")

        # Área central: Acción (izquierda) y Visualización (derecha) usando grid
        self.frame_central = ctk.CTkFrame(self, height=400, fg_color="#222222")
        self.frame_central.pack(side="top", fill="both", expand=True)
        self.frame_central.pack_propagate(True)
        self.frame_central.grid_rowconfigure(0, weight=1)
        self.frame_central.grid_columnconfigure(0, weight=3)  # Acción
        self.frame_central.grid_columnconfigure(1, weight=1)  # Visualización

        # Acción (izquierda) dividida en 3 partes (notas ocupa 1/3)
        self.frame_accion = ctk.CTkFrame(self.frame_central, fg_color="#333333")
        self.frame_accion.grid(row=0, column=0, sticky="nsew")
        self.frame_accion.grid_rowconfigure(0, weight=1)
        self.frame_accion.grid_rowconfigure(1, weight=2)
        self.frame_accion.grid_rowconfigure(2, weight=2)
        self.frame_accion.grid_columnconfigure(0, weight=1)
        label_accion = ctk.CTkLabel(self.frame_accion, text="Acción", anchor="w", font=("Arial", 12))
        label_accion.grid(row=0, column=0, sticky="nw", padx=20, pady=10)

        # Editor de notas ocupa la parte derecha del panel de acción (columna 2)
        self.frame_accion.grid_columnconfigure(0, weight=1)
        self.frame_accion.grid_columnconfigure(1, weight=1)
        self.frame_accion.grid_columnconfigure(2, weight=3)
        ruta_txt = None
        if ruta_proyecto:
            nombre = nombre_proyecto if nombre_proyecto else os.path.basename(ruta_proyecto)
            ruta_txt = os.path.join(ruta_proyecto, f"{nombre}.txt")
        self.editor_notas = EditorNotas(self.frame_accion, ruta_txt=ruta_txt)
        self.editor_notas.texto.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10,5))
        self.editor_notas.btn_guardar.grid(row=1, column=0, sticky="ew", padx=10, pady=(0,10))
        self.editor_notas.grid(row=1, column=2, sticky="nsew", padx=10, pady=5)
        self.frame_accion.grid_columnconfigure(1, weight=1)

        # Visualización (derecha)
        self.frame_visual = ctk.CTkFrame(self.frame_central, fg_color="#222222")
        self.frame_visual.grid(row=0, column=1, sticky="nsew")
        label_visual = ctk.CTkLabel(self.frame_visual, text="Visualización", anchor="w", font=("Arial", 12))
        label_visual.pack(side="top", anchor="nw", padx=20, pady=10)

        # Área inferior: Historial (más alta)
        self.frame_historial = ctk.CTkFrame(self, height=120, fg_color="#2a2a2a")  # Altura al doble (antes 60)
        self.frame_historial.pack(side="bottom", fill="x")
        self.frame_historial.pack_propagate(False)
        label_hist = ctk.CTkLabel(self.frame_historial, text="Historial", anchor="w", font=("Arial", 12))
        label_hist.pack(side="left", padx=20, pady=5)

    def cerrar_pestana(self):
        # Busca el notebook padre y cierra la pestaña actual
        parent = self.master
        while parent is not None:
            if isinstance(parent, ttk.Notebook):
                idx = parent.index(self)
                parent.forget(idx)
                break
            parent = getattr(parent, 'master', None)
