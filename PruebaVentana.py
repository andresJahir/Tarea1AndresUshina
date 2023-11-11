import tkinter as tk

# Función que se ejecuta cuando se hace clic en el botón
def mostrar_texto():
    texto = cuadro_texto.get()  # Obtener el texto del cuadro de texto
    etiqueta.config(text=texto)  # Actualizar la etiqueta con el texto

# Crear una instancia de la clase Tk
ventana = tk.Tk()
ventana.title("Ejemplo de Botón y Cuadro de Texto")
ventana.geometry("400x200")

# Etiqueta
etiqueta = tk.Label(ventana, text="Texto a mostrar aquí")
etiqueta.pack(pady=10)

# Cuadro de Texto
cuadro_texto = tk.Entry(ventana)
cuadro_texto.pack()

# Botón
boton_mostrar = tk.Button(ventana, text="Mostrar Texto", command=mostrar_texto)
boton_mostrar.pack(pady=10)

# Mostrar la ventana
ventana.mainloop()