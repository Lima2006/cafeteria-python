print("-----------------------------------------")
with open("./cardapio.txt", "w") as arquivo:
    arquivo.write(json.dumps(cardapio))

print("Cardápio completo:")
print(cardapio)

itens = input("Qual a informaçao do cardápio que deseja alterar: ")

if itens in cardapio:
    novo_valor = input(f"Informe a nova informaçao para o produto: '{itens}': ")
    cardapio[itens] = novo_valor

    print("\nCardápio atualizado:")

    print(cardapio)

else:
    print(f"A informaçao '{itens}' nao existe no cardápio.")
print("-----------------------------------------")
