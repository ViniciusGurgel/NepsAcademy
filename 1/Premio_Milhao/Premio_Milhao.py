def main():
    A = int(input())
    lista = []
    for dias in range(A):
        lista.append(int(input()))
    mil = 0
    for index, value in enumerate(lista):
        mil += value
        if mil >= 1000000:
            print(index + 1)
            break

if __name__ == "__main__":
    main()
