

# Funcion para convertir un archivo a lista
# recibe una ubicacion de archivo 
# retorna una lista con formato [[valor,valor,valor,valor],[valor,valor,valor,valor]]
def archivoAlista(ubicacion):
    f=open(ubicacion, "r")
    ListaPrecios=[]
    Lista=[]
    ingrediente=[]
    for i in f:
        Lista=i.splitlines()
        ingrediente=Lista[0].split(",")
        ListaPrecios.append(ingrediente)

    f.close()
    return ListaPrecios

# Funcion para agregar un ingrediente al archivo precios.txt
# recibe 3 strings
def ingresarIngredienteArchivo(nombre, precio, comando):
    f=open("Datos/precios.txt", "a")
    f.write("\n"+nombre+","+precio+","+comando)
    f.close






def codigosIngredientes():
    f=open("Datos/precios.txt", "r")
    ListaCodigos=[]
    Lista=[]
    ingrediente=[]
    for i in f:
        Lista=i.splitlines()
        ingrediente=Lista[0].split(",")
        ListaCodigos.append(ingrediente[2])

    f.close()
    return ListaCodigos


def devolverIngredienteApartirDeCodigo(codigo):
    f=open("Datos/precios.txt", "r")
    ListaPrecios=[]
    Lista=[]
    ingrediente=[]
    for i in f:
        Lista=i.splitlines()
        ingrediente=Lista[0].split(",")
        if ingrediente[2]==codigo:
              print( ingrediente[0])
              break

    f.close()
    return ListaPrecios


def guardarCompra(tipo, precio, ingredientes):
    f=open("Datos/historial.txt", "a")
    f.write("\n"+tipo+","+str(ingredientes)+","+str(precio))
    f.close()

def guardarTotal(total):
    f=open("Datos/historial.txt", "a")
    f.write("\n"+str(total)+"\n")
    f.close()
