import json

# Variável global
CATEGORIAS = ["bebidas", "entrada", "pratos principais", "sobremesas"]


def ler_arquivo_json(caminho):
    with open(caminho, "r") as arquivo:
        conteudoArquivo = arquivo.read()
        return json.loads(conteudoArquivo)


def escrever_arquivo_json(dados, caminho):
    with open(caminho, "w") as arquivo:
        arquivo.write(json.dumps(dados))


escrever_arquivo_json(
    {"nome_da_cafeteria": "Cafeteria Tô com Fome", "porcentagem_do_garcom": 0.015},
    "configuracoes.txt",
)


# Carrega o conteúdo do arquivo cardapio.txt e atribui à variável cardapio
cardapio = ler_arquivo_json("./cardapio.txt")
carrinho = ler_arquivo_json("./carrinho.txt")
configuracoes = ler_arquivo_json("./configuracoes.txt")


def adicionar_item():
    nome = str(input("Nome do produto: "))
    preco = float(input("Preço do produto: "))
    categoria = ""
    while True:
        print("Selecione uma categoria:")
        for i, opcao in enumerate(CATEGORIAS):
            print(f"{i} - {opcao}")
        escolha = int(input("Digite o número da categoria: "))
        if escolha >= 0 and escolha <= len(CATEGORIAS):
            categoria = CATEGORIAS[escolha]
            break
    sub_categoria = str(input("Subcategoria do produto: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "categoria": categoria,
        "sub_categoria": sub_categoria,
    }

    cardapio.append(produto)


def alterar_item():
    print("-----------------------------------------")
    for i, categoria in enumerate(CATEGORIAS):
        print(f"{i} - {categoria}")

    while True:
        indexCategoriaEscolhida = int(
            input("Selecione a categoria do item a ser editado: ")
        )
        if indexCategoriaEscolhida >= 0 and indexCategoriaEscolhida < len(CATEGORIAS):
            break
        print("Insira um valor válido!")
    quantidadeDeItemsElegiveis = 0
    for i, produto in enumerate(cardapio):
        if produto["categoria"] == CATEGORIAS[indexCategoriaEscolhida]:
            quantidadeDeItemsElegiveis += 1
            print(f"|{i} - {produto['nome']}")
    if quantidadeDeItemsElegiveis == 0:
        print("Sem produtos nessa categoria!")
        return
    while True:
        indexProdutoSelecionado = int(input("Selecione o produto para alterar: "))
        if (
            indexProdutoSelecionado >= 0
            and indexProdutoSelecionado < quantidadeDeItemsElegiveis
        ):
            break
        print("Insira um valor válido!")
        print("Insira os novos valores (se não deseja alterar o campo, deixe vazio)")
    itemParaEditar = cardapio.pop(indexProdutoSelecionado)
    nome = str(input("Nome do produto: ")) or itemParaEditar["nome"]
    preco = float(input("Preço do produto: ") or 0) or itemParaEditar["preco"]
    categoria = itemParaEditar["categoria"]
    opcoes = ["não alterar"]
    opcoes.extend(CATEGORIAS)
    while True:
        print("Selecione uma categoria:")
        for i, opcao in enumerate(opcoes):
            print(f"{i} - {opcao}")
        escolha = int(input("Digite o número da categoria: "))
        if escolha == 0:
            break
        if escolha > 0 and escolha < len(opcoes):
            categoria = CATEGORIAS[escolha - 1]
            break
        print("Insira uma opção válida!")
    sub_categoria = (
        str(input("Subcategoria do produto: ")) or itemParaEditar["sub_categoria"]
    )

    produto = {
        "nome": nome,
        "preco": preco,
        "categoria": categoria,
        "sub_categoria": sub_categoria,
    }

    cardapio.append(produto)
    print("-----------------------------------------")


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
            print(f'|{i} - {item["nome"]} R${float(item["preco"]):.2f}')
            listaEscolhida.append(i)

    while True:
        EscolhaEX = int(
            input("\nEscolha o número correspondente ao produto para apagá-lo: ")
        )
        if EscolhaEX in listaEscolhida:
            print(
                f'\nFoi apagado o item ({cardapio[EscolhaEX]["nome"]}) com preço (R${cardapio[EscolhaEX]["preco"]:.2f})'
            )
            del cardapio[EscolhaEX]
            break
        else:
            print("\nInsira um número válido!")

    print(f"\nCardápio Atualizado!")
    print(47 * "-")


def buscar():
    print("-----------------------------------------------------------")
    esc = str(input("Digite o nome do produto: "))
    var_escolha = False
    for item in cardapio:
        if item["nome"].lower() == esc.lower():
            var_escolha = True
            print("Nome do produto: ", item["nome"])
            print("Custo do produto : R$", item["preco"])
            print("Categoria: ", item["categoria"])
            print("Sub Categoria: ", item["sub_categoria"])
    if var_escolha == False:
        print("Produto nao encontrado")
    print("-----------------------------------------------------------")


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


def add_carrinho():
    print("---------------------------------------------------------------------------")
    for i, categoria in enumerate(CATEGORIAS):
        print(f"{i} - {categoria}")

    while True:
        indexCategoriaEscolhida = int(
            input("Selecione a categoria do item a ser adicionado ao carrinho: ")
        )
        if indexCategoriaEscolhida >= 0 and indexCategoriaEscolhida < len(CATEGORIAS):
            break
        print("Insira um valor válido!")
    indicesElegiveis = []
    for i, produto in enumerate(cardapio):
        if produto["categoria"] == CATEGORIAS[indexCategoriaEscolhida]:
            indicesElegiveis.append(i)
            print(f"|{i} - {produto['nome']}")
    if len(indicesElegiveis) <= 0:
        print("Sem produtos nessa categoria!")
        return
    while True:
        indiceProdutoSelecionado = int(
            input("Selecione o produto para adicionar ao carrinho: ")
        )
        if indiceProdutoSelecionado in indicesElegiveis:
            carrinho.append(cardapio[indiceProdutoSelecionado])
            break
        print("Insira um índice válido!")
        print("Itens no carrinho: ")
    print("---------------------------------------------------------------------------")


def mostrar_carrinho():
    soma = 0
    porcentagemDoGarcom = float(configuracoes["porcentagem_do_garcom"])
    for item in carrinho:
        soma += float(item["preco"])
        print(f"{item['nome']} (R$ {float(item['preco']):.2f})")
    print(f"A soma dos valores dos produtos escolhidos será R$ {soma:.2f}")
    print(f"A porcentagem do garçom é {porcentagemDoGarcom * 100}%")
    totalCarrinho = soma * (porcentagemDoGarcom + 1)
    print(f"O total dos valores será R$ {totalCarrinho:.2f}")


def limpar_carrinho():
    carrinho.clear()
    print("Carrinho esvaziado com sucesso!")

def remov_item_carrinho():
    for i, item in enumerate(CATEGORIAS):
            print(f"{i} - {item}")

    while True: 
        Cat_Escolhida = []
        Escolha = str(input("\nEscolha um número para selecionar a categoria do item a ser removido: "))
        while True: 
            if Escolha == "0":
                Escolha = "bebidas"
                break
            elif Escolha == "1":
                Escolha = "entrada"
                break
            elif Escolha == "2":
                Escolha = "pratos principais"
                break
            elif Escolha == "3":
                Escolha = "sobremesas"
                break
            else:
                break
            
        for i, item in enumerate(carrinho):
            if Escolha in item.values():
                Cat_Escolhida.append(i)
        if len(Cat_Escolhida) == 0:
            print("\nA opção é inválida ou essa categoria ainda não foi adicionada ao carrinho. Escolha outra!")
        else:
            break
   
    print("Carrinho")
    print(47 * "-")
    
    for i, item in enumerate(carrinho):
        if Escolha in item.values():
            print(f"|{i} - {item['nome']} R${float(item['preco']):.2f}")
            Cat_Escolhida.append(str(i))
    
    while True:
        Escolha_remov = str(input("\nEscolha o indíce correspondente ao produto para removê-lo: "))
        if Escolha_remov in Cat_Escolhida:
            print(f'\nFoi removido o item ({carrinho[int(Escolha_remov)]["nome"]}) com preço (R${carrinho[int(Escolha_remov)]["preco"]:.2f})')
            del carrinho[int(Escolha_remov)]
            break
        else:
            print("\nInsira um número válido!")

        print(f"\nCarrinho Atualizado!")
        print(47 * "-")
                


print("-----------------------------------------")
print(configuracoes["nome_da_cafeteria"])
print("-----------------------------------------")
print("Escolha a função do programa")

print("0 - Adicionar itens ao cardápio")
print("1 - Excluir itens do cardápio")
print("2 - Alterar itens do cardápio")
print("3 - Buscar itens no cardápio")
print("4 - Listar todos os itens do cardápio")
print("5 - Adicionar produtos ao carrinho")
print("6 - Mostrar carrinho")
print("7 - Remover item do carrinho")
print("8 - Limpar o carrinho")
print("-----------------------------------------")

while True:
    escolha = int(input("Digite o número referente a função: "))
    
    if escolha == 0:
        adicionar_item()
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

    if escolha == 5:
        add_carrinho()
        break

    if escolha == 6:
        mostrar_carrinho()
        break

    if escolha == 7:
        remov_item_carrinho()
        break

    if escolha == 8:
        limpar_carrinho()
        break

    else:
        print("Escolha uma opção válida")


# Guardar o cardapio atualizado no arquivo cardapio.txt
escrever_arquivo_json(cardapio, "./cardapio.txt")
# Guardar o carrinho atualizado no arquivo carrinho.txt
escrever_arquivo_json(carrinho, "./carrinho.txt")
