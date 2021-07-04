# -*- coding: utf-8 -*-


class Canguro:
 def __init__(self, contenido_marsupio):
self.contenido_marsupio = contenido_marsupio
   
    def meter_en_marsupio(self, item):
        self.contenido_marsupio.append(item)

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + self.__str__(obj)
            t.append(s)
        return '\n'.join(t)
#%%
m = Canguro([])
m.meter_en_marsupio('5')
m.contenido_marsupio
#%%
class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=None):
    #def __init__(self, nombre, contenido=[]): Aqui hay un error, al definirse la clase se crea una lista a la que van a hacer referencia todas las instancias creadas por igual
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + obj.__str__()
            #s = '    ' + self.__str__(obj) error al imprimir
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objeto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)