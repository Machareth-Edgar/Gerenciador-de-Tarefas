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
    lista_de_tarefas = []
    adicionar_tarefa = input("Adicione Uma Tarefa: ")
    lista_de_tarefas.append(adicionar_tarefa)
    print(f"Tarefa adicionada com sucesso!:", lista_de_tarefas)
    continuar = input("Deseja adicionar mais tarefas? (s/n): ")

