def main():
    N = int(input())
    lista = list(map(int,input().split()))
    count = 0
    count1 = 0
    for i in range(N):
        if lista[i] < 50:
            count += 1
        elif lista[i] >= 85:
            pass
        else:
            count1 += 1
    print(count , count1)

if __name__ == "__main__":
    main()
