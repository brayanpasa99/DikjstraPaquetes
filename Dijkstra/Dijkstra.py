import math

INF = float('inf')
RED = [[0, 15, INF, 5, INF, INF, INF],
        [15, 0, 61, INF, 21, INF, INF],
        [INF, 61, 0, 9, INF, INF, INF],
        [5, INF, 8, 0, INF, INF, 7],
        [INF, 21, INF, INF, 0, 17, 34],
        [INF, INF, INF, INF, 17, 0, 82],
        [INF, INF, INF, 7, 34, 82, 0]]

class Dijkstra():

    def __init__(self):
        pass

    def numeros(self):
        for i in range(0, len(RED)):
            for j in range(0, len(RED)):
                print (RED[i][j])


