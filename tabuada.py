#n = int(input("Tabuada de: "))
#x = 1
#while x<=10:
    #print(n+x)
    #x=x+1

#Ex5.6
#n = int(input("Tabuada de: "))
#x = 1
#while x<=10:
    #print((n), "x", (x),"= ", n*x)
    #x=x+1



#Ex5.7
#def Tabuada():
    #n1 = int(input("Digite o número que você quer multiplicar: "))
    #n2 = int(input("Digite até onde vai a tabuada: "))
    #while n1<=n2:
        #print((n1), "x", (n2),"= ", n1*n2)
        #n1=n1+1
#Tabuada()


#S=0
#while True:
    #V=int(input("Digite um número a somar ou 0 para sair: "))
    #if V==0:
        #break
    #S = S+V
#print(S)



#Ex5.14
soma = 0
L = []
while True:
    numeros = int(input("Digite um número (digite 0 para fazer a lista de números digitados): "))
    if numeros==0:
        break
    L.append(numeros)
    soma+=numeros
print("O Resultado da soma é: ", soma)
print("A média aritmética: ", soma/ len(L))