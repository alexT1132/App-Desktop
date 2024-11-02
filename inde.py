import tkinter as tk
from tkinter import filedialog, messagebox, Frame

# Función para subir archivos de audio
def subir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3;*.wav;*.ogg")])
    if archivo:
        messagebox.showinfo("Archivo seleccionado", f"Has seleccionado: {archivo}")

# Funciones para los botones adicionales
def boton_accion(i):
    messagebox.showinfo("Botón pulsado", f"Has pulsado el botón {i + 1}")

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de Audio")
root.geometry("900x600")

# Sección 1: Tarjeta con botón para subir archivos
seccion1 = Frame(root, pady=20)
seccion1.pack(pady=10)

tarjeta1 = Frame(seccion1, bd=1, relief=tk.SUNKEN, padx=10, pady=10)
tarjeta1.pack(pady=10)

etiqueta_titulo1 = tk.Label(tarjeta1, text="Subir Archivo de Audio", font=("Arial", 14))
etiqueta_titulo1.pack()

boton_subir = tk.Button(tarjeta1, text="Subir archivo de audio", command=subir_archivo)
boton_subir.pack(pady=10)

# Cuatro botones adicionales
botones_frame = Frame(seccion1)
botones_frame.pack(pady=10)

for i in range(4):
    boton = tk.Button(botones_frame, text=f"Botón {i + 1}", command=lambda i=i: boton_accion(i))
    boton.grid(row=0, column=i, padx=5)

# Sección 2: Tarjeta con 4 tarjetas dentro
seccion2 = Frame(root, pady=20)
seccion2.pack(pady=10)

tarjeta2 = Frame(seccion2, bd=1, relief=tk.SUNKEN, padx=10, pady=10)
tarjeta2.pack(pady=10)

etiqueta_titulo2 = tk.Label(tarjeta2, text="Tarjeta con Cuatro Tarjetas", font=("Arial", 14))
etiqueta_titulo2.pack()

# Crear las 4 tarjetas dentro de tarjeta2
for i in range(4):
    tarjeta_interna = Frame(tarjeta2, bd=1, relief=tk.RAISED, padx=10, pady=10)
    tarjeta_interna.pack(side=tk.LEFT, padx=5, pady=5)

    etiqueta_titulo_interna = tk.Label(tarjeta_interna, text=f"Tarjeta {i + 1}", font=("Arial", 12))
    etiqueta_titulo_interna.pack()

    etiqueta_contenido = tk.Label(tarjeta_interna, text="Contenido de la tarjeta", font=("Arial", 10))
    etiqueta_contenido.pack()

# Ejecutar la aplicación
root.mainloop()
