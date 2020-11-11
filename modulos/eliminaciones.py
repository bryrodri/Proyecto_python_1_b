def eliminarFalsosIngrediente(listaCodigos,listaDudosa):
   listaNueva=[]
   for i in listaDudosa:
       for j in listaCodigos:
           if i==j:
              listaNueva.append(i)
   return listaNueva
       