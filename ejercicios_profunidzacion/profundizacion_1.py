# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

# Solicito numeros reales para realizar las operaciones de la calculadora
print ('Ingrese primer numero')
numero_1= float(input())
print ('Ingrese segundo numero')
numero_2= float(input())

# Solicito ingresar operacion deseada



print ('Seleccione la operación deseada ingresando la letra correspondiente')
print (" A) Suma \n B) Resta \n C) Multiplicación \n D) División \n E) Exponente/Potencia")
opcion=str(input()).upper()
while  opcion != "A" and  opcion != "B" and  opcion != "C" and  opcion != "D" and  opcion != "E"  :
  print ('Por favor seleccione una opcion correcta')
  print (" A) Suma \n B) Resta \n C) Multiplicación \n D) División \n E) Exponente/Potencia")
  opcion=str(input()).upper()


# Realizo las opraciones con los numeros ingresados, guardandolos cada uno en una variable
if opcion=="A":
  Operacion = numero_1 + numero_2
  Operacion_descripcion= "Suma"
elif opcion=="B":
  Operacion = numero_1 - numero_2
  Operacion_descripcion= "Resta"
elif opcion=="C":
  Operacion =  numero_1 * numero_2
  Operacion_descripcion= "Multiplicación"
elif opcion=="D":
  Operacion = numero_1 / numero_2
  Operacion_descripcion= "División"
elif opcion=="E":
  Operacion = numero_1 ** numero_2
  Operacion_descripcion= "Potencia"


# #Imprimo los resultados con elf ormato ejemplo  "La suma entre 4.2 y 6.5 es 10.7"

print ("La", Operacion_descripcion ,"entre", numero_1 , "y", numero_2, "es", Operacion)










