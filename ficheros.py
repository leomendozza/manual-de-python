def ejercicioFc01():
    numero = int(input("ingrese un numero entre el 1 y el 10: "))
    nombre_fichero = 'tabla-' + str(numero) + ".txt"
    f = open(nombre_fichero, 'w')
    for i in range(1,11):
        f.write(str(numero) + ' x ' + str(i) + '=' + str(numero * i) + '/n')
    f.close()
    
def ejercicioFc02():
    numero = int(input("ingrese un numero del 1 al 10"))
    nombre_fichero = 'tabla-' + str(numero) + '.txt'
    try:
        f = open(nombre_fichero, 'r')
    except FileNotFoundError:
        print('no existe el fichero de la tabla del ', numero)
    else:
        print(f.read())
        f.close()
        
def ejercicioFc03():
    n = int(input('Introduce un número entero entre 1 y 10: '))
    m = int(input('Introduce otro número entero entre 1 y 10: '))
    nombre_fichero = 'tabla-' + str(n) + '.txt'
    try: 
        with open(nombre_fichero, 'r') as f:
            lineas = f.readlines()
        print(lineas[m-1])
    except FileNotFoundError:
        print('No existe el fichero con la tabla del ', n)
    
def ejercicioFc04():
    def contar_palabras(url):
        from urllib import request
        from urllib.error import URLError
        try:
            f=request.urlopen(url)
        except URLError:
            return('la url ' + url + ' no existe')
        else:
            contenido = f.read()
            return len(contenido.split())
    print(contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt'))
    print(contar_palabras('https://no-existe.txt'))
    
def ejercicioFc05():
    def parsear_pib(url):
        from urllib import request
        from urllib.error import URLError
        try:
            with request.urlopen(url) as f:
                datos = f.read().decode('utf-8').split('\n') 
        except URLError:
            return('¡La url ' + url + ' no existe!')
        else:
            años = datos.pop(0).split('\t')[1:]
            dict_pibs = {}
            for pais in datos:
                datos_pais = pais.split('\t')
                codigo_pais = datos_pais.pop(0)[-2:]
                dict_pais = {}
                for i in range(len(datos_pais)):
                    dict_pais[años[i].strip()] = datos_pais[i].strip()
                dict_pibs[codigo_pais] = dict_pais
            return dict_pibs

    def pib(pibs, pais = "ES"):
        print("Año\tPIB")
        for i, j in pibs[pais].items():
            print(i, '\t', j)

    pais = input('Introduce el código de un país: ')
    print('Producto Interior Bruto per cápita de', pais)
    pib(parsear_pib("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"), pais)