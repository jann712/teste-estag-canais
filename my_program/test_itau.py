import unittest
from itau import PessoaFisica, Emissor, Receptor


class TestTransferencia(unittest.TestCase):

	def setUp(self):
		print('NOVO TESTE')
		self.emissor = Emissor('Joao', '001', 1234, '123.123.123-12')
		self.receptor = Receptor('Maria', '002', 1335, '112.113.114-15')

	def tearDown(self):
		print()
		pass

	def test_pix(self):
		print('TESTE PIX')
		self.assertEqual(self.emissor.Transferencia(565.56, 'PIX', self.receptor), 'Sucesso')
		self.assertEqual(self.emissor.Transferencia(5001, 'PIX', self.receptor), 'PIX valor excedido')

	def test_doc(self):
		print('TESTE DOC')
		self.assertEqual(self.emissor.Transferencia(15000.75, 'DOC', self.receptor), 'Sucesso')
		self.assertEqual(self.emissor.Transferencia(9000, 'DOC', self.receptor), 'DOC valor mínimo')

	def test_ted(self):
		print('TESTE TED')
		self.assertEqual(self.emissor.Transferencia(7000.25, 'TED', self.receptor), 'Sucesso')
		self.assertEqual(self.emissor.Transferencia(3000, 'TED', self.receptor), 'TED valor mínimo')
		self.assertEqual(self.emissor.Transferencia(12000, 'TED', self.receptor), 'TED valor excedido')

	def test_mesmaConta(self):
		print('TESTE ERRO: MESMA CONTA BANCÁRIA')
		self.receptor.conta = self.emissor.conta
		self.assertEqual(self.emissor.Transferencia(500, 'PIX', self.receptor), 'Contas coincidentes')

	def test_transfEmissor(self):
		print('TESTE ERRO: TRANSFERÊNCIA ENTRE DOIS EMISSORES DIFERENTES')
		emissor2 = Emissor('Marco','003',1553,'114.115.116-17')
		self.assertEqual(self.emissor.Transferencia(500, 'PIX', emissor2), 'Emissor emissor')

		self.receptor.nome, self.receptor.cpf = self.emissor.nome, self.emissor.cpf
		self.assertEqual(self.emissor.Transferencia(500, 'PIX', self.receptor), 'Sucesso')

	def test_zero(self):
		print('TESTE ERRO: VALOR NULO')
		self.assertEqual(self.emissor.Transferencia(0, 'PIX', self.receptor), 'Zero')

	def test_centavos1(self):
		print('TESTE CENTAVOS')
		self.assertEqual(self.emissor.Transferencia(700.98, 'PIX', self.receptor), 'Sucesso')

	def test_centavos2(self):
		print('TESTE CENTAVOS2')
		self.assertEqual(self.emissor.Transferencia(1500.3, 'PIX', self.receptor), 'Sucesso')

	def test_centavos3(self):
		print('TESTE CENTAVOS3')
		self.assertEqual(self.emissor.Transferencia(4900.07, 'PIX', self.receptor), 'Sucesso')

	def test_Emissor(self):
		print('TESTE TRANSFERÊNCIA ENTRE DUAS CONTAS DO MESMO EMISSOR')
		emissor2 = Emissor('Joao', '001', 1220, '123.123.123-12')
		self.assertEqual(self.emissor.Transferencia(25.98, 'PIX', emissor2), 'Sucesso')



if __name__ == '__main__':
	unittest.main()






