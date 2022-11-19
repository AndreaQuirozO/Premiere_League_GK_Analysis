#Autor: Andrea Quiroz, A01026486, (IDM)
#Analiza información recolectada sobre los porteros de la Premier League de Inglaterra hasta la fecha de 10 de octubre de 2021

import csv 
import matplotlib.pyplot as plot


def encontrar_maximo(datos, index_categoria):
    '''Encuentra y regresa el nombre o los nombres de porteros con el máximo valor de una categoría en específico (index_categoria)'''
    dato_maximo = 0
    portero_maximo = []
    for renglon in datos:
        if int(renglon[index_categoria]) > dato_maximo:
            dato_maximo = int(renglon[index_categoria])
    for renglon in datos:
        if int(renglon[index_categoria]) == dato_maximo:   
            portero_maximo.append(renglon[1])
    
    return portero_maximo   #Regresa una lista con los nombres de los porteros que tienen el máximo valor en cierta columna


def resumir_datos():
    '''Resume e imprime los datos del archivo considerando los valores de una sola columna, ya sea el promedio o el máximo valor de esta'''
    archivo = open('data_gk_pl.csv')
    entrada = csv.reader(archivo)
    
    datos = list(entrada)[1:]   #Quita el renglón de los títulos
    
    numero_porteros = 0
    apariciones_totales = 0
    salvadas_totales = 0
    cleansheets_totales = 0
    penales_salvados_totales = 0
    goles_porteros = 0
    porteros_sin_apariciones = 0
    goles_concedidos_totales = 0
    errores_gol_totales = 0
    autogoles_totales = 0
    for renglon in datos:
        numero_porteros += 1
        apariciones_totales += int(renglon[2])
        salvadas_totales += int(renglon[6])
        cleansheets_totales += int(renglon[3])
        penales_salvados_totales += int(renglon[7])
        if int(renglon[20]) != 0:
            goles_porteros += 1
        if int(renglon[2]) == 0:
            porteros_sin_apariciones += 1
        goles_concedidos_totales += int(renglon[14])
        errores_gol_totales += int(renglon[15])
        autogoles_totales += int(renglon[16])
        
    portero_mas_apariciones = encontrar_maximo(datos, 2)    
    portero_mas_salvadas = encontrar_maximo(datos, 6)
    portero_mas_cleansheets = encontrar_maximo(datos, 3)
    portero_mas_penales_salvados = encontrar_maximo(datos, 7)
    portero_mas_goles = encontrar_maximo(datos, 20)
    portero_mas_asistencias = encontrar_maximo(datos, 21)
    portero_mas_goles_concedidos = encontrar_maximo(datos, 14)
    portero_mas_errores = encontrar_maximo(datos, 15)
    portero_mas_autogoles = encontrar_maximo(datos, 16)
    portero_mas_tarjetas_amarillas = encontrar_maximo(datos, 17)
    portero_mas_tarjetas_rojas = encontrar_maximo(datos, 18)
    
    print('\nResúmen de los datos sobre los porteros de la Premier League\n')
    print('Número de porteros en la Premier League:', "{:,}".format(numero_porteros))  #Este formato imprime los números con separador de millares. Ej: 5,345,590
    print('Apariciones totales de los porteros de la Premier League:', "{:,}".format(apariciones_totales))
    print('Salvadas totales de los porteros de la Premier League:', "{:,}".format(salvadas_totales))
    print('Clean sheets totales de los porteros de la Premier League:', "{:,}".format(cleansheets_totales))
    print('Total de penales salvados por porteros de la Premier League:', "{:,}".format(penales_salvados_totales))
    print('Número de porteros que han anotado goles en la Premier League:', "{:,}".format(goles_porteros))
    print('Número de porteros sin apariciones en la Premier League:', "{:,}".format(porteros_sin_apariciones))
    print('Goles totales concedidos por los porteros de la Premier League:', "{:,}".format(goles_concedidos_totales))
    print('Errores totales de porteros en la Premier League que terminaron en gol:', "{:,}".format(errores_gol_totales))
    print('Autogoles totales de porteros en la Premier League:', "{:,}".format(autogoles_totales))
    print('')
    print('Portero con más apariciones:', ','.join(portero_mas_apariciones))  #Este formato imprime los nombres en la lista sin los corchetes y comillas y separados por comas
    print('Portero con más salvadas:', ','.join(portero_mas_salvadas))
    print('Portero con más clean sheets (partidos sin recibir goles):', ','.join(portero_mas_cleansheets))
    print('Portero con más penales salvados:', ', '.join(portero_mas_penales_salvados))
    print('Portero con más goles anotados:', ', '.join(portero_mas_goles))
    print('Portero con más asistencias:', ', '.join(portero_mas_asistencias))
    print('Portero con más goles concedidos:', ', '.join(portero_mas_goles_concedidos))
    print('Portero con más errores que terminaron en gol:', ', '.join(portero_mas_errores))
    print('Portero con más autogoles:', ', '.join(portero_mas_autogoles))   
    print('Portero con más tarjetas amarillas:', ', '.join(portero_mas_tarjetas_amarillas))
    print('Portero con más tarjetas rojas:', ', '.join(portero_mas_tarjetas_rojas))

    
