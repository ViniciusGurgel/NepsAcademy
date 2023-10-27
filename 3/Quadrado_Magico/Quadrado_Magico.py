def main():
    A = int(input())
    lista = []
    for i in range(A):
        lista.append(list(map(int,input().split())))
    lista_aux = []
    for _ in lista:
        lista_aux.append(sum(_))
        for i in range(len(_)):
            diagonal = i
            soma_numero = 0
            soma_diagonal = 0
            for n in range(A):
                soma_numero += lista[n][i]
                if i == 0:
                    soma_diagonal += lista[n][diagonal]
                    diagonal += 1
                elif i == len(lista) - 1:
                    soma_diagonal += lista[n][diagonal]
                    diagonal -= 1
            lista_aux.append(soma_numero)
            if i == 0 or i == len(lista) - 1:
                lista_aux.append(soma_diagonal)
    printar = True
    for num in lista_aux:
        if num != lista_aux[len(lista_aux)-1]:
            printar = False
            break
    print(f"{lista_aux[0]}" if printar else "-1")
    
if __name__ == "__main__":
    main()
