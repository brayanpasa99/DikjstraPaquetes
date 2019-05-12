import math

from Dijkstra.Dijkstra import Dijkstra
from Paquetes.Paquetes import Paquetes


def main():
    ori = raw_input("Ingrese el computador de origen: ")
    fin = raw_input("Ingrese el computador de destino: ")

    if ori.isalpha() and fin.isalpha() and not ori.isdigit() and not fin.isdigit() and ori.isupper() and fin.isupper():

        subCadenas = Paquetes().capturaPaquete()
        Dijkstra().Algoritmo(ori, fin, 0, 0)

    else:

        print("Los computadores son nombrados con letras de la A a la F")

if __name__ == "__main__":
    main()
