# rede_social.py

class ConexoesSociais:
    def __init__(self):
        # Estrutura de dados: {'Alice': {'Bruno', 'Carla'}}
        self.rede = {}

    # --------------------------------------------
    # Usuários
    # --------------------------------------------
    def cadastrar_usuario(self, nome):
        if nome not in self.rede:
            self.rede[nome] = set()
            print(f"👤 Usuário '{nome}' cadastrado com sucesso.")
        else:
            print(f"O nome '{nome}' já está em uso na rede.")

    def excluir_usuario(self, nome):
        if nome in self.rede:
            self.rede.pop(nome)
            for amigos in self.rede.values():
                amigos.discard(nome)
            print(f"Usuário '{nome}' removido da rede.")
        else:
            print("Usuário não encontrado.")

    # --------------------------------------------
    # Amizades
    # --------------------------------------------
    def adicionar_amizade(self, u1, u2):
        if u1 in self.rede and u2 in self.rede:
            self.rede[u1].add(u2)
            self.rede[u2].add(u1)
            print(f"🤝 Agora {u1} e {u2} são amigos!")
        else:
            print("Erro: um dos usuários não foi encontrado.")

    def remover_amizade(self, u1, u2):
        if u1 in self.rede and u2 in self.rede[u1]:
            self.rede[u1].remove(u2)
            self.rede[u2].remove(u1)
            print(f"Amizade entre {u1} e {u2} foi encerrada.")
        else:
            print("Esses usuários não possuem amizade registrada.")

    # --------------------------------------------
    # Consultas e análises
    # --------------------------------------------
    def mostrar_amigos(self, nome):
        if nome not in self.rede:
            print("Usuário inexistente.")
            return

        amigos = self.rede[nome]
        if amigos:
            print(f"Amigos de {nome}: {', '.join(amigos)}")
        else:
            print(f"{nome} ainda não tem amigos na rede.")

    def verificar_amizade(self, u1, u2):
        if u1 in self.rede and u2 in self.rede:
            if u2 in self.rede[u1]:
                print(f"Sim! {u1} e {u2} são amigos.")
            else:
                print(f"Não, {u1} e {u2} não têm amizade direta.")
        else:
            print("Usuário não encontrado.")

    def sugerir_conhecidos(self, nome):
        if nome not in self.rede:
            print("Usuário não encontrado.")
            return

        sugestoes = set()
        for amigo in self.rede[nome]:
            for amigo_do_amigo in self.rede[amigo]:
                if amigo_do_amigo != nome and amigo_do_amigo not in self.rede[nome]:
                    sugestoes.add(amigo_do_amigo)

        if sugestoes:
            print(f"👥 Sugestões de amizade para {nome}: {', '.join(sugestoes)}")
        else:
            print(f"Nenhuma sugestão disponível para {nome}.")

    def grau_popularidade(self, nome):
        if nome in self.rede:
            total = len(self.rede[nome])
            print(f"⭐ {nome} possui {total} amizade(s).")
        else:
            print("Usuário não encontrado.")