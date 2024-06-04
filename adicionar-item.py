import os
import json


categorias = ["Bebida", "Entradas", "Pratos Principais", "Sobremesas"]


def criarArquivoBase():
    with open("./cardapio.txt", "w") as arquivo:
        arquivo.write("[]")


if not os.path.exists("./cardapio.txt"):
    criarArquivoBase()

with open("./cardapio.txt", "r") as arquivo:
    conteudoArquivo = arquivo.read()
    if conteudoArquivo == "":
        criarArquivoBase()
    cardapio = json.loads(conteudoArquivo)

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

with open("./cardapio.txt", "w") as arquivo:
    arquivo.write(json.dumps(cardapio))
