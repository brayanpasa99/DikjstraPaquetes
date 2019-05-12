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


class Dijkstra():
    etiquetas = []
    definitivos = []

    def __init__(self):
        pass

    def Algoritmo(self, ori, fin, distancia, paso):

        while paso < 3:

            for i in range(0, len(RED)):
                if RED[VER[ori]][i] != INF:
                    if VIS[VERTICES[i]]:
                        pass
                    else:
                        self.etiquetas.append([RED[VER[ori]][i]+distancia, ori, VERTICES[i]])

            menor = min(self.etiquetas)

            print(ori, "NODO ORIGEN", menor[2], "OTRO NODO")
            print("Relacion: ", RED[VER[ori]][VER[menor[2]]])

            if (RED[VER[ori]][VER[menor[2]]] == INF):
                pass


            print(menor)
            print(self.etiquetas)

            distancia += menor[0]
            VIS[menor[2]] = True

            self.definitivos.append(menor[2])

            print(self.definitivos)

            veces = 0
            for i in range(0, len(self.etiquetas)):
                if self.etiquetas[i] == menor:
                    borrar = self.etiquetas[i]
                    veces += 1

            for i in range(0, veces):
                self.etiquetas.remove(borrar)

            paso += 1

            menora = menor

            self.Algoritmo(menor[2], fin, distancia, paso)
