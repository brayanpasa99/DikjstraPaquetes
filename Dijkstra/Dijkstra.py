INF = float('inf')
RED = [[INF, 15, INF, 5, INF, INF, INF],
        [15, INF, 61, INF, 21, INF, INF],
        [INF, 61, INF, 9, INF, INF, INF],
        [5, INF, 8, INF, INF, INF, 7],
        [INF, 21, INF, INF, INF, 17, 34],
        [INF, INF, INF, INF, 17, INF, 82],
        [INF, INF, INF, 7, 34, 82, INF]]
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

            self.caminoCorto(0)


    def caminoCorto(self, nodo):

        min(RED[nodo])
        for i in range()













