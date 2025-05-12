def notamedia():
    nota1 = int(input("Digite sua primeira nota: "))
    nota2 = int(input("Digite sua segunda nota: "))
    media = (nota1+nota2)/2
    if media >= 7:
        print("Parabéns, você está aprovado.")
    else:
        print("Você foi reprovado.")

notamedia()