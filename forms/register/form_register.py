import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import re
import os
import util.generic as utl

class RegisterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Registro - PoliNinjaGames")
        self.ventana.geometry("800x500")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(False, False)
        utl.centrar_ventana(self.ventana, 800, 500)

        # Imagen logo
        logo = utl.leer_imagen("./imagenes/logoninja.png", (200, 200))

        # Frame izquierdo con imagen
        frame_logo = tk.Frame(self.ventana, width=300, bg='#3a7ff6')
        frame_logo.pack(side="left", fill=tk.BOTH)
        if logo:
            label = tk.Label(frame_logo, image=logo, bg='#3a7ff6')
            label.image = logo
            label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame derecho con formulario
        frame_form = tk.Frame(self.ventana, bg='white')
        frame_form.pack(side="right", fill=tk.BOTH, expand=True)

        title = tk.Label(frame_form, text="Crear cuenta", font=('Arial', 20, BOLD), bg='white', fg='#666a88')
        title.pack(pady=10)

        # Campos del formulario
        self.campos = {}
        self.labels = ["Nombres", "Apellidos", "Edad", "Nickname", "Correo Electrónico", "Contraseña"]
        for label_text in self.labels:
            lbl = tk.Label(frame_form, text=label_text, font=('Arial', 12), bg='white', anchor="w")
            lbl.pack(fill='x', padx=20)
            entry = ttk.Entry(frame_form, font=('Arial', 12), show="*" if label_text == "Contraseña" else None)
            entry.pack(fill='x', padx=20, pady=5)
            self.campos[label_text] = entry

        # Botón de registrar
        btn_registrar = ttk.Button(frame_form, text="Registrarse", command=self.validar_datos)
        btn_registrar.pack(pady=20)

        self.ventana.mainloop()

    def validar_datos(self):
        datos = {campo: self.campos[campo].get().strip() for campo in self.campos}

        if any(not valor for valor in datos.values()):
            messagebox.showwarning("Campos requeridos", "Debe completar todos los campos.")
            return

        if not datos["Edad"].isdigit() or int(datos["Edad"]) <= 0:
            messagebox.showerror("Error", "La edad debe ser un número positivo.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", datos["Correo Electrónico"]):
            messagebox.showerror("Error", "Correo electrónico inválido.")
            return

        if len(datos["Contraseña"]) < 8:
            messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres.")
            return

        # Leer usuarios existentes
        usuarios_existentes = []
        if os.path.exists("usuarios.txt"):
            with open("usuarios.txt", "r", encoding="utf-8") as archivo:
                usuarios_existentes = archivo.readlines()

        for linea in usuarios_existentes:
            partes = linea.strip().split(",")
            if len(partes) >= 5:
                if datos["Nickname"] == partes[3]:
                    messagebox.showerror("Error", "El nickname ya está en uso.")
                    return
                if datos["Correo Electrónico"] == partes[4]:
                    messagebox.showerror("Error", "El correo electrónico ya está registrado.")
                    return

        # Guardar todos los datos del usuario
        with open("usuarios.txt", "a", encoding="utf-8") as archivo:
            fila = ",".join([
                datos["Nombres"],
                datos["Apellidos"],
                datos["Edad"],
                datos["Nickname"],
                datos["Correo Electrónico"],
                datos["Contraseña"]
            ])
            archivo.write(fila + "\n")

        messagebox.showinfo("Registro exitoso", f"Bienvenido/a {datos['Nombres']} {datos['Apellidos']} 👋")
        self.ventana.destroy()

        from forms.login.form_login import LoginPanel
        LoginPanel()
