import tkinter as tk
from tkinter import filedialog, messagebox

# Función para manejar el clic en el botón de subir archivos
def subir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3;*.wav;*.ogg")])
    if archivo:
        messagebox.showinfo("Archivo seleccionado", f"Has seleccionado: {archivo}")

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de Audio")
root.geometry("900x600")

# Crear una barra de navegación
navbar = tk.Frame(root, bg="#333")
navbar.pack(fill=tk.X)

# Título en la barra de navegación
titulo = tk.Label(navbar, text="CODECRAFT", bg="#333", fg="white", font=("Arial", 16))
titulo.pack(pady=10)

# Botón para subir archivos de audio
boton_subir = tk.Button(root, text="Subir archivo de audio", command=subir_archivo,
bg="#4CAF50", fg="white", font=("Arial", 12), height=8, padx=10, pady=10)
boton_subir.pack(pady=20, padx=10, fill=tk.X)

# Crear un marco para los cuatro botones
botones_frame = tk.Frame(root)
botones_frame.pack(pady=10)

# Crear los cuatro botones
for i in range(4):
    boton = tk.Button(botones_frame, text=f"Botón {i + 1}", bg="#008CBA", fg="white", font=("Arial", 12), padx=10, pady=5)
    boton.grid(row=0, column=i, padx=5)

    # Crear una barra de navegación
navbar2 = tk.Frame(root, bg="#333")
navbar2.pack(fill=tk.X)

# Título en la barra de navegación
titulo2 = tk.Label(navbar2, text="Historial", bg="#333", fg="white", font=("Arial", 16))
titulo2.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
