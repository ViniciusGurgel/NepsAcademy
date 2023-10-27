def main():
    A = int(input())
    lista = [int(input()) for _ in range(A)]
    for i in range(A):
        if i == 0:
            print(sum(lista[:2]))
        else:
            print(sum(lista[i-1:i+2]))

if __name__ == "__main__":
    main()
