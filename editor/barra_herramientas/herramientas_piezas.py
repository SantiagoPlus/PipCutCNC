import customtkinter as ctk

class HerramientasPiezas(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        label = ctk.CTkLabel(self, text="Barra de Herramientas: Pieza", font=("Arial", 12))
        label.pack(padx=10, pady=10)
        # Aquí puedes agregar más widgets para la barra de piezas
