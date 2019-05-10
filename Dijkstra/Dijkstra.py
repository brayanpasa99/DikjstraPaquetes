INF = float('inf')
RED = [[INF, 15, INF, 5, INF, INF, INF],
        [15, INF, 61, INF, 21, INF, INF],
        [INF, 61, INF, 9, INF, INF, INF],
        [5, INF, 8, INF, INF, INF, 9],
        [INF, 21, INF, INF, INF, 17, 34],
        [INF, INF, INF, INF, 17, INF, 82],
        [INF, INF, INF, 9, 34, 82, INF]]
VER = {"A": False, "B": False, "C": False, "D": False, "E": False, "F": False, "G": False}

class Dijkstra():

    def __init__(self, origen, fin, paquetes):
        self.__nodoOrigen = origen
        self.__nodoFin = fin
        self.__subCadenas = paquetes

    def envio(self):

        self.__nodos = []

        for i in range(0, len(self.__subCadenas)):
            self.__nodos.append(VER)

        for i in range(0, len(self.__subCadenas)):
            self.caminoCorto(0, 1)
            '''self.caminoCorto(self.__nodoOrigen, self.__nodoFin, 0)'''
            '''Transformar letras a numeros'''

        ''''temporizador todos pasan por la misma ruta'''


    def caminoCorto(self, nodoOrigen, nodoFin):

        valAcomulado = 0
        visitados = []

        ponderado = [nodoOrigen,valAcomulado]

        while (nodoOrigen is not nodoFin):
            ponderado = [nodoOrigen, valAcomulado]
            print("Ciclo...")
            print("Ponderado:")
            print(ponderado)

            visitados.append(nodoOrigen)
            print("Nodos visitados:")
            print(visitados)

            minAdy = min(RED[nodoOrigen])
            print("Minimo adyacente: ")
            print(minAdy)

            nodoSiguiente = self.buscar(RED[nodoOrigen], minAdy)
            print("Siguiente nodo: ")
            print(nodoSiguiente)

            print(nodoSiguiente,"=", nodoOrigen)

            k = self.buscarAnterior(visitados,nodoSiguiente)
            print(k)

            if k>0:
                print("Nodo origen: ", nodoOrigen)
                print("Nodo anterior: ", nodoAnterior)
                RED[nodoOrigen][nodoAnterior] = INF
                minAdy = min(RED[nodoOrigen])
                print("Minimo ady nuevo: ", minAdy)
                print("If")
                nodoSiguiente = self.buscar(RED[nodoOrigen], minAdy)
                print("Siguiente nodo: ")
                print(nodoSiguiente)

            valAcomulado = valAcomulado + minAdy
            ponderado = [nodoSiguiente, valAcomulado]
            print("Nuevo ponderado: ")
            print(ponderado)
            nodoAnterior = nodoOrigen
            nodoOrigen = nodoSiguiente
            print("Nodo origen: ",nodoOrigen)


            print("")





        '''print("Ponderado:")
        print(ponderado)

        minAdy = min(RED[nodoOrigen])
        print("Minimo: ")
        print(minAdy)

        posicionMin = self.buscar(RED[nodoOrigen],minAdy)
        print("Valor en la posicion: ")
        print(posicionMin)

        valAcomulado = valAcomulado + minAdy
        ponderado = [posicionMin,valAcomulado]
        print("Nuevo ponderado: ")
        print(ponderado)'''

        '''print(min(RED[nodoOrigen]))

        for i in range(1):
            pass'''

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













