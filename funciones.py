def ejecicioF01():
    print("hola amiga")
    return

def ejercicioF02(nombre):
    print("bienvenido"+ nombre)
    return

def ejercicioF03(numero):
    tmp = 1 
    for i in range(numero):
        tmp *= i+1
    return tmp
print(ejercicioF03(4))
print(ejercicioF03(24))

def ejercicioF04(cantidad, iva = 21):
    return cantidad + cantidad * iva/100
print(ejercicioF04)

def ejercicioF05():
    def radio_circulo(radio):
        pi = 3.1415
        return pi*(radio**2)
    
    def volumen_circulo(radio, altura):
        return radio_circulo(radio)*altura
    print(volumen_circulo(3,5))