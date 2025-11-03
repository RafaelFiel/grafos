# main.py
# ==========================================
# Interface: Sistema de Conexões Sociais
# ==========================================

from rede_social import ConexoesSociais

def menu():
    print("\n🌐 REDE DE CONEXÕES SOCIAIS")
    print("1. Cadastrar usuário")
    print("2. Excluir usuário")
    print("3. Adicionar amizade")
    print("4. Remover amizade")
    print("5. Mostrar lista de amigos")
    print("6. Verificar se dois usuários são amigos")
    print("7. Sugerir novos amigos")
    print("8. Ver grau de popularidade")
    print("0. Encerrar programa")

def main():
    app = ConexoesSociais()

    # Usuários iniciais
    app.cadastrar_usuario("Alice")
    app.cadastrar_usuario("Bruno")
    app.cadastrar_usuario("Carla")
    app.cadastrar_usuario("Diego")

    # Amizades iniciais
    app.adicionar_amizade("Alice", "Bruno")
    app.adicionar_amizade("Bruno", "Carla")

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do novo usuário: ").title()
            app.cadastrar_usuario(nome)

        elif opcao == "2":
            nome = input("Usuário a ser removido: ").title()
            app.excluir_usuario(nome)

        elif opcao == "3":
            u1 = input("Primeiro usuário: ").title()
            u2 = input("Segundo usuário: ").title()
            app.adicionar_amizade(u1, u2)

        elif opcao == "4":
            u1 = input("Primeiro usuário: ").title()
            u2 = input("Segundo usuário: ").title()
            app.remover_amizade(u1, u2)

        elif opcao == "5":
            nome = input("Nome do usuário: ").title()
            app.mostrar_amigos(nome)

        elif opcao == "6":
            u1 = input("Usuário 1: ").title()
            u2 = input("Usuário 2: ").title()
            app.verificar_amizade(u1, u2)

        elif opcao == "7":
            nome = input("Nome do usuário: ").title()
            app.sugerir_conhecidos(nome)

        elif opcao == "8":
            nome = input("Nome do usuário: ").title()
            app.grau_popularidade(nome)

        elif opcao == "0":
            print("👋 Encerrando o sistema de conexões sociais...")
            break

        else:
            print("Opção inválida, tente novamente!")

if __name__ == "__main__":
    main()
