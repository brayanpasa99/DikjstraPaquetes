class Paquetes():

    def __init__(self):
        pass

    def capturaPaquete(self):
        cadena = raw_input("Ingrese la cadena que desea enviar: ")
        subCadenas = []

        for i in range(0, len(cadena)):
            subCadenas.append(cadena[i])


        return subCadenas




