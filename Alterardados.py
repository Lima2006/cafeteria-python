produtoscafeteria = {
    "nome": "cappuccino",
    "pr": 7,
    "categoria": "bebidas",
    "sub-categoria": "bebida quente"
}

print("produtos:")
print(produtoscafeteria)

itens = input("Qual a informaçao que deseja alterar: ")

if itens in produtoscafeteria:
    novo_valor = input(f"Informe o novo valor para o produto: '{itens}': ")
    produtoscafeteria[itens] = novo_valor

    print("\nInformaçoes atualizadas:")

    print(produtoscafeteria)

else:
    print(f"A informaçao '{itens}' nao exite no catálogo.")