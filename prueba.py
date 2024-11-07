import tkinter as tk
from tkinter import filedialog, messagebox, Frame

# Función para subir archivos de audio
def subir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3;*.wav;*.ogg")])
    if archivo:
        messagebox.showinfo("Archivo seleccionado", f"Has seleccionado: {archivo}")

# Funciones específicas para cada botón adicional
def boton_accion_1():
    messagebox.showinfo("Botón pulsado", "Has pulsado el botón 1")

def boton_accion_2():
    messagebox.showinfo("Botón pulsado", "Has pulsado el botón 2")

def boton_accion_3():
    messagebox.showinfo("Botón pulsado", "Has pulsado el botón 3")

def boton_accion_4():
    messagebox.showinfo("Botón pulsado", "Has pulsado el botón 4")

# Funciones para cada tarjeta Otras Opciones
def funcion_tarjeta_1():
    messagebox.showinfo("Función de Tarjeta", "Función de la Tarjeta 1 ejecutada")

def funcion_tarjeta_2():
    messagebox.showinfo("Función de Tarjeta", "Función de la Tarjeta 2 ejecutada")

def funcion_tarjeta_3():
    messagebox.showinfo("Función de Tarjeta", "Función de la Tarjeta 3 ejecutada")

def funcion_tarjeta_4():
    messagebox.showinfo("Función de Tarjeta", "Función de la Tarjeta 4 ejecutada")


# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de Audio")
root.geometry("900x600")

# Sección 1: Tarjeta con botón para subir archivos
seccion1 = Frame(root, pady=20)
seccion1.pack(pady=10)

tarjeta1 = Frame(seccion1, bd=1, relief=tk.SUNKEN, padx=10, pady=10, background='#5DBFD2')
tarjeta1.pack(pady=10)

# Etiqueta y botón para subir archivo
etiqueta_titulo1 = tk.Label(tarjeta1, text="Creador de Historial Medico", font=("Arial", 26), bg="#5DBFD2", fg="white")
etiqueta_titulo1.pack()

boton_subir = tk.Button(tarjeta1, text="Subir archivo de audio", command=subir_archivo)
boton_subir.pack(pady=10)

# Cuatro botones adicionales, cada uno con su propio comando
botones_frame = Frame(seccion1)
botones_frame.pack(pady=10)

# Crear cada botón como una variable individual
boton1 = tk.Button(botones_frame, text="Botón 1", command=boton_accion_1)
boton1.grid(row=0, column=0, padx=5)

boton2 = tk.Button(botones_frame, text="Botón 2", command=boton_accion_2)
boton2.grid(row=0, column=1, padx=5)

boton3 = tk.Button(botones_frame, text="Botón 3", command=boton_accion_3)
boton3.grid(row=0, column=2, padx=5)

boton4 = tk.Button(botones_frame, text="Botón 4", command=boton_accion_4)
boton4.grid(row=0, column=3, padx=5)

# Sección 2: Tarjeta con 4 tarjetas dentro y funciones editables
seccion2 = Frame(root, pady=20)
seccion2.pack(pady=10)

tarjeta2 = Frame(seccion2, bd=1, relief=tk.SUNKEN, padx=10, pady=10)
tarjeta2.pack(pady=10)

etiqueta_titulo2 = tk.Label(tarjeta2, text="Otras Opciones", font=("Arial", 14))
etiqueta_titulo2.pack()

# Información de cada tarjeta: nombre y función asociada
tarjetas_info = [
    {"nombre": "Tarjeta 1", "funcion": funcion_tarjeta_1},
    {"nombre": "Tarjeta 2", "funcion": funcion_tarjeta_2},
    {"nombre": "Tarjeta 3", "funcion": funcion_tarjeta_3},
    {"nombre": "Tarjeta 4", "funcion": funcion_tarjeta_4}
]

# Crear las 4 tarjetas dentro de tarjeta2 con nombres y funciones editables
for info in tarjetas_info:
    tarjeta_interna = Frame(tarjeta2, bd=1, relief=tk.RAISED, padx=10, pady=10)
    tarjeta_interna.pack(side=tk.LEFT, padx=5, pady=5)

    etiqueta_titulo_interna = tk.Label(tarjeta_interna, text=info["nombre"], font=("Arial", 12))
    etiqueta_titulo_interna.pack()

    etiqueta_contenido = tk.Label(tarjeta_interna, text="Contenido de la tarjeta", font=("Arial", 10))
    etiqueta_contenido.pack()

    boton_accion_tarjeta = tk.Button(tarjeta_interna, text="Ejecutar", command=info["funcion"])
    boton_accion_tarjeta.pack(pady=5)


# Ejecutar la aplicación
root.mainloop()
