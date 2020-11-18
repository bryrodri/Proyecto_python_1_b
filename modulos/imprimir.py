

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
    print('Todo           (todo)')

def imprimirCodigos(lista):
    pantalla="codigos"
    print(pantalla)

    for i in lista:
        print (i)

def imprimirNumeroSandwich(numeroSandwich):
    print(f'Sandwich número {numeroSandwich}')


def imprimir_precio(tipo,ing,listing,todo):
    ini,resp,nombre="con","",""
    valor_ing,total_ing,precio=0,0,0
    if tipo=="t":
        precio=580
        nombre="Triple"
    elif tipo=="d":
        precio=430
        nombre="Doble"
    elif tipo=="i":
        precio=280
        nombre="Individual"

    for i in listing:
        for j in ing:
            if i==j[2] or i=="todo":
                valor_ing=j[1]
                valor_ing=float(valor_ing)
                total_ing=total_ing + valor_ing


    print("Subtotal a pagar por un sándwich",nombre,":",precio+total_ing)
    return precio+total_ing
