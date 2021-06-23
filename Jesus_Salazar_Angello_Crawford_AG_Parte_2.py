# -*- coding: utf-8 -*-
"""
Creado por:
Jesus Salazar Araya, Angello Crawford Clark
"""
#Librerías utilizadas
import numpy as np
import matplotlib.pyplot as plt



#Se define el tamaño de la población, y la cantidad de ciudades que existen
tamañoPoblación = 200
nCiudades = 50


  
    
def Distancia_entre_vecinos(Ciudad_inicial,Ciudad_vecina,coordenadas_x,coordenadas_y):
    Lista_x_coordenada_ciudad = []
    Lista_y_coordenada_ciudad = []
    distancia_euclideana = 0
    
    Lista_x_coordenada_ciudad.append(coordenadas_x[int(Ciudad_inicial)])
    Lista_x_coordenada_ciudad.append(coordenadas_x[int(Ciudad_vecina)])
    Lista_y_coordenada_ciudad.append(coordenadas_y[int(Ciudad_inicial)])
    Lista_y_coordenada_ciudad.append(coordenadas_y[int(Ciudad_vecina)])
    
    delta_X = Lista_x_coordenada_ciudad[1]-Lista_x_coordenada_ciudad[0]
    delta_Y = Lista_y_coordenada_ciudad[1]-Lista_y_coordenada_ciudad[0]
    distancia_euclideana = np.sqrt(delta_X**2 + delta_Y**2)
    
    return distancia_euclideana 
    
def InicializaciónModificada(tamañoPoblación, nCiudades):
    poblacion = np.zeros((tamañoPoblación, nCiudades))
    for i in range(tamañoPoblación):
        nodo_Aleatorio = np.random.randint(0,nCiudades)
        Ciudad_inicial = nodo_Aleatorio
        
        lista_Ciudades_recorridas = []
        lista_Ciudades_recorridas.append(Ciudad_inicial)
        
        
        #Para cada cromosoma
        for j in range(nCiudades):
            
            #Calcule la distancia entre cada ciudad
            listaR = []
            lista_Ciudad = []
            for Ciudad_vecina in range(nCiudades):
                
                if Ciudad_vecina not in lista_Ciudades_recorridas and Ciudad_inicial != Ciudad_vecina:
                    R = Distancia_entre_vecinos(Ciudad_inicial,Ciudad_vecina,coordenadas_x,coordenadas_y)
                    
                    lista_Ciudad.append(Ciudad_vecina)
                    listaR.append(R)
                else:
                    pass
             
           
            if len(lista_Ciudad) != 0:
                valorMin = min(listaR)
                index = listaR.index(valorMin)
                Ciudad_vecina_mas_cercana = lista_Ciudad[index]
                
                
                lista_Ciudades_recorridas.append(Ciudad_vecina_mas_cercana)
                Ciudad_inicial = Ciudad_vecina_mas_cercana
            poblacion[i, j] = lista_Ciudades_recorridas[j]
           
    
    return poblacion





def DecodificaciónCromosoma(cromosoma,coordenadas_x,coordenadas_y):
    """Esta función se encarga de calcular la distancia total que existe en el recorrido, para
    el cromosoma(trayecto) correspondiente"""
    
    #Se define una lista que alberga las coordenas del cromosoma correspondiente
    Lista_coordenadas_x_cromosoma = []
    Lista_coordenadas_y_cromosoma = []
    #Se inicializa la distancia euclideana del trayecto
    distancia_euclideana = 0
    #La cantidad de ciudades va a ser la longitud del cromosoma
    nCiudades = len(cromosoma)
    
    #Se recorre el cromosoma
    for i in cromosoma:
        
        #Las siguientes listas se encargan de albergar las coordenadas
        #Como el cromosoma contiene la ciudad respectiva, se encuentran
        #las coordenadas en x y en y para la respectiva ciudad
        Lista_coordenadas_x_cromosoma.append(coordenadas_x[int(i)])
        Lista_coordenadas_y_cromosoma.append(coordenadas_y[int(i)])
        
    """Dado que la trayectoria es cerrada, se debe calcular la distancia entre el último valor del trayecto y el primero"""
    #Se calcula la diferencia del paso en x y en y, para posteriormente calcular la distancia euclideana entre el valor final y el inicial.    
    delta_1_x = Lista_coordenadas_x_cromosoma[nCiudades-1]-Lista_coordenadas_x_cromosoma[0]
    delta_1_y = Lista_coordenadas_y_cromosoma[nCiudades-1]-Lista_coordenadas_y_cromosoma[0]
    distancia_1 = np.sqrt(delta_1_x**2 + delta_1_y**2)
       
    #Este ciclo for se usa para calcular la distancia euclideana en el trayecto
    for j in range(0,nCiudades-1):
        
        delta_X = Lista_coordenadas_x_cromosoma[j+1]-Lista_coordenadas_x_cromosoma[j]
        delta_Y = Lista_coordenadas_y_cromosoma[j+1]-Lista_coordenadas_y_cromosoma[j]
        distancia_euclideana += np.sqrt(delta_X**2 + delta_Y**2)
    #Se suma la distancia de todo el trayecto y la trayectoria entre la ciudad final e inicial
    distancia_total = distancia_1 + distancia_euclideana
    
    return distancia_total
    
    

