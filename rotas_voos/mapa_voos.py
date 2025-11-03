# mapa_voos.py

import heapq

class MapaVoos:
    def __init__(self):
        # Exemplo de estrutura interna:
        # {'SP': {'RJ': {'tempo': 1.2, 'dist': 380}}}
        self.malha = {}

    # ----------------------------
    # Aeroportos
    # ----------------------------
    def criar_aeroporto(self, codigo):
        if codigo not in self.malha:
            self.malha[codigo] = {}
            print(f"Aeroporto '{codigo}' criado com sucesso.")
        else:
            print(f"O aeroporto '{codigo}' já existe na rede.")

    def apagar_aeroporto(self, codigo):
        if codigo in self.malha:
            self.malha.pop(codigo)
            for origem in self.malha:
                self.malha[origem].pop(codigo, None)
            print(f"Aeroporto '{codigo}' removido do sistema.")
        else:
            print("Esse aeroporto não existe.")

    # ----------------------------
    # Rotas entre aeroportos
    # ----------------------------
    def incluir_rota(self, origem, destino, tempo, distancia):
        if origem in self.malha and destino in self.malha:
            self.malha[origem][destino] = {"tempo": tempo, "dist": distancia}
            print(f"✈️  Rota {origem} → {destino} adicionada ({tempo}h | {distancia}km)")
        else:
            print("Erro: uma das siglas de aeroporto é inválida.")

    def excluir_rota(self, origem, destino):
        if origem in self.malha and destino in self.malha[origem]:
            self.malha[origem].pop(destino)
            print(f"Rota {origem} → {destino} removida.")
        else:
            print("Essa rota não existe na malha aérea.")

    # ----------------------------
    # Consultas
    # ----------------------------
    def exibir_rotas(self, origem):
        if origem not in self.malha:
            print("Aeroporto não encontrado.")
            return

        rotas = self.malha[origem]
        if not rotas:
            print(f"Não há voos saindo de {origem}.")
        else:
            print(f"\nVoos disponíveis a partir de {origem}:")
            for destino, info in rotas.items():
                print(f" - {destino}: {info['tempo']}h | {info['dist']}km")

    def verificar_voo(self, origem, destino):
        if origem in self.malha and destino in self.malha[origem]:
            print(f"Existe voo direto entre {origem} e {destino}.")
        else:
            print(f"Não há voo direto entre {origem} e {destino}.")

    # ----------------------------
    # Algoritmo de Dijkstra (menor tempo)
    # ----------------------------
    def calcular_menor_tempo(self, partida):
        if partida not in self.malha:
            print("Aeroporto não encontrado.")
            return

        tempos = {aeroporto: float("inf") for aeroporto in self.malha}
        tempos[partida] = 0
        fila = [(0, partida)]

        while fila:
            tempo_atual, atual = heapq.heappop(fila)
            for destino, dados in self.malha[atual].items():
                novo_tempo = tempo_atual + dados["tempo"]
                if novo_tempo < tempos[destino]:
                    tempos[destino] = novo_tempo
                    heapq.heappush(fila, (novo_tempo, destino))

        print(f"\n🕒 Menores tempos a partir de {partida}:")
        for aeroporto, tempo in tempos.items():
            if tempo == float("inf"):
                print(f" - {aeroporto}: sem rota disponível")
            else:
                print(f" - {aeroporto}: {tempo}h")