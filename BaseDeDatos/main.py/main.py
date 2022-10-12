password='73505233'
for intentos in range(1,4):
 print('este es tu',intentos,'intento')
 newPassword=input('ingresa el password correcto:')
 if newPassword==password:
  print('bienvenido al sistema joven')
  break
else:
  print('password incorrecto sigue intentando gil')

