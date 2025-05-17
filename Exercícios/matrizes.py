def mult_matrizes(a,b):
    nLinhasA = len(a); # pega o numero de linhas na Matriz A
    nColunasA = len(a[0]); # pega o numero de Colunas na Matriz A
    nColunasB = len(b[0]); # pega o numero de Colunas na Matriz B

    M = []; # Cria a matriz Vazia para conter o resultado

    for linha in range(nLinhasA): # para cada linha presente na matriz A
        # Começa uma nova linha em M
        M.append([]);
        for coluna in range(nColunasB): # para cada coluna na matriz B
            M[linha].append(0); # cria uma nova coluna na matriz M
            for k in range(nColunasA): # para cada coluna na Matriz A
                M[linha][coluna] +=a[linha][k]*b[k][coluna] # o Valor M [linha] [coluna] será ela mesma mais o valor linha Coluna da matriz A Multiplicado pelo valor b linha coluna da matriz B.
    return M;

A = [
    [1,1,1],
    [2,2,2],
    [3,3,3]
    ];
B = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
    ];


print(mult_matrizes(A,B));
            