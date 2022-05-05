#Fiz um arquivo de testes para facilitar a checagem das condições(test_itau.py)

class PessoaFisica:

	#Variaveis de classe
	id_transferencia = 1
	saldo = 0

	def __init__(self, nome, agencia, conta, cpf):
		self.nome = nome	
		self.agencia = agencia
		self.conta = conta
		self.cpf = cpf
		
class Emissor(PessoaFisica):
	"""Somente o emissor pode realizar transferencias, exceto se o emissor realizar transferencias para outra
	   conta dele"""
	def Transferencia(self, valor_transferencia, tipo, receptor):
		"""Varios testes relacionados à condição do problema de lógica -
		 valor limite, contas iguais, transf. entre duas contas do mesmo emissor"""
		if valor_transferencia <= 0:
			print('Sua transferência não foi completada pois o valor transferido não pode ser nulo ou negativo.')
			return 'Zero'

		if self.conta == receptor.conta:
			print('Sua transferência não foi completada pois o número da conta bancária do receptor é a mesma do operador.')
			return 'Contas coincidentes'

		if not isinstance(receptor, Receptor) and self.cpf != receptor.cpf and self.nome != receptor.nome:
			print('Sua transferência não foi completada pois é possível realizar apenas transferências entre emissor e receptor ou o emissor não há posse de ambas as contas.')
			return 'Emissor emissor'


		if tipo == 'PIX' and valor_transferencia > 5000:
			print('Sua transferência não foi completada pois o valor limite de transferência via PIX é de R$5000,00 - Valor recebido: R${}.'.format(valor_transferencia))
			return 'PIX valor excedido'


		if tipo == 'DOC' and valor_transferencia < 10000:
			print('Sua transferência não foi completada pois o valor mínimo de transferência via DOC é de R$10.000,00 - Valor recebido: R${}.'.format(valor_transferencia))
			return 'DOC valor mínimo'


		if tipo == 'TED':
			if valor_transferencia < 5000:
				print('Sua transferência não foi completada pois o valor mínimo de transferência via TED é de R$5000,00 - Valor recebido: R${}.'.format(valor_transferencia))
				return 'TED valor mínimo'

			elif valor_transferencia > 10000:
				print('Sua transferência não foi completada pois o valor limite de transferência via TED é de R$10000,00 - Valor recebido: R${}.'.format(valor_transferencia))	
				return 'TED valor excedido'

		"""Realização da transferência: o dinheiro entra na conta do emissor,
		 e em seguida sai da conta do emissor para a conta do receptor"""
		self.saldo += valor_transferencia
		self.saldo, receptor.saldo = self.saldo -valor_transferencia, receptor.saldo +valor_transferencia

		#Formatação para o formato R$XX,XX
		emissor_reais, emissor_centavos = str(float(self.saldo)).split('.')
		receptor_reais, receptor_centavos = str(float(receptor.saldo)).split('.')
		emissor_centavos, receptor_centavos = emissor_centavos + '0', receptor_centavos + '0'

		print('Sua transferência foi realizada com sucesso!')
		print('Saldo do emissor: R$ {},{}'.format(emissor_reais, emissor_centavos[:2]))
		print('Saldo do receptor: R$ {},{}'.format(receptor_reais, receptor_centavos[:2]))

		#Atualizando ID da transferência
		PessoaFisica.id_transferencia += 1

		return 'Sucesso'
		
class Receptor(PessoaFisica):
	#Classe que somente recebe o valor da transferência
	pass


#As strings no return são para identificar a conclusão da transferência para os testes no arquivo test_itau.py

"""Formato: Classe('Nome','Agencia','Conta','CPF')
			Emissor.Transferencia(Valor,'Tipo de Transferência','Receptor')"""
			
# emissor1 = Emissor('Joao', '001', 1234, '123.123.123-12')
# receptor1 = Receptor('Maria', '002', 1335, '112.113.114-15')

# emissor1.Transferencia(500, 'PIX', receptor1)

	