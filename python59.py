n1 = int(input('primeiro valor'))
n2 = int(input('segundo valor'))
opção = 0
while opção !=5:
    print('''    20
          [1] somar
    [2] multiplicar
    [3] maior
    [4] novbos números
    [5] sair do programa''')
    opção = int(input('Qual é sua opção: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} e {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2 
        print('A multiplicação entre {} e {} e {}'.format(n1, n2, produto))   
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe números novamente')
        n1 = int(input("primeiro valor"))
        n2 = int(input("segundo valor"))
    elif opção == 5:
        print('finalizando')
    else:
        print('Opção inválida. Tente novamente')
print('Fim do programa, Volte sempre')