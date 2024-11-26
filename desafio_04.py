# Imagine que você está criando um sistema de login. A pessoa que está tentando acessar precisa digitar a senha correta, 
# mas tem apenas 3 tentativas. Se ela errar as 3 vezes, o sistema bloqueia o acesso.

# O programa deve:

# Guardar uma senha pré-definida, como "1234".
# Permitir que o usuário digite a senha até 3 vezes.
# Exibir uma mensagem de sucesso se a senha estiver correta e uma mensagem de erro se o limite de tentativas for atingido.

senha = "1234"
tentativa = 3

while tentativa > 0:
    senhausuario = input("Senha: ")
    if senha == senhausuario:
        print("Acesso realizado com sucesso!")
        break
    else:
        tentativa -= 1
        if tentativa > 0:
            print(f"senha incorreta! você tem mais {tentativa} tentativa(s)")
        else:        
            print("acesso bloquedo")
