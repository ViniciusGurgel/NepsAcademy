def main():
    A = input()
    lista = [int(n) for n in input().split()]
    lista_0 = [index for index,value in enumerate(lista) if value == 0]
    lista_final = []
    for i,v in enumerate(lista):
        lista_ax = []
        for _ in lista_0:
            lista_ax.append(abs(i-_))
        lista_final.append(min(lista_ax))
    print(' '.join(map(str,lista_final)))
    
if __name__ == "__main__":
    main()
