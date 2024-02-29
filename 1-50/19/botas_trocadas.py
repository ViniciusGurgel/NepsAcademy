def main():
    N = int(input())
    lista = [input().split() for _ in range(N)]
    count = 0
    i = 0

    while i < len(lista):
        number = lista[i][0]
        char = lista[i][1]
        j = i + 1
        while j < len(lista):
            if number == lista[j][0] and char != lista[j][1]:
                lista.pop(j)
                lista.pop(i)
                count += 1
                break
            j += 1
        else:
            i += 1

    print(count)

if __name__ == "__main__":
    main()
