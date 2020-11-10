


def archivoAlista():
    f=open("Datos/precios.txt", "r")
    ListaPrecios=[]
    Lista=[]
    ingrediente=[]
    for i in f:
        Lista=i.splitlines()
        ingrediente=Lista[0].split(",")
        ListaPrecios.append(ingrediente)

    f.close() 
    return ListaPrecios