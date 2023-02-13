from tkinter import*
import turtle


raiz = Tk()
raiz.geometry('500x630')
raiz.title("ROOMBA")
raiz.config(bg="blue") #color de fondo
raiz.config(cursor='pirate') #cambia el cursor
raiz.config(bd=55) #borde del frame


miFrameROJO = Frame() #creamos un frame, hay que meterlo en la raiz
miFrameROJO.pack(side='top',anchor='ne') #para que este empaquetado/ side(right,left,top,bottom) / anchor(n,s,e,w,center)
miFrameROJO.config(bg="brown") #color de fondo, hay que darle tamaño al frame para que se vea
miFrameROJO.config(width="250", height="150") #tamaño del frame(fijo)
miFrameROJO.config(bd=35) #borde del frame
miFrameROJO.config(cursor="hand2") #cambia el cursor







raiz.mainloop() #para que pueda estar en ejecucion

