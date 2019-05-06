INF = float('inf')
RED = [[0, 15, INF, 5, INF, INF, INF],
        [15, 0, 61, INF, 21, INF, INF],
        [INF, 61, 0, 9, INF, INF, INF],
        [5, INF, 8, 0, INF, INF, 7],
        [INF, 21, INF, INF, 0, 17, 34],
        [INF, INF, INF, INF, 17, 0, 82],
        [INF, INF, INF, 7, 34, 82, 0]]
VER = {"A": False, "B": False, "C": False, "D": False, "E": False, "F": False, "G": False}

class Dijkstra():

    def __init__(self, origen, fin, paquetes):
        self.__nodoOrigen = origen
        self.__nodoFin = fin
        self.__subCadenas = paquetes

    def numeros(self):
        for i in range(0, len(VER)):
            print(self.__nodoOrigen, self.__nodoFin)

        for i in range(0, self.__subCadenas):


        self.caminoCorto()

    def caminoCorto(self):
        print(VER[self.__nodoOrigen], VER[self.__nodoFin], RED[0][2])
        VER[self.__nodoOrigen] = True
        RED[0][2] = 5
        print(VER[self.__nodoOrigen], VER[self.__nodoFin], RED[0][2])






