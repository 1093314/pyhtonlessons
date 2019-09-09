# -*- coding: utf-8 -*-
def main():
    resp = ""
    lista= ["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4", "Opcion 5"]

    while (resp<>'N'):
        for opcion in lista:
            print ('> '+opcion)
        seleccion = int(input("Cual opcion desea?"))

        if (seleccion == 1):
            print ("Usted ha elegido excelente!")
        elif (seleccion == 2):
            print ("Usted puede cambiar su selección")
        elif (seleccion == 3):
            print ("Usted no ha elegido correctamente")
        else:
            print ("Vuelva a intentarlo")

        resp=raw_input("Desea continuar? (S/N) ")

main()
