print("hola mundo")

variable = "hola mundo"
print(variable)

def ejercicio04():
    nombre = input("introduce tu nombre")
    print("hola" + nombre + "!")
    print(((3+2)/(2*5))**2)

def ejercicio05():
    sueldoPorHora = 100
    horas= int(input("ingrese sus horas trabajadas"))
    print("sueldo", sueldoPorHora * horas)

def ejercicio06():
    numero = int(input("Ingrese un numero entero: "))
    suma = numero * (numero + 1) / 2
    print("La suma de los primeros numeros enteros desde 1 hasta " + str(numero) + " es " + str(suma))

def ejercicio07():
    peso = input("¿Cuál es tu peso en kg? ")
    estatura = input("¿Cuál es tu estatura en metros?")
    imc = round(float(peso)/float(estatura)**2,2)
    print("Tu índice de masa corporal es " + str(imc))

def ejercicio08():
    n = input("Ingrese un numero entero")
    m = input("ingrese otro numero entero")
    print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))

def ejercicio09():
    inversion = float(input("Ingrese el dinero que quiere invertir"))
    interes = float(input("ingresar el interes anual"))
    años = int(input("Cuantos años de inversion"))
    print("Capital final: " + str(round(inversion * (interes / 100 + 1) ** años, 2)))

def ejercicio10():
    pesoPayasoEnG = 112
    pesoMuñecaEnG = 75
    pedidoPayasos = int(input("Ingrese la cantidad de payasos"))
    pedidoMuñecas = int(input("ingrese la cantidad de muñecas"))
    peso_total = (pesoPayasoEnG * pedidoPayasos) + (pesoMuñecaEnG * pedidoMuñecas)
    print("el peso total es " + str(peso_total))

def ejercicio11():
    interes = 0.04
    Inversion = float(input("ingrese la inversion inicial"))
    balance1 = float(Inversion * (1 + interes))
    print("El balance del primer año es: " + str(balance1))
    balance2 = float(balance1 * (1 + interes))
    print("El balance del del segundo año es: " + str(balance2))
    balance3 = float(balance2 * (1 + interes))
    print("El balance del tercer año es: " + str(round(balance3)))
    
def ejercicio12():
    barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
    precio = 3.49 
    descuento = 0.6
    coste = barras * precio * (1 - descuento)
    print("El coste de una barra fresca es " + str(precio) + "€")
    print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
    print("El coste final a pagar es " + str(round(coste, 2)) + "€")
    
