def main():
    A = int(input())
    B = input()
    lista = [float(n) for n in B.split()]
    for n in lista:
        print("{:.4f}".format(n ** (1/2)))
if __name__ == "__main__":
    main()
