# Estrutura de dados para representar tarefas
tarefas = []

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada.")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"{i + 1}. {tarefa['nome']} - {tarefa['descricao']} - Prioridade: {tarefa['prioridade']} - Categoria: {tarefa['categoria']} - Status: {status}")

def marcar_concluida(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluida'] = True
        print(f"Tarefa '{tarefas[indice]['nome']}' marcada como concluída.")
    else:
        print("Índice inválido.")

def exibir_por_prioridade(prioridade):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['prioridade'] == prioridade]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada com prioridade '{prioridade}'.")
        return
    for tarefa in tarefas_filtradas:
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"{tarefa['nome']} - {tarefa['descricao']} - Categoria: {tarefa['categoria']} - Status: {status}")

def exibir_por_categoria(categoria):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['categoria'] == categoria]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")
        return
    for tarefa in tarefas_filtradas:
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"{tarefa['nome']} - {tarefa['descricao']} - Prioridade: {tarefa['prioridade']} - Status: {status}")

def menu():
    while True:
        print("\nMenu de Tarefas:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade (Baixa, Média, Alta): ")
            categoria = input("Categoria: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            indice = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
            marcar_concluida(indice)
        elif opcao == '4':
            prioridade = input("Digite a prioridade para filtrar (Baixa, Média, Alta): ")
            exibir_por_prioridade(prioridade)
        elif opcao == '5':
            categoria = input("Digite a categoria para filtrar: ")
            exibir_por_categoria(categoria)
        elif opcao == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
