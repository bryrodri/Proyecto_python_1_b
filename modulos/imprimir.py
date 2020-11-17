

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
    lista=[]
    valor_ing,total_ing,precio,k=0,0,0,0
    if tipo=="t":
        precio=580
    elif tipo=="d":
        precio=430
    elif tipo=="i":
        precio=280
    
    for i in listing:
        for j in ing:
            if i==j[2] or i=="todo":
                valor_ing=j[1]
                valor_ing=float(valor_ing)
                total_ing=total_ing + valor_ing
                lista.append(j[0])
                k=k+1

    
    if  tipo=="t":
        print("Subtotal a pagar por un sándwich Triple:",precio +total_ing)
    elif  tipo=="d":
        print("Subtotal a pagar por un sándwich Doble:",precio +total_ing)
    elif tipo=="i":
        print("Subtotal a pagar por un sándwich Individual:",precio +total_ing)
    elif  k==len(ing):
        print("Subtotal a pagar por un sándwich con todo:",precio +total_ing)

        


   