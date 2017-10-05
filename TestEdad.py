import unittest

from edad import Edad

class EdadTest(unittest.TestCase):

	def setUp(self):
		self.ed = Edad()

	def test_edad_igual_0(self):
		self.ed.edad(0)
		self.assertEquals(self.ed.obtener_resultado(),'No Existes')

	def test_edad_igual_12(self):
		self.ed.edad(12)
		self.assertEquals(self.ed.obtener_resultado(),'Eres Nino')

	def test_edad_igual_17(self):
		self.ed.edad(17)
		self.assertEquals(self.ed.obtener_resultado(),'Eres Adolescente')

	def test_edad_igual_64(self):
		self.ed.edad(64)
		self.assertEquals(self.ed.obtener_resultado(),'Eres Adulto')

	def test_edad_igual_119(self):
		self.ed.edad(119)
		self.assertEquals(self.ed.obtener_resultado(),'Eres Adulto Mayor')

	def test_edad_igual_L(self):
		self.ed.edad('L')
		self.assertEquals(self.ed.obtener_resultado(),'No Valido')

	def test_edad_igual_135(self):
		self.ed.edad(135)
		self.assertEquals(self.ed.obtener_resultado(),'Eres Mumm-Ra')

if __name__ == '__main__':
	unittest.main()