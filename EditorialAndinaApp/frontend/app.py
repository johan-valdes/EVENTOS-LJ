import tkinter as tk
from tkinter import messagebox
import threading
import time
import requests

API_URL = "http://127.0.0.1:8000/api"

def enviar_datos_autor(nombre, nacionalidad, edad):
    if not nombre and not nacionalidad and not edad:
        messagebox.showwarning("Advertencia", "Todos los campos del autor están vacíos.")
        return
    if not nombre:
        messagebox.showwarning("Advertencia", "El campo 'Nombre' no puede estar vacío.")
        return
    if not nacionalidad:
        messagebox.showwarning("Advertencia", "El campo 'Nacionalidad' no puede estar vacío.")
        return
    if not edad:
        messagebox.showwarning("Advertencia", "El campo 'Edad' no puede estar vacío.")
        return
    if not edad.isdigit():
        messagebox.showwarning("Advertencia", "El campo 'Edad' debe ser un número.")
        return

    try:
        response = requests.post(f"{API_URL}/autores/", json={
            "nombre": nombre,
            "nacionalidad": nacionalidad,
            "edad": int(edad)
        })
        response.raise_for_status()
        messagebox.showinfo("Éxito", "Autor registrado con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"Error al registrar autor: {e}")

def enviar_datos_libro(titulo, genero, paginas, año):
    if not titulo and not genero and not paginas and not año:
        messagebox.showwarning("Advertencia", "Todos los campos del libro están vacíos.")
        return
    if not titulo:
        messagebox.showwarning("Advertencia", "El campo 'Título' no puede estar vacío.")
        return
    if not genero:
        messagebox.showwarning("Advertencia", "El campo 'Género' no puede estar vacío.")
        return
    if not paginas:
        messagebox.showwarning("Advertencia", "El campo 'Páginas' no puede estar vacío.")
        return
    if not paginas.isdigit():
        messagebox.showwarning("Advertencia", "El campo 'Páginas' debe ser un número.")
        return
    if not año:
        messagebox.showwarning("Advertencia", "El campo 'Año' no puede estar vacío.")
        return
    if not año.isdigit():
        messagebox.showwarning("Advertencia", "El campo 'Año' debe ser un número.")
        return

    try:
        response = requests.post(f"{API_URL}/libros/", json={
            "titulo": titulo,
            "genero": genero,
            "paginas": int(paginas),
            "anio": int(año)
        })
        response.raise_for_status()
        messagebox.showinfo("Éxito", "Libro registrado con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"Error al registrar libro: {e}")

def obtener_autores():
    try:
        r = requests.get(f"{API_URL}/autores/listar/")
        r.raise_for_status()
        return r.json()
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener autores: {e}")
        return []

def obtener_libros():
    try:
        r = requests.get(f"{API_URL}/libros/listar/")
        r.raise_for_status()
        return r.json()
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener libros: {e}")
        return []

def respaldo_periodico():
    while True:
        autores = obtener_autores()
        libros = obtener_libros()
        try:
            with open("respaldo_autores.txt", "w", encoding="utf-8") as f:
                for a in autores:
                    f.write(
                        f"Nombre: {a['nombre']}\n"
                        f"Nacionalidad: {a['nacionalidad']}\n"
                        f"Edad: {a['edad']}\n\n"
                    )
            with open("respaldo_libros.txt", "w", encoding="utf-8") as f:
                for l in libros:
                    f.write(
                        f"Título: {l['titulo']}\n"
                        f"Género: {l['genero']}\n"
                        f"Páginas: {l['paginas']}\n"
                        f"Año: {l['anio']}\n\n"
                    )
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar respaldo: {e}")
        time.sleep(60)

def crear_interfaz():
    root = tk.Tk()
    root.title("Editorial Andina")

    def validar_numerico(entry, label_error, campo):
        valor = entry.get()
        if not valor:
            entry.config(highlightbackground="red", highlightthickness=2)
            label_error.config(text=f"El campo '{campo}' no puede estar vacío.")
        elif not valor.isdigit():
            entry.config(highlightbackground="red", highlightthickness=2)
            label_error.config(text=f"El campo '{campo}' debe ser numérico.")
        else:
            entry.config(highlightthickness=0)
            label_error.config(text="")

    def validar_campo_vacio(entry, label_error, campo):
        valor = entry.get()
        if not valor:
            entry.config(highlightbackground="red", highlightthickness=2)
            label_error.config(text=f"El campo '{campo}' no puede estar vacío.")
        else:
            entry.config(highlightthickness=0)
            label_error.config(text="")

    # Autor
    tk.Label(root, text="Autores", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)

    tk.Label(root, text="Nombre").grid(row=1, column=0)
    nombre = tk.Entry(root)
    nombre.grid(row=1, column=1)
    nombre_error = tk.Label(root, text="", fg="red", font=("Arial", 8))
    nombre_error.grid(row=2, column=1, sticky="w")

    tk.Label(root, text="Nacionalidad").grid(row=3, column=0)
    nacionalidad = tk.Entry(root)
    nacionalidad.grid(row=3, column=1)
    nacionalidad_error = tk.Label(root, text="", fg="red", font=("Arial", 8))
    nacionalidad_error.grid(row=4, column=1, sticky="w")

    tk.Label(root, text="Edad").grid(row=5, column=0)
    edad = tk.Entry(root)
    edad.grid(row=5, column=1)
    edad_error = tk.Label(root, text="", fg="red", font=("Arial", 8))
    edad_error.grid(row=6, column=1, sticky="w")

    tk.Button(
        root, text="Registrar Autor",
        command=lambda: enviar_datos_autor(nombre.get(), nacionalidad.get(), edad.get())
    ).grid(row=7, column=0, columnspan=2, pady=5)

    # Libro
    tk.Label(root, text="Libros", font=("Arial", 14)).grid(row=8, column=0, columnspan=2)

    tk.Label(root, text="Título").grid(row=9, column=0)
    titulo = tk.Entry(root)
    titulo.grid(row=9, column=1)
    titulo_error = tk.Label(root, text="", fg="red", font=("Arial", 8))
    titulo_error.grid(row=10, column=1, sticky="w")

    tk.Label(root, text="Género").grid(row=11, column=0)
    genero = tk.Entry(root)
    genero.grid(row=11, column=1)
    genero_error = tk.Label(root, text="", fg="red", font=("Arial", 8))
    genero_error.grid(row=12, column=1, sticky="w")

    tk.Label(root, text="Páginas").grid(row=13, column=0)
    paginas = tk.Entry(root)
    paginas.grid(row=13, column=1)
    paginas_error = tk.Label(root, text="", fg="red", font=("Arial", 8))
    paginas_error.grid(row=14, column=1, sticky="w")

    tk.Label(root, text="Año").grid(row=15, column=0)
    año = tk.Entry(root)
    año.grid(row=15, column=1)
    año_error = tk.Label(root, text="", fg="red", font=("Arial", 8))
    año_error.grid(row=16, column=1, sticky="w")

    tk.Button(
        root, text="Registrar Libro",
        command=lambda: enviar_datos_libro(titulo.get(), genero.get(), paginas.get(), año.get())
    ).grid(row=17, column=0, columnspan=2, pady=5)

    # Validaciones en tiempo real
    campos_texto = [
        (nombre, nombre_error, "Nombre"),
        (nacionalidad, nacionalidad_error, "Nacionalidad"),
        (titulo, titulo_error, "Título"),
        (genero, genero_error, "Género")
    ]
    campos_numericos = [
        (edad, edad_error, "Edad"),
        (paginas, paginas_error, "Páginas"),
        (año, año_error, "Año")
    ]

    for entry, label, campo in campos_texto:
        entry.bind("<KeyRelease>", lambda e, ent=entry, lab=label, camp=campo: validar_campo_vacio(ent, lab, camp))

    for entry, label, campo in campos_numericos:
        entry.bind("<KeyRelease>", lambda e, ent=entry, lab=label, camp=campo: validar_numerico(ent, lab, camp))

    root.mainloop()

crear_interfaz()
