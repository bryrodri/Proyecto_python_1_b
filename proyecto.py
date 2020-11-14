from modulos.archivos import *
from modulos.imprimir import * 
from modulos.pedir_datos import *
from modulos.validaciones import *
from modulos.lista_vacias import *
from modulos.eliminaciones import *



def compraSW(ingredientes):
    SWtotales=1
    condi="s"

    while condi=="s" :
        imprimirLogo()
        print("Sandwich número "+  str(SWtotales))
        imprimirPanes()


        condi=input("¿Desea continuar [s/n]?: ")

def agregarIngrediente():
    ingre=archivoAlista("Datos/precios.txt")
    print(ingre)
    nombre=str(input("ingrese el nombre del ingrediente"))
    precio=str(input("ingrese el el precio del ingrediente"))
    comando=str(input("ingrese el comando del ingrediente"))
    if precio.isdigit()==False:
        print("* precio incorrecto *")
        return 0
    for i in ingre:
        if nombre.upper()==i[0].upper() or comando.upper()==i[2].upper():
            print("* producto no creado ya que tiene datos similares a "+i[0]+" "+i[2]+" *")
            return 0
    ingresarIngredienteArchivo(nombre, precio, comando)
    return 1

def login():
    usuario=str(input("ingresa tu nombre de usuario"))
    contrasena=str(input("ingresa tu nombre de usuario"))
    usuarios=archivoAlista("Datos/usuarios.txt")
    for i in usuarios:
        if usuario==i[0] and contrasena==i[1]:
            return 1
    return 0

if __name__=="__main__":

            imprimirLogo()
            imprimirPanes()
            while 1==1:
               tipoSandwich=ingresarTipoSandwich()
               validadr=validarDatos(['t','d','i'],tipoSandwich)
               if validadr==1:
                  print('Elija una opcion valida')
               else:
                 break 
    

            Ingredientes=archivoAlista("Datos/precios.txt")
            imprimirIngredientes(Ingredientes)
            lisCodigosingredientes=codigosIngredientes()
            listaIngredientesIngresados=[]
          
            while 1==1:
              
              #istaIngredientesIngresados.append(ingresarIngredientes())
              tipoIngrediente=ingresarIngredientes()
              validadr=validarDatos(lisCodigosingredientes, tipoIngrediente) 
           
              listaIngredientesIngresados.append(tipoIngrediente)         
                
              if  listaIngredientesIngresados[len(listaIngredientesIngresados)-1]=='' :
                   listaIngredientesIngresados.pop()
                   listaIngredientesIngresados=eliminarFalsosIngrediente( lisCodigosingredientes,listaIngredientesIngresados)
                   print(listaIngredientesIngresados)
                   break
              elif validadr==1:
                    print('Elija una opcion valida')

            if tipoSandwich=='t':
               if is_empty(listaIngredientesIngresados)==True:
                   print("Usted seleccionó un sándwich Triple solo")
               else:
                 print("Usted seleccionó un sándwich Triple con los sigueinetes ingredientes :")
                 for i  in listaIngredientesIngresados:
                    devolverIngredienteApartirDeCodigo(i)
            elif tipoSandwich=='d':
               if is_empty(listaIngredientesIngresados)==True:
                   print("Usted seleccionó un sándwich Doble solo")
               else:

                print("Usted seleccionó un sándwich Doble con los sigueinetes ingredientes :")
                for i  in listaIngredientesIngresados:
                  devolverIngredienteApartirDeCodigo(i)
            elif tipoSandwich=='i':
                  if is_empty(listaIngredientesIngresados)==True:
                    print("Usted seleccionó un sándwich individual solo")
                  else:
                    print("Usted seleccionó un sándwich Individual con los sigueinetes ingredientes :")
                    for i  in listaIngredientesIngresados:
                      devolverIngredienteApartirDeCodigo(i)
                      

         
                 

                    
                                      
                       

          
    