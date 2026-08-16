tarefas = []


def menu():
    print("\n ======= TO-DO LIST =======")
    print("1 - Adicionar tarefa")
    print("2 - Lista tarefas")
    print("3 - Remover tarefa")
    print("4 - atualizar tarefa")
    print("5 - Sair")
    return input("escolha uma opção: ")

while True:
    opcao = menu()

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        print("\n ======= LISTA DE TAREFAS =======")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1} - {tarefa}")

    elif opcao == "3":
        print("\n ======= REMOVER TAREFA =======")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1} - {tarefa}")
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida com sucesso!")
        else:
            print("Índice inválido.")

    elif opcao == "4":
        print("\n ======= ATUALIZAR TAREFA =======")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1} - {tarefa}")
        indice = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
        if 0 <= indice < len(tarefas):
            nova_tarefa = input("Digite a nova descrição da tarefa: ")
            tarefas[indice] = nova_tarefa
            print("Tarefa atualizada com sucesso!")
        else:
            print("Índice inválido.")

    elif opcao == "5":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")