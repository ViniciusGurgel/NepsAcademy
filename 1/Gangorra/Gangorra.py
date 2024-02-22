def main():
    P1, C1, P2, C2 = map(int, input().split())
    produto_esquerda = P1 * C1
    produto_direita = P2 * C2
    print(0 if produto_esquerda == produto_direita else (1 if produto_esquerda < produto_direita else -1))

if __name__ == "__main__":
    main()
