from modulos.archivos import *
from modulos.imprimir import * 



def compraSW(ingredientes):
    SWtotales=1
    condi="s"

    while condi=="s" :
        imprimirLogo()
        print("Sandwich número "+  str(SWtotales))
        imprimirPanes()


        condi=input("¿Desea continuar [s/n]?: ")



if __name__=="__main__":
    Ingredientes=archivoAlista()
    imprimirIngredientes(Ingredientes)
    