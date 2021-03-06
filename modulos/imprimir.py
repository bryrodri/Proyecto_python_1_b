
# Funcion para imprimir Panes
def imprimirPanes():
    pantalla="""
Opciones:"""
    print(pantalla)

# Funcion para imprimir Logo
def imprimirLogo():
    pantalla="""
    **************************
    *    SANDWICHES UCAB     *
    **************************
    """
    print(pantalla)

def imprimirIngredientes(lista):
    pantalla="Ingredientes:"
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


# Funcion para imprimir el menu inicial
def imprimirMenuAdministrador():
    mensaje="""
         Menu
    1.Agregar Ingrediente
    2.Pedir Sandwiches

    """
    print(mensaje)



# Funcion para imprimir nombre de ingrediente, precio y comando
# recibe una lista de formato [[nombre,precio,comando],[nombre,precio,comando]]
def imprimirIngredientesCompletos(lista):
    print("**   Ingredientes Disponibles Actualmente    **")
    contador=1
    for i in lista:
        print(str(contador)+ ". "+ i[0]+" "+i[1]+" "+ i[2])
        contador=contador+1
