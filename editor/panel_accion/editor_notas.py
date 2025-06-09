import customtkinter as ctk
import os

class EditorNotas(ctk.CTkFrame):
    def __init__(self, parent, ruta_txt=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ruta_txt = ruta_txt
        self.configure(fg_color="#333333")

        self.texto = ctk.CTkTextbox(self, fg_color="#222222", text_color="#fff")
        self.btn_guardar = ctk.CTkButton(
            self, text="Guardar Cambios", command=self.guardar_notas,
            fg_color="#444444", hover_color="#666666"
        )
        self.after(100, self.cargar_notas)

    def cargar_notas(self):
        if self.ruta_txt and os.path.exists(self.ruta_txt):
            try:
                with open(self.ruta_txt, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                self.texto.delete("1.0", "end")
                self.texto.insert("1.0", contenido)
            except Exception as e:
                self.texto.delete("1.0", "end")
                self.texto.insert("1.0", f"[Error al leer notas: {e}]")
        else:
            self.texto.delete("1.0", "end")
            self.texto.insert("1.0", "Notas del proyecto, escribí con libertad..")

    def guardar_notas(self):
        if self.ruta_txt:
            try:
                from datetime import datetime
                texto = self.texto.get("1.0", "end-1c").strip()
                fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                marca_roja = f"(ROJO) Cambios guardados {fecha}\n"
                with open(self.ruta_txt, 'a', encoding='utf-8') as f:
                    f.write(f"\n{marca_roja}")
                    f.write(texto + "\n")
                # Mostrar confirmación temporal en el widget (no borrar el texto)
                self.texto.insert("end", f"\n--- Cambios guardados {fecha} ---")
            except Exception as e:
                self.texto.delete("1.0", "end")
                self.texto.insert("1.0", f"[Error al guardar notas: {e}]")
