import variables

def lerArquivo(arquivo):
	linhas = arquivo.readlines()
	contarPalavrasNoTexto(linhas)

def contarPalavrasNoTexto(linhas):
	palavrasTexto = {} #Create a Python dictionary
	
	#Percorre todas as palavras do arquivo e salva em um dicionário
	for linha in linhas:
		#palavras = linha.lower().split(' ')
		palavras = linha.lower().replace('.',' ').replace(':',' ').replace(',',' ').replace(';',' ').replace('?',' ').replace('¿',' ').replace("'",' ').replace('"',' ').replace('/',' ').replace('|',' ').replace('\\',' ').replace('(',' ').replace(')',' ').replace('[',' ').replace(']',' ').replace('{',' ').replace('}',' ').split(' ') #replace(' ','').

		#Adiciona palavras ao dicionário
		for palavra in palavras:
			palavrasTexto[palavra] = palavrasTexto.get(palavra, 0) + 1
	
	detectarPalindromos_e_imprimir(palavrasTexto)

def limparConteudoArquivoExterno(nomeArquivo):
	file = open(nomeArquivo, "w", encoding='utf8')
	file.truncate(0)
	file.close()
	
	#Limpa o conteúndo do arquivo externo (método: overwrite)
	#with open('arquivo_saida.txt', 'w') as arquivo_externo_auxiliar:
	#	print('', file=arquivo_externo_auxiliar)

def detectarPalindromos_e_imprimir(conteudo):
	limparConteudoArquivoExterno(variables.arquivo_externo_saida1)

	#Percorrer todos os items do dicionário
	for key, ocorrencias in conteudo.items():
		palavra_normal = str(key).strip().lower()
		palavra_invertida = ''
		palindromo = False
		
		for letra in range(len(palavra_normal) -1 , -1, -1):
			palavra_invertida += palavra_normal[letra]

		if palavra_normal == palavra_invertida:
			palindromo = True
		else:
			palindromo = False

		#Display on terminal
		#print("{:<30} {:<30} {:<30}".format(ocorrencias, palavra_normal, palindromo))
		
		#Exportar os resultados para um arquivo externo (método: append)
		with open(variables.arquivo_externo_saida1, 'a', encoding='utf8') as arquivo_externo:
			#print("{:<30} {:<30} {:<30}".format(palavra_normal, ocorrencias, palindromo), file=arquivo_externo)
			print("{},{},{},".format(palavra_normal, ocorrencias, palindromo), file=arquivo_externo)