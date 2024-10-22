# -*- coding: utf-8 -*-

class Vertice:

  def __init__(self, rotulo, distancia_objetivo):
    self.rotulo = rotulo
    self.visitado = False
    self.distancia_objetivo = distancia_objetivo
    self.adjacentes = []

  def adiciona_adjacente(self, adjacente):
    self.adjacentes.append(adjacente)

  def mostra_adjacentes(self):
    for i in self.adjacentes:
      print(i.vertice.rotulo, i.custo)

class Adjacente:
  def __init__(self, vertice, custo):
    self.vertice = vertice
    self.custo = custo

    # Novo atributo
    self.distancia_aestrela = vertice.distancia_objetivo + self.custo
        
class Grafo:
  def __init__(self):
    self.arad = Vertice('Arad', 366)
    self.zerind = Vertice('Zerind', 374)
    self.oradea = Vertice('Oradea', 380)
    self.sibiu = Vertice('Sibiu', 253)
    self.timisoara = Vertice('Timisoara', 329)
    self.lugoj = Vertice('Lugoj', 244)
    self.mehadia = Vertice('Mehadia', 241)
    self.dobreta = Vertice('Dobreta', 242)
    self.craiova = Vertice('Craiova', 160)
    self.rimnicu = Vertice('Rimnicu', 193)
    self.fagaras = Vertice('Fagaras', 178)
    self.pitesti = Vertice('Pitesti', 98)
    self.bucharest = Vertice('Bucharest', 0)
    self.giurgiu = Vertice('Giurgiu', 77)

    self.arad.adiciona_adjacente(Adjacente(self.zerind, 75))
    self.arad.adiciona_adjacente(Adjacente(self.sibiu, 140))
    self.arad.adiciona_adjacente(Adjacente(self.timisoara, 118))

    self.zerind.adiciona_adjacente(Adjacente(self.arad, 75))
    self.zerind.adiciona_adjacente(Adjacente(self.oradea, 71))

    self.oradea.adiciona_adjacente(Adjacente(self.zerind, 71))
    self.oradea.adiciona_adjacente(Adjacente(self.sibiu, 151))

    self.sibiu.adiciona_adjacente(Adjacente(self.oradea, 151))
    self.sibiu.adiciona_adjacente(Adjacente(self.arad, 140))
    self.sibiu.adiciona_adjacente(Adjacente(self.fagaras, 99))
    self.sibiu.adiciona_adjacente(Adjacente(self.rimnicu, 80))

    self.timisoara.adiciona_adjacente(Adjacente(self.arad, 118))
    self.timisoara.adiciona_adjacente(Adjacente(self.lugoj, 111))

    self.lugoj.adiciona_adjacente(Adjacente(self.timisoara, 111))
    self.lugoj.adiciona_adjacente(Adjacente(self.mehadia, 70))

    self.mehadia.adiciona_adjacente(Adjacente(self.lugoj, 70))
    self.mehadia.adiciona_adjacente(Adjacente(self.dobreta, 75))

    self.dobreta.adiciona_adjacente(Adjacente(self.mehadia, 75))
    self.dobreta.adiciona_adjacente(Adjacente(self.craiova, 120))

    self.craiova.adiciona_adjacente(Adjacente(self.dobreta, 120))
    self.craiova.adiciona_adjacente(Adjacente(self.pitesti, 138))
    self.craiova.adiciona_adjacente(Adjacente(self.rimnicu, 146))

    self.rimnicu.adiciona_adjacente(Adjacente(self.craiova, 146))
    self.rimnicu.adiciona_adjacente(Adjacente(self.sibiu, 80))
    self.rimnicu.adiciona_adjacente(Adjacente(self.pitesti, 97))

    self.fagaras.adiciona_adjacente(Adjacente(self.sibiu, 99))
    self.fagaras.adiciona_adjacente(Adjacente(self.bucharest, 211))

    self.pitesti.adiciona_adjacente(Adjacente(self.rimnicu, 97))
    self.pitesti.adiciona_adjacente(Adjacente(self.craiova, 138))
    self.pitesti.adiciona_adjacente(Adjacente(self.bucharest, 101))

    self.bucharest.adiciona_adjacente(Adjacente(self.fagaras, 211))
    self.bucharest.adiciona_adjacente(Adjacente(self.pitesti, 101))
    self.bucharest.adiciona_adjacente(Adjacente(self.giurgiu, 90))

# Instanciando o grafo
grafo = Grafo()

import numpy as np
class VetorOrdenado:
  
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    # Mudança no tipo de dados
    self.valores = np.empty(self.capacidade, dtype=object)

  # Referência para o vértice e comparação com a distância para o objetivo
  def insere(self, adjacente):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
        break
      if i == self.ultima_posicao:
        posicao = i + 1
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1
    self.valores[posicao] = adjacente
    self.ultima_posicao += 1

  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i].vertice.rotulo, ' - ', 
              self.valores[i].custo, ' - ', 
              self.valores[i].vertice.distancia_objetivo, ' - ',
              self.valores[i].distancia_aestrela)  

print(grafo.arad.adjacentes[0].vertice.rotulo, grafo.arad.adjacentes[0].vertice.distancia_objetivo)

print(grafo.arad.adjacentes[0].distancia_aestrela, grafo.arad.adjacentes[0].custo)

vetor = VetorOrdenado(20)
vetor.insere(grafo.arad.adjacentes[0])
vetor.insere(grafo.arad.adjacentes[1])
vetor.insere(grafo.arad.adjacentes[2])

vetor.imprime()

class AEstrela:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual):
    print('------------------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado = True
          vetor_ordenado.insere(adjacente)
      vetor_ordenado.imprime()

      if vetor_ordenado.valores[0] != None:
        self.buscar(vetor_ordenado.valores[0].vertice)

busca_aestrela = AEstrela(grafo.bucharest)
busca_aestrela.buscar(grafo.arad)