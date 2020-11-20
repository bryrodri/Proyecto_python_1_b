
import os

def is_empty(data_structure):
    if data_structure:
        #print("No está vacía")
        return False
    else:
        #print("Está vacía")
        return True
def limpiar(ListaDudosa,codigosIngredientes):
    listaIngredientesDefinitiva=[]
    for i in ListaDudosa:
    
        miniLista = i.split(',')
        for j in  miniLista:
        
            for k in codigosIngredientes:
                if k==j:
                    listaIngredientesDefinitiva.append(j)

  
    return(listaIngredientesDefinitiva)

def sumarIngredientes(listaIngredientesDefinitiva,listaCodigos):
    listaSuma=[]
    suma=0
    for i in listaCodigos:
        for j in listaIngredientesDefinitiva:
            if i==j:
                suma=suma+1
        listaSuma.append(i+'*'+str(suma))
        suma=0

 
   
    return(listaSuma)

def obtenerIngredienteMasPedido(sumaOrdenada,codigos):

    mayor=0
    i=0
    vacia=0
    valorAEliminar=""
   
    ingredienteMayor =""
    if is_empty(sumaOrdenada)== True:
        vacia=1
    else:
        while i < len(sumaOrdenada):
         miniSuma = sumaOrdenada[i].split('*')
         a=miniSuma[1]
         a=int(a)
    
         if a>=mayor:
              mayor= a
              if a!=0:                  
              
                 ingredienteMayor =miniSuma[0]
                 valorAEliminar=sumaOrdenada[i]

              

         i=i+1
  

    return(valorAEliminar,vacia)
          
    
    
         
   
def eliminarIngredienteMasPedido(Ingrediente,listaSumada):
  
       listaSumada.remove(Ingrediente)

       return(listaSumada)

def revisarQueSoloQuedenCeros(suma):
    sumacero=0
    for i in suma:
        miniSuma = i.split('*')
        sumacero=sumacero+int(miniSuma[1])
    return(sumacero)


def generarListaOrdenada(suma):

    listaordenada=[]
    ingredienteAEliminar=''
    vacia=""


    while 1==1:
        if revisarQueSoloQuedenCeros(suma)!=0:
           ingredienteAEliminar,vacia=obtenerIngredienteMasPedido(suma,['ja','ch','pi','dq','ac','pp','sa','todo'])
           listaordenada.append(ingredienteAEliminar)
           suma=eliminarIngredienteMasPedido(ingredienteAEliminar,suma)
        else:
            break
    return(listaordenada)

def DevolverNombreIngrediente(codigo):
    f = open ('Datos/Precios.txt','r')
    lineas = f.readlines()
   
    i = 0
    while i < len(lineas):       
        a=lineas[i]
   
        linea = a.split(',')
        if codigo==linea[2].rstrip('\n'):
              
             return(linea[0])
        i += 1

def imprimirTopIngredientes(listaOrdenada):
    contador=1
    print('Acontinuaciòn se muestra una lista desde Ingrediente mas pedido al menos pedido :')
    for i in listaOrdenada:
        listaResumida=i.split('*')
        ingredieteAImprimir=DevolverNombreIngrediente(listaResumida[0])
        if  ingredieteAImprimir!=None:

          print(f'{contador}  {ingredieteAImprimir}')
          contador=contador+1

def verificarSiSoloHaySanwichConTodo(listaSumada):
   todo=0
   for i in listaSumada:
       a=i.split('*')
       if a[0]!='todo' and int(a[1])>0:
           
           break
   else:
        todo=1
   return todo # se rotorna 0 si hay algun ingrediente adicional en la lista 
                #y se retorna 1 si en la lista solo hay sanwich que tienen todos sus ingredintes



def leerYGuadarHistorialDeVentas():
    # archivo-entrada.py
    f = open ('Datos/historial.txt','r')
    lineas = f.readlines()
    listaIngredientes=[]
    i = 0
    while i < len(lineas):
        # lineas[i].remove('[')
        # lineas[i].remove('[')
        a=lineas[i]
        a=a.replace('[',"")
        a=a.replace(']',"")
        a=a.replace("'","")
        a=a.replace(" ","")
        a=a.strip()
    

        listaIngredientes.append(a)

        i += 1
    f.close()
    return(listaIngredientes)
       


    

def inicicarTopIngredienteMasPedido(listaCodigos):
     if os.stat("Datos/historial.txt").st_size != 0:
         
         listaIngredientesDudosa= leerYGuadarHistorialDeVentas()
         listaIngredientesDefinitiva=limpiar(listaIngredientesDudosa,listaCodigos)
        #  print(f' lista de ingredientes leida {listaIngredientesDefinitiva}')
         if  is_empty(listaIngredientesDefinitiva)==False:

             listaIngredientesSumada=sumarIngredientes(listaIngredientesDefinitiva,listaCodigos)
            #  print(f'Lista de ingredientes sumado {listaIngredientesSumada}')
             if  verificarSiSoloHaySanwichConTodo(listaIngredientesSumada)==0:                   

                     listaOrdenada=generarListaOrdenada(listaIngredientesSumada)
                    #  print(f'Esta es la lista ordenada del top :{listaOrdenada}')
                     imprimirTopIngredientes(listaOrdenada)
             else:
                    print('Hasta ahora solo se registrados sanwiches con todos los ingredientes por lo que no hay un top')
        
         else:
             print('Hasta ahora solo se han regitrados sandwiches si ingredientes adicionales')
     else:
         print('No hay sandwich Registrados')

def imprimirOpcionTop():
    pantalla="""
    Desea ver nuestro Top de Ingredientes:
    Si ( s ) No ( n ) : """
    print(pantalla)





        
      
   









