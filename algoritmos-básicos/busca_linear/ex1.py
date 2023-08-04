import time #importando para comparação de tempo necessário para a execução
import random # importando geração do lista com 100 posições numeros aleatórios
"""
Dado uma lista de números inteiros e um valor alvo, crie uma função em Python chamada 
busca_linear que realize uma busca linear na lista e retorne o índice da primeira 
ocorrência do valor alvo. Caso o valor alvo não seja encontrado, retorne -1.
"""

lista = list(range(1, 40)) #Criando uma lista de 1 a 40
random.shuffle(lista) #Embaralhando a lista
valor_alvo = 4

#resolução 1 utilizando estrutura de repetição for 

def busca_linear_1(lista, valor_alvo):
  tamanho = len(lista)
  for indice in range(tamanho):
    if lista[indice] == valor_alvo:
      return indice
      break
  return - 1
    
tempo_inicial = time.time()

resultado1 = busca_linear_1(lista, valor_alvo)

tempo_final = time.time()

if resultado1 != -1:
  print(f'O valor {valor_alvo} foi encontrado na posição {resultado1}')
else:
  print(f'O valor não foi encontrado {resultado1}')

tempo_execucao1 = tempo_final - tempo_inicial
print(f'A funcão 1 foi executada em {tempo_execucao1:4f} segundos')

#resolução 2 utilizando estrutura de repetição while

def busca_linear_2(lista, valor_alvo):
  indice = 0
  tamanho = len(lista)
  while (indice <= tamanho):
    if lista[indice] == valor_alvo:
      return indice 
      break
    indice += 1 
  return -1

tempo_inicial1, tempo_final2 = time.time(), time.time()

resultado2 = busca_linear_2(lista, valor_alvo)

tempo_execucao2 = tempo_final2 - tempo_inicial1

if resultado2 != -1:
  print(f'O valor {valor_alvo} foi encontrado na posição {resultado2}')
else:
  print(f'O valor não foi encontrado {resultado2}')

print(f'A funcão 1 foi executada em {tempo_execucao1:4f} segundos')



"""

  O funcionamento das duas funções é semelhante, e percebe-se isso no tempo de execução das mesmas, 
  que é igual. Basicamente a busca linear é buscar o elemento percorrerendo a lista ou um array todo de forma sequencial buscando encontrá-lo.
  Este algoritmo, funciona com complexidade de O(n) onde o n é o tamanho da entrada. É importante ressaltar que a busca sequencial, funciona 
  em listas não ordenadas enquanto a busca binária, só funciona em listas ordenadas. A busca binária ainda será explicada por aqui :)


  Você pode ver o resultado, desta função copiando este código e executando na sua máquina, ou então rodando em algum ambiente virtual como o replit.

"""
