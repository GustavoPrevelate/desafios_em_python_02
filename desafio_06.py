# Você está criando um programa para um caixa de supermercado.

# O programa deve:

# Perguntar ao usuário o preço dos produtos (um por vez).
# Continuar perguntando até o usuário digitar 0 (que indica o fim das compras).
# No final, mostre:
# O total da compra.
# Quantos produtos foram comprados.


total = 0.0
qtdproduto = 0

while True:
    produto = float(input("qual o preço do produto: "))
    if produto == 0:
        break
    total += produto
    qtdproduto += 1

print("Compra finalizada!")
print(f"O valor total da sua compra é {total:.2f}")
print(f"VOcê comprou {qtdproduto} produto(s).")




