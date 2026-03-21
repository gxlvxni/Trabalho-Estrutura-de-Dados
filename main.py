from cliente import Cliente
from ListaEncadeada import ListaEncadeada
from produto import Produto

def exibir_menu():
    print("\n===== MENU ESTOQUE =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar produto")
    print("4 - Listar produtos")
    print("5 - Pesquisar produto")
    print("6 - Realizar venda")
    print("7 - Ver fila de vendas")
    print("8 - Desfazer última operação")
    print("9 - Exibir valor total do estoque")
    print("10 - Exibir valor total de vendas")
    print("11 - Exibir clientes e valores gastos")
    print("12 - Sair")
    print("========================")


def main():
    clientes = ListaEncadeada()
    proximo_id_cliente = 1

    produtos = ListaEncadeada()
    proximo_id_produto = 1
    
    
    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except:
            print("⚠️ Entrada inválida! Digite um número.")
            continue

        if opcao == 1:
            nome = input("Digite o nome do cliente: ").strip()

            if nome == "":
                print("⚠️ Nome não pode ser vazio!")
                continue

            cliente = Cliente(proximo_id_cliente, nome)
            clientes.inserir(cliente)

            print("✅ Cliente cadastrado com sucesso!")
            print(cliente)

            proximo_id_cliente += 1

        elif opcao == 2:
            print("\n--- Lista de Clientes ---")
            clientes.listar()

        elif opcao == 3:
            while True:

             nome = input("Digite o nome do produto: ").strip()

             if nome == "":
                print("⚠️ Nome não pode ser vazio!")
                continue           
             try:
                quantidade = int(input("Digite a quantidade do produto: "))
                preco = float(input("Digite o preço do produto: "))     
             except:
                print("⚠️ Quantidade e preço devem ser números!")
                continue
             produto = Produto(proximo_id_produto, nome, quantidade, preco)
             produtos.inserir(produto)
             print("✅ Produto cadastrado com sucesso!")
             print(produto)
             proximo_id_produto += 1 
            

        elif opcao == 4:
            print("\n--- Lista de Produtos ---")
            produtos.listar()

        elif opcao == 5:
            print("Pesquisar produto")

        elif opcao == 6:
            print("Realizar venda")

        elif opcao == 7:
            print("Ver vendas")

        elif opcao == 8:
            print("Desfazer operação")

        elif opcao == 9:
            print("Total estoque")

        elif opcao == 10:
            print("Total vendas")

        elif opcao == 11:
            print("Clientes e gastos")

        elif opcao == 12:
            print("Saindo do sistema...")
            break

        else:
            print("⚠️ Opção inválida!")


if __name__ == "__main__":
    main()