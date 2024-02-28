def main():
    N = int(input())
    lista = [int(input()) for _ in range(N)]
    repeated = len(lista) - len(set(lista))
    print(N-repeated)

if __name__ == "__main__":
    main()
