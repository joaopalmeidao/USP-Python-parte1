import math
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

    # FUNCÕES À FAZER:

#calcula a quantidade de caracteres
def quantidade_caracteres_total(conjuntos): 
    quantidade_caracteres = 0
    for conjunto in conjuntos:
        quantidade_caracteres += len(conjunto)
    return quantidade_caracteres

# Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.
def compara_assinatura(as_a, as_b): 
    somatorio = 0
    for i in range(0, 6):
        somatorio += math.fabs(as_a[i] - as_b[i])
    somatorio = (somatorio / 6)
    return round(somatorio, 2)

# Essa funcao recebe um texto e deve devolver a assinatura do texto.
def calcula_assinatura(texto):
    frases = []
    palavras = []
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases += separa_frases(sentenca)
    for frase in frases:
        palavras += separa_palavras(frase)
    wal = quantidade_caracteres_total(palavras)/len(palavras)
    ttr = n_palavras_diferentes(palavras)/len(palavras)
    hlr = n_palavras_unicas(palavras)/len(palavras)
    sal = quantidade_caracteres_total(sentencas) / len(sentencas)
    sac = len(frases) / len(sentencas)
    pal = quantidade_caracteres_total(frases) / len(frases)
    return [wal, ttr, hlr, sal, sac, pal]

# Essa funcao recebe uma lista de textos e uma assinatura ass_cp e 
# deve devolver o numero (1 a n) do texto com maior probabilidade de 
# ter sido infectado por COH-PIAH.
def avalia_textos(textos, ass_cp):
    comparacoes = []
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        comparacao = compara_assinatura(assinatura, ass_cp)
        comparacoes.append(comparacao)
    menor_comparacao = min(comparacoes)
    indice_menor_comparacao = (comparacoes.index(menor_comparacao) + 1)
    print("O autor do texto {} está infectado com COH-PIAH".format(indice_menor_comparacao))
    return indice_menor_comparacao

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    avalia_textos(textos, le_assinatura())

if __name__==main():
    main()
