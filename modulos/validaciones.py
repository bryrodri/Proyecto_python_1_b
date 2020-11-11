def validarDatos(datosCorrectos,datoIngresado):
      correcto=0

      for i in datosCorrectos:
       

        if i == datoIngresado:
            break
      else:
          correcto=1

      return correcto

