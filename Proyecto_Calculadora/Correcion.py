mensajeopciones="""
====================
selecciona una opcion
  1)suma
  2)resta
  3)division
  4)multiplicacion 
  5)salir
====================
"""

while true:
    print(mensajeopciones)
    opcion=input('ingresa una opcion validad entre (1-5): ')
    numeroUno=int(input('ingresa el primer numero'))
    numeroDos=int(input('ingresa el segundo numero'))
    match opcion:
        case '1':
            print(f'la suma de (numeroUno)+(numeroDos)=(numeroUno+numeroDos)')
        case '2':
            print(f'la suma de (numeroUno)-(numeroDos)=(numeroUno-numeroDos)')
        case '3':
            print(f'la division de (numeroUno)/(numeroDos)=(numeroUno/numeroDos)')
        case '4':
            print(f'la multiplicacion de (numeroUno)*(numeroDos)=(numeroUno*numeroDos)')
        case '5':
            break
        case _:
            print('esta opcion no existe')