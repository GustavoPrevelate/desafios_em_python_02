# O computador vai "pensar" em um número aleatório entre 1 e 100, e o usuário precisa adivinhar qual é esse número.

#O programa deve:

# Gerar o número aleatório usando a biblioteca random.
# Permitir que o usuário tente adivinhar várias vezes.
# Dizer se o número digitado é maior ou menor do que o número gerado.
# Mostrar uma mensagem de parabéns quando o usuário acertar.

import random
numerosecreto = random.randint(1, 100)

while True:
    numerousuario = int(input("Qual o nº secreto? "))
    if numerosecreto == numerousuario:
        print("Parabéns você acertou!")
        break
    elif numerosecreto > numerousuario:
        print("O número secreto é maior que esse")
    else:
        print("O nº secreto é menor que esse.")

              