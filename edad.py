class Edad():

	def __init__(self):
		self.resultado = 0

	def obtener_resultado(self):
		return self.resultado

	def edad(self, num1):
		if num1 == 0:
			self.resultado = 'No Existes'
		elif num1 < 13:
			self.resultado = 'Eres Nino'
		elif num1 < 18:
			self.resultado = 'Eres Adolescente'
		elif num1 < 65:
			self.resultado = 'Eres Adulto'
		elif num1 < 120:
			self.resultado = 'Eres Adulto Mayor'
		elif type(num1) is str:
			self.resultado = 'No Valido'
		else:
			self.resultado = 'Eres Mumm-Ra'