def EvaluarIndividuo(distancia_euclideana):
    """
    Función que evalúa el ajuste del individuo. Se define como el inverso de la distancia euclideana del trayecto
    """
    ValorF = 1/distancia_euclideana
    
    return ValorF



def OperadorMutación(cromosoma, p_mut):
    """
    Función que realiza la mutación de un cromosoma con probabilidad p_mut
    Se encarga de tomar dos posiciones aleatorias e intercambiar los valores respectivos en dichas posiciones.
    Esta función se encarga de realizar de 3 a 10 mutaciones por cromosoma o individuo
    """
    nCiudades = len(cromosoma)
    #Se hace una copia del cromosoma original
    cromosomaMutado = np.copy(cromosoma)

    #Se escoge un numero aleatorio entre 0 y 1
    nAleatorio = np.random.random()
    
    #Numero de mutaciones a aplicar (de 3 a 10)
    numero_mutaciones = np.random.randint(3,10)
    
    for i in range(numero_mutaciones):
        #Se escoge aleatoriamente las posiciones a mutar
        Pos1 = np.random.randint(0,nCiudades)
        Pos2 = np.random.randint(0,nCiudades)
        #Se actualiza del cromosoma, para que tome los valores de mutaciones nuevas y no del original, sin mutar
        cromosoma_Mutado_actualizado = np.copy(cromosomaMutado)
        #Si el número aleatorio está dentro de la probabilidad de mutación, se hace la mutación
        if (nAleatorio < p_mut):
            #Se intercambian los valores en las posiciones respectivas
            cromosomaMutado[Pos1] = cromosoma_Mutado_actualizado[Pos2]
            cromosomaMutado[Pos2] = cromosoma_Mutado_actualizado[Pos1]
            
        else:
            pass
           
    return cromosomaMutado

"""Se toma el archivo CoordenadasCiudades.txt y se modifica manualmente removiéndole 
ciertos paréntesis y comas para leerlo de una forma más sencilla.
El archivo de donde se leen las ciudades se llama Coordenadas_Ciudades_modificado.txt y 
debe estar en la misma carpeta donde se encuentra el código."""
coordenadas_x_str = []
coordenadas_y_str = []
with open("Coordenadas_Ciudades_modificado.txt") as f:
     for line in f:
         x, y = line.split(", ")
         coordenadas_x_str.append(x)
         coordenadas_y_str.append(y)


#Convierte las coordenadas de strings a floats
coordenadas_x = [float(i) for i in coordenadas_x_str]

coordenadas_y = [float(i) for i in coordenadas_y_str]





def ValorFP(poblacion):
    """Función que actualiza la lista de los valores de ajuste F para la población"""
    lista_valorF=[]
    for i in range(len(poblacion)):
        cromosoma = poblacion[i]
        distancia_euclideana = DecodificaciónCromosoma(cromosoma,coordenadas_x,coordenadas_y)
        valorF_ajuste = EvaluarIndividuo(distancia_euclideana)
        lista_valorF.append(valorF_ajuste)
    lista_valorFtotal.append(lista_valorF)
    return



def MejorCamino(lista_valorFtotal,lista_Ptotal):
    """Función que calcula el mejor camino dado una lista 
    total de valores F y otra lista de poblaciones totales."""
    #El valor de ajuste máximo comienza en 0
    valorFmax=0
    for i in range(nGeneraciones):
        for k in  range(tamañoPoblación):
            valorFA=lista_valorFtotal[i][k]
            #Si el valor de ajuste F es mayor al valor previo máximo de F
            #Se actualiza el valor Fmax
            if valorFA>valorFmax:
                valorFmax=valorFA
                Imax=i
                Kmax=k
            else:
                pass
    #El mejor camino guarda el mejor trayecto recorrido
    mejor_camino=lista_Ptotal[Imax][Kmax]
    
    return mejor_camino


