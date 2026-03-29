tabuleiro = [["   " for j in range(8)]for i in range(8)]
pecas_brancas = [' T ',' C ','>B ',' D ',' R ',' B<',' C ',' T ',' P ']
pecas_pretas = [' t ',' c ','>b ',' d ',' r ',' b<',' c ',' t ',' p ']

for z in range(8):
    for n in range(8):
        if z == 0:
            tabuleiro[z][n] = pecas_brancas[n]
        elif z == 1:
            tabuleiro[z][n] = pecas_brancas[8]

        if z == 6:
            tabuleiro[z][n] = pecas_pretas[8]
        elif z == 7:
            tabuleiro[z][n] = pecas_pretas[n]
        print(f"[{tabuleiro[z][n]}]", end="")

    print()
