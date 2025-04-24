#a = 1
#
#while a < 101:
#    print(a)
#    a = a + 1

#a = 50
#
#while a < 101:
#    print(a)
#    a = a + 1

#print("10, 9, 8, 7, 6, 5, 4, 3, 2, 1 e Fogo!")


#numero = int(input("Digite um número:"))
#
#i = 1
#
#while i <= numero:
#    if i % 2 == 0:
#        print(i)
#    i += 1

#numero = int(input("Digite um número:"))
#
#i = 1
#
#while i <= numero:
#    if i % 2 != 0:
#        print(i)
#    i += 1

inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

soma = 0

if inicio > fim:
    print("O número inicial deve ser menor ou igual ao número final.")
else:
    i = inicio
    while i <= fim:
        soma += i
        i += 1

    print(f"A soma dos números de {inicio} até {fim} é: {soma}")
