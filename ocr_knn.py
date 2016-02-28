# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:21:44 2016

@author(s): 
Luis Alberto Muñoz Cruz
Rafael Martinez Rocha
"""

#Libreria para el manejo de archivos .csv
import csv
#Libreria pqra la creacion de formulas matematicas
import math
#Importación de clase ocr_datset para la obtención de caracteristicas
import ocr_dataset as ocrds

#Nombre:nuevaInstanciaK
#Desc:Metodo que lee la imagen y obtiene sus caracteriscas, tambien se determina el numero de
#los k-vecinos que el usuario quiere
#Argumentos:Ninguno
#Regresa: nuevainstancia
def nuevaInstanciaK():
    #Mensaje del estado del proceso
    print('\nObteniendo características de imagen...')
    #Ruta de la imagen a clasificar
    ruta = 'D:/Users/ASUS/Documents/python_dm/test/6.png'
    #Funciones importadas de la clase ocr_dataset.py para obtener las caracteristicas
    #de la imagen a clasificar
    li = ocrds.LeerImagen(ruta)
    rfc = ocrds.RazonFilasColumnas(li[1],li[2])
    abc = ocrds.AreaBlancosNegros(li[0],li[1],li[2])
    amsbn = ocrds.AreaMitadSuperiorBlancosNegros(li[0],li[1],li[2])
    cmv = ocrds.CortesMitadVertical(li[0],li[1],li[2])
    cmh = ocrds.CortesMitadHorizontal(li[0],li[1],li[2])
    ccv = ocrds.CortesCuartoVertical(li[0],li[1],li[2])
    cch = ocrds.CortesCuartoHorizontal(li[0],li[1],li[2])
    ctcv = ocrds.CortesTresCuartosVertical(li[0],li[1],li[2])
    ctch = ocrds.CortesTresCuartosHorizontal(li[0],li[1],li[2])
    cbn = ocrds.CruzBlancosNegros(li[0],li[1],li[2])
    dma = ocrds.DiferenciaMitadArea(li[0],li[1],li[2])
    #Numero de intancias cercanas que se desean obtener
    k = 10
    #Arreglo que guarda las caracteristicas de la nueva intancia
    nuevainstancia = [rfc,abc[0],abc[1],amsbn[0],amsbn[1],cmv,cmh,ccv,cch,ctcv,ctch,cbn[0],cbn[1],dma,k]
    #Regresa el arreglo nuevainstancia que contiene las caracteristicas de la nueva instancia  
    return nuevainstancia

#Nombre:cargarDataset
#Desc:Metodo que carga el dataset
#Argumentos:Ruta o nombre del archivo .csv que contiene el dataset
#Regresa: dataset
def cargarDataset(nombrearchivo):
    #Abrir el archivo csv con permisos de lectura
    with open(nombrearchivo, 'r') as csvfile:
        #Leer un archivo con reader()
        lineas = csv.reader(csvfile)
        #Obtener lista de las instancias del dataset
        dataset = list(lineas)
        #Contador que identificara el numero de instancias dentro del dataset
        contadorinstancias = 0
        #Recorrer cada instancia obtenida
        for x in range(len(dataset)):
            #Aumento de contador al detectar una instancia
            contadorinstancias = contadorinstancias + 1
            #Ciclo para recorrer cada caraacteristica de la instancia
            for y in range(15):
                #Condicion para verificar el tamaño de las caracteristicas
                if(y<14):
                    #Convierte los valores del dataset en flotantes
                    dataset[x][y] = float(dataset[x][y])
                else:
                    #Guarda el valor de la clase
                    dataset[x][y] = dataset[x][y]
        #Informacion del dataset
        print("============ Información del Dataset ============")
        print("\tNúmero de Instancias: " + str(contadorinstancias))
    #Regresa el dataset cargado en un arreglo
    return dataset

#Nombre:calcularDistancia
#Desc:Metodo que realiza opraciones para el calculo de la distancia euclidiana a cada una
#de las instancias del dataset
#Argumentos:Dataset y nuevainstancia
#Regresa: distancias euclidianas
def calcularDistancia(dataset,ni):
    #Impresion del estado del proceso
    print('\nCalculando distancias...')
    #Arreglo para guardar las distancias calculadas
    distancias = []
    #Ciclo que recorre cada instancia del dataset y obtiene la distancia
    #euclidiana con respecto a la nueva instancia
    for x in range(len(dataset)):
        #Calculo de distancia euclidiana
        distancias.append([math.sqrt(pow((dataset[x][0] - float(ni[0])),2)+pow((dataset[x][1]-float(ni[1])),2)+pow((dataset[x][2]-float(ni[2])),2)+pow((dataset[x][3]-float(ni[3])),2)+pow((dataset[x][4]-float(ni[4])),2)+pow((dataset[x][5]-float(ni[5])),2)+pow((dataset[x][6]-float(ni[6])),2)+pow((dataset[x][7]-float(ni[7])),2)+pow((dataset[x][8]-float(ni[8])),2)+pow((dataset[x][9]-float(ni[9])),2)+pow((dataset[x][10]-float(ni[10])),2)+pow((dataset[x][11]-float(ni[11])),2)+pow((dataset[x][12]-float(ni[12])),2)+pow((dataset[x][13]-float(ni[13])),2)),dataset[x][14],x+1])
    #variable que contendra valores temporales
    temp = 0
    #Variable que contiene el tamaño del arreglo distancias
    tam = len(distancias)
    #Ciclo para recorrer el tamaño del arreglo
    for i in range(1, tam):
        #Ciclo para recorrer las instancias
        for j in range(0,tam-1):
            #Verifica el valor de la instancia actual y la compara con la instancia delantera
            #Si es mayor realiza las operaciones
            if(distancias[j]>distancias[j+1]):
               #Guarda el valor de la instacia posterior en la variable temporal
               temp = distancias[j+1]
               #Iguala el valor de la distancia posterior a la actual
               distancias[j+1] = distancias[j]
               #Iguala el valor de la distancia actual a la temporal
               distancias[j] = temp
    #Regresa las distancias ordenadas ascendentemente
    return distancias     

#Nombre:clasificarInstancia
#Desc:Metodo que ordena las distancias obtenidas anteriormente, y arroja las instancias que mas 
#se acercan a la nuevainstancia
#Argumentos:distancias y nuevainstancia
#Regresa: Ninguno
def clasificarInstancia(distancias,ni):
    print('\nObteniendo distancias mas cercanas...')
    #Contador de las instancias mas cercanas
    contadorinstancias = 1
    #Contadores para el numero de veces que se repite la clase
    contadorcero = 0
    contadoruno = 0
    contadordos = 0
    contadortres = 0
    contadorcuatro = 0
    contadorcinco = 0
    contadorseis= 0
    contadorsiete = 0
    contadorocho = 0
    contadornueve = 0
    #Encabezado
    print('\n')
    print('     K      |       Distancia     |Clase|Fila|')
    print('----------------------------------------------')
    #Ciclo de Impresion de las distancias mas cercanas
    for x in range(int(ni[14])):
        print('Instancia '+str(contadorinstancias)+" = "+str(distancias[x]))
        #Contador de instancias cercanas
        contadorinstancias = contadorinstancias + 1
        #Evaluacion de la clase de la instancia
        if(distancias[x][1]=='0'):
            contadorcero += 1
        if(distancias[x][1]=='1'):
            contadoruno += 1
        if(distancias[x][1]=='2'):
            contadordos += 1
        if(distancias[x][1]=='3'):
            contadortres += 1
        if(distancias[x][1]=='4'):
            contadorcuatro += 1
        if(distancias[x][1]=='5'):
            contadorcinco += 1
        if(distancias[x][1]=='6'):
            contadorseis += 1
        if(distancias[x][1]=='7'):
            contadorsiete += 1
        if(distancias[x][1]=='8'):
            contadorocho += 1
        if(distancias[x][1]=='9'):
            contadornueve += 1
    #Arreglo que contendra los contadores de las clases
    clases = []
    #Arreglo lleno con los contadores de las clases
    clases = [contadorcero,contadoruno,contadordos,contadortres,contadorcuatro,contadorcinco,contadorseis,contadorsiete,contadorocho,contadornueve]
    #Variable para comprobar los valores de las clases    
    clasemayor = 0
    #Variable para identificar la clase con mayor numero de elementos mas cercanos
    clasificacion = 0
    for x in range(len(clases)):
        #Condicion para verificar el tamañao de cada clase
        if(clases[x] > clasemayor):
            #Guarda el valor de la clase con el valor mas alto
            clasemayor = clases[x]
            #Guarda la identidad de la clase
            clasificacion = x    
    #Impresion del numero de instancias detectadas en cada clase
    #Solo se imprimiran si los contadores de clases son mayores a cero
    if(contadorcero>0):
        print('\nInstancias detectadas - Clase 0: '+str(contadorcero))
    if(contadoruno>0):
        print('\nInstancias detectadas - Clase 1: '+str(contadoruno))
    if(contadordos>0):
        print('\nInstancias detectadas - Clase 2: '+str(contadordos))
    if(contadortres>0):
        print('\nInstancias detectadas - Clase 3: '+str(contadortres))
    if(contadorcuatro>0):
        print('\nInstancias detectadas - Clase 4: '+str(contadorcuatro))
    if(contadorcinco>0):
        print('\nInstancias detectadas - Clase 5: '+str(contadorcinco))
    if(contadorseis>0):
        print('\nInstancias detectadas - Clase 6: '+str(contadorseis))
    if(contadorsiete>0):
        print('\nInstancias detectadas - Clase 7: '+str(contadorsiete))
    if(contadorocho>0):
        print('\nInstancias detectadas - Clase 8: '+str(contadorocho))
    if(contadornueve>0):
        print('\nInstancias detectadas - Clase 9: '+str(contadornueve))
    #Impresion de caracter predicho de acuerdo a las distancias mas cercanas
    print('\n\nCaracter predicho: ' + str(clasificacion))


#Funcion que carga el dataset, con el nombre o ruta del archivo como entrada
ds = cargarDataset("data.csv")
#Generacion de caracteristicas de la nueva instancia
nik = nuevaInstanciaK()    
#Calculo de las distancias mas cercanas
cd = calcularDistancia(ds,nik)
#Clasificacion de las distancias mas cercanas y determinacion de la clase de la nueva instancia
clasificarInstancia(cd,nik)

