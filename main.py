import json

# Variável global
categorias = ["Bebida", "Entradas", "Pratos Principais", "Sobremesas"]


# Carregar o conteúdo do arquivo cardapio.txt e atribui à variável cardapio
with open("./cardapio.txt", "r") as arquivo:
    conteudoArquivo = arquivo.read()
    cardapio = json.loads(conteudoArquivo)


def buscar():
    print("-----------------------------------------------------------")
    esc = str(input("Digite o nome do produto: "))
    var_escolha = False
    for item in cardapio:
        if item["nome"] == esc.title():
            var_escolha = True
            print("Nome do produto: ", item["nome"])
            print("Custo do produto : R$", item["pr"])
            print("Categoria: ", item["categoria"])
            print("Sub Categoria: ", item["sub_categoria"])
    if var_escolha == False:
        print("Produto nao encontrado")
    print("-----------------------------------------------------------")


def alterar_item():
    print("-----------------------------------------")
    print("\n1 - Bebidas \n2 - Entradas \n3 - Pratos Principais \n4 - Sobremesas")
    
    while True:
        Escolha = int(
            input(
                "\nEscolha um número para selecionar a categoria do item a ser apagado: "
            )
        )
        if Escolha == 1:
            Escolha = "bebidas"
            break
        elif Escolha == 2:
            Escolha = "entrada"
            break
        elif Escolha == 3:
            Escolha = "pratos principais"
            break
        elif Escolha == 4:
            Escolha = "sobremesas"
            break
        else:
            print("\nNúmero inválido, digite um válido!")
    for i,produto in enumerate(cardapio):
        
        if produto['categoria'] == Escolha:
            print(f"|{i} - {produto['nome']}")
            
            
    
    # # while True:
    # #     produto_alterar = input("\nQual produto deseja alterar no cardápio: ")

    # #     encontrou_produto = False
    # #     for produto in cardapio:
    # #         if produto["nome"].lower() == produto_alterar.lower(): 
    # #             encontrou_produto = True


    # #             print("\nEscolha qual informação deseja alterar:")
    # #             print("1. Nome")
    # #             print("2. Preço")
    # #             print("3. Categoria")
    # #             print("4. Sub-categoria")
    # #             opcao = input("Opção: ")


    #             # if opcao == "1":
    #             #     novo_nome = input("Digite o novo nome: ")
    #             #     produto["Nome"] = novo_nome
    #             # elif opcao == "2":
    #             #     novo_preco = input("Digite o novo preço: ")
    #             #     produto["pr"] = novo_preco
    #             # elif opcao == "3":
    #             #     nova_categoria = input("Digite a nova categoria: ")
    #             #     produto["categoria"] = nova_categoria
    #             # elif opcao == "4":
    #             #     nova_subcategoria = input("Digite a nova sub-categoria: ")
    #             # else:
    #             #     print("Opção inválida.")
            

    #             print(f"\n'{produto_alterar}' foi atualizado.")
    #             break

    #     if not encontrou_produto:
    #         print(f"\n'{produto_alterar}' não foi encontrado no cardápio da cafeteria. Tente novamente.")
    #         continue

    #     print("\nProdutos depois da alteração:")
    #     for produto in cardapio:
    #         print(produto)
        
        # break
    print("-----------------------------------------")


def adicionarItem():
    nome = str(input("Nome do produto: "))
    preco = float(input("Preço do produto: "))
    categoria = ""
    while True:
        print("Selecione uma categoria:")
        for i, opcao in enumerate(categorias):
            print(f"{i + 1} - {opcao}")
        escolha = int(input("Digite o número da categoria: ")) - 1
        if escolha >= 0 and escolha <= len(categorias):
            categoria = categorias[escolha]
            break
    sub_categoria = str(input("Subcategoria do produto: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "categoria": categoria,
        "sub_categoria": sub_categoria,
    }

    cardapio.append(produto)


def listar_produtos():
    print(
        "1 - Bebidas\n2 - Entrada\n3 - Pratos Principais\n4 - Sobremesas\n5 - Todos os Produtos"
    )

    while True:
        esc = int(input("\nDigite o número referente a listagem: "))
        print("\nListagem dos produtos a seguir\n")
        if esc == 1:
            for item in cardapio:
                if item["categoria"] == str("bebidas"):
                    print(item["nome"])
            break
        if esc == 2:
            for item in cardapio:
                if item["categoria"] == str("entrada"):
                    print(item["nome"])
            break
        if esc == 3:
            for item in cardapio:
                if item["categoria"] == str("pratos principais"):
                    print(item["nome"])
            break
        if esc == 4:
            for item in cardapio:
                if item["categoria"] == str("sobremesas"):
                    print(item["nome"])
            break
        if esc == 5:
            for item in cardapio:
                if item["categoria"]:
                    print(item["nome"])
            break
        else:
            print("Escolha uma opção válida")
    print("-------------------------------------------------------------------------")


def excluir():
    print("\n1 - Bebidas \n2 - Entradas \n3 - Pratos Principais \n4 - Sobremesas")

    while True:
        Escolha = int(
            input(
                "\nEscolha um número para selecionar a categoria do item a ser apagado: "
            )
        )
        if Escolha == 1:
            Escolha = "bebidas"
            break
        elif Escolha == 2:
            Escolha = "entrada"
            break
        elif Escolha == 3:
            Escolha = "pratos principais"
            break
        elif Escolha == 4:
            Escolha = "sobremesas"
            break
        else:
            print("\nNúmero inválido, digite um válido!")

    listaEscolhida = []
    print("Cardápio")
    print(47 * "-")
    for i, item in enumerate(cardapio):
        if Escolha in item.values():
            print(f'|{i} - {item["nome"]} R${item["pr"]:.2f}')
            listaEscolhida.append(i)

    while True:
        EscolhaEX = int(
            input("\nEscolha o número correspondente ao produto para apagá-lo: ")
        )
        if EscolhaEX in listaEscolhida:
            print(
                f'\nFoi apagado o item ({cardapio[EscolhaEX]["nome"]}) com preço (R${cardapio[EscolhaEX]["pr"]:.2f})'
            )
            del cardapio[EscolhaEX]
            break
        else:
            print("\nInsira um número válido!")

    print(f"\nCardápio Atualizado!")
    print(47 * "-")

    for index in cardapio:
        print(f'|{index["nome"]} R${index["pr"]:.2f}')


print("-----------------------------------------")
print("Escolha a função do programa")

print("0 - Adicionar itens ao cardápio")
print("1 - Excluir itens do cardápio")
print("2 - Alterar itens do cardápio")
print("3 - Buscar itens no cardápio")
print("4 - Listar todos os itens do cardápio")
print("-----------------------------------------")

while True:
    escolha = int(input("Digite o número referente a função: "))
    if escolha == 0:
        adicionarItem()
        break
    if escolha == 1:
        excluir()
        break

    if escolha == 2:
        alterar_item()
        break

    if escolha == 3:
        buscar()
        break

    if escolha == 4:
        listar_produtos()
        break
    print("Escolha uma opção válida")

with open("./cardapio.txt", "w") as arquivo:
    arquivo.write(json.dumps(cardapio))
