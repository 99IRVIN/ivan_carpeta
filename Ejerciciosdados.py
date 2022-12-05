##definir una funcion max() que tome como argumento un array de num y devuelva el mayor del array
# mayor=["hoal","como estas", "hola como estas"] 
# min=max=mayor[0]
# for clase in mayor:
#      if clase < min:
#          min = clase
#      elif clase > max:
#          max = clase
# print("El mínimo es " + str(min))  


##escribir una funcion que almacene en una lista los siguientes precios,
##50,75,46,22,80,65,8, y muestre por pantalla el menor y el mayor de los precios
# precios = [50,75,46,22,80,65,8]
# min = max = precios[0]
# for precios in precios :
#     if precios < min:
#         min = precios
#     elif precios > max:
#         max = precios
# print("el minimo es " + str(min))
# print("el maximo es " + str(max))


##escribir una funcion mas larga () que tome una array de palabras y devuelva la mas larga
let palabras = ['mucho', 'muchomucho', 'muchomuchomucho', 'muchomuchomuchomuchoa'];
let totales  = [];
for(let palabra of palabras) {
    totales.push(palabra.length);
}
    
let maximo = Math.max.apply(null, totales);
    
for (let elemento of palabras) {
    if (elemento.length === maximo) {
        console.log(elemento);
    }
}
##escribir un programa que reciba una cadena de caracter y duelvuelva un diccionario con cada palabra que contiene