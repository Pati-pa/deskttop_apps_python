# Se importa la libreria de tkinter con todas sus funciones
from tkinter import *

#------------------------------
#funciones de la appp
#------------------------------

#------------------------------
#Ventana principal
#------------------------------

#Se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un obtjeto Tk()
ventana_principal = Tk()

#titulo de la ventana 
ventana_principal.title("Hola bro")

#Tamaño de la ventana
ventana_principal.geometry("500x500")

# Quitar boton de maximizar
ventana_principal.resizable(0,0)

ventana_principal.config(bg="cyan")

#-----------------------
#Agregar frame
#---------------------------
mi_frame = Frame(ventana_principal)
mi_frame.place(x=0, y=0)
mi_frame.config(bg="yellow")
mi_frame.config(width="500", height="250")

mi_frame = Frame(ventana_principal)
mi_frame.place(x=0, y=250)
mi_frame.config(bg="blue")
mi_frame.config(width="500", height="125")

frame_resultados= Frame(ventana_principal)
frame_resultados.config(bg="red", width=500, height=125)
frame_resultados.place(x=0, y=375)


#run
#se ejecuuta kla funcion (metodo) mainloop() de la clase Tk() a través de la instancia ventana_principal. 
#  Este metodo despliega una ventana simple en pantala y queda a la espera de lo que el usuario haga. 
# Cada acción del usuario se conoce copmo evento. El mainloop() en un bucle infinito
ventana_principal.mainloop()