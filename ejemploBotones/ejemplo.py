# Author: Cristian Steib
#
#
# -*- encoding: utf-8 -*-

import pilasengine
from botones import *

pilas = pilasengine.iniciar(alto=640,ancho=800)

'''
 Vamos a llamar "comando" a los botones que tengan una instruccion.

 Definicion de las clases

 BotonComando
 ----------------
 +boton             -> retorna el actor boton de pilas.
 +botonDuplicado    -> retorna la instancia de la clase BotonArrastrable
 +comando           -> retorna o setea el valor del comando para ese boton.
 +posicionOk()      -> Crea un nuevo boton arrastable.


 BotonArrastrable      *** No es necesario usarla.. BotonComando() hace uso de esta.
 ----------------
 +boton             -> retorna el actor boton de pilas.


*** IMPORTANTE  = Enviar pilas como argumento al contructor de la clase BotonComando. Ej: mirar en el script.

'''

lista_de_comandos=[] # son los botones.. cada boton tiene asociado un boton duplicado
                     # para poder ser arrastrado.




def evento_click(evento):
    #TODO: cuando un boton esta en la posicion correcta ir guardando la secuenci y los actores! para poder moverlos en cualquier momento y eliminarlos-

    # chequeamos si alguno de los botones estan en la posicion siguiente valida
    # de alguna lista, que tenga las coordenas.. y de ahi saco la siguiente posicion habilitada
    for boton in lista_de_comandos:
        # adicionalmente podriamos ver si el actor se arrastro fuera del marco del juego y volverlo para un extremo
        if abs(boton.boton_duplicado.boton.x) > 300:  # suponga que 300 es el limite de la pantalla de  x
            boton.boton_duplicado.boton.x = 100
        if boton.boton_duplicado.boton.x>150:   # vamos a tomar como valido a los botones que este por valores mayores a 150 en X
            boton.posicionOk() # si la posicion esta bien, entonces le avisamos a la clase que ya puede duplicar ese "comando"
            print "Crear boton arrastable para  -> "+ boton.comando


#cada vez que se haga un click, y se termine de soltar, se va a ejecutar esta funcion
pilas.evento.termina_click.conectar(evento_click)





#Se crean los botones, y le asignamos un comando
a=BotonComando(pilas=pilas,x=0,y=200,comando='arriba')
b=BotonComando(pilas,x=0,y=150)
b.comando='abajo'
c=BotonComando(pilas,x=0,y=100,comando='derecha')
d=BotonComando(pilas,x=0,y=50)
d.comando='izquierda'




lista_de_comandos=[a,b,c,d] # cargamos los "comandos" en la lista






pilas.ejecutar()
