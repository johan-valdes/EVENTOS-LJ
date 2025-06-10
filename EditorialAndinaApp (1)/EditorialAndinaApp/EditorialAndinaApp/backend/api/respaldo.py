import time
import requests

API_URL = "http://127.0.0.1:8000/api"

def respaldo_periodico():
    print("Respaldo automático iniciado desde Django.")
    while True:
        try:
            autores = requests.get(f"{API_URL}/autores/listar/").json()
            libros = requests.get(f"{API_URL}/libros/listar/").json()

            with open("respaldo_autores.txt", "w", encoding="utf-8") as f:
                for a in autores:
                    f.write(f"Nombre: {a['nombre']}\nNacionalidad: {a['nacionalidad']}\nEdad: {a['edad']}\n\n")

            with open("respaldo_libros.txt", "w", encoding="utf-8") as f:
                for l in libros:
                    f.write(f"Título: {l['titulo']}\nGénero: {l['genero']}\nPáginas: {l['paginas']}\nAño: {l['anio']}\n\n")

        except Exception as e:
            print(f"[ERROR] Respaldo fallido: {e}")
        
        time.sleep(60)  # Esperar 60 segundos entre respaldos
