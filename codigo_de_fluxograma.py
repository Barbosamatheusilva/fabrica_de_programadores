def banco():
    saldo_numero = int(input("Digite seu saldo bancário: "))
    saque_numero = int(input("Digite o valor do saque: "))

    if saldo_numero >= saque_numero:
        saldo_numero = saldo_numero - saque_numero

        print("Você realizou o saque com sucesso.")
    else:
        print("Você não possui saldo suficiente, para realizar este saque.")

banco()