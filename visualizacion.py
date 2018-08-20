# Aqui importamos los modulos necesarios para el modelo
import pandas as pd
import numpy as np
import matplotlib as mpl
import math as mt
from simulCantidadUsuarios import CantidadUsuarios
from simulFlujoCaja import Token

#Introducimos valores de prueba
totalToken = int(input("Introduzca máximo de tokens a generar:  "))
maximo = int(input("Introduzca valor máximo de usuarios esperados:  "))
cantidadAños = int(input("Introduzca años de estudio: "))
constanteK = float(input("Introduzca constante de inflexión: "))
cantidadTxnsPorUsuario = int(input("Introduzca cantidad de transacciones por usuario:  "))
valorTxn = int(input("Introduzca el valor de cada transacción con tokens: "))


#Instanciamos las clases con los valores de prueba:
cantidadUsuarios = CantidadUsuarios(maximo, cantidadAños, constanteK)
mi_Token = Token(totalToken, valorTxn, cantidadTxnsPorUsuario, cantidadAños)

#Ejecutamos la funcion logistica:
listaUsuarios = cantidadUsuarios.funcionLogistica(cantidadUsuarios.get_maximo(), 
	cantidadUsuarios.get_cantidadAños(), cantidadUsuarios.get_constanteK())

listaTasas = mi_Token.tasaDescuento(mi_Token.get_cantidadAños())
totalToken = mi_Token.get_totalTokens()

#  Definicion del Flujo de Caja a partir de las transacciones con token
def flujoCaja(valorTxn, cantidadTxnsPorUsuario):
	cantidadTrimestres = cantidadUsuarios.get_cantidadAños() * 4	
	flujoPorTrimestre = [0.0] * cantidadTrimestres
	for i in range(0, len(listaUsuarios)):
		tmp = listaUsuarios[i] * cantidadTxnsPorUsuario * valorTxn 
		flujoPorTrimestre[i] = tmp
	return flujoPorTrimestre

flujoPorTrimestre = flujoCaja(mi_Token.get_valorTxn(), mi_Token.get_cantidadTxnsPorUsuario())

def ValorPresenteNeto():
 	valorPresenteNeto = [] 
 	for i in range(0,len(listaTasas)):
 		valorTerminal = flujoPorTrimestre[len(flujoPorTrimestre)-1] / listaTasas[i]
 		flujoPorTrimestre.append(valorTerminal)
 		tmp = np.npv(listaTasas[i],flujoPorTrimestre)
 		valorPresenteNeto.append(tmp)
 		flujoPorTrimestre.pop(len(flujoPorTrimestre)-1)
 	return valorPresenteNeto

valorPresenteNeto = ValorPresenteNeto()

def ValorToken():
	valorToken = []
	for x in range(0,len(valorPresenteNeto)):
		tmp = valorPresenteNeto[x] / totalToken
		valorToken.append(tmp)
	return valorToken

valorToken = ValorToken()

# Definimos los trimestres:
trimestres = ['2018 - 4', '2019 - 1', '2019 - 2', '2019 - 3', '2019 - 4', '2020 - 1', '2020 - 2', '2020 - 3', '2020 - 4', '2021 - 1', '2021 - 2', '2021 - 3', '2021 - 4', '2022 - 1', '2022 - 2', '2022 - 3', '2022 - 4', '2023 - 1', '2023 - 2', '2023 - 3']
# Graficamos la cantidad de usuarios por trimestres
#Data a ser grafcada
data1 = {'listaUsuarios' : pd.Series(listaUsuarios, index=trimestres)} 		
grafica1 = pd.DataFrame(data1)
grafica1.plot()
#Se muestra como ventana emergente la grafica
mpl.pyplot.show(block=True)

#Grafica del flujo de caja
data2 = {'flujodeCaja' : pd.Series(flujoPorTrimestre, index=trimestres)}
grafica2 = pd.DataFrame(data2)
grafica2.plot(color="r")
#Se muestra como ventana emergente la grafica
mpl.pyplot.show(block=True)


#Gráfica del crecimiento del valor del token
data3 = {'valorToken' : pd.Series(valorToken, index=trimestres)}
grafica3 = pd.DataFrame(data3)
grafica3.plot(color='g')
#Se muestra como ventana emergente la grafica
mpl.pyplot.show(block=True)





