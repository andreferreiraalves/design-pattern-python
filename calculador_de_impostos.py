# -*- coding: UTF-8 -*-

class Calculador_de_impostos(object):
	def realiza_calculo(self, orcamento, importo):
		icms_calculado = importo(orcamento)
		print(icms_calculado)

if __name__ == '__main__':
	from orcamento import Orcamento
	from impostos import calcula_ICMS, calcula_ISS

	orcamento = Orcamento(500.0)

	calculador_de_impostos = Calculador_de_impostos()

	calculador_de_impostos.realiza_calculo(orcamento, calcula_ISS)
	calculador_de_impostos.realiza_calculo(orcamento, calcula_ICMS)
