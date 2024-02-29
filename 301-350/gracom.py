def main():
    A = int(input())
    lista = [list(map(int, input().split())) for _ in range(A)]
    copos = 0
    for i in range(A):
        if lista[i][0] > lista[i][1]:
            copos += lista[i][1]
    print(copos)
if __name__ == "__main__":
    main()
