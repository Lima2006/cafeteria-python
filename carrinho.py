import json

CATEGORIAS = ['bebidas', 'entradas', 'pratos principais', 'sobremesas' ]
opc_carrinho = ['Adicionar ao carrinho', 'Mostrar o carrinho', 'Remover item do carrinho', 'Redefinir carrinho']

def ler_arquivo_json(caminho):
    with open(caminho, "r") as arquivo:
        conteudoArquivo = arquivo.read()
        return json.loads(conteudoArquivo)


def escrever_arquivo_json(dados, caminho):
    with open(caminho, "w") as arquivo:
        arquivo.write(json.dumps(dados))


# Carrega o conteúdo do arquivo cardapio.txt e atribui à variável cardapio
cardapio = ler_arquivo_json("./cardapio.txt")
carrinho = ler_arquivo_json("./carrinho.txt")
        
def add_carrinho():
    
    for i, item in enumerate(CATEGORIAS):
        print(f"{i} - {item}")
    while True:
        escolha_add = str(input("\nEscolha o índice da categoria do item a ser adicionado: "))
        if escolha_add == "0":
            escolha_add = "bebidas"
            break
        elif escolha_add == "1":
            escolha_add = "entrada"
            break
        elif escolha_add == "2":
            escolha_add = "pratos principais"
            break
        elif escolha_add == "3":
            escolha_add = "sobremesas"
            break
        else: 
            print("\nOpção inválida, escolha uma válida!")

    Cat_escolhida = []
    print("Cardápio")
    print(47 * "-")

    for i, item in enumerate(cardapio):
        if escolha_add in item.values():
            print(f"|{i} - {item['nome']} R${float(item['preco']):.2f}")
            Cat_escolhida.append(str(i))

    while True:
        escolha_add1 = str(input("\nEscolha o indíce do item a ser adicionado no carrinho: "))
        if escolha_add1 in Cat_escolhida:
            print(f"\nO item adicionado ao carrinho foi ({cardapio[int(escolha_add1)]['nome']}) com o preço (R${cardapio[int(escolha_add1)]['preco']:.2f})")
            carrinho.append(cardapio[int(escolha_add1)])
            break
        else:
            print("\nSelecione uma opção válida!")


def mostrar_carrinho():
    soma = 0
    print("\nO carrinho é composto por:\n")
    for i, item in enumerate(carrinho):
        print(f"|{i} - {item['nome']} R${item['preco']:.2f}")
        soma += item['preco']
    print(f"\nO preço do carrinho é R${soma:.2f}")

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
                
def redefinir_carrinho():
    carrinho.clear()
    print("\nO carrinho foi redefinido!")

print()
for i, item in enumerate(opc_carrinho):
    print(f"{i} - {item}")
while True:
    carrinho_alter = str(input("\nEscolha o que quer fazer com o carrinho: "))
    print()
    if carrinho_alter == "0":
        add_carrinho()
        break
    if carrinho_alter == "1":
        mostrar_carrinho()
        break
    if carrinho_alter == "2":
        remov_item_carrinho()
        break
    if carrinho_alter == "3":
        redefinir_carrinho()
        break
    else:
        print("\nOpção inválida, selecione uma válida!")
        
escrever_arquivo_json(carrinho, "./carrinho.txt")
        