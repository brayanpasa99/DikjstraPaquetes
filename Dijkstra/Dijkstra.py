INF = float('inf')
RED = [[0, 15, INF, 5, INF, INF, INF],
       [15, 0, 61, INF, 21, INF, INF],
       [INF, 61, 0, 8, INF, INF, INF],
       [5, INF, 8, 0, INF, INF, 7],
       [INF, 21, INF, INF, 0, 17, 34],
       [INF, INF, INF, INF, 17, 0, 82],
       [INF, INF, INF, 7, 34, 82, 0]]

VIS = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False}
VER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
VERTICES = ["A", "B", "C", "D", "E", "F", "G"]

'''RED = [[0, 7, 9, INF, INF, 14],
       [7, 0, 10, 15, INF, INF],
       [9, 10, 0, 11, INF, 2],
       [INF, 15, 11, 0, 6, INF],
       [INF, INF, INF, 6, 0, 9],
       [14, INF, 2, INF, 9, 0]]

VIS = {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False}
VER = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5}
VERTICES = ["1", "2", "3", "4", "5", "6"]'''


class Dijkstra():

    def __init__(self):
        for i in VIS:
            VIS[i] = False
        self.definitivos = []
        self.etiquetas = []
        self.distanciaActual = 0

    def nodoInicial(self, ori, fin):
        print(VIS)
        VIS[ori] = True
        self.definitivos.append(ori)
        for i in range(0, len(RED)):
            if RED[VER[ori]][i] != INF:
                if VIS[VERTICES[i]]:
                    pass
                else:
                    self.etiquetas.append([RED[VER[ori]][i], ori, VERTICES[i]])

        self.Algoritmo(fin)

    def Algoritmo(self, fin):

        if not VIS[fin]:

            menor = min(self.etiquetas)
            self.distanciaActual = menor[0]
            nodoActual = menor[2]

            for i in range(0, len(RED)):
                if RED[VER[nodoActual]][i] != INF:
                    if VIS[VERTICES[i]]:
                        pass
                    else:
                        if nodoActual == VERTICES[i]:
                            pass
                        else:
                            self.etiquetas.append([RED[VER[nodoActual]][i]+self.distanciaActual, nodoActual, VERTICES[i]])

            for i in range(0, len(self.etiquetas)):
                if self.etiquetas[i][0] > self.etiquetas[i][0]+self.distanciaActual:
                    self.etiquetas[i][0] = self.etiquetas[i][0]+self.distanciaActual

            menor = min(self.etiquetas)
            self.etiquetas.remove(menor)
            self.definitivos.append(menor[2])
            VIS[menor[2]] = True

            self.Algoritmo(fin)

        print(self.definitivos)

        for i in range(0, len(self.definitivos)-1):
            if self.definitivos[i] != "BORRAR" and self.definitivos[i+1] != "BORRAR":
                print(self.definitivos[i], self.definitivos[i+1], "DISTANCIA", RED[VER[self.definitivos[i]]][VER[self.definitivos[i+1]]])
                if RED[VER[self.definitivos[i]]][VER[self.definitivos[i+1]]] == INF:
                    self.definitivos[i] = "BORRAR"
                    aux = self.definitivos[i+1]

            print(self.definitivos, "ESTOY  BORRANDO", i)

        #print(self.distanciaActual, self.definitivos)

