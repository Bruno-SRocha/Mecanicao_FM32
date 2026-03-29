#Titulo
print('     Pergunte ao Mecanicão\n'.upper())
print('===============================\nManutenção das prensas FM-32\n===============================\n')
sintoma=input('Qual é o sintoma?\n')
#Barulho/Ruído
if sintoma.lower()=='barulho' or sintoma.lower()=='barulho excessivo' or sintoma.lower()=='ruído' or sintoma.lower()=='ruído excessivo':
	filtro=input('O filtro de óleo está limpo?\n')
	if filtro.lower()=='não' or filtro.lower()=='nao' or filtro.lower()=='no' or filtro.lower()=='n':
		print('Limpe o filtro de oléo.')
	#Bomba de paletas
	else:
		bomba=input('A bomba de paletas já foi manutenida?\n')
		if bomba.lower()=='não' or bomba.lower()=='n' or bomba.lower()=='nao':
			print('Faça a revisão da bomba de paletas.')
		else:
			print('Vish... Chama o mestrão.')
#Baixo desempenho
elif sintoma.lower()=='baixo desempenho' or sintoma.lower()=='pouca pressão' or sintoma.lower()=='pouca pressao' or sintoma.lower()=='baixa pressão' or sintoma.lower()=='baixa pressao':
	#Nível de óleo
	oleo=input('O nível do óleo está acima do primeiro visor do tanque (80 litros)?\n')
	if oleo.lower()=='não' or oleo.lower()=='n' or oleo.lower()=='nao':
		print('Complete o nível de óleo (AW 46).')
	#Vazamento de óleo
	else:
		vazamento=input('Identificou algum vazamento de óleo?\n')
		if vazamento.lower()=='sim' or vazamento.lower()=='s':
			print('Elimine o vazamento. Caso o vazamento esteja dentro do poço, na parte inferior do corpo da prensa, é provavél que seja necessário efetuar a troca da anilha ou da sola.')
		#Pressão de Alta
		else:
			pressao_a=input('A pressão de Alta atinge 2800kg/cm²?\n')
			#Intensificador
			if pressao_a.lower()=='não' or pressao_a.lower()=='n' or pressao_a.lower()=='nao':
				intensificador=input('O êmbolo do intensificador de pressão continua levantado mesmo após a Descarga ter sido efetua repetidas vezes?\n')
				if intensificador.lower()=='sim' or intensificador.lower()=='s':
					print('Faça a revisão do intensificador de pressão.')
				#Pressão de Baixa
				else:
					pressao_b=input('A pressão de Baixa atinge 1500kg/cm²?\n')
					if pressao_b.lower=='não' or pressao_b.lower()=='n' or pressao_b.lower()=='nao':
						print('Vish... Chama o mestrão.')
					#Retenção da pressão de Baixa
					else:
						retencao_b=input('A rede mantém a pressão de Baixa quando o botão deixa de ser pressionado?\n')
						if retencao_b.lower()=='não' or retencao_b.lower()=='n' or retencao_b.lower()=='nao':
							valvula_ret=input('As duas válvulas de retenção foram manutenidas?\n')
							if valvula_ret.lower()=='não' or valvula_ret.lower()=='n' or valvula_ret.lower()=='nao':
								print('Faça a revisão das duas válvulas de retenção.')
							#Válvula reguladora de vazão
							else:
								valvula_vaz=input('A válvula reguladora de vazão foi manutenida?\n')
								if valvula_vaz.lower()=='não' or valvula_vaz.lower()=='n' or valvula_vaz.lower()=='nao':
									print('Faça a revisão da válvula reguladora de vazão.')
								else:
									print('Vish... Chama o mestrão.')
						else:
							print('Ajuste a válvula reguladora de pressão na saída da bomba de paletas. Caso o problema persista, faça a revisão do intensificador de pressão.')					
			#Retenção da pressão de Alta
			else:
				retencao_a=input('A rede mantém a pressão de Alta quando o botão deixa de ser pressionado?\n')
				if retencao_a.lower()=='não' or retencao_a.lower()=='n' or retencao_a.lower()=='nao':
					valvula_ret=input('As duas válvulas de retenção foram manutenidas?\n')
					if valvula_ret.lower()=='não' or valvula_ret.lower()=='n' or valvula_ret.lower()=='nao':
						print('Faça a revisão das duas válvulas de retenção.')
					#Válvula reguladora de vazão
					else:
						valvula_vaz=input('A válvula reguladora de vazão foi manutenida?\n')
						if valvula_vaz.lower()=='não' or valvula_vaz.lower()=='n' or valvula_vaz.lower()=='nao':
							print('Faça a revisão da válvula reguladora de vazão.')
						else:
							print('Vish... Chama o mestrão.')
				else:
					print('Então não tem nada de errado com a prensa. Francamente hein, mestre.')		
#Mestrão resolve
else:
	print('Vish... Chama o mestrão.')