
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
    

