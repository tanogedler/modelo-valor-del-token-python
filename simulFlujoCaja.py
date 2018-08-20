# Se implementa el flujo de caja trimestral 
# a partir del Valor Neto Actual del movimiento de
# transacciones de los tokens, la cantidad de usuarios por 
# trimestres y la cantidad de tokens disponibles
from simulCantidadUsuarios import CantidadUsuarios
#Clase que maneja los valores relacionados a los tokens



class Token:
	def __init__(self, totalTokens, valorTxn, cantidadTxnsPorUsuario, cantidadAños):
		self.totalTokens = totalTokens
		self.valorTxn = valorTxn
		self.cantidadTxnsPorUsuario = cantidadTxnsPorUsuario
		self.cantidadAños = cantidadAños

	def get_totalTokens(self):
		return self.totalTokens

	def get_valorTxn(self):
		return self.valorTxn

	def get_cantidadTxnsPorUsuario(self):
		return self.cantidadTxnsPorUsuario

	def get_cantidadAños(self):
		return self.cantidadAños

	def tasaDescuento(self, cantidadAños):
		cantidadTrimestres = self.cantidadAños * 4		
		listaTasas = [0.0] *cantidadTrimestres
		for i in range(1,cantidadTrimestres + 1):
			tmp = (-1/40) * i +  31/40
			ti = (1 + tmp)**(1/4) -1
			listaTasas[i -1] = ti
		return listaTasas


	# Modelamos el fondo de reserva:
	def fondoReserva(self, totalTokens):
		tokenPorEtapas = []
		tokenPorEtapas.append(0.3* self.totalTokens)
		tokenPorEtapas.append(0.2 * self.totalTokens)
		tokenPorEtapas.append(0.15 * self.totalTokens)
		tokenPorEtapas.append(0.1 * self.totalTokens)
		tokenPorEtapas.append(0.05 * self.totalTokens)

		fondoPorEtapas = []
		for etapa in range(0,len(tokenPorEtapas)):
			fondoPorEtapas.append(0.1 * tokenPorEtapas[etapa])

		distribucionFondo = {}
		distribucionFondo["fundadores"] = [0.1 * self.totalTokens]
		distribucionFondo["primeraEtapa"] = [fondoPorEtapas[0]]
		distribucionFondo["segundaEtapa"] = [fondoPorEtapas[1]]
		distribucionFondo["terceraEtapa"] = [fondoPorEtapas[2]]
		distribucionFondo["cuartaEtapa"] = [fondoPorEtapas[3]]
		distribucionFondo["quintaEtapa"] = [fondoPorEtapas[4]]
		return distribucionFondo


