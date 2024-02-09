def ejercicioB01():
    word = input("ingrese una palabra")
    for i in range(10):
       print(word)
       
def ejercicioB02():    
    cumpleaños = int(input("ingrese su edad"))
    for i in range(cumpleaños):
        print("cumpliste ", i+1, "años")
        
def ejercicioB03():
    numeroEntero = int(input("Ingrese un numero entero positivo"))
    for i in range(1, numeroEntero+1, 2):
        print(i, end=" ")
        
def ejercicioB04():
    numeroIntero = int(input("Ingrese un numero entero positivo"))
    for i in range(numeroIntero, -1, -1):
        print(i, end=", ")
        
def ejercicioB05():
    inversion = float(input("Ingrese la cantidad que desea invertir"))
    interes = float(input("Ingrese el interes anual"))
    año = int(input("Ingrese la cantida de años que quiere fijar"))
    for i in range(año):
         inversion*= 1 + interes / 100 
         print("Capital tras " + str(i+1) + " años: " + str(round(inversion, 2)))
         
def ejercicioB06():
    numero = int(input("Ingrese un numero"))
    for i in range(numero):
        for j in range(i+1):
            print("*", end = ""  )  
        print("")
        
def ejercicioB07():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i*j, end="\t")
        print("")
        
def ejercicioB08():
    n = int(input("Introduce la altura del triángulo (entero positivo): "))
    for i in range(1, n+1, 2):
        for j in range(i, 0, -2):
            print(j, end=" ")
        print("")

def ejercicioB09():
    contraseña = "leomendozza2"
    contraseñaIn = ""
    while contraseña != contraseñaIn:
        contraseñaIn = input("ingrese contraseña")
    print("contraseña correcta")     
    
def ejercicioB10():
    numero = int(input("Introduce un número entero positivo mayor que 2: "))
    i = 2
    while numero % i != 0:
        i += 1
    if i == numero:
        print(str(numero) + " es primo")
    else:
        print(str(numero) + " no es primo")
        
def ejercicioB11():
    word = input("Introduce una palabra: ")
    for i in range(len(word)-1, -1, -1):
        print(word[i])
        
def ejercicioB12():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra")
    contador = 0
    for i in frase:
        if i == letra:
            contador += 1
    print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))
    
def ejercicioB13():
    while True:
        frase = input("Introduce algo: ")
        if frase == "salir":
         break
    print(frase)