def obtener_estadisticas():
    '''Calcula e imprime estadísticas de todos los porteros de la Premier League usando información de dos columnas'''
    archivo = open('data_gk_pl.csv')
    entrada = csv.reader(archivo)
    
    datos = list(entrada)[1:]
    
    numero_porteros = 0
    apariciones_totales = 0
    salvadas_totales = 0
    cleansheets_totales = 0
    goles_concedidos_totales = 0
    errores_gol_totales = 0
    pases_por_partido_totales = 0
    for renglon in datos:
        numero_porteros += 1
        apariciones_totales += int(renglon[2])
        salvadas_totales += int(renglon[6])
        cleansheets_totales += int(renglon[3])
        goles_concedidos_totales += int(renglon[14])
        errores_gol_totales += int(renglon[15])
        pases_por_partido_totales += float(renglon[23])
        
    promedio_salvadas_portero = salvadas_totales/numero_porteros
    promedio_cleansheets_portero = cleansheets_totales/numero_porteros
    promedio_goles_concedidos_portero = goles_concedidos_totales/numero_porteros
    promedio_goles_concedidos_partido = goles_concedidos_totales/apariciones_totales
    promedio_pases_portero = pases_por_partido_totales/numero_porteros
    
    print('\nEstadísticas de los datos sobre los porteros de la Premier League\n')
    print('Promedio de salvadas de un portero en la Premier League: %.2f' %(promedio_salvadas_portero)) #Este formato imprime el número con 2 decimales
    print('Promedio de clean sheets de un portero en la Premier League: %.2f' %(promedio_cleansheets_portero))
    print('Promedio de goles concedidos de un portero en la Premier League: %.2f' %(promedio_goles_concedidos_portero))
    print('Promedio de goles concedidos por partido de un portero en la Premier League: %.2f' %(promedio_goles_concedidos_partido))
    print('Promedio de pases por partido de un portero en la Premier League: %.2f' %(promedio_pases_portero))
    

