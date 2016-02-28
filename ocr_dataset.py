# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:45:11 2016

@author(s): 
Luis Alberto Muñoz Cruz
Rafael Martinez Rocha
"""
#libreria de imagenes en python
from PIL import Image
#Libreria para generar la matriz de la imagen
import matplotlib.image as mpimg
#Libreria para lectura de directorios
import os
#Libreria para la manipulacion de arhcivos csv
import csv

#Nombre:RazonFilasColumnas
#Desc:Metodo para obtener la razon de filas/columnas
#Argumentos:numfilas,numcolumnas
#Regresa: la razon de las filas respecto a las columnas
def RazonFilasColumnas(numfilas,numcolumnas):
    #Operacion para obtener la razon de filas respecto a las columnas
    razonfilascolumnas = numfilas/numcolumnas
    #regresa: la razon de las filas respecto a las columnas
    return razonfilascolumnas

#Nombre:AreaBlancosNegros
#Desc:Metodo para obtener el area de la letra respecto al tamaño total de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: la razon del area de la letra respecto al tamaño de la imagen
def AreaBlancosNegros(imagenmatriz,numfilas,numcolumnas):
    #Lleva el conteo de los ceros
    contadorceros = 0
    #Lleva el conteo de los ceros    
    contadorunos = 0
    #Creacion de un arreglo que contenga la razon de los 1s y los 0s
    razonesarea = []
    #For recorre las filas de la matriz
    for x in range(numfilas):
        #for recorre las columnas de la matriz
        for y in range(numcolumnas):
            #Se realiza una comparacion para encontrar 0s
            if(imagenmatriz[x][y]==0):
                #Si hay un cero se aumenta en uno la variable contadorceros
                contadorceros = contadorceros + 1
            else:
                #Si hay un uno se aumenta en uno la variable contadorunos               
                contadorunos = contadorunos + 1
    #Se realiza la operacion para encontrar la razon del numero de ceros respecto al area total             
    razonunos = contadorceros/(numfilas*numcolumnas)
    #Se realiza la operacion para encontrar la razon del numero de unos respecto al area total
    razonceros = contadorunos/(numfilas*numcolumnas)
    #Utilizamos el arreglo razonesarea para guardar los dos resultados    
    razonesarea = [razonunos,razonceros]
    #Regresa: la razon del area de la letra respecto al tamaño de la imagen
    return razonesarea

#Nombre:AreaMitadSuperiorBlancosNegros
#Desc:Metodo para obtener el area de la letra respecto al tamaño total de la imagen usando solo la mitad superior de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: la razon de los 1s y 0s de la parte superior de la imagen respecto al tamaño original
def AreaMitadSuperiorBlancosNegros(imagenmatriz,numfilas,numcolumnas):
    #Lleva el conteo de los ceros
    contadorceros = 0
    #Lleva el conteo de los unos    
    contadorunos = 0
    #Creacion de un arreglo que contenga la razon de los 1s y los 0s
    razonesareamitad = []
    #Opereación para hallar la mitad del numero de filas
    mitadfilas = int(numfilas/2)
    #for que recorrre la matriz hasta la mitad de las filas
    for x in range(mitadfilas):
        #for que recorre la matriz por todas sus columnas
        for y in range(numcolumnas):
            #Se realiza una condicion para hallar los 1s y los 0s
            if(imagenmatriz[x][y]==0):
                #Si hay un cero se aumenta en uno la variable contadorceros
                contadorceros = contadorceros + 1
            else:
                #Si hay un cero se aumenta en uno la variable contadorunos
                contadorunos = contadorunos + 1
    #Se realiza la operacion para encontrar la razon del numero de unos de la parte superior de la imagen respecto al area total
    razonunos = contadorunos/(mitadfilas*numcolumnas)
    #Se realiza la operacion para encontrar la razon del numero de ceros de la parte superior de la imagen respecto al area total
    razonceros = contadorceros/(mitadfilas*numcolumnas)
    #Utilizamos el arreglo razonesarea para guardar los dos resultados    
    razonesareamitad = [razonunos,razonceros]
    #Regresa: la razon de los 1s y 0s de la parte superior de la imagen respecto al tamaño original
    return razonesareamitad

#Nombre:CortesMitadVertical
#Desc:Metodo que obtiene el numero de veces que toca una linea vertical al caracter dentro de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: el numero de cortes encontrados    
def CortesMitadVertical(imagenmatriz,numfilas,numcolumnas):
    #Guarda la posicion actual    
    apuntadoractual = 0
    #Guarda una posicion adelante de apuntadoractual 
    apuntadordelantero = 0
    #Lleva el conteo de los cortes hechos por la linea
    cortes = 0
    #Contador utilizado para la evaluacion de la fila 1 de la imagen
    filauno = 0
    #Se realiza una operacion para obtener el numero que es igual a la mitad del total de columnas de la imagen
    mitadcolumnas = int(numcolumnas/2)
    #for recorre las filas de la matriz
    for x in range(numfilas):
        #Igualamos apuntador actual a la fila actual del arreglo y justo a la mitad de columnas
        apuntadoractual = imagenmatriz[x][mitadcolumnas]
        #Evalua que el for no sobrepase el tamaño de la imagen para el apuntadordelantero
        if(x<numfilas-1):
            #Igualamos apuntadordelantero una fila adelante de la fila actual del arreglo y justo a la mitad de columnas
            apuntadordelantero = imagenmatriz[x+1][mitadcolumnas]
            #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (filauno==0 and imagenmatriz[0][mitadcolumnas]==1)):
                #Al cumplirse la condicion la variable cortes aumenta mas 1 su valor
                cortes = cortes + 1
                #Al cumplirse la condicion la variable filauno aumenta mas 1 su valor                
                filauno = filauno + 1
    #Regresa: el numero de cortes encontrados    
    return cortes
    

#Nombre:CortesMitadVertical
#Desc:Metodo que obtiene el numero de veces que toca una linea horizontal al  caracter dentro de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: el numero de cortes encontrados
def CortesMitadHorizontal(imagenmatriz,numfilas,numcolumnas):
    #Guarda la posicion actual        
    apuntadoractual = 0
    #Guarda una posicion adelante de apuntadoractual 
    apuntadordelantero = 0
    #Lleva el conteo de los cortes hechos por la linea
    cortes = 0
    #Contador utilizado para la evaluacion de la columna 1 de la imagen
    columnauno = 0
    #Se realiza una operacion para obtener el numero que es igual a la mitad del total de filas de la imagen
    mitadfilas = int(numfilas/2)
    #for recorre las columnas de la matriz
    for x in range(numcolumnas):
        #Igualamos apuntador actual a la fila actual del arreglo y justo a la mitad de columnas
        apuntadoractual = imagenmatriz[mitadfilas][x]
        #Evalua que el for no sobrepase el tamaño de la imagen para el apuntadordelantero
        if(x<numcolumnas-1):
            #Igualamos apuntadordelantero una fila adelante de la fila actual del arreglo y justo a la mitad de columnas            
            apuntadordelantero = imagenmatriz[mitadfilas][x+1]
            #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (columnauno==0 and imagenmatriz[mitadfilas][0]==1)):
                #Al cumplirse la condicion la variable cortes aumenta mas 1 su valor                
                cortes = cortes + 1
                #Al cumplirse la condicion la variable filauno aumenta mas 1 su valor
                columnauno = columnauno + 1
    #Regresa: el numero de cortes encontrados        
    return cortes

#Nombre:CortesCuartoVertical
#Desc:Metodo que obtiene el numero de veces que toca una linea vertical en la 
# cuarta parte del numero de columnas al caracter dentro de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: el numero de cortes encontrados
def CortesCuartoVertical(imagenmatriz,numfilas,numcolumnas):
    #Guarda la posicion actual            
    apuntadoractual = 0
    #Guarda una posicion adelante de apuntadoractual 
    apuntadordelantero = 0
    #Lleva el conteo de los cortes hechos por la linea    
    cortes = 0
    #Contador utilizado para la evaluacion de la fila 1 de la imagen    
    filauno = 0
    #Se realiza una operacion para obtener el numero que es igual a la cuarta parte del total de filas de la imagen    
    cuartocolumnas = int(numcolumnas/4)
    #for recorre las filas de la matriz    
    for x in range(numfilas):
        #Igualamos apuntador actual a la fila actual del arreglo y justo a un cuarto de columnas
        apuntadoractual = imagenmatriz[x][cuartocolumnas]
        #Evalua que el for no sobrepase el tamaño de la imagen para el apuntadordelantero
        if(x<numfilas-1):
            #Igualamos apuntadordelantero una fila adelante de la fila actual del arreglo y justo a la mitad de columnas            
            apuntadordelantero = imagenmatriz[x+1][cuartocolumnas]
            #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (filauno==0 and imagenmatriz[0][cuartocolumnas]==1)):
                #Al cumplirse la condicion la variable cortes aumenta mas 1 su valor                
                cortes = cortes + 1
                #Al cumplirse la condicion la variable filauno aumenta mas 1 su valor
                filauno = filauno + 1
    #Regresa: el numero de cortes encontrados        
    return cortes
            
#Nombre:CortesCuartoHorizontal
#Desc:Metodo que obtiene el numero de veces que toca una linea horizontal en la 
# cuarta parte del numero de columnas al caracter dentro de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: el numero de cortes encontrados            
def CortesCuartoHorizontal(imagenmatriz,numfilas,numcolumnas):
    #Guarda la posicion actual                
    apuntadoractual = 0
    #Guarda una posicion adelante de apuntadoractual 
    apuntadordelantero = 0
    #Lleva el conteo de los cortes hechos por la linea    
    cortes = 0
    #Contador utilizado para la evaluacion de la columna 1 de la imagen    
    columnauno = 0
    #Se realiza una operacion para obtener el numero que es igual a la cuarta parte del total de filas de la imagen   
    cuartofilas = int(numfilas/4)
    #for recorre las columnas de la matriz        
    for x in range(numcolumnas):
        #Igualamos apuntador actual a la fila actual del arreglo y justo a un cuarto de columnas
        apuntadoractual = imagenmatriz[cuartofilas][x]
        #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes
        if(x<numcolumnas-1):
            #Igualamos apuntadordelantero una fila adelante de la fila actual del arreglo y justo a la mitad de columnas            
            apuntadordelantero = imagenmatriz[cuartofilas][x+1]
            #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes            
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (columnauno==0 and imagenmatriz[cuartofilas][0]==1)):
                #Al cumplirse la condicion la variable cortes aumenta mas 1 su valor                               
                cortes = cortes + 1
                #Al cumplirse la condicion la variable filauno aumenta mas 1 su valor
                columnauno = columnauno + 1
    #Regresa: el numero de cortes encontrados        
    return cortes
            
#Nombre:CortesTresCuartosVertical
#Desc:Metodo que obtiene el numero de veces que toca una linea vertical en la 
# tercer cuarta parte del numero de columnas al caracter dentro de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: el numero de cortes encontrados    
def CortesTresCuartosVertical(imagenmatriz,numfilas,numcolumnas):
    #Guarda la posicion actual                
    apuntadoractual = 0
    #Guarda una posicion adelante de apuntadoractual 
    apuntadordelantero = 0
    #Lleva el conteo de los cortes hechos por la linea    
    cortes = 0
    #Contador utilizado para la evaluacion de la fila 1 de la imagen    
    filauno = 0
    #Se realiza una operacion para obtener el numero que es igual a la tercer cuarta parte del total de columnas de la imagen  
    cuartocolumnas = int((numcolumnas/4)*3)
    #for recorre las filas de la matriz        
    for x in range(numfilas):
        #Igualamos apuntador actual a la fila actual del arreglo y justo al tercer cuarto de columnas
        apuntadoractual = imagenmatriz[x][cuartocolumnas]
        #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes
        if(x<numfilas-1):
            #Igualamos apuntadordelantero una fila adelante de la fila actual del arreglo y justo a la mitad de columnas                        
            apuntadordelantero = imagenmatriz[x+1][cuartocolumnas]
            #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes            
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (filauno==0 and imagenmatriz[0][cuartocolumnas]==1)):
                #Al cumplirse la condicion la variable cortes aumenta mas 1 su valor                                               
                cortes = cortes + 1
                #Al cumplirse la condicion la variable filauno aumenta mas 1 su valor
                filauno = filauno + 1
    #Regresa: el numero de cortes encontrados    
    return cortes
            
#Nombre:CortesTresCuartosHorizontal
#Desc:Metodo que obtiene el numero de veces que toca una linea horizontal en la 
# tercer cuarta parte del numero de columnas al caracter dentro de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: el numero de cortes encontrados               
def CortesTresCuartosHorizontal(imagenmatriz,numfilas,numcolumnas):
    #Guarda la posicion actual                    
    apuntadoractual = 0
    #Guarda una posicion adelante de apuntadoractual 
    apuntadordelantero = 0
    #Lleva el conteo de los cortes hechos por la linea    
    cortes = 0
    #Contador utilizado para la evaluacion de la columna 1 de la imagen    
    columnauno = 0
    #Se realiza una operacion para obtener el numero que es igual a la tercer cuarta parte del total de columnas de la imagen  
    cuartofilas = int((numfilas/4)*3)
    #for recorre las columnas de la matriz            
    for x in range(numcolumnas):
        #Igualamos apuntador actual a la fila actual del arreglo y justo al tercer cuarto de columnas
        apuntadoractual = imagenmatriz[cuartofilas][x]
        #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes
        if(x<numcolumnas-1):
            #Igualamos apuntadordelantero una fila adelante de la fila actual del arreglo y justo a la mitad de columnas                        
            apuntadordelantero = imagenmatriz[cuartofilas][x+1]
            #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes            
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (columnauno==0 and imagenmatriz[cuartofilas][0]==1)):
                #Al cumplirse la condicion la variable cortes aumenta mas 1 su valor                                                               
                cortes = cortes + 1
                #Al cumplirse la condicion la variable filauno aumenta mas 1 su valor
                columnauno = columnauno + 1
    #Regresa: el numero de cortes encontrados    
    return cortes

#Nombre:CruzBlancosNegros
#Desc:Metodo que obtiene la razon del area de blancos respecto a la suma del área de una linea vertical y una horizontal 
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: razonescruz               
def CruzBlancosNegros(imagenmatriz,numfilas,numcolumnas):   
    #Lleva el conteo de ceros en la linea vertical que se esta evaluando    
    contadorcerosvertical = 0
    #Lleva el conteo de unos en la linea horizontal que se esta evaluando    
    contadorunosvertical = 0
    #Lleva el conteo de ceros en la linea vertical que se esta evaluando    
    contadorceroshorizontal = 0
    #Lleva el conteo de unos en la linea horizontal que se esta evaluando    
    contadorunoshorizontal = 0
    #Creacion de un arreglo que contenga la razon resultante
    razonescruz = []
    #Operación que encuentra el numero medio de filas en la imagen
    mitadfilas = int(numfilas/2)
    #Operación que encuentra el numero medio de columnas en la imagen
    mitadcolumnas = int(numcolumnas/2)
    #for recorre las filas de la matriz    
    for x in range(numfilas):
        #Busqueda de 0 en la columna vertical
        if(imagenmatriz[x][mitadcolumnas]==0):
            #Si se encuentra algun cero se aumenta uno el valor de contadorcerosvertical
            contadorcerosvertical = contadorcerosvertical + 1
        else:
            #Si se encuentra algun uno se aumenta uno el valor de contadorunosvertical
            contadorunosvertical = contadorunosvertical + 1
    #for recorre las columnas de la matriz        
    for y in range(numcolumnas):
        #Busqueda de 0 en la columna vertical
        if(imagenmatriz[mitadfilas][y]==0):
            #Si se encuentra algun cero se aumenta uno el valor de contadorceroshorizontal
            contadorceroshorizontal = contadorceroshorizontal + 1
        else:
            #Si se encuentra algun uno se aumenta uno el valor de contadorunosvertical
            contadorunoshorizontal = contadorunoshorizontal + 1
    #Se calcula la razon de pixeles blancos respecto al tamaño total de la imagen
    razonblancos = (contadorcerosvertical + contadorceroshorizontal)/(numcolumnas+numfilas)  
    #Se calcula la razon de pixeles negros respecto al tamaño total de la imagen
    razonnegros = (contadorunosvertical + contadorunoshorizontal)/(numcolumnas+numfilas)
    #Se alamcenan ambas razones en el arreglo llamado razones cruz
    razonescruz = [razonblancos,razonnegros]
    #Regresa: razonescruz              
    return razonescruz        

#Nombre:DiferenciaMitadArea
#Desc:Metodo que obtiene la diferencia de el area total de blancos menos el doble del area de blancos de la mitad izauierda de la imagen 
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: diferenciaunos                
def DiferenciaMitadArea(imagenmatriz,numfilas,numcolumnas):
    #Lleva el conteo de ceros en la mitad de la imagen
    contadorcerosmitad = 0
    #Lleva el conteo de unos en la mitad de la imagen
    contadorunosmitad = 0
    #Se calcula el numero medio de columnas de la imagen
    mitadcolumnas = int(numcolumnas/2)
    #Lleva el conteo de ceros 
    contadorceros = 0
    #lleva el conteo de unos
    contadorunos = 0
    #for recorre las filas de la matriz            
    for x in range(numfilas):
        #for recorre las columnas de la matriz    
        for y in range(numcolumnas):
            #Busqueda de 0 en la imagen
            if(imagenmatriz[x][y]==0):
                #Si se encuentra algun cero se aumenta uno el valor de contadorceros
                contadorceros = contadorceros + 1
            else:
                #Si se encuentra algun cero se aumenta uno el valor de contadorunos                
                contadorunos = contadorunos + 1
    #for recorre las filas de la matriz            
    for x in range(numfilas):
        #for recorre la mitad de columnas de la matriz   
        for y in range(mitadcolumnas):
            #Busqueda de 0 en la imagen
            if(imagenmatriz[x][y]==0):
                #Si se encuentra algun cero se aumenta uno el valor de contadorcerosmitad
                contadorcerosmitad = contadorcerosmitad + 1
            else:
                 #Si se encuentra algun cero se aumenta uno el valor de contadorcerosmitad
                contadorunosmitad = contadorunosmitad + 1
    #Se realiza la diferencia de unos respecto a los unos de la mitad
    diferenciaunos = contadorunos - (contadorunosmitad*2)
    #regresa el resultado de la operación previmamente hecha
    return diferenciaunos
    
#Nombre:LeerImagen
#Desc:Metodo para procesar la lectura de la imagen 
#Argumentos:ruta
#Regresa: parametrosimagen
def LeerImagen(ruta):
    #Se crea un arreglo para contener los parametros necesarios para el uso de la imagen    
    parametrosimagen = []
    #imagenjpg almacena la ruta de la imagen seleccionada
    imagenjpg = Image.open(ruta)
    #imagenmatriz hace que la imagen pueda ser usada como una matriz
    imagenmatriz = mpimg.imread(ruta)
    #con imagenjpg.size se obtienen las dimensiones de la imagen en este caso numcolumnas y numfilas    
    numcolumnas, numfilas = imagenjpg.size
    #En paramentrosimagen se almacena imagenmatriz,numfilas,numcolumna    
    parametrosimagen = [imagenmatriz,numfilas,numcolumnas]
    #Regresa los paramentrosimagen obtenidos previamente
    return parametrosimagen
    
#Nombre: main
#Desc:Metodo principal de funcionamiento  
def main():
    #Se crea un arreglo que almacene las caracteristicas de un numero en una fila del archivo csv
    datasetfila = []
    #Directorio principal
    rootDir= './dataset/'
    #Se crea un nuevo archivo .csv con privilegios de escritura y delimitado por comas 
    f = open('data.csv','w',newline='')
    #documento usa  la funcion csv.writer para escribir el archivo .csv delimitado por comas     
    documento = csv.writer(f,delimiter=',')
    #Ciclo que recorrera los directorios y subdirectorios para obtener cada una de las imagenes a procesar    
    for dirName, subdirList, fileList in os.walk(rootDir):
        #Impresion de mensaje que nos dice que clase se esta procesando actualmente
        print('Procesando clase: %s' % dirName)
        #Recorre la lista de ficheros localizados        
        for fname in fileList:
            #Ruta de cada fichero
            ruta = dirName + '/' + fname
            #Clase procesada
            clase = dirName[10]
            #Funciones para obtener caracteristcas
            #Nota: el nombre de las variables son las inicales de las funciones
            li = LeerImagen(ruta)
            rfc = RazonFilasColumnas(li[1],li[2])
            abc = AreaBlancosNegros(li[0],li[1],li[2])
            amsbn = AreaMitadSuperiorBlancosNegros(li[0],li[1],li[2])
            cmv = CortesMitadVertical(li[0],li[1],li[2])
            cmh = CortesMitadHorizontal(li[0],li[1],li[2])
            ccv = CortesCuartoVertical(li[0],li[1],li[2])
            cch = CortesCuartoHorizontal(li[0],li[1],li[2])
            ctcv = CortesTresCuartosVertical(li[0],li[1],li[2])
            ctch = CortesTresCuartosHorizontal(li[0],li[1],li[2])
            cbn = CruzBlancosNegros(li[0],li[1],li[2])
            dma = DiferenciaMitadArea(li[0],li[1],li[2])
            #Arrelo que agrega una nueva instancia al dataset     
            datasetfila.append([rfc,abc[0],abc[1],amsbn[0],amsbn[1],cmv,cmh,ccv,cch,ctcv,ctch,cbn[0],cbn[1],dma,clase])
    #Escritura del archivo .csv
    documento.writerows(datasetfila)
    #Cerrar archivo .csv
    f.close()
main()
