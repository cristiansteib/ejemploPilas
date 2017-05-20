# Author: Cristian Steib
#
#
# -*- encoding: utf-8 -*-

import pilasengine
class consoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class BotonComando():
    '''
    Representa cada boton para una instruccion determinada

    '''

    def __init__(self,*args,**kwargs):
        self.pilas = args[0] if (len(args) and type(args[0]) is pilasengine.Pilas)else kwargs['pilas'] if kwargs.get(
               'pilas', None) else None
        if self.pilas == None:
            print (consoleColors.FAIL + "Te olvidaste de enviar pilas como parametro?? " + consoleColors.ENDC)
            print (
            consoleColors.OKGREEN + self.__class__.__name__ + "(pilas=pilas) o " + self.__class__.__name__ + "(pilas=pilas)" + consoleColors.ENDC)
            exit(1)
        self.boton=self.pilas.actores.Boton(x=kwargs.get('x',0),y=kwargs.get('y',0))
        self.comando=kwargs.get('comando','')
        self.boton_duplicado = BotonArrastrable(self.pilas,x=kwargs.get('x',0),y=kwargs.get('y',0),comando=self.comando)



    def get_comando(self):
        return self.comando


    def duplicar_boton(self):
        ''' se duplica el boton, para que el boton duplicado sea el
        que se puede arrastrar'''
        self.boton_duplicado=BotonArrastrable(self.pilas,comando=self.comando)
        self.boton_duplicado.boton.y=self.boton.y
        self.boton_duplicado.boton.x=self.boton.x

    def posicionOk(self):
        ''' Esta ubicado en una posicion valida dentro del mapa del juego.
        '''
        self.duplicar_boton()



    def get_boton_duplicado(self):
        return self.boton_duplicado

    def get_boton(self):
        return self.boton


    boton = property(get_boton)
    botonDuplicado = property(get_boton_duplicado)
    comando = property(get_comando)




class BotonArrastrable():
    def __init__(self,pilas,x=0,y=0, comando=''):
        self.comando=comando
        self.pilas=pilas
        self.boton_dup=self.pilas.actores.Boton(x,y)
        self.boton_dup.aprender(self.pilas.habilidades.Arrastrable)


    def get_boton(self):
        return self.boton_dup


    def set_comando(self,comando):
        self.comando = comando

    def get_comando(self,comando):
        return comando

    boton = property(get_boton)
    comando = property(get_comando,set_comando)