def graficar_informacion():
    '''Grafica información de los porteros respecto a cierta categoría.
Tiene funciones adentro para hacer diferentes gráficas usando los datos analizados al principio de esta función'''
    archivo = open('data_gk_pl.csv')
    entrada = csv.reader(archivo)
    
    datos = list(entrada)[1:]
    
    porteros = []
    apariciones = []
    cleansheets = []
    penales_salvados = []
    promedio_errores = []
    promedio_goles = []
    porteros_con_apariciones = 0
    porteros_sin_apariciones = 0
    for renglon in datos:
        porteros.append(renglon[1])
        apariciones.append(int(renglon[2]))
        cleansheets.append(int(renglon[3]))
        penales_salvados.append(int(renglon[3]))
        if int(renglon[2]) > 0:
            promedio_errores.append((int(renglon[15])/int(renglon[2])))
            promedio_goles.append((int(renglon[14])/int(renglon[2])))
        else:
            promedio_errores.append(0)
            promedio_goles.append(0)
        if int(renglon[2]) == 0:
            porteros_sin_apariciones += 1
        else:
            porteros_con_apariciones += 1
        
        
    def graficar_apariciones_portero():  #Se hicieron funciones dentro de función para que no se mezclaran los datos de las gráficas y estas salieran bien
        '''Grafica las apariciones por portero usando una gráfica de barras'''
        figure1 = plot.figure(figsize = (20, 15))
        plot.bar(porteros, apariciones, color = 'purple')
        plot.title('Apariciones por portero')
        plot.xlabel('Porteros')
        plot.ylabel('Apariciones')
        plot.xticks(rotation=90)
        plot.show()
    
    
    def graficar_porcentaje_apariciones():
        '''Grafica el porcentaje de porteros con apariciones y el porcentaje sin con una gráfica de pie'''
        figure2 = plot.figure(figsize = (10, 10))
        labels = ['Porteros con apariciones', 'Porteros sin apariciones']
        plot.pie([porteros_con_apariciones, porteros_sin_apariciones], labels = labels, colors = ['cyan', 'pink'], startangle = 50, explode = [0.1, 0], autopct = '%1.1f%%', normalize = True)
        plot.title('Porcentaje de porteros con y sin apariciones')
        plot.show()
        
        
    def graficar_cleansheets():
        '''Grafica los penales salvados por portero usando una gráfica de barras'''
        figure3 = plot.figure(figsize = (20, 15))
        plot.bar(porteros, penales_salvados, color = 'darkorange')
        plot.title('Penales salvados por portero')
        plot.xlabel('Porteros')
        plot.ylabel('Penales salvados')
        plot.xticks(rotation=90)
        plot.show()
        
        
    def graficar_penales_salvados():
        '''Grafica las clean sheets por portero usando una gráfica de barras'''
        figure4 = plot.figure(figsize = (20, 15))
        plot.bar(porteros, cleansheets, color = 'greenyellow')
        plot.title('Clean sheets por portero')
        plot.xlabel('Porteros')
        plot.ylabel('Clean sheets')
        plot.xticks(rotation=90)
        plot.show()
        
        
    def graficar_errores_portero():
        '''Grafica el promedio de errores por partido de cada portero usando una gráfica de barras'''
        figure4 = plot.figure(figsize = (20, 15))
        plot.bar(porteros, promedio_errores, color = 'salmon')
        plot.title('Promedio de errores por partido de cada portero')
        plot.xlabel('Porteros')
        plot.ylabel('Promedio de errores por partido')
        plot.xticks(rotation=90)
        plot.show()
        
        
    def graficar_goles_portero():
        '''Grafica el promedio de goles concedidos por partido de cada portero usando una gráfica de barras'''
        figure5 = plot.figure(figsize = (20, 15))
        plot.bar(porteros, promedio_goles, color = 'red')
        plot.title('Promedio de goles concedidos por partido de cada portero')
        plot.xlabel('Porteros')
        plot.ylabel('Promedio de goles concedidos por partido')
        plot.xticks(rotation=90)
        plot.show()


    print('\nGráficas de los datos sobre los porteros de la Premier League\n')   
    graficar_apariciones_portero() #Llama a las fucniones de las gráficas y muestra una por una
    graficar_porcentaje_apariciones()
    graficar_cleansheets()
    graficar_penales_salvados()
    graficar_errores_portero()
    graficar_goles_portero()
    

