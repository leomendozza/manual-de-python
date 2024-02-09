def ejercicioD01():
    monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    moneda = input("Ingrese la divisa: ")
    print(monedas.get(moneda.title(), "la divisa no esta"))
    
def ejercicioD02():
    nombre = input("ingrese su nombre")
    edad = int(input("ingrese su edad"))
    direccion = input("ingrese su direccion")
    telefono = int(input("ingrese su telefono"))
    persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
    print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])
    
def ejercicioD03():
    frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
    fruta = input('¿Qué fruta quieres? ').title()
    kg = float(input('¿Cuántos kilos? '))
    if fruta in frutas:
        print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
    else: 
        print("Lo siento, la fruta", fruta, "no está disponible.")
        
def ejercicioD04():
    meses = {1:"enero", 2:"Febrero", 3:"marzo", 4:"abril", 5:"mayo"}
    fecha = input("ingrese una fecha en formato dd/mm/aaaa")
    fecha = fecha.split('/')
    print(fecha[0], "de", meses[int(fecha[1])], "De", fecha[2])