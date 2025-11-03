# main.py
# ==========================================
# Interface interativa — Rotas Aéreas
# ==========================================

from mapa_voos import MapaVoos

def menu():
    print("\n🌐 SISTEMA DE ROTAS AÉREAS")
    print("1. Criar aeroporto")
    print("2. Apagar aeroporto")
    print("3. Incluir rota de voo")
    print("4. Excluir rota")
    print("5. Exibir voos de um aeroporto")
    print("6. Verificar voo direto")
    print("7. Calcular menor tempo (Dijkstra)")
    print("0. Sair")

def main():
    sistema = MapaVoos()

    # Aeroportos iniciais
    sistema.criar_aeroporto("SP")
    sistema.criar_aeroporto("RJ")
    sistema.criar_aeroporto("BSB")
    sistema.criar_aeroporto("SSA")

    # Rotas iniciais
    sistema.incluir_rota("SP", "RJ", 1.2, 380)
    sistema.incluir_rota("RJ", "BSB", 2.0, 850)
    sistema.incluir_rota("BSB", "SSA", 2.6, 800)
    sistema.incluir_rota("SP", "BSB", 3.0, 900)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cod = input("Código do aeroporto (ex: POA, SP, RJ): ").upper()
            sistema.criar_aeroporto(cod)

        elif opcao == "2":
            cod = input("Código do aeroporto a excluir: ").upper()
            sistema.apagar_aeroporto(cod)

        elif opcao == "3":
            o = input("Origem: ").upper()
            d = input("Destino: ").upper()
            tempo = float(input("Tempo de voo (h): "))
            dist = float(input("Distância (km): "))
            sistema.incluir_rota(o, d, tempo, dist)

        elif opcao == "4":
            o = input("Origem: ").upper()
            d = input("Destino: ").upper()
            sistema.excluir_rota(o, d)

        elif opcao == "5":
            origem = input("Aeroporto de origem: ").upper()
            sistema.exibir_rotas(origem)

        elif opcao == "6":
            o = input("Origem: ").upper()
            d = input("Destino: ").upper()
            sistema.verificar_voo(o, d)

        elif opcao == "7":
            partida = input("Aeroporto de partida: ").upper()
            sistema.calcular_menor_tempo(partida)

        elif opcao == "0":
            print("🛬 Encerrando o programa... até a próxima viagem!")
            break

        else:
            print("Opção inválida! Digite um número de 0 a 7.")

if __name__ == "__main__":
    main()