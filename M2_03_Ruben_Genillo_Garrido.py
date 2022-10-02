#pido un número y muestro su resultado y tipo
num1 = input("Dame un número: ")
print("resultado:", num1," tipo:", type(num1))

#pido un número y me aseguro que sea un integer
num2 = int(input("Dame otro número: "))
print("resultado:", num2," tipo:", type(num2))

#pido un número y me aseguro de que sea float
num3 = float(input("Dame otro número: "))
print("resultado:", num3," tipo:", type(num3))

#pido un número entero
num4 = int(input("Dame un número entero: "))
#y lo muestro con 5 dígitos rellenos con 0s por delante
print("{:05d}".format(num4))

#pido un número flotante
num5 = float(input("Dame un número flotante: "))
#y lo muestro con 5 dígitos para la parte entera y 3 dígitos para la parte decimal
print("{:09.3f}".format(num5))

#muestro los siguientes datos de 2 formas posibles
altura = 1.80
peso = 80.135
print("La altura es de", altura ,"metros y el peso es de", peso ,"KG") #La altura es de 1, 80 metros y el peso es de 80, 135 KG
print("La altura es de {} metros y el peso es de {} KG".format(altura, peso)) #La altura es de 1, 80 metros y el peso es de 80, 135 KG