# ponto de entrada — menu e navegação
from tarefas import cadastrar_livro, menu_consultas, atualizar_status, contar_por_status, ver_historico_lidos
from utils import titulo

def mostrar_menu():
    # Abre o menu principal com título e opções
    titulo("PyShelf: Biblioteca Pessoal")
    print()
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Atualizar Status")
    print("4. Contar por Status") 
    print("5. Histórico de Livros Lidos")
    print("6. Sair")

while True:
    # Loop principal do programa: exibe o menu, recebe a opção do usuário e chama a função correspondente
    mostrar_menu()  # chama a função em vez de repetir os prints

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        menu_consultas()

    elif opcao == "3":
        atualizar_status()

    elif opcao == "4":
        contar_por_status()

    elif opcao == "5":    
        ver_historico_lidos()

    elif opcao == "6":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
