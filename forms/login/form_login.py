import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.form_master import MasterPanel
import os

class LoginPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('PoliNinjaGames')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)

        # Cargar logo
        logo = utl.leer_imagen("./imagenes/logoninja.png", (200, 200))

        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        if logo:
            label = tk.Label(frame_logo, image=logo, bg='#3a7ff6')
            label.image = logo
            label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='white')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        title = tk.Label(frame_form, text="Iniciar sesión", font=('Arial', 20, BOLD), bg='white', fg='#666a88')
        title.pack(pady=20)

        # Usuario
        lbl_usuario = tk.Label(frame_form, text="Usuario (Nickname)", font=('Arial', 12), bg='white', anchor="w")
        lbl_usuario.pack(fill='x', padx=20)
        self.entry_usuario = ttk.Entry(frame_form, font=('Arial', 12))
        self.entry_usuario.pack(fill='x', padx=20, pady=10)

        # Contraseña
        lbl_password = tk.Label(frame_form, text="Contraseña", font=('Arial', 12), bg='white', anchor="w")
        lbl_password.pack(fill='x', padx=20)
        self.entry_password = ttk.Entry(frame_form, font=('Arial', 12), show="*")
        self.entry_password.pack(fill='x', padx=20, pady=10)

        # Botón login
        login_btn = ttk.Button(frame_form, text="Ingresar", command=self.verificar_login)
        login_btn.pack(pady=20)

        self.ventana.mainloop()

    def verificar_login(self):
        usuario = self.entry_usuario.get().strip()
        clave = self.entry_password.get().strip()

        if not usuario or not clave:
            messagebox.showwarning("Campos requeridos", "Debe completar todos los campos para iniciar sesión.")
            return

        if not os.path.exists("usuarios.txt"):
            messagebox.showerror("Error", "No hay usuarios registrados.")
            return

        with open("usuarios.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 7:
                    nombre, _, _, nickname, _, password, rol = datos
                    if usuario == nickname and clave == password:
                        if rol.lower() == "administrador":
                            messagebox.showinfo("Bienvenido", f"¡Bienvenido al Panel Administrativo, {nombre}! 🛠️")
                        else:
                            messagebox.showinfo("Bienvenido", f"¡Bienvenido al Mini Mundo Ninja, {nombre}! 🥷")
                        
                        self.ventana.destroy()
                        MasterPanel()
                        return  # Solo salir del método si inicia sesión correctamente

        # Si no se encontró ninguna coincidencia
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
