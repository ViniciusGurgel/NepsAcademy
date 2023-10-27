def main():
    A = int(input())
    estados = input()
    lista = [int(n) for n in estados.split()]
    A = 0
    B = 0
    for _ in lista:
        if _ == 1:
            A += 1 
        else:
            A += 1 
            B += 1
    print("1" if A % 2 else "0")
    print("1" if B % 2 else "0")

if __name__ == "__main__":
    main()
