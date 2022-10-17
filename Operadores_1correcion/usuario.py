##tendremos una variable con el mensaje hola mundo
##pedir al usuario un texto
##si el texto ingresado es hola
##mostrara el mensaje completo
##si el ingresado es como estas
##mostrara el mensaje la palabra hola
##si el texto ingresado es saludos
##extraeras del mensaje la palabra mundo
##si se ingrersa otro texto
##mostraras por defecto el mensaje de error

mensaje='hola mundo'
texto=input('ingrese un texto: ')
match texto:
 case 'hola':
  print(mensaje[:])
 case 'como estas':
  print(mensaje[:4])
 case 'saludos':
  print(mensaje[5:])
 case _:
  print(error )