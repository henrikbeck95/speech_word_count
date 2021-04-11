import variables
from Analise import limparConteudoArquivoExterno

def ordernarArquivoExterno():
    super_vetor = list()

    with open(variables.arquivo_externo_saida1, 'r', encoding='utf8') as r:
        for linha in r: #arquivo_externo
            aux = linha.strip().split(',')
            aux[1] = int(aux[1])
            #print(aux)

            super_vetor.append(aux)
            #print(aux[0], aux[1],aux[2])
            #print(super_vetor[0])

    palavra = lambda indice: indice[0]
    ocorrencias = lambda indice: indice[1]
    palindromo = lambda indice: indice[2]

    #super_vetor.sort(key=palavra, reverse=True)
    super_vetor.sort(key=ocorrencias, reverse=True)
    # super_vetor.sort(key=palindromo, reverse=True)

    limparConteudoArquivoExterno(variables.arquivo_externo_saida2)

    imprimirArquivoExterno(super_vetor)

def imprimirArquivoExterno(conteudo):
    with open(variables.arquivo_externo_saida2, 'a', encoding='utf8') as arquivo_externo:
        for linha in conteudo:
            #Display on terminal
            #print(linha[0], str(linha[1]), linha[2])
            
            #Exportar os resultados para um arquivo externo (método: append)
            #print("{:<30} {:<30} {:<30}".format(linha[0], str(linha[1]), linha[2]), file=arquivo_externo)
            
            #Verificar se palavra existe ou é vazia
            if linha[0] != '':
                print("{:<30} {:<30} {:<30}".format(linha[0], str(linha[1]), linha[2]), file=arquivo_externo)