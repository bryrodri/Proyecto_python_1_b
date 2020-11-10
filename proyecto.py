

def imprimirPanes():
    pantalla="""
    Opciones:
    Tamaños: Triple ( t ) Doble ( d ) Individual ( i ): """
    print(pantalla)

def imprimirLogo():
    pantalla="""
    **************************
    *    SANDWICHES UCAB     *
    **************************
    """
    print(pantalla)

def compraSW():
    SWtotales=1
    condi="s"

    while condi=="s" :
        imprimirLogo()
        print("Sandwich número "+  str(SWtotales))
        imprimirPanes()


        condi=input("¿Desea continuar [s/n]?: ")



if __name__=="__main__":
    compraSW()