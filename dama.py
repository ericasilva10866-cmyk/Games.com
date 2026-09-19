# Tabuleiro: 8x8 | 0=vazio, 1=peça jog1, 2=peça jog2, 3=dama1, 4=dama2
def criar_tabuleiro():
    tab = [[0]*8 for _ in range(8)]
    # Jogador 2 (cima)
    for l in range(3):
        for c in range(8):
            if (l+c) % 2 == 1: tab[l][c] = 2
    # Jogador 1 (baixo)
    for l in range(5,8):
        for c in range(8):
            if (l+c) % 2 == 1: tab[l][c] = 1
    return tab

def mostrar(tab):
    print("  0 1 2 3 4 5 6 7")
    for l in range(8):
        print(f"{l}", end=" ")
        for c in range(8):
            simb = {0:'.',1:'○',2:'●',3:'◉',4:'◎'}[tab[l][c]]
            print(simb, end=" ")
        print()

def pode_mover(tab, l1, c1, l2, c2, jog):
    peca = tab[l1][c1]
    if tab[l2][c2] != 0: return False
    dl = l2 - l1
    dc = abs(c2 - c1)
    if dc != abs(dl): return False
    # Peça normal
    if peca in (1,2):
        if dl*(-1 if jog==1 else 1) < 0: return False # só pra frente
        if abs(dl)==1 and dc==1: return True
    # Dama: qualquer direção
    if peca in (3,4) and abs(dl)==dc: return True
    return False

def pode_capturar(tab, l1, c1, l2, c2, jog):
    peca = tab[l1][c1]
    if peca in (1,2):
        meio_l = (l1+l2)//2; meio_c = (c1+c2)//2
        if abs(l2-l1)==2 and abs(c2-c1)==2:
            oponente = 2 if jog==1 else 1
            if tab[meio_l][meio_c] in (oponente, oponente+2) and tab[l2][c2]==0:
                return True, meio_l, meio_c
    return False,0,0

def jogar():
    tab = criar_tabuleiro()
    jog = 1
    while True:
        mostrar(tab)
        print(f"→ Vez Jogador {jog}")
        try:
            l1,c1 = map(int,input("De (lin col): ").split())
            l2,c2 = map(int,input("Para (lin col): ").split())
        except: continue
        if tab[l1][c1] in (jog, jog+2):
            capt,ml,mc = pode_capturar(tab,l1,c1,l2,c2,jog)
            if capt:
                tab[l2][c2] = tab[l1][c1]
                tab[l1][c1] = tab[ml][mc] = 0
                print("⚔️ Capturou!")
            elif pode_mover(tab,l1,c1,l2,c2,jog):
                tab[l2][c2] = tab[l1][c1]
                tab[l1][c1] = 0
            else:
                print("❌ Movimento inválido!")
                continue
            # Virar Dama
            if jog==1 and l2==0: tab[l2][c2] = 3
            if jog==2 and l2==7: tab[l2][c2] = 4
            jog = 2 if jog==1 else 1

if __name__ == "__main__":
    jogar()

