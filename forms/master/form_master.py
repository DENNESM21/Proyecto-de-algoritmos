import tkinter as tk
from tkinter.font import BOLD
from PIL import ImageTk, Image
import os


class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Master Panel")

        ancho = 800
        alto = 600
        self.ventana.resizable(False, False)
        self.centrar_ventana(self.ventana, ancho, alto)

        # Fondo
        ruta_imagen = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "imagenes", "ninja.png"))
        self.fondo = self.leer_imagen(ruta_imagen, (ancho, alto))
        label_fondo = tk.Label(self.ventana, image=self.fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # ---------- TÍTULO CON ESTILO Y ANIMACIÓN ----------
        self.tamano_fuente = 26
        self.subiendo = True
        self.titulo = tk.Label(
            self.ventana,
            text="¡Bienvenido al Clan Ninja!",
            font=("Comic Sans MS", self.tamano_fuente, BOLD),
            fg="white",
            bg="#00aaff"
        )
        self.titulo.place(relx=0.5, rely=0.15, anchor="center")
        self.animar_titulo()
        self.descripcion = tk.Label(
        self.ventana,
        text="🥷 Pon a prueba tus reflejos y habilidades ninja en este divertido minijuego.\n¡Entrena, esquiva y conviértete en el maestro del Clan!",
        font=("Comic Sans MS", 16, BOLD),
        fg="black",
        justify="center"
        )
        self.descripcion.place(relx=0.5, rely=0.32, anchor="center")
        
        # ---------- BOTÓN REGISTRARSE ----------
        self.btn_registro = tk.Button(
            self.ventana,
            text="Registrarse",
            font=("Verdana", 12, BOLD),
            width=15,
            height=2,
            bg="#ffffff",
            fg="#000000",
            activebackground="#00ccff",
            activeforeground="#ffffff",
            cursor="hand2",
            bd=2,
            relief="raised",
            command=self.ir_a_registro
        )
        self.btn_registro.place(relx=0.3, rely=0.75, anchor="center")
        self.animar_hover(self.btn_registro)

        # ---------- BOTÓN INICIAR SESIÓN ----------
        self.btn_login = tk.Button(
            self.ventana,
            text="Iniciar Sesión",
            font=("Verdana", 12, BOLD),
            width=15,
            height=2,
            bg="#ffffff",
            fg="#000000",
            activebackground="#00ccff",
            activeforeground="#ffffff",
            cursor="hand2",
            bd=2,
            relief="raised",
            command=self.ir_a_login
        )
        self.btn_login.place(relx=0.7, rely=0.75, anchor="center")
        self.animar_hover(self.btn_login)

        self.ventana.mainloop()

    # ---------- EFECTO ZOOM EN EL TÍTULO ----------
    def animar_titulo(self):
        if self.subiendo:
            self.tamano_fuente += 1
            if self.tamano_fuente >= 30:
                self.subiendo = False
        else:
            self.tamano_fuente -= 1
            if self.tamano_fuente <= 26:
                self.subiendo = True

        self.titulo.config(font=("Comic Sans MS", self.tamano_fuente, BOLD))
        self.ventana.after(100, self.animar_titulo)

    # ---------- EFECTO HOVER EN BOTONES ----------
    def animar_hover(self, boton):
        def on_enter(e):
            boton.config(bg="#00ccff", fg="#ffffff", font=("Verdana", 13, BOLD))

        def on_leave(e):
            boton.config(bg="#ffffff", fg="#000000", font=("Verdana", 12, BOLD))

        boton.bind("<Enter>", on_enter)
        boton.bind("<Leave>", on_leave)

    def ir_a_registro(self):
        from forms.register.form_register import RegisterPanel  
        self.ventana.destroy()
        RegisterPanel() 

    def ir_a_login(self):
        from forms.login.form_login import LoginPanel  
        self.ventana.destroy()
        LoginPanel() 
    def leer_imagen(self, path, size):
        return ImageTk.PhotoImage(Image.open(path).resize(size))

    def centrar_ventana(self, ventana, ancho, alto):
        pantalla_ancho = ventana.winfo_screenwidth()
        pantalla_alto = ventana.winfo_screenheight()
        x = int((pantalla_ancho - ancho) / 2)
        y = int((pantalla_alto - alto) / 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

if __name__ == "__main__":
    MasterPanel()
