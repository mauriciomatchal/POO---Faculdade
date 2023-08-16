def valor_final(desconto, preco):
    valor = preco * (100 - desconto) / 100
    return valor

print(valor_final(5, 100))
