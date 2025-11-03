# sistema_disciplinas.py

class SistemaAcademico:
    def __init__(self):
        # Estrutura interna:
        # {'Cálculo I': {'Álgebra Linear'}, 'Estrutura de Dados': {'Algoritmos'}}
        self.matriz = {}

    # --------------------------------------------
    # Disciplinas
    # --------------------------------------------
    def adicionar_disciplina(self, nome):
        if nome not in self.matriz:
            self.matriz[nome] = set()
            print(f"📘 Disciplina '{nome}' incluída no sistema.")
        else:
            print(f"A disciplina '{nome}' já está cadastrada.")

    def remover_disciplina(self, nome):
        if nome in self.matriz:
            self.matriz.pop(nome)
            for deps in self.matriz.values():
                deps.discard(nome)
            print(f"📕 Disciplina '{nome}' removida com sucesso.")
        else:
            print("Disciplina não encontrada.")

    # --------------------------------------------
    # Pré-requisitos
    # --------------------------------------------
    def vincular_prerequisito(self, materia, requisito):
        if materia in self.matriz and requisito in self.matriz:
            self.matriz[materia].add(requisito)
            print(f"✅ '{requisito}' agora é pré-requisito de '{materia}'.")
        else:
            print("Erro: uma das disciplinas não existe.")

    def desvincular_prerequisito(self, materia, requisito):
        if materia in self.matriz and requisito in self.matriz[materia]:
            self.matriz[materia].remove(requisito)
            print(f"❌ Pré-requisito '{requisito}' removido de '{materia}'.")
        else:
            print("Não há vínculo entre essas disciplinas.")

    # --------------------------------------------
    # Consultas
    # --------------------------------------------
    def listar_requisitos(self, materia):
        if materia not in self.matriz:
            print("Disciplina não encontrada.")
            return

        requisitos = self.matriz[materia]
        if requisitos:
            print(f"📚 '{materia}' depende de: {', '.join(requisitos)}")
        else:
            print(f"'{materia}' não possui pré-requisitos cadastrados.")

    def existe_dependencia(self, origem, destino):
        visitados = set()

        def dfs(atual):
            if atual == destino:
                return True
            visitados.add(atual)
            for vizinho in self.matriz.get(atual, []):
                if vizinho not in visitados and dfs(vizinho):
                    return True
            return False

        if dfs(origem):
            print(f"🔗 Existe dependência entre '{origem}' e '{destino}'.")
        else:
            print(f"❌ Nenhuma relação entre '{origem}' e '{destino}'.")

    # --------------------------------------------
    # Verificação de ciclos
    # --------------------------------------------
    def detectar_ciclo(self):
        visitados = set()
        pilha = set()

        def dfs(atual):
            if atual not in visitados:
                visitados.add(atual)
                pilha.add(atual)
                for vizinho in self.matriz.get(atual, []):
                    if vizinho not in visitados and dfs(vizinho):
                        return True
                    elif vizinho in pilha:
                        return True
            pilha.discard(atual)
            return False

        for disciplina in self.matriz:
            if dfs(disciplina):
                print("⚠️  Há um ciclo! Pré-requisito circular detectado.")
                return True
        print("✅ Nenhum ciclo encontrado.")
        return False

    # --------------------------------------------
    # Ordenação topológica (ordem de estudo)
    # --------------------------------------------
    def gerar_plano_estudos(self):
        indegree = {d: 0 for d in self.matriz}
        for requisitos in self.matriz.values():
            for req in requisitos:
                indegree[req] += 1

        fila = [d for d in indegree if indegree[d] == 0]
        ordem = []

        while fila:
            atual = fila.pop(0)
            ordem.append(atual)
            for vizinho in self.matriz:
                if atual in self.matriz[vizinho]:
                    indegree[vizinho] -= 1
                    if indegree[vizinho] == 0:
                        fila.append(vizinho)

        if len(ordem) == len(self.matriz):
            print("\n📖 Ordem sugerida de disciplinas para o curso:")
            print(" → ".join(ordem))
        else:
            print("❌ Não foi possível gerar a ordem (há dependências circulares).")
