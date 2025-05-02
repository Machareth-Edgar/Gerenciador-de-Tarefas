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
lista_de_tarefas = []
def salvar_tarefa(nome_tarefa):
    with open(nome_tarefa, "w", encoding="utf-8") as arquivo:
        arquivo.write("[\n")

        for i, tarefa in enumerate(lista_de_tarefas):
            arquivo.write(f'  {{"tarefa": "{tarefa}"}}')
            if i < len(lista_de_tarefas) - 1:
                arquivo.write(",\n")
            else:
                arquivo.write("\n")

        arquivo.write("]")

    print(f'Tarefa salva em {nome_tarefa}')

def gerenciador_tarefas():
    print("\nBem-Vindo ao Gerenciador de Tarefas!")
    print("1 - Adicionar uma Tarefa")
    print("2 - Adicionar uma Descrição")
    print("3 - Progresso da Tarefa")
    print("4 - Excluir uma Tarefa")
    print("5 - Sair")

    opcao = input("Qual opção deseja?: ")
    if opcao == "1":
        print("Você optou por adicionar uma Tarefa!")
        tarefa = input("Adicione a sua Tarefa: ")
        print(f'Tarefa {tarefa} adicionada com sucesso!')
        lista_de_tarefas.append(tarefa)
        salvar_tarefa("tarefas.json")

gerenciador_tarefas()