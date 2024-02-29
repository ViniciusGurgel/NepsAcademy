def main():
    A = int(input())
    lista = [str(i) for i in input().split()]
    if lista[1] == '+':
        resultado = int(int(lista[0]) + int(lista[2]))
    else:
        resultado = int(int(lista[0]) * int(lista[2]))
    print("OK" if resultado <= A else "OVERFLOW")
    
if __name__ == "__main__":
    main()
