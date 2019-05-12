import copy

INF = float('inf')
RED =   [[INF, 15 , INF, 5  , INF, INF, INF],
        [15  , INF, 61 , INF, 21 , INF, INF],
        [INF , 61 , INF, 8  , INF, INF, INF],
        [5   , INF, 8  , INF, INF, INF, 7  ],
        [INF , 21 , INF, INF, INF, 17 , 34 ],
        [INF , INF, INF, INF, 17 , INF, 82 ],
        [INF , INF, INF, 7  , 34 , 82 , INF]]

RED_ORI =   [[INF, 15 , INF, 5  , INF, INF, INF],
        [15  , INF, 61 , INF, 21 , INF, INF],
        [INF , 61 , INF, 8  , INF, INF, INF],
        [5   , INF, 8  , INF, INF, INF, 7  ],
        [INF , 21 , INF, INF, INF, 17 , 34 ],
        [INF , INF, INF, INF, 17 , INF, 82 ],
        [INF , INF, INF, 7  , 34 , 82 , INF]]

VERTICES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
VIS = {"A": False, "B": False, "C": False, "D": False, "E": False, "F": False, "G": False}

class Dijkstra():

    def __init__(self, origen, fin, paquetes):
        self.__nodoOrigen = origen
        self.__nodoFin = fin
        self.__subCadenas = paquetes

    def envio(self, origen, fin, paquetes):

        posicionOrigen = self.buscarLetra(VERTICES, origen)
        posicionDestino = self.buscarLetra(VERTICES, fin)

        print ''
        print 'Posicion del Computador de origen en la Matriz de Adyacencia:', posicionOrigen
        print 'Posicion del Computador de destino en la Matriz de Adyacencia:', posicionDestino

        self.__nodos = []

        for i in range(0, len(self.__subCadenas)):
            self.__nodos.append(VIS)

        for i in range(0, len(self.__subCadenas)):

            if (posicionOrigen == posicionDestino):
                print ''
                print 'El nodo origen es igual al nodo destino...'
            else:
                print ''
                print 'Envio de la subcadena:', self.__subCadenas[i]
                self.caminoCorto(posicionOrigen, posicionDestino)


    def caminoCorto(self, nodoOrigen, nodoFin):

        valAcomulado = 0
        visitados = []
        visitadosPr = []

        ponderado = [nodoOrigen,valAcomulado]

        print ''
        print 'Algoritmo de Dijkstra...'
        print 'Envio de nodo', VERTICES[nodoOrigen], 'a', VERTICES[nodoFin]
        print ''
        while (nodoOrigen is not nodoFin):

            ponderado = [nodoOrigen, valAcomulado]
            ponderadoPr = [VERTICES[nodoOrigen], valAcomulado]
            print'Ponderado:', ponderadoPr

            visitados.append(nodoOrigen)
            visitadosPr.append(VERTICES[nodoOrigen])
            print 'Nodos visitados:', visitadosPr

            minAdy = min(RED[nodoOrigen])
            print 'Valor minimo adyacente:', minAdy

            nodoSiguiente = self.buscar(RED[nodoOrigen], minAdy)
            nodoSiguientePr = VERTICES[nodoSiguiente]
            print 'Siguiente nodo:', nodoSiguientePr

            print 'Es nodo anterior igual a siguiente...' , nodoSiguientePr, '=', VERTICES[nodoOrigen]

            k = self.buscarAnterior(visitados,nodoSiguiente)
            print 'Numero de veces de visita al nodo siguiente:', k

            if k>0:
                print ''
                print 'El nodo siguiente ya fue visitado ', k, 'veces'
                print 'Nodo actual:', VERTICES[nodoOrigen]
                print 'Nodo anterior:', VERTICES[nodoAnterior]

                print 'Nodo siguiente:', nodoSiguiente
                print 'Nodo anterior:',nodoAnterior

                valAux = RED[nodoOrigen][nodoSiguiente]
                valAuxi = RED[nodoOrigen][nodoAnterior]

                print 'Fila:', RED[nodoOrigen]

                RED[nodoOrigen][nodoAnterior] = INF
                RED[nodoOrigen][nodoSiguiente] = INF

                print 'Nueva fila:', RED[nodoOrigen]

                minAdy = min(RED[nodoOrigen])
                RED[nodoOrigen][nodoSiguiente] = valAux
                RED[nodoOrigen][nodoAnterior] = valAuxi
                print 'Nuevo valor minimo adyacente:', minAdy
                nodoSiguiente = self.buscar(RED[nodoOrigen], minAdy)
                nodoSiguientePr = VERTICES[nodoSiguiente]
                print 'Siguiente nodo:', nodoSiguientePr
                print ''

            if self.buscarVisitados(visitados,nodoSiguiente):
                print 'El nodo ya se ha visitado antes...'
                valAux = RED[nodoOrigen][nodoSiguiente]
                valAuxi = RED[nodoOrigen][nodoAnterior]

                RED[nodoOrigen][nodoSiguiente] = INF
                RED[nodoOrigen][nodoAnterior] = INF

                minAdy = min(RED[nodoOrigen])

                if minAdy == INF:
                    print 'Todos los vertices adyacentes han sido visitados...'
                    print 'Reestableciendo la fila:', nodoOrigen
                    RED[nodoOrigen] = RED_ORI[nodoOrigen][:]

                    minAdy = min(RED[nodoOrigen])
                    print 'Nuevo valor minimo adyacente:', minAdy


                RED[nodoOrigen][nodoSiguiente] = valAux
                RED[nodoOrigen][nodoAnterior] = valAuxi
                print 'Fila de la red: ', RED[nodoOrigen]

                nodoSiguiente = self.buscar(RED[nodoOrigen], minAdy)

                nodoSiguientePr = VERTICES[nodoSiguiente]
                print 'Siguiente nodo:', nodoSiguientePr
                print ''


            valAcomulado = valAcomulado + minAdy

            ponderado = [nodoSiguiente, valAcomulado]
            ponderadoPr = [VERTICES[nodoSiguiente], valAcomulado]
            print 'Nuevo ponderado:', ponderadoPr

            nodoAnterior = nodoOrigen
            nodoOrigen = nodoSiguiente
            print 'Nuevo nodo origen:', VERTICES[nodoOrigen]

            print("")

        print 'Nodo destino alcanzado...'
        print 'Ponderado: ', ponderadoPr
        print 'Nodos visitados para llegar...', visitadosPr


    def buscar(self, lista, val):
        for i in range(len(lista)):
            if lista[i] == val:
                return i

    def buscarAnterior(self, lista, val):
        j = 0
        for i in range(len(lista)):
            if lista[i] == val:
                j = j + 1
        return j

    def buscarLetra(self, lista, val):
        for i in range(len(lista)):
            if lista[i] == val:
                return i

    def buscarVisitados(self, lista, val):
        for i in range(len(lista)):
            if lista[i] == val:
                return True












