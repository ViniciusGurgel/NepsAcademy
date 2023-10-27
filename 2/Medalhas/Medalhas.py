def main():
    A = int(input())
    B = int(input())
    C = int(input())
    lista = [A, B, C]
    primeiro = lista.index(min(lista))+1
    terceiro = lista.index(max(lista))+1
    lista[lista.index(min(lista))] = 0
    lista[lista.index(max(lista))] = 0
    print(primeiro)
    print(lista.index(max(lista))+1)
    print(terceiro)

if __name__ == "__main__":
    main()