def imprimir_nombres_porteros():
    '''Obtiene e imprime una lista de los nombres de todos los porteros de la Premiere League'''
    archivo = open('data_gk_pl.csv')
    entrada = csv.reader(archivo)
    
    datos = list(entrada)[1:]
    
    porteros = []
    for renglon in datos:
        porteros.append(renglon[1])
    print('\nPorteros de la Premier League:\n', )
    print('\n'.join(porteros))  #Este formato imprime cada elemento en la lista porteros, en este caso los nombres de cada portero, en un renglón diferente


def obtener_informacion_portero(portero):
    '''Obtiene e imprime la ficha informativa del portero en específico que el usuario ingresa (que se usa como parámetro)'''
    archivo = open('data_gk_pl.csv')
    entrada = csv.reader(archivo)
    
    datos = list(entrada)[1:]
    
    if portero in (item for sublist in datos for item in sublist): #Esta condicional checa si el ususario ingresó un nombre que está en los datos.
        #(item for sublist in datos for item in sublist) checa si un elemento está en la lista de listas
        for renglon in datos:
            if renglon[1].startswith(portero):
                apariciones = int(renglon[2])
                salvadas = renglon[6]
                cleansheets = renglon[3]
                penales_salvados = renglon[7]
                goles = renglon[20]
                asistencias = renglon[21]
                pases = int(renglon[22])
                goles_concedidos = renglon[14]
                errores = renglon[15]
                autogoles = renglon[16]
                tarjetas_amarillas = renglon[17]
                tarjetas_rojas = renglon[18]
    
        print('\nFicha informativa de:', portero + '\n')        
        print('Apariciones:', apariciones)
        print('Salvadas:', salvadas)
        print('Clean sheets:', cleansheets)
        print('Penales salvados:', penales_salvados)
        print('Goles anotados:', goles)
        print('Asistencias:', asistencias)
        print('Pases completados:', "{:,}".format(pases))
        print('Goles concedidos:', goles_concedidos)
        print('Errores que terminaron en gol:', errores)
        print('Autogoles:', autogoles)
        print('Tarjetas amarillas:', tarjetas_amarillas)
        print('Tarjetas rojas:', tarjetas_rojas)
        
    else:      #Si el nombre no está en los datos, se imprime un mensaje para que el usuario sepa
        print('\nLo sentimos, ese jugador no es portero de la Premier League.')     
        

def main():
    decision = input('''\nEn este programa se analiza información recolectada sobre los porteros
de la Premier League de Inglaterra hasta la fecha de 10 de octubre de 2021.
¿Qué información quieres ver? (Ingresa el número del apartado que quieres ver. Para salir escribe 'exit')
1. Resúmen
2. Estadísticas
3. Gráficas
4. Ficha informativa de un portero
\n''')   #Se imprime el menú con todas las opciones que el programa ofrece y se inicializa la condición del while
    
    while decision != 'exit':    #Se usa un while loop para que el menú se despliegue y el programa corra hasta que el usuario escriba 'exit'
        if decision == '1':
            resumir_datos()
        elif decision == '2':
            obtener_estadisticas()
        elif decision == '3':
            graficar_informacion()
        elif decision == '4':
            imprimir_nombres_porteros()
            portero = input('\n¿Cuál es el nombre del portero del que quieres información? ')
            obtener_informacion_portero(portero)
        else:
            print('\nNúmero no válido, intente de nuevo.')     #Por si el usuario ingresa un número o tecla que no viene en el menú
        decision = input('''\nEn este programa se analiza información recolectada sobre los porteros
de la Premier League de Inglaterra hasta la fecha de 10 de octubre de 2021.
¿Qué información quieres ver? (Ingresa el número del apartado que quieres ver. Para salir escribe 'exit')
1. Resúmen
2. Estadísticas
3. Gráficas
4. Ficha informativa de un portero
\n''')   #Se imprime otra vez el menú para que se pueda cambiar la condición del while y el usuario pueda salir del programa o loop
    
    print('\nGracias por usar este programa.')
    
main()
