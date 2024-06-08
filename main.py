import json

# Variável global
NOME_DO_RESTAURANTE = "Tô com Fome"
CATEGORIAS = ["bebidas", "entradas", "pratos principais", "sobremesas"]

# Carrega o conteúdo do arquivo cardapio.txt e atribui à variável cardapio
with open("./cardapio.txt", "r") as arquivo:
    conteudoArquivo = arquivo.read()
    cardapio = json.loads(conteudoArquivo)


def adicionar_item():
    nome = str(input("Nome do produto: "))
    preco = float(input("Preço do produto: "))
    categoria = ""
    while True:
        print("Selecione uma categoria:")
        for i, opcao in enumerate(CATEGORIAS):
            print(f"{i + 1} - {opcao}")
        escolha = int(input("Digite o número da categoria: ")) - 1
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
            print(f'|{i} - {item["nome"]} R${item["preco"]:.2f}')
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
    print("Escolha uma opção válida")

# Guardar o cardapio atualizado no arquivo cardapio.txt
with open("./cardapio.txt", "w") as arquivo:
    arquivo.write(json.dumps(cardapio))
