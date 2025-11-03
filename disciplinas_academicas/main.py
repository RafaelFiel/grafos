# main.py
# ==========================================
# Interface do Sistema Acadêmico de Disciplinas
# ==========================================

from sistema_disciplinas import SistemaAcademico

def menu():
    print("\n🎓 SISTEMA ACADÊMICO DE DISCIPLINAS")
    print("1. Adicionar disciplina")
    print("2. Remover disciplina")
    print("3. Vincular pré-requisito")
    print("4. Desvincular pré-requisito")
    print("5. Listar pré-requisitos de uma disciplina")
    print("6. Verificar dependência entre disciplinas")
    print("7. Detectar ciclos")
    print("8. Gerar plano de estudos (ordenação topológica)")
    print("0. Encerrar programa")

def main():
    uni = SistemaAcademico()

    # Disciplinas iniciais
    uni.adicionar_disciplina("Lógica de Programação")
    uni.adicionar_disciplina("Algoritmos")
    uni.adicionar_disciplina("Estrutura de Dados")
    uni.adicionar_disciplina("Banco de Dados")
    uni.adicionar_disciplina("Redes de Computadores")

    # Pré-requisitos iniciais
    uni.vincular_prerequisito("Algoritmos", "Lógica de Programação")
    uni.vincular_prerequisito("Estrutura de Dados", "Algoritmos")
    uni.vincular_prerequisito("Banco de Dados", "Estrutura de Dados")
    uni.vincular_prerequisito("Redes de Computadores", "Estrutura de Dados")

    while True:
        menu()
        op = input("Escolha uma opção: ")

        if op == "1":
            nome = input("Nome da nova disciplina: ").title()
            uni.adicionar_disciplina(nome)

        elif op == "2":
            nome = input("Disciplina a remover: ").title()
            uni.remover_disciplina(nome)

        elif op == "3":
            materia = input("Disciplina principal: ").title()
            prereq = input("Pré-requisito: ").title()
            uni.vincular_prerequisito(materia, prereq)

        elif op == "4":
            materia = input("Disciplina principal: ").title()
            prereq = input("Pré-requisito a desvincular: ").title()
            uni.desvincular_prerequisito(materia, prereq)

        elif op == "5":
            materia = input("Nome da disciplina: ").title()
            uni.listar_requisitos(materia)

        elif op == "6":
            d1 = input("Primeira disciplina: ").title()
            d2 = input("Segunda disciplina: ").title()
            uni.existe_dependencia(d1, d2)

        elif op == "7":
            uni.detectar_ciclo()

        elif op == "8":
            uni.gerar_plano_estudos()

        elif op == "0":
            print("📚 Encerrando o sistema acadêmico. Até breve!")
            break

        else:
            print("Opção inválida! Escolha um número entre 0 e 8.")

if __name__ == "__main__":
    main()
