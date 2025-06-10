import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "http://127.0.0.1:8000/api"

def enviar_datos_autor(nombre, nacionalidad, edad):
    if not nombre or not nacionalidad or not edad:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")
        return
    if not edad.isdigit():
        messagebox.showwarning("Advertencia", "Edad debe ser un número.")
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
    if not titulo or not genero or not paginas or not año:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")
        return
    if not paginas.isdigit() or not año.isdigit():
        messagebox.showwarning("Advertencia", "Páginas y Año deben ser números.")
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

def crear_interfaz():
    root = tk.Tk()
    root.title("📘 Editorial Andina")
    root.geometry("550x500")
    root.configure(bg="#e6f0ff")

    # No permitir redimensionar ventana
    root.resizable(False, False)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TNotebook", background="#e6f0ff", borderwidth=0)
    style.configure("TNotebook.Tab", background="#dbeafe", foreground="#0a2540", font=('Segoe UI', 11, 'bold'), padding=10)
    style.map("TNotebook.Tab", background=[("selected", "#ffffff")])
    style.configure("TButton", background="#1e3a8a", foreground="white", font=('Segoe UI', 10, 'bold'))
    style.map("TButton", background=[('active', '#3b82f6')], foreground=[('active', 'white')])

    notebook = ttk.Notebook(root)
    notebook.pack(pady=15, expand=True, fill="both")

    frame_autor = tk.Frame(notebook, bg="white", bd=1, relief="solid")
    frame_libro = tk.Frame(notebook, bg="white", bd=1, relief="solid")

    notebook.add(frame_autor, text="Autores")
    notebook.add(frame_libro, text="Libros")

    def crear_campo(frame, label_text, tipo="texto"):
        container = tk.Frame(frame, bg="white")
        label = tk.Label(container, text=label_text, bg="white", fg="#0a2540", font=("Segoe UI", 10))
        entry = tk.Entry(container, font=("Segoe UI", 10), bg="#f0f4ff", fg="#0a2540", relief="flat",
                         highlightthickness=1, highlightbackground="#1e3a8a")
        error_label = tk.Label(container, text="", fg="red", bg="white", font=("Segoe UI", 8))

        def validar(event):
            valor = entry.get()
            if tipo == "numero":
                if valor and not valor.isdigit():
                    error_label.config(text="Solo se permiten números")
                else:
                    error_label.config(text="")
            elif tipo == "texto":
                if valor and not valor.replace(" ", "").isalpha():
                    error_label.config(text="Solo se permiten letras")
                else:
                    error_label.config(text="")
            else:  # tipo libre (como título)
                error_label.config(text="")

        entry.bind("<KeyRelease>", validar)

        label.pack(anchor="w")
        entry.pack(fill="x")
        error_label.pack(anchor="w")

        container.pack(padx=20, pady=5, fill="x")
        return entry

    # --- AUTOR ---
    tk.Label(frame_autor, text="Registrar Autor", bg="white", fg="#0a2540", font=("Segoe UI", 13, "bold")).pack(pady=10)

    nombre = crear_campo(frame_autor, "Nombre:", tipo="texto")
    nacionalidad = crear_campo(frame_autor, "Nacionalidad:", tipo="texto")
    edad = crear_campo(frame_autor, "Edad:", tipo="numero")

    ttk.Button(
        frame_autor, text="Registrar Autor",
        command=lambda: enviar_datos_autor(nombre.get(), nacionalidad.get(), edad.get())
    ).pack(pady=20)

    # --- LIBRO ---
    tk.Label(frame_libro, text="Registrar Libro", bg="white", fg="#0a2540", font=("Segoe UI", 13, "bold")).pack(pady=10)

    titulo = crear_campo(frame_libro, "Título:", tipo="libre")  # ← Título sin restricciones
    genero = crear_campo(frame_libro, "Género:", tipo="texto")
    paginas = crear_campo(frame_libro, "Páginas:", tipo="numero")
    año = crear_campo(frame_libro, "Año:", tipo="numero")

    ttk.Button(
        frame_libro, text="Registrar Libro",
        command=lambda: enviar_datos_libro(titulo.get(), genero.get(), paginas.get(), año.get())
    ).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    crear_interfaz()
