def main():
    A = int(input())
    lista = []
    for i in range(A):
        lista.append(list(map(int,input().split())))
    
    nova_lista = []
    linha = [sum(i) for i in lista]
    nova_lista.append(linha)
    
    col = [sum(lista[i][j] for i in range(A)) for j in range(A)]
    nova_lista.append(col)
    
    lista_temp = []
    lista_final = []
    maximo = 0
    for i in range(A):
        lista_temp = [nova_lista[0][i] + nova_lista[1][n] for n in range(A)]
        lista_final.append(lista_temp)
        lista_temp = []
    for _ in range(len(lista_final)):
        for n in range(len(lista_final)):
            lista_final[_][n] -= lista[_][n]*2
        if maximo < max(lista_final[_]):
            maximo = max(lista_final[_])
    print(maximo)
    
if __name__ == "__main__":
    main()
