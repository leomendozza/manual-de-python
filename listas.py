def ejercicioL01():
    curso = ["matematica", "fisica", "quimica", "lengua","historia"]
    print(curso)
    
def ejercicioL02():
    cursos = ["matematica", "fisica", "quimica", "lengua","historia"]
    for curso in cursos:
        print("Yo estudio la asignatura de: " + curso)
        
def ejercicioL03():
    cursos = ["matematica", "fisica", "quimica", "lengua","historia"]
    notas = []
    for curso in cursos:
        nota = input("Que nota sacaste en " + curso + "?")
        notas.append(nota)
    for i in range(len(cursos)):
        print("en " + cursos[i] + " has sacado " + notas[i])
        
def ejercicioL04():
    ganadores = []
    for i in range(6):
        ganadores.append(int(input("introduce los ganadores: ")))
        ganadores.sort()
        print("Los numeros ganadores son "+ str(ganadores))
        
def ejercicioL05():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    for i in range(1,11):
        print(numeros[-i], end=", ")
        
def ejercicioL06():
    cursos = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    aprobadas = []
    for curso in cursos:
        notas = float(input("¿Qué nota has sacado en " + curso + "?"))
        if notas >= 5:
            aprobadas.append(curso)
    for curso in aprobadas:
        cursos.remove(curso)
    print("Tienes que repetir " + str(cursos))


    