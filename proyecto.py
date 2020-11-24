from modulos.archivos import *
from modulos.imprimir import *
from modulos.pedir_datos import *
from modulos.validaciones import *
from modulos.lista_vacias import *
from modulos.eliminaciones import *
from modulos.ListaTopIngredienteMasPedido import *



# funcion para agregar un ingrediente a el archivo de precios
# retorna 1 si lo creo y 0 si no 
def agregarIngrediente():
    ingre=archivoAlista("Datos/precios.txt")
    imprimirIngredientesCompletos(ingre)
    nombre=str(input("ingrese el nombre del ingrediente  "))
    precio=str(input("ingrese el el precio del ingrediente  "))
    comando=str(input("ingrese el comando del ingrediente  "))
    print("\n"*3)
    if precio.isdigit()==False:
        print("* precio incorrecto ingrediente no agregado *")
        return 0
    if nombre.isalpha()== False:
        print("* Nombre incorrecto ingrediente no agregado *")
        return 0
    if comando.isalpha()== False:
        print("* Comando incorrecto ingrediente no agregado *")
        return 0
    for i in ingre:
        if nombre.upper()==i[0].upper() or comando.upper()==i[2].upper():
            print("* producto no creado ya que tiene datos similares a "+i[0]+" "+i[2]+" *")
            return 0
    ingresarIngredienteArchivo(nombre, precio, comando)
    print("***   Creado Exitosamente   ***")
    return 1

# Funcion para login, retorna 1 si el login fue exitoso y 0 si no
def login():
    print("**    Login    **")
    usuario=str(input("ingresa tu nombre de usuario  "))
    contrasena=str(input("ingresa tu contraseña  "))
    usuarios=archivoAlista("Datos/usuarios.txt")
    for i in usuarios:
        if usuario==i[0] and contrasena==i[1]:
            return 1
    return 0

def procesar_ingreso_tipo_sandwich():
  while 1==1:
               tipoSandwich=ingresarTipoSandwich()#varible que guarda el tipo de Sandwich
               validadr=validarDatos(['t','d','i'],tipoSandwich)# Se validad que la opcion elgida sea valida
               if validadr==1:
                  print('=> Debe seleccionar el tamaño correcto!!')
               else:
                 break
  return(tipoSandwich)

def procesar_ingreso_tipo_ingrediente(Ingredientes):
            lisCodigosingredientes=codigosIngredientes()# Se obtiene una lista con los codigos que identifican cada ingrediente
            lisCodigosingredientes.append('todo')# Se agrega el codigo de todo a la lita de codigo de los ingredientes
            listaIngredientesIngresados=[]#list que contendra todos los codigos de los ingredientes ingrsados por el cliente
            conTodo=0# Esta variable se usa para saber si el ciente  quiere todos los ingrdentes en su sandwich

            """ En este ciclo es donde se procesa el ingreso del tipo de ingrediente """
            while 1==1:

              #istaIngredientesIngresados.append(ingresarIngredientes())
              tipoIngrediente=ingresarIngredientes()# Se almacena el codigo del tipo de ingrediente seleccionado por el usuario en la varible tipoIngrediente
              validadr=validarDatos(lisCodigosingredientes, tipoIngrediente) #Se validan los datos

              listaIngredientesIngresados.append(tipoIngrediente) # Se agrega el codigo del ingrediente ingresado a una list
              """   El siguiente if es para finalizar el ingreso de ingredientes ya sea que el usurio desidiera finalizar
              el proceso indicando '' o indicando que quiere todos los ingredientes """
              if  listaIngredientesIngresados[len(listaIngredientesIngresados)-1]=='' or listaIngredientesIngresados[len(listaIngredientesIngresados)-1]=='todo':
                   if listaIngredientesIngresados[len(listaIngredientesIngresados)-1]=='todo':
                     conTodo=1
                     listaIngredientesIngresados.append(Ingredientes)
                   listaIngredientesIngresados.pop()
                   listaIngredientesIngresados=eliminarFalsosIngrediente( lisCodigosingredientes,listaIngredientesIngresados)
                   break
              elif validadr==1:
                    print('Elija una opcion valida')
            return listaIngredientesIngresados,conTodo

