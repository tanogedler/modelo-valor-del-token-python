# Se implementa la funcion logistica para modelar la 
# cantidad de usuarios de la lataforma.
import math as mt
#Definicion de la clase que modela la cantidad de usuarios

class CantidadUsuarios:
	def __init__(self, maximo, cantidadAños, constanteK):
		self.maximo = maximo
		self.cantidadAños = cantidadAños
		self.constanteK = constanteK		

	def get_maximo(self):
		return self.maximo

	def get_cantidadAños(self):
		return self.cantidadAños
	
	def get_constanteK(self):
		return self.constanteK

	#Funcion logistica 	
	def funcionLogistica(self, maximo, cantidadAños, constanteK):
		cantidadTrimestres = self.cantidadAños * 4
		valores = [0.0] * cantidadTrimestres
		puntoMedio = cantidadTrimestres // 2
		for x in range(1, cantidadTrimestres + 1):
			y = int(self.maximo //(1 + mt.exp(- self.constanteK * (x - puntoMedio))))
			valores[x - 1] = y
		return valores