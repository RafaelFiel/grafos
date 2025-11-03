# grafo_transporte.py

import heapq

class SistemaTransporte:
    def __init__(self):
        # Estrutura: {'Central': {'Norte': 8, 'Leste': 6}}
        self.mapa = {}

    # --------------------------------------------
    # Estações
    # --------------------------------------------
    def adicionar_estacao(self, nome):
        if nome not in self.mapa:
            self.mapa[nome] = {}
            print(f"🚉 Estação '{nome}' registrada com sucesso.")
        else:
            print(f"A estação '{nome}' já está cadastrada.")

    def remover_estacao(self, nome):
        if nome in self.mapa:
            self.mapa.pop(nome)
            for est in self.mapa:
                self.mapa[est].pop(nome, None)
            print(f"Estação '{nome}' removida do sistema.")
        else:
            print("Essa estação não foi encontrada.")

    # --------------------------------------------
    # Conexões entre estações
    # --------------------------------------------
    def criar_conexao(self, origem, destino, tempo):
        if origem in self.mapa and destino in self.mapa:
            self.mapa[origem][destino] = tempo
            print(f"🚌 Ligação criada: {origem} → {destino} ({tempo} min)")
        else:
            print("Erro: uma das estações informadas não existe.")

    def apagar_conexao(self, origem, destino):
        if origem in self.mapa and destino in self.mapa[origem]:
            del self.mapa[origem][destino]
            print(f"Conexão {origem} → {destino} foi apagada.")
        else:
            print("Essa conexão não existe na rede.")

    # --------------------------------------------
    # Consultas e verificações
    # --------------------------------------------
    def exibir_conexoes(self, estacao):
        if estacao not in self.mapa:
            print("Estação não localizada.")
            return

        conexoes = self.mapa[estacao]
        if not conexoes:
            print(f"A estação '{estacao}' não tem conexões diretas.")
        else:
            print(f"\nRotas saindo da estação '{estacao}':")
            for destino, tempo in conexoes.items():
                print(f" - {destino}: {tempo} minutos")

    def verificar_ligacao(self, origem, destino):
        if origem in self.mapa and destino in self.mapa[origem]:
            print(f"Existe ligação direta entre {origem} e {destino}.")
        else:
            print(f"Não há ligação direta entre {origem} e {destino}.")

    # --------------------------------------------
    # Algoritmo de Dijkstra — menor tempo de viagem
    # --------------------------------------------
    def menor_tempo(self, partida):
        if partida not in self.mapa:
            print("Estação não existe.")
            return

        tempos = {e: float("inf") for e in self.mapa}
        tempos[partida] = 0
        fila = [(0, partida)]

        while fila:
            tempo_atual, atual = heapq.heappop(fila)
            for vizinho, tempo in self.mapa[atual].items():
                novo_tempo = tempo_atual + tempo
                if novo_tempo < tempos[vizinho]:
                    tempos[vizinho] = novo_tempo
                    heapq.heappush(fila, (novo_tempo, vizinho))

        print(f"\n⏱️ Menores tempos de viagem a partir de '{partida}':")
        for estacao, tempo in tempos.items():
            if tempo == float("inf"):
                print(f" - {estacao}: sem trajeto disponível")
            else:
                print(f" - {estacao}: {tempo} minutos")
