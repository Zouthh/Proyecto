import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time


def cargar_imagen(imagen_label, boton_volver, boton_frame, imagen_path):
    boton_volver.config(state=tk.DISABLED)
    boton_volver.update()

    # Ocultar los botones
    boton_frame.pack_forget()

    imagen_label.config(text="Buscando...")
    imagen_label.update()

    time.sleep(1.5)  # Retardo de 5 segundos (simulación de carga)

    try:
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((300, 300))  # Ajusta el tamaño de la imagen según tus necesidades

        imagen_tk = ImageTk.PhotoImage(imagen)
        imagen_label.config(image=imagen_tk)
        imagen_label.image = imagen_tk

        imagen_label.config(text="")
        boton_volver.config(state=tk.NORMAL)
        boton_volver.pack()

    except IOError:
        imagen_label.config(text="Error al cargar la imagen")


def quitar_imagen(imagen_label, boton_volver, boton_frame):
    imagen_label.config(image="")
    imagen_label.config(text="Presiona un Objeto para buscar")

    # Mostrar los botones nuevamente
    boton_frame.pack()
    boton_volver.pack_forget()


def mostrar_creditos():
    ventana_creditos = tk.Toplevel()
    ventana_creditos.title("Créditos")

    # Contenido de los créditos
    creditos_texto = "Antonio Basto: Programador\n\nVictor Romero: Prototipo\n\nFabela Bedolla: Materiales\n\nBrandon Mora: Ideas/Tester"

    creditos_label = ttk.Label(ventana_creditos, text=creditos_texto)
    creditos_label.pack(padx=20, pady=20)


def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Buscador de Objetos")

    # Estilo de la interfaz
    estilo = ttk.Style()
    estilo.configure('TButton', font=('Arial', 12), padding=5)
    estilo.configure('TLabel', font=('Arial', 14))

    imagen_label = ttk.Label(ventana, text="Qué objeto quieres buscar?")
    imagen_label.pack(pady=20)

    boton_frame = ttk.Frame(ventana)
    boton_frame.pack()

    boton1 = ttk.Button(boton_frame, text="Lápiz", command=lambda: cargar_imagen(imagen_label, boton_volver, boton_frame, "imagen1.jpeg"))
    boton1.grid(row=0, column=0, padx=10)

    boton2 = ttk.Button(boton_frame, text="Pluma", command=lambda: cargar_imagen(imagen_label, boton_volver, boton_frame, "imagen2.jpeg"))
    boton2.grid(row=0, column=1, padx=10)

    boton3 = ttk.Button(boton_frame, text="Celular", command=lambda: cargar_imagen(imagen_label, boton_volver, boton_frame, "imagen3.jpeg"))
    boton3.grid(row=0, column=2, padx=10)

    boton_creditos = ttk.Button(boton_frame, text="Créditos", command=mostrar_creditos)
    boton_creditos.grid(row=1, column=0, columnspan=3, pady=10)

    boton_volver = ttk.Button(ventana, text="Volver", state=tk.DISABLED, command=lambda: quitar_imagen(imagen_label, boton_volver, boton_frame))
    boton_volver.pack(pady=20)

    ventana.mainloop()


if __name__ == '__main__':
    crear_interfaz()
