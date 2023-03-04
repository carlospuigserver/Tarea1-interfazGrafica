# Primera tarea empleando tkinter

El link al repositorio es el siguiente: https://github.com/carlospuigserver/Tarea1-interfazGrafica.git

Miembros del grupo:
- Carlos Puigserver
- Germán Llorente

Este código utiliza la biblioteca Tkinter para crear una interfaz gráfica de usuario (GUI) en la que se puede calcular el tiempo de limpieza de una habitación después de haberse ingresado un mueble. La habitación se representa gráficamente en un canvas(aplicación de tkinter) y se dibuja un mueble en ella con la altura y el ancho ingresados por el usuario. La velocidad de limpieza es una constante predeterminada elegida por nosotros al igual que las medidas de la habitación, que constan en el enunciado del ejercicio, y el cálculo del tiempo de limpieza se realiza en función del área que queda por limpiar al haber establecido un mueble. Cuando se hace clic en el botón "Calcular tiempo", se muestra el tiempo de limpieza en una etiqueta y se dibuja la habitación y el mueble en el canvas.


# Código en el que nos hemos basado para interpretar que hacer con la interfaz gráfica:

```
Habitacion=500*630
velocidad=800 #cm2/min
    


h =int(input('Escriba la altura del mueble: '))
p = int(input('Escriba el ancho del mueble: '))
    

area=p*h
print('El area del mueble es: ', area)

limpiar=Habitacion-area
print('El area que se puede limpiar es: ', limpiar)
tiempo=limpiar/velocidad
print('El tiempo que se tarda en limpiar es: ', tiempo)
 ```
 
 
 
 # Código del programa con tkinter:
 
 ```
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

```
