import tkinter as tk

root = tk.Tk()
root.title("Tiempo de Limpieza")

# Variables
Habitacion = 500 * 630 # cm^2
velocidad = 800 # cm^2/min

# Variables de entrada
altura = tk.StringVar()
ancho = tk.StringVar()
tiempo = tk.StringVar()

# Etiquetas y cuadros de texto para la altura y el ancho
altura_label = tk.Label(root, text="Altura:")
altura_label.pack()
altura_entry = tk.Entry(root, textvariable=altura)
altura_entry.pack()

ancho_label = tk.Label(root, text="Ancho:")
ancho_label.pack()
ancho_entry = tk.Entry(root, textvariable=ancho)
ancho_entry.pack()

# Función para calcular el tiempo de limpieza
def calculate_time():
    h = int(altura.get())
    p = int(ancho.get())
    area = p * h
    limpiar = Habitacion - area
    tiempo_limpieza = limpiar / velocidad
    tiempo.set("{:.2f} minutos".format(tiempo_limpieza))

# Botón para calcular el tiempo de limpieza
calculate_button = tk.Button(root, text="Calcular Tiempo", command=calculate_time)
calculate_button.pack()

# Etiqueta para mostrar el tiempo de limpieza
time_label = tk.Label(root, textvariable=tiempo)
time_label.pack()

root.mainloop()





