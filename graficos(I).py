from tkinter import*
raiz = Tk()
raiz.title("Hola Mundo")
raiz.config(bg="blue") #color de fondo
raiz.config(cursor='pirate') #cambia el cursor
raiz.config(bd=55) #borde del frame
raiz.config(relief="groove") #tipo de borde

miFrame = Frame() #creamos un frame, hay que meterlo en la raiz
miFrame.pack(side='top',anchor='center') #para que este empaquetado/ side(right,left,top,bottom) / anchor(n,s,e,w,center)
miFrame.config(bg="red") #color de fondo, hay que darle tamaño al frame para que se vea
miFrame.config(width="700", height="400") #tamaño del frame(fijo)
miFrame.config(bd=35) #borde del frame
miFrame.config(relief="sunken") #tipo de borde
miFrame.config(cursor="hand2") #cambia el cursor

#sintaxis para crear un label
miLabel = Label(miFrame, text="German te quiero") #creamos un label, hay que meterlo en el frame
miLabel.pack() #para que este empaquetado
miLabel.config(bg="green") #color de fondo
miLabel.config(fg="white") #color de letra
miLabel.config(font=("Comic Sans MS",18)) #tipo de letra y tamaño
miLabel.config(bd=10) #borde del label
miLabel.config(relief="groove") #tipo de borde
miLabel.config(cursor="pirate") #cambia el cursor
miLabel.place(x=190,y=150) #para que se coloque en una posicion especifica

cuadroTexto = Entry(miLabel) #creamos un cuadro de texto, hay que meterlo en el frame
cuadroTexto.pack() #para que este empaquetado
cuadroTexto.config(justify="center") #para que el texto este centrado
cuadroTexto.config(state="normal") #para que no se pueda escribir
cuadroTexto.config(cursor="arrow") #cambia el cursor
cuadroTexto.place(x=100,y=100) #para que se coloque en una posicion especifica

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.place(x=80,y=80)


raiz.mainloop() #para que pueda estar en ejecucion

