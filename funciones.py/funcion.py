##OperacionMatematica(4,5,'suma')
##por consola la suma de 4+5
#1. utilizar la palabra reservada def
#2. asignamos un nombre a la funcion--descriptivo
#3. siempre toene que recibir parametros
 #()-- no sirve parametros
 #(nombre)-- que la funcion esta recibiendo el parametro
 #(edad,nombre)
#4. siempre la funcion tiene que retornar un tipo de dato

def saludo(nombre):
    respuesta=f'hola como estas{nombre}'
    return respuesta

#como uso
##dato='jose'
##print(saludo('diego'))

##print(saludo('wiskisiqui'))

##arrayAmigos=['ronald no fuimos a tu cumple', 'claudio no estas en el proyecto']
##print(saludo(arrayAmigos[0], end=arrayAmigos[1]))


ArrayAmigos=[' ronald',' claudio',' diego',' jose',' mozetar',' kevin',' lilian']
for amigo in range(0,len(ArrayAmigos)):
    print(saludo(ArrayAmigos[amigo]))
