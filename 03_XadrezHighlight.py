N = int(input('entre com N'))
while N != 0:
    # coletando os dados
    nome_coluna_linha = input().split(' ')
    nome = nome_coluna_linha[0]
    c = ord(nome_coluna_linha[1])-ord('a')
    l = int(nome_coluna_linha[2])


    # printando as informaçoes
    for i in range(N, 0, -1):
        print(i, end=' ')
        for j in range(N):
            if i == l and j == c:
                print('o', end=' ')
            # movimento de cada peça (Rei, Dama,Torre,Bispo,Cavalo,Peao)
            elif nome == "Rei" and (((l-i)**2+(c-j)**2)**1/2) <= 1:
                print('x', end=' ')

            elif nome == "Dama" and (i == l or j == c or (abs(c-j) == abs(i-l))):
                print('x', end=' ')

            else:
                print('-', end=' ')

        print()
    print(end='  ')
    for i in range(N):
        print(chr(ord('a')+i), end=' ')