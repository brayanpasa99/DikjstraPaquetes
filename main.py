import threading
from Dijkstra.Dijkstra import Dijkstra
from Paquetes.Paquetes import Paquetes


def main():
    ori = raw_input("Ingrese el computador de origen: ")
    fin = raw_input("Ingrese el computador de destino: ")



    if ori.isalpha() and fin.isalpha() and not ori.isdigit() and not fin.isdigit() and ori.isupper() and fin.isupper():

        listaHilos = []
        subCadenas = Paquetes().capturaPaquete()
        for i in range(0, len(subCadenas)):

            hilo = threading.Thread(target=Dijkstra().nodoInicial(ori, fin), name='hilo%s' %i)
            listaHilos.append(hilo)
            print("ENVIANDO PAQUETE: ", subCadenas[i], "NOMBRE HILO: ", hilo.name)
            hilo.start()

    else:

        print("Los computadores son nombrados con letras de la A a la F")

if __name__ == "__main__":
    main()