def Grafica(lista_valorFtotal):
    """Función que grafica la evolución de los valores de ajuste de población."""
    
    matriz_ValordeAjuste=np.asarray(lista_valorFtotal)
    #Se calcula el promedio de ajuste de la matriz de valores de ajuste
    PromedioAjuste = np.mean(matriz_ValordeAjuste,1)
    #Se calcula el máximo ajuste de la matriz de valores de ajuste
    MaximoAjuste = np.max(matriz_ValordeAjuste,1)
    
    fig,ax = plt.subplots(dpi=120)
    ax.plot(PromedioAjuste, label ='ajuste promedio')
    ax.plot(MaximoAjuste, label = 'ajuste máximo')
    
    ax.set_title('Evolución de los valores de ajuste de la población')
    ax.set_xlabel('generaciones')
    ax.set_ylabel('valores de ajuste')
    ax.legend(loc='best')
    plt.show()
        
#Se inicializa la población   
poblacion = InicializaciónModificada(tamañoPoblación, nCiudades)
                                   
#Se inicializan las distintas listas necesarias
lista_valorFtotal = []
lista_Ptotal = []
lista_valorF = []

#Se define la cantidad de generaciones y la probabilidad de mutación
nGeneraciones = 400
P_Mut = 0.5

 #Ciclos for que se encargan de realizar las mutaciones respectivas para la población y generación respectiva             
for i in range(nGeneraciones):
    #Se inicializa una lista que contiene las poblaciones mutadas por generación
    PoblacionMutada=[]
    for k in range(0,len(poblacion)):
        #Para la poblacion inicial, k = 0, i = 0, no se muta el cromosoma
        if k == 0 and i ==0:
            cromosoma1 = poblacion[k]
            PoblacionMutada.append(cromosoma1)
        #Para las demás poblaciones, si se dan las mutaciones
        else:
            cromosoma = poblacion[k]
            #Se muta el cromosoma
            cromosoma_mutado = OperadorMutación(cromosoma, P_Mut)
       
            poblacion[k]=cromosoma_mutado
        
            PoblacionMutada.append(cromosoma_mutado)
    #Se actualizan los valores de ajuste F y la lista de población total
    ValorFP(poblacion)
    lista_Ptotal.append(PoblacionMutada) 
    
    
#Se llama a la función que encuentra el mejor camino dada la lista total de valores de ajuste F y de población
mejor_camino_encontrado = MejorCamino(lista_valorFtotal,lista_Ptotal)
#Se encuentra la distancia del mejor camino encontrado
R_mejorCamino = DecodificaciónCromosoma(mejor_camino_encontrado,coordenadas_x,coordenadas_y)
print("La distancia total del mejor camino encontrado es: ", R_mejorCamino)

Grafica(lista_valorFtotal)



"""Se grafica el mejor cromosoma encontrado"""
Coordenadas_MejorCamino_x = []
Coordenadas_MejorCamino_y = []

for h in mejor_camino_encontrado:
    
    Coordenadas_MejorCamino_x.append(coordenadas_x[int(h)])
    Coordenadas_MejorCamino_y.append(coordenadas_y[int(h)])
    
    
#Para que la trayectoria sea cerrada

Coordenadas_MejorCamino_x.append(Coordenadas_MejorCamino_x[0])
Coordenadas_MejorCamino_y.append(Coordenadas_MejorCamino_y[0])


#Gráfica del camino más corto encontrado
fig,ax=plt.subplots(dpi=120)
ax.plot(Coordenadas_MejorCamino_x,Coordenadas_MejorCamino_y, "c-")
ax.plot(Coordenadas_MejorCamino_x,Coordenadas_MejorCamino_y, "ro")
ax.set_title('Camino más corto')
ax.set_xlabel('Coordenada x')
ax.set_ylabel('Coordenada y')
ax.legend(["Camino","Punto en el mapa"])
plt.show()    

#Se hace una lista que va a contener las coordenadas en x y en y del camino más corto
Lista_coordenadas_mejor_camino = np.zeros((51,2))

#Se agregan las coordenadas x y y a la lista
cont_x = 0
cont_y = 0
for i in Coordenadas_MejorCamino_x:
    Lista_coordenadas_mejor_camino[cont_x][0] = i
    cont_x += 1
for j in Coordenadas_MejorCamino_y:
    Lista_coordenadas_mejor_camino[cont_y][1] = j
    cont_y += 1



#Aqui se escribe en un documento txt el camino mas corto encontrado
np.savetxt('caminoMásCorto_AGM.txt',Lista_coordenadas_mejor_camino)




