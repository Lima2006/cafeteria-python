import json

# Variáveis globais
categorias = ["Bebida", "Entradas", "Pratos Principais", "Sobremesas"]


##### Funções para manipulação de arquivos #####
# Carrega o conteúdo do arquivo cardapio.txt e atribui à variável cardapio
with open("./cardapio.txt", "r") as arquivo:
    conteudoArquivo = arquivo.read()
    cardapio = json.loads(conteudoArquivo)
################################################


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
        break

    if escolha == 2:
        break

    if escolha == 3:
        break

    if escolha == 4:
        break
    print("Escolha uma opção válida")

with open("./cardapio.txt", "w") as arquivo:
    arquivo.write(json.dumps(cardapio))
