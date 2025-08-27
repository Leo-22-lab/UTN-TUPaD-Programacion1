"""1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”."""
print("Actividad 1")
print("Hola Mundo!")
print("--------------------------------------------------------------------------------------------------------------------------------------")

"""2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla. """
print("Actividad 2")
nombre = input("ingrese un nombre: ")
print("hola", nombre)
print("--------------------------------------------------------------------------------------------------------------------------------------")

"""3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla."""
print("Actividad 3")
nombre2 = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = input("ingrese su edad: ")
residencia = input("ingrese su lugar de recidencia: ")
print("soy", nombre2, apellido, "tengo", edad, "años", "y vivo en", residencia)
print("--------------------------------------------------------------------------------------------------------------------------------------")

"""4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro."""
print("Actividad 4")
radio = float(input("ingrese el radio del circulo: "))
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
print("el area es: ", area)
print("el perimetro es: ", perimetro)
print("--------------------------------------------------------------------------------------------------------------------------------------")

"""5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale."""
print("Actividad 5")
segundos = int(input("ingrese los segundos: "))
horas = segundos / 3600
print(segundos, "segundos es igual a", horas, "horas")
print("--------------------------------------------------------------------------------------------------------------------------------------")

"""6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número."""
print("Actividad 6")
num = int(input("ingrese un numero: "))
for i in range(1, 11):
    resultado = num * i
    print(num, "×", i, "=", resultado)
print("--------------------------------------------------------------------------------------------------------------------------------------")

"""7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."""
print("Actividad 7")
num1 =int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
if num1 and num2 != 0 :
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    divicion = num1 / num2
    print("el resultado de la suma es: ", suma)
    print("el resultado de la resta es: ", resta)
    print("el resultado de la multiplicacion es: ", multiplicacion)
    print("el resultado de la divicion es: ", divicion)
print("--------------------------------------------------------------------------------------------------------------------------------------")

"""8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:
𝐼𝑀𝐶 =𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
     (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2"""
print("Actividad 8")
altura = float(input("ingrese su altura: "))
peso = int(input("ingrese su peso: "))
imc = peso / (altura ** 2)
print("el indice de masa corporal imc es de: ", imc)
print("--------------------------------------------------------------------------------------------------------------------------------------")

"""9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =95 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32"""
print("Actividad 9")
grados_celcius = int(input("ingrese la temperatura en grados celcius: "))
grados_f𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = grados_celcius * (9/5) +32
print("la convercion de grados celcius a fahrenheit es de: ", grados_fahrenheit)
print("--------------------------------------------------------------------------------------------------------------------------------------")

"""10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.
"""
print("Actividad 10")
numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
numero3 = int(input("ingrese el tercer numero: "))
promedio = numero1 + numero2 + numero3 / 3
print("el promedio de los tres numeros es de: ", promedio)