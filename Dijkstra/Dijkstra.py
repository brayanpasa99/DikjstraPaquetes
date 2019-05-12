INF = float('inf')
'''RED =   [[0, 15 , INF, 5  , INF, INF, INF],
        [15  , 0, 61 , INF, 21 , INF, INF],
        [INF , 61 , 0, 8  , INF, INF, INF],
        [5   , INF, 8  , 0, INF, INF, 7  ],
        [INF , 21 , INF, INF, 0, 17 , 34 ],
        [INF , INF, INF, INF, 17 , 0, 82 ],
        [INF , INF, INF, 7  , 34 , 82 , 0]]'''

RED = [[INF, 15, INF, 5, INF, INF, INF],
       [15, INF, 61, INF, 21, INF, INF],
       [INF, 61, INF, 8, INF, INF, INF],
       [5, INF, 8, INF, INF, INF, 7],
       [INF, 21, INF, INF, INF, 17, 34],
       [INF, INF, INF, INF, 17, INF, 82],
       [INF, INF, INF, 7, 34, 82, INF]]

VIS = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False}
VER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
VERTICES = ["A", "B", "C", "D", "E", "F", "G"]


class Dijkstra():
    etiquetas = []
    definitivos = []
    l = 0

    def __init__(self):
        pass

    def primerPaso(self, ori, fin):
        self.definitivos.append(ori)
        VIS[ori] = True

        self.Algoritmo(ori, fin, 0, 0)

    def Algoritmo(self, ori, fin, distancia, paso):

        while(paso < 3):

            for i in range(0, len(RED)):
                if RED[VER[ori]][i] != INF:
                    if VIS[VERTICES[i]]:
                        pass
                    else:
                        self.etiquetas.append([RED[VER[ori]][i]+distancia, VERTICES[i]])

            menor = min(self.etiquetas)

            distancia += menor[0]
            VIS[menor[1]] = True

            self.definitivos.append(menor[1])

            for i in range(0, len(self.etiquetas)):
                if self.etiquetas[i] == menor:
                    borrar = i

            self.etiquetas.pop(borrar)






            print (VIS)
            print self.definitivos

            paso += 1
            print(self.etiquetas)
            print(distancia)
            self.Algoritmo(min(self.etiquetas)[1], fin, distancia, paso)


