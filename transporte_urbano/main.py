# main.py
# ==========================================
# Interface do Sistema de Transporte Urbano
# ==========================================

from grafo_transporte import SistemaTransporte

def menu():
    print("\n🚇 SISTEMA DE TRANSPORTE URBANO")
    print("1. Registrar nova estação")
    print("2. Excluir estação existente")
    print("3. Criar conexão entre estações")
    print("4. Apagar conexão")
    print("5. Exibir conexões de uma estação")
    print("6. Verificar se há ligação direta")
    print("7. Calcular menor trajeto (Dijkstra)")
    print("0. Finalizar programa")

def main():
    rede = SistemaTransporte()

    # Estações iniciais
    rede.adicionar_estacao("Central")
    rede.adicionar_estacao("Leste")
    rede.adicionar_estacao("Oeste")
    rede.adicionar_estacao("Norte")
    rede.adicionar_estacao("Sul")

    # Conexões iniciais
    rede.criar_conexao("Central", "Leste", 8)
    rede.criar_conexao("Leste", "Oeste", 10)
    rede.criar_conexao("Oeste", "Sul", 12)
    rede.criar_conexao("Central", "Norte", 7)
    rede.criar_conexao("Norte", "Oeste", 5)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da estação: ").title()
            rede.adicionar_estacao(nome)

        elif opcao == "2":
            nome = input("Nome da estação a remover: ").title()
            rede.remover_estacao(nome)

        elif opcao == "3":
            origem = input("Estação de origem: ").title()
            destino = input("Estação de destino: ").title()
            tempo = int(input("Tempo de viagem (minutos): "))
            rede.criar_conexao(origem, destino, tempo)

        elif opcao == "4":
            origem = input("Estação de origem: ").title()
            destino = input("Estação de destino: ").title()
            rede.apagar_conexao(origem, destino)

        elif opcao == "5":
            estacao = input("Digite o nome da estação: ").title()
            rede.exibir_conexoes(estacao)

        elif opcao == "6":
            origem = input("Origem: ").title()
            destino = input("Destino: ").title()
            rede.verificar_ligacao(origem, destino)

        elif opcao == "7":
            partida = input("Estação inicial: ").title()
            rede.menor_tempo(partida)

        elif opcao == "0":
            print("🚌 Encerrando o sistema de transporte... Até logo!")
            break

        else:
            print("Opção inválida! Escolha uma opção entre 0 e 7.")

if __name__ == "__main__":
    main()
