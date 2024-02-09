def ejercicio01():
    edadUsuario = int(input("Ingrese su edad"))
    if edadUsuario < 18:
        print("es menor de edad")
    else:
        print("es mayor de edad")
        
def ejercicio02():
    contraseñaGuardada = "leomendozza2"
    contraseña = str(input("ingrese su contraseña"))
    if contraseña == contraseñaGuardada:
        print("la contraseña es correcta")
    else:
        print("la contraseña es incorrecta")
        
def ejercicio03():
    numberOne = int(input("ingrese el primer numero"))
    numberTwo = int(input("Ingrese el segundo numero"))
    operation = float(numberOne / numberTwo)
    if operation != 0:
        print("the result is  ", operation)
    else:
        print("ERROR")
        
def ejercicio04():
    date = int(input("enter a number"))
    if date % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")
    
def ejercicio05():
    age = int(input("enter your age"))
    income = int(input("enter your income"))
    if age > 16 and income >= 1000:
        print("must pay taxes")
    else:
        print("should not be taxes")

def ejercicio06():
    name = input("Ingrese su nombre")
    gender = input("Ingrese su sexo con M o F")
    if gender == "M":
        if name.lower() < "m":
            group = "A"
        else: 
            group = "B"
    else:
        if name.lower() > "n":
            group = "A"
        else: 
            group = "B"
    print("tu grupo es " + group)
    
def ejercicio07():
    date = float(input("ingrese su renta anual"))
    if date < 10000:
        tipo = 5
    elif date < 20000:
        tipo = 15
    elif date < 35000:
        tipo = 20
    elif date < 60000:
        tipo = 30
    else:
        tipo = 45
    print("Debe pagar ", date * tipo / 100,"$", sep=" ")
    
def ejercicio08():
    bonificacion = 2400
    inaceptable = 0
    aceptable = 0.4
    puntos = float(input("Introduce tu puntuación: "))
    # Clasifiación por niveles de rendimiento
    if puntos == inaceptable:
        nivel = "Inaceptable"
    elif puntos == aceptable:
        nivel = "Aceptable"
    elif puntos >= 0.6:
        nivel = "Meritorio"
    else:
        nivel = ""
    # Mostrar nivel de rendimiento
    if nivel == "":
        print("Esta puntuación no es válida")
    else:
        print("Tu nivel de rendimiento es %s" % nivel)
        print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))  
        
def ejercicio09():
    edad = int(input("Introduce tu edad: "))
    # Decisión del precio en función de la edad
    if edad < 4:
        precio = 0
    elif edad <= 18:
        precio = 5
    else:
        precio = 10
    # Mostrar precio
    print("El precio de la entrada es", precio, "€.")
    

def ejercicio10():
    print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
    tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
    if tipo == "1":
        print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
        ingrediente = input("Introduce el ingrediente que deseas: ")
        print("Pizza vegetariana con mozzarella, tomate y ", end="")
        if ingrediente == "1":
            print("pimiento")
        else: 
            print("tofu")
    else:
        print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
        ingrediente = input("Introduce el ingrediente que deseas: ")
        print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")
        