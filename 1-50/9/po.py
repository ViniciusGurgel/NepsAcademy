def main():
    N = int(input())
    lista = [int(input()) for _ in range(3)]
    lista.sort()
    count = 0
    for i in lista:
        if i <= N:
            count += 1
            N -= i
        else:
            break
    print(count)

if __name__ == "__main__":
    main()
