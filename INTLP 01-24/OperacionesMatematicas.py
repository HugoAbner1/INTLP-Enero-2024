# Operaciones matematicas (Suma,resta,division,potensia,raiz cuadrada,modulo)

#IMportar librerias de funciones matematicas
import math

# Entrada de datos
número1 = 10
número2 = 5.7

# PROCESOS (Operaciones y/o cálculos matematicos y lógicos)
suma = número1+número2
resta=número1-número2
multiplicación=número1*número2
división=número1/número2

potencia_1=número1**número2
potencia_2=pow(número1,número2)
cuadrado=número1**2
cubo=número2**3

raíz_cuadrada_1=math.sqrt(27)
raíz_cuadrada_1=pow(27,1/2)
raíz_cúbica=pow(27,1/3)

módulo_residuo=número1%número2

# SALIDA DE DATOS
print("La suma es =",suma) #1ra forma para imprimir
print("La suma es ="+str(suma)) #segunda forma para imprimir CONCATENAR:
print(f"La suma es ={suma}")#3ra forma para imprimir
print("La resta es =",resta)
print("La multiplicación es=", multiplicación)

