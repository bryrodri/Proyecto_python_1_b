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
    

            Ingredientes=archivoAlista()
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
                      

         
                 

                    
                                      
                       

          
    