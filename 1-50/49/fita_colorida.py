def main():
    A = int(input())
    lista = list(map(int, input().split()))
    n = len(lista)
    resultado = [0] * n
    lista_0 = [i for i in range(n) if lista[i] == 0]
    for i in range(n):
        if lista[i] == -1:
            distancia_minima = min(abs(i - j) for j in lista_0)
            resultado[i] = min(distancia_minima, 9)
    print(" ".join(map(str, resultado)))
    
if __name__ == "__main__":
    main()