def imprimir_sandwich(tipo,todo,listing,ing ):
    lista=[]
    ini,resp,nombre="con","",""
    k=0
    if tipo=="t":
        nombre="Triple"
    elif tipo=="d":
        nombre="Doble"
    elif tipo=="i":
        nombre="Individual"

    for i in listing:
        for j in ing:
            if i==j[2] or i=="todo":
                lista.append(j[0])

    for t in lista:
        if k==0:
            resp=ini+" "+t
        k=k+1
        if k==1 and k==len(lista):
            break
        elif k>1 and k!= len(lista):
            resp=resp+", "+t
        elif k>1 and k==len(lista):
             resp=resp+" y "+t


    if todo ==0:
        print("Usted seleccionó un sándwich",nombre,resp)
    else:
        print("Usted seleccionó un sándwich",nombre,"con todo")


# Funcion para el menu administrativo de agregar ingrediente
def menuAdministrador():
    print("\n"*3)
    veces=0
    acceso=0
    while veces<3:
        
        acceso=login()

        if acceso==1:
            print("\n"*3)
            agregarIngrediente()
            break
        else:
            print("\n"*3)
            veces= veces+1
            if veces < 3:
                print("Datos incorrectos, tienes  "+ str(3- veces)+" intentos")
            
    


def procesar_ingreso_opcion_top():
  while 1==1:
               respuesta=str(input('Ingrese opcion: '))
               validadr=validarDatos(['s','n'],respuesta)# Se validad que la opcion elgida sea valida
               if validadr==1:
                  print('Elija una opcion valida')
               else:
                 break
  return(respuesta)



def procesar_salir_opcion_top():

  while 1==1:
               respuesta=str(input('Presione enter para salir: '))
               validadr=validarDatos([''],respuesta)# Se validad que la opcion elgida sea valida
               if validadr==1:
                  print('Error presione enter para salir')
               else:
                 break
  return(respuesta)

if __name__=="__main__":

    while(1==1):
        imprimirMenuAdministrador()
        respuesta=str(input("indique la opcion que prefiera  "))

        if respuesta=="1":
            menuAdministrador()
        elif respuesta=="2":
            break
        else:
            print("\n"*3)
            print("** Marque una opcion correcta **")
    




    imprimirOpcionTop()
    respuesta=procesar_ingreso_opcion_top()
    if respuesta=='s':
        inicicarTopIngredienteMasPedido(codigosIngredientes())
        procesar_salir_opcion_top()

    ans='s'
    cont, precio= 0, 0
    imprimirLogo()
    while ans.lower()=='s':
            cont+=1
            imprimirNumeroSandwich(cont)#Se imprime por pantalla el numero del sandwich que esta siendo pedido
            imprimirPanes()
            tipoSandwich=procesar_ingreso_tipo_sandwich()#Se obtiene el tipo de sandwich
            Ingredientes=archivoAlista("Datos/precios.txt")# Se consulta y se guarda los ingredientes leido en el archivo txt
            imprimirIngredientes(Ingredientes)# se imprimen por pantalla los ingredientes almacenado en el archivo txt
            """Se obtiene la lista de los codigos de los ingredientes seleccionados por el cliente
            y si es el caso tambien se obtiene una variable que nos permite saber
            si el cliente selecciono todos los ingredientes """
            listaIngredientesIngresados,conTodo=procesar_ingreso_tipo_ingrediente(Ingredientes)
            imprimir_sandwich(tipoSandwich,conTodo,listaIngredientesIngresados,Ingredientes )# Se imprime en pantalla el Sandwich creado junto con sus ingredientes si los tiene
            subtotal= imprimir_precio(tipoSandwich,Ingredientes,listaIngredientesIngresados,conTodo)
            precio+= subtotal
            guardarCompra(tipoSandwich,subtotal,listaIngredientesIngresados)
            ans= input('¿Desea continuar [s/n]?: ')

    print("El pedido tiene un total de", cont, "sándwich(es) por un monto de:",precio)
    guardarTotal(precio)
    print("Gracias por su compra, regrese pronto")
