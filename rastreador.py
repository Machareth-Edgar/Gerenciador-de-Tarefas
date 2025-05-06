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


#Gerenciador de opções
def gerenciador():
    print("\n Seja Bem-Vindo, em que posso ajudar ?")
    print("1 - Adicionar uma Tarefa")
    print("2 - Progresso de uma Tarefa")
    print("3 - Listar Tarefas")
    print("4 - Sair")
    opcao = input("Qual opção você deseja? ")

    if opcao == "1":
        tarefa_json = input("Digite a sua Tarefa: ")
        contador = 1
        while True:
            nome_tarefa = f"tarefa_{contador}.json"
            try:
                with open(nome_tarefa, "r"):
                    contador += 1
            except FileNotFoundError:
                break
        with open(nome_tarefa,"w", encoding="utf-8") as arquivo:
            arquivo.write(f'{{"Tarefa":"{tarefa_json}"}}')
        print(f"{nome_tarefa} criada!")
    


    if opcao == "2":
        nome_arquivo = input("Digite a Tarefa que Gostaria de Progredir: ")
    
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                progresso = arquivo.read()
                if progresso.endswith("}"):
                    progresso = progresso[:-1] + ",\n"
                else:
                    progresso = "{\n"

        except FileNotFoundError:
            progresso = "{\n"

        dados_progresso = input("Qual o progresso da Tarefa ? (Concluida) (Em andamento) (Não Concluida): ")
        texto_progresso = f'"Progresso": "{dados_progresso}"'
        progresso_json =  progresso + texto_progresso + "\n}"

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(progresso_json)


    if opcao == "3":
        print("\nComo gostaria de visualizar as Tarefas ?")
        print("1 - Listar Todas as Tarefas")
        print("2 - Listar Apenas Concluídas")
        print("3 - Listar Não Concluídas")
        print("4 - Listar Em Andamento")
gerenciador()