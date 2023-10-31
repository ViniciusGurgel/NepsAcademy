def main():
    valores = list(map(int, input().split()))
    N = int(input())
    indices = []
    count = 0
    for i in range(10):
        if valores[i] == N:
            count += 1
            indices.append(i)
    if count > 0:
        print(count)
        print(" ".join(map(str,indices)))
    else:
        print("Mia x")

if __name__ == "__main__":
    main()
