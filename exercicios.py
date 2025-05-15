#def depositopoupanca():
    #valor_total = int(input("Deposite o valor de depósito em sua poupança: R$"))
    #porcentagem = 1.3
    #valor_parte = valor_total * (porcentagem/100)
    #valor_rendido = valor_parte + valor_total
    #mensagem = "Após 1 mês seu dinheiro vai ser " + str(valor_rendido) +"R$, rendendo 1,3% ao mês."
    #print(mensagem)

#depositopoupanca()


#def CelsiusparaF():
    #C = int(input("Digie a temperatura em graus Celsius: "))
    #F = (9*C+160)/5
    #valor_convertido = "A temperatura " + str(C) + "ºC" +" em Graus Celsius, convertida para Fahrenheit fica: "+str(F) + "F"
    #print(valor_convertido)

#CelsiusparaF()


def Diferenca():
    V1 = int(input("Digite um valor: "))
    V2 = int(input("Digite o segundo valor: "))
    
    if V1 > V2:
        print ("A Diferença de valores é de:", V1-V2)
    
    else:
        print ("A Diferença de valores é de:", V2-V1)

Diferenca()