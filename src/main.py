import variables
from Analise import lerArquivo
from OrdenarArquivo import ordernarArquivoExterno

arquivo = open(variables.arquivo_externo_entrada, "r", encoding='utf8') #Ler arquivo

#Calling the functions
lerArquivo(arquivo)
ordernarArquivoExterno()

print("O Speech Word Count realizou a análise com sucesso.\nAbra o arquivo arquivo_saida.txt e confira!\n")