# regras de negócio (cadastrar, consultar, atualizar)

from dados import livros, prioridades, status, fila_pendente, pilha_lida
from utils import titulo

def cadastrar_livro():
    # Cadastro de um novo livro, com prioridade e status inicial "A Ler"
    titulo("Cadastrar Livro")

    nome_livro   = input("Título: ")
    autor        = input("Autor: ")
    ano          = input("Ano de Publicação: ")
    genero       = input("Gênero: ")

    print(' - Prioridades: 1. Baixa | 2. Média | 3. Alta')
    opcao = input("Prioridade: ")

    # Lê a prioridade da tupla pelo índice
    if opcao == "1":
        prioridade = prioridades[0]  # "Baixa"
    elif opcao == "2":
        prioridade = prioridades[1]  # "Média"
    else:
        prioridade = prioridades[2]  # "Alta"

    # Cria o dicionário representando a livro
    dict_livro = {
        "id":              len(livros) + 1,
        "nome_livro":      nome_livro,
        "autor":           autor,
        "ano":             ano,
        "genero":          genero,
        "prioridade":      prioridade,
        "status":          status[0]  # sempre "A Ler"
    }

    livros.append(dict_livro)         # adiciona à lista principal
    fila_pendente.append(dict_livro)  # adiciona à fila de pendentes (FIFO)

    print("Livro cadastrado com sucesso!")

def consultas():
    # Menu de opções para escolher o atributo de consulta
    print("1. Título") 
    print("2. Autor") 
    print("3. Gênero") 
    print("4. Liste Todos")
    print() 

def menu_consultas():
    # Menu de consultas: título, autor, gênero ou listar todos
    titulo("Consultar por:")
    consultas()
    opcao_consulta = input("Escolha uma opção: ")

    if opcao_consulta == "1":
        consulta_titulo()

    elif opcao_consulta == "2":
        consulta_autor()

    elif opcao_consulta == "3":
        consulta_genero()

    elif opcao_consulta == "4":
        consultar_livro()

    else:
        print("Opção inválida.")

def consultar_livro():
    # Consulta geral: lista todos os livros cadastrados, sem filtro
    titulo("Consultar Livros")
    
    # Bloco de diagnóstico contra lista vazia
    if len(livros) == 0:
        print("Nenhum livro foi cadastrado ainda.")
        print("Cadastre um livro primeiro.")
        print()  # linha em branco
        return  # Interrompe a execução da função imediatamente

    for i, livro in enumerate(livros, start=1):
        print(f'LIVRO: {i}')
        print(f"ID: {livro['id']}")
        print(f"Título: {livro['nome_livro']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano de Publicação: {livro['ano']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Prioridade: {livro['prioridade']}")
        print(f"Status: {livro['status']}")
        print()  # linha em branco entre livros

def consulta_titulo():
    # Consulta por título: busca pelo nome do livro (ou parte dele) e exibe os resultados encontrados
    titulo("Consultar por Título")

    if len(livros) == 0:
        print("Nenhum livro foi cadastrado ainda.")
        print("Cadastre um livro primeiro.")
        print()  # linha em branco
        return  # Interrompe a execução da função imediatamente

    atributo = input("Digite o título para buscar: ").lower()

    resultados = []
    for livro in livros:
        if atributo in livro["nome_livro"].lower():
            resultados.append(livro)

    if len(resultados) == 0:
        print("Nenhum livro encontrado.")
        return

    for i, livro in enumerate(resultados, start=1):
        print(f'RESULTADO {i}')
        print(f"ID: {livro['id']}")
        print(f"Título: {livro['nome_livro']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano de Publicação: {livro['ano']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Prioridade: {livro['prioridade']}")
        print(f"Status: {livro['status']}")
        print()  # linha em branco entre resultados

def consulta_autor():
    # Consulta por autor: busca pelo nome do autor (ou parte dele) e exibe os resultados encontrados
    titulo("Consultar por Autor")

    if len(livros) == 0:
        print("Nenhum livro foi cadastrado ainda.")
        print("Cadastre um livro primeiro.")
        print()  # linha em branco
        return  # Interrompe a execução da função imediatamente

    atributo = input("Digite o autor para buscar: ").lower()

    resultados = []
    for livro in livros:
        if atributo in livro["autor"].lower():
            resultados.append(livro)

    if len(resultados) == 0:
        print("Nenhum livro encontrado.")
        return

    for i, livro in enumerate(resultados, start=1):
        print(f'RESULTADO {i}')
        print(f"ID: {livro['id']}")
        print(f"Título: {livro['nome_livro']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano de Publicação: {livro['ano']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Prioridade: {livro['prioridade']}")
        print(f"Status: {livro['status']}")
        print()  # linha em branco entre resultados

def consulta_genero():
    # Consulta por gênero: busca pelo nome do gênero (ou parte dele) e exibe os resultados encontrados
    titulo("Consultar por Gênero")

    if len(livros) == 0:
        print("Nenhum livro foi cadastrado ainda.")
        print("Cadastre um livro primeiro.")
        print()  # linha em branco
        return  # Interrompe a execução da função imediatamente

    atributo = input("Digite o gênero para buscar: ").lower()

    resultados = []
    for livro in livros:
        if atributo in livro["genero"].lower():
            resultados.append(livro)

    if len(resultados) == 0:
        print("Nenhum livro encontrado.")
        return

    for i, livro in enumerate(resultados, start=1):
        print(f'RESULTADO {i}')
        print(f"ID: {livro['id']}")
        print(f"Título: {livro['nome_livro']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano de Publicação: {livro['ano']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Prioridade: {livro['prioridade']}")
        print(f"Status: {livro['status']}")
        print()  # linha em branco entre resultados

def atualizar_status():
    # Atualiza o status de um livro específico, escolhendo entre "A Ler", "Lendo" ou "Lido"
    if len(livros) == 0:
        titulo("Atualizar Status")
        print("Nenhum livro foi cadastrado ainda.")
        print("Cadastre um livro primeiro.")
        print()  # linha em branco
        return  # Interrompe a execução da função imediatamente
    else:
        print("\n--- Atualizar Status ---")
        consultar_livro()

    # Guarda 1: lista vazia — nada a atualizar
    if len(livros) == 0:
        return

    # Guarda 2: usuário pode digitar texto em vez de número
    try:
        id_livro = int(input("Digite o ID do livro: "))
    except ValueError:
        print("Digite um número válido.")
        return

    for livro in livros:
        if livro["id"] == id_livro:
            print("\nEscolha o novo status:")
            print("1 - A Ler")
            print("2 - Lendo")
            print("3 - Lido")
            opcao = input("Opção: ")

            if opcao == "1":
                livro["status"] = status[0]
                if livro not in fila_pendente:
                    fila_pendente.append(livro)   # volta para a fila A Ler
            elif opcao == "2":
                livro["status"] = status[1]
            elif opcao == "3":
                livro["status"] = status[2]
                pilha_lida.append(livro)   # empilha!
                if livro in fila_pendente:
                    fila_pendente.remove(livro)  # sai da fila

            print("Status atualizado com sucesso!")
            return

    print("Livro não encontrado.")

def contar_por_status():
    # Conta quantos livros estão em cada status: "A Ler", "Lendo" e "Lido"
    titulo("Total de Livros por Status")

    a_ler = 0
    lendo = 0
    lido = 0

    for livro in livros:

        if livro["status"] == "A Ler":
            a_ler += 1

        elif livro["status"] == "Lendo":
            lendo += 1
        
        elif livro["status"] == "Lido":
            lido += 1

    print()
    print(f"Livros A Ler: {a_ler}")
    print(f"Livros Lendo: {lendo}")    
    print(f"Livros Lidos: {lido}")
    print()

def ver_historico_lidos():
    # Exibe o histórico dos livros lidos, do mais recente para o mais antigo (comportamento LIFO)
    titulo("Histórico de Livros Lidos")
    if len(pilha_lida) == 0:
        print("Nenhum livro lido.")
        print("Cadastre um livro e marque-o como lido.")
        print()  # linha em branco
        return

    # reversed() percorre do TOPO para a BASE
    # = mais recente primeiro (comportamento LIFO)
    for i, livro in enumerate(reversed(pilha_lida), start=1):
        print(f'LIVRO CONCLUÍDO: {i}')
        print(f"ID: {livro['id']}")
        print(f"Título: {livro['nome_livro']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano de Publicação: {livro['ano']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Prioridade: {livro['prioridade']}")
        print()