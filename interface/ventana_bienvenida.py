import customtkinter as ctk
from tkinter import messagebox, simpledialog, filedialog
from interface.Visual_Global import VisualGlobal
from services.gestor_proyectos import crear_nuevo_proyecto_desde_interfaz, listar_proyectos_disponibles, cargar_proyecto
import os

def mostrar_ventana_bienvenida():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")  # Tema gris oscuro
    root = ctk.CTk()
    root.title("PipCut CNC - 3ejes")
    # Pantalla completa compatible multiplataforma
    root.attributes('-fullscreen', True)
    root.configure(bg="#222222")  # Fondo gris oscuro para toda la ventana

    # Callbacks para el menú global
    def ir_bienvenida():
        root.destroy()
        mostrar_ventana_bienvenida()

    def abrir_proyecto():
        cargar_proyecto_existente()

    def guardar_proyecto():
        messagebox.showinfo("Guardar", "Funcionalidad de guardado aún no implementada.")

    def cerrar_proyecto():
        messagebox.showinfo("Cerrar", "Funcionalidad de cerrar proyecto aún no implementada.")

    def configuracion():
        messagebox.showinfo("Configuración", "Aquí iría la configuración global.")

    visual = VisualGlobal(
        master=root,
        callback_ventana_bienvenida=ir_bienvenida,
        callback_abrir=abrir_proyecto,
        callback_guardar=guardar_proyecto,
        callback_cerrar=cerrar_proyecto,
        callback_config=configuracion,
        ruta_proyecto=""
    )

    # Crear notebook y pestaña de inicio
    visual.agregar_notebook()
    tab_inicio = ctk.CTkFrame(visual.notebook, fg_color="#222222")
    visual.agregar_pestana(tab_inicio, "Inicio")
    # Contenido de la pestaña de inicio
    label_inicio = ctk.CTkLabel(tab_inicio, text="Bienvenido a PipCut CNC", font=("Arial", 16))
    label_inicio.pack(pady=20)
    # Botones de la pestaña de inicio
    def salir():
        root.destroy()
    def ver_proyectos():
        proyectos = listar_proyectos_disponibles()
        if not proyectos:
            messagebox.showinfo("Proyectos", "No hay proyectos guardados.")
        else:
            messagebox.showinfo("Proyectos", "Proyectos guardados:\n" + "\n".join(proyectos))
    def crear_nuevo_proyecto():
        carpeta_predeterminada = os.path.abspath("data/proyectos")
        carpeta = filedialog.askdirectory(
            parent=root,
            initialdir=carpeta_predeterminada,
            title="Selecciona la carpeta donde crear el proyecto"
        )
        if not carpeta:
            return
        nombre = simpledialog.askstring("Nuevo Proyecto", "Nombre del proyecto:", parent=root)
        if not nombre:
            return
        cliente = simpledialog.askstring("Nuevo Proyecto", "Nombre del cliente:", parent=root)
        if not cliente:
            return
        exito, mensaje, ruta_proyecto = crear_nuevo_proyecto_desde_interfaz(nombre, cliente, carpeta)
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            visual.actualizar_ruta(ruta_proyecto)
            abrir_ventana_editor(nombre)
        else:
            messagebox.showerror("Error", mensaje)
    def cargar_proyecto_existente():
        resultado = cargar_proyecto()
        if resultado is not None:
            proyecto, ruta = resultado
            if proyecto and ruta:
                visual.actualizar_ruta(ruta)
                abrir_ventana_editor(proyecto.nombre, ruta_proyecto=ruta)
    btn_nuevo = ctk.CTkButton(tab_inicio, text="Crear nuevo proyecto", width=220, command=crear_nuevo_proyecto, fg_color="#444444", hover_color="#666666")
    btn_nuevo.pack(pady=5)
    btn_cargar = ctk.CTkButton(tab_inicio, text="Cargar proyecto existente", width=220, command=cargar_proyecto_existente, fg_color="#444444", hover_color="#666666")
    btn_cargar.pack(pady=5)
    btn_ver = ctk.CTkButton(tab_inicio, text="Ver proyectos guardados", width=220, command=ver_proyectos, fg_color="#444444", hover_color="#666666")
    btn_ver.pack(pady=5)
    btn_salir = ctk.CTkButton(tab_inicio, text="Salir", width=220, command=salir, fg_color="#444444", hover_color="#666666")
    btn_salir.pack(pady=20)

    # Función para cerrar pestañas
    def cerrar_pestana(indice):
        visual.notebook.forget(indice)

    # Función para abrir o cargar proyecto y crear pestaña
    def abrir_ventana_editor(nombre_pestana, ruta_proyecto=None):
        from interface.Ventana_Editor import EditorFrame
        import tkinter as tk
        contenedor = tk.Frame(visual.notebook)  # Frame estándar de Tkinter
        frame_editor = EditorFrame(contenedor, ruta_proyecto=ruta_proyecto, nombre_proyecto=nombre_pestana)
        frame_editor.pack(fill="both", expand=True)
        visual.agregar_pestana(contenedor, nombre_pestana)
        idx = visual.notebook.index("end") - 1
        visual.notebook.select(idx)

    root.mainloop()
