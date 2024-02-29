def main():
    A = int(input())
    B = input()
    lista = [int(n) for n in B.split()]
    consecutive = 0
    max = 0
    for n in range(len(lista)-1):
        if lista[n] == lista[n + 1]:
            consecutive += 1
        else:
            consecutive += 1
            if consecutive > max:
                max = consecutive
            consecutive = 0
    if consecutive > max:
        consecutive += 1
        max = consecutive
    print(max)

if __name__ == "__main__":
    main()
