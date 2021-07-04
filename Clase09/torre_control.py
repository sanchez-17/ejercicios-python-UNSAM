# -*- coding: utf-8 -*-

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
    def __str__(self):
        return self.items

class  TorreDeControl:
    '''Crea una torre de control con arribos y despegues'''
    
    def __init__(self):
        '''Se generan dos objetos tipo cola para los arribos y despegues'''
        self.partidas = Cola()
        self.arribos = Cola()
    
    def nuevo_arribo(self, vuelo):
        self.arribos.encolar(vuelo)
    
    def nueva_partida(self, vuelo):
        self.partidas.encolar(vuelo)
    
    def asignar_pista(self):
        '''Procesa los arribos y despegues, los arribos tienen prioridad
        si no hay vuelos que procesar lo notifica'''
        
        if not self.arribos.esta_vacia():
            print( f'El vuelo {self.arribos.desencolar()} aterrizó con éxito' )
        
        elif not self.partidas.esta_vacia():
            print( f'El vuelo {self.partidas.desencolar()} despegó con éxito' )
        
        else:
            print('No hay vuelos en espera.')
            
    def ver_estado(self):
        print(f'Vuelos esperando para aterrizar: ', end='')
        for i in self.arribos.items:
            print(i)
        print()
        print(f'Vuelos esperando para despegar:', end='')
        for i in self.partidas.items:
            print(i)
        print()
        
#%%
torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
