# Projeto: Gerenciador de Tarefas Simples
# O aplicativo deve ser executado a partir da linha de comando, aceitar ações e entradas do usuário como argumentos e armazenar as tarefas em um arquivo JSON. O usuário deve ser capaz de:

# Adicionar, atualizar e excluir tarefas
# Marcar uma tarefa como em andamento ou concluída
# Listar todas as tarefas
# Listar todas as tarefas que foram realizadas
# Listar todas as tarefas que não foram concluídas
# Listar todas as tarefas em andamento
# Aqui estão algumas restrições para orientar a implementação:

# Você pode usar qualquer linguagem de programação para construir este projeto.
# Use argumentos posicionais na linha de comando para aceitar entradas do usuário.
# Use um arquivo JSON para armazenar as tarefas no diretório atual.
# O arquivo JSON deve ser criado se não existir.
# Use o módulo do sistema de arquivos nativo da sua linguagem de programação para interagir com o arquivo JSON.
# Não use nenhuma biblioteca ou estrutura externa para construir este projeto.
# Certifique-se de lidar com erros e casos extremos com elegância.
#Criar arquivo caso não exista



while True:
    print("\nBem-Vindo Ao Gerenciador de Tarefas! O que você deseja fazer ?")
    print("1 - Adicionar uma Tarefa")
    print("2 - Adicionar Descrição a uma Tarefa")
    print("3 - Progresso da Tarefa")
    print("4 - Excluir uma Tarefa")
    print("5 - Visualizar Tarefas")
    print("6 - Sair")
    menu = input("Opcao: ")
    lista_de_tarefas = []
    if menu == "1":
        print("Você escolheu adicionar uma Tarefa")
        adicionar_tarefa = input("Adicione Uma Tarefa: ")
        lista_de_tarefas.append(adicionar_tarefa)
        print(f"Tarefa adicionada com sucesso!:", lista_de_tarefas)
        continuar = input("Deseja adicionar mais tarefas? (s/n): ")
        if continuar == "s":
            limite = 5
            for limites in range(limite):
                nova_tarefa = input("Adicione uma nova tarefa: ")
                lista_de_tarefas.append(nova_tarefa)
                if len(lista_de_tarefas) >= limite:
                    print("Você alcançou o máximo de tarefas hoje, conclua-as primeiro!")
                    break
                print(f"Você optou por adicionar uma nova Tarefa.")
                print(f"\nSua lista de Tarefas é: ", lista_de_tarefas)
                continuar = input("Deseja adicionar mais tarefas? (s/n): ")
                if continuar == "s":
                    continue
                elif continuar == "n":
                    break



        elif continuar == "n":
            ...
    if menu == "5":
        print(f"\nSua lista de tarefas é: ",lista_de_tarefas)
        break