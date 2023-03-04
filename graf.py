import tkinter as tk

root = tk.Tk()
root.title("Tiempo de Limpieza")

# Variables
Habitacion = 500 * 630 # cm^2
velocidad = 1800 # cm^2/min

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
    dibujar_habitacion_y_mueble(p, h)

# Botón para calcular el tiempo de limpieza
calculate_button = tk.Button(root, text="Calcular Tiempo", command=calculate_time)
calculate_button.pack()

# Etiqueta para mostrar el tiempo de limpieza
time_label = tk.Label(root, textvariable=tiempo)
time_label.pack()

# Canvas para dibujar la habitación y el mueble
canvas = tk.Canvas(root, width=600, height=700)
canvas.pack()

def dibujar_habitacion_y_mueble(p, h):
    canvas.delete("all") # Elimina todo lo dibujado en el canvas
    canvas.create_rectangle(50, 50, 550, 650, fill="light blue") # Dibuja la habitación
    canvas.create_rectangle(100, 500, 100+p, 500-h, fill="brown") # Dibuja el mueble

root.mainloop()
