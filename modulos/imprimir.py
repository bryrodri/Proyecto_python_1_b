

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

def imprimirIngredientes(lista):
    pantalla="ingredientes"
    print(pantalla)
    espacio=0
    for i in lista:
        print(i[0], end="")
        espacio=15-len(i[0])
        print(" "*espacio, end="")
        print("("+i[2]+")")
    #print("Indique ingrediente (enter para terminar): ")

def imprimirCodigos(lista):
    pantalla="codigos"
    print(pantalla)
   
    for i in lista:
        print (i)
   