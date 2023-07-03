# if / elif    / else
# se / se não se / se não

entrada = input("Você quer entrar ou sair? ").strip().upper()
if entrada == "entrar".upper().strip():
    print("Você entrou no sistema!")
elif entrada == "sair".upper().strip():
    print("Você saiu do sistema")
else:
    print("Você não digitou nem entrar nem sair")

print("Fora dos blocos")