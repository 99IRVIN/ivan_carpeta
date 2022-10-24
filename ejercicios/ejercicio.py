## pedir un texto, contando las vocales que existe en ls textos.
# oracion=input('ingrese su oracion: ')
# vocales=['a','e','i','o','u']
# contadorvocales=0
# for letras in oracion:
#     if letras in vocales:
#         contadorvocales+=1
# print('la cantidad de vocales es: ', contadorvocales)

sentence=input('ingresa una oracion: ')
countvocals=0
for words in sentence:
    match words:
        case 'a':
            countvocals+=1
        case 'e':
            countvocals+=1
        case 'i':
            countvocals+=1
        case 'o':
            countvocals+=1
        case 'u':
            countvocals+=1
print('la cantidad de vocales es: ', countvocals)