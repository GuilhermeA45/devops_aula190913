from unittest import TestCase
from com.Guilherme.operacoes import Operacoes

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
	
	def soma(self):
		self.assertEqual(self.operecoes.soma([1, 5]), 6, 'Deveria ser 6')