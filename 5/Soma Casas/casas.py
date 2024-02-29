def main():
    lista = []
    for _ in range(int(input())):
        lista.append(int(input()))
    K = int(input())
    esquerda, direita = 0, len(lista) - 1
    while esquerda < direita:
        soma = lista[esquerda] + lista[direita]
        if soma == K:
            print(f'{lista[esquerda]} {lista[direita]}')
            break
        elif soma < K:
            esquerda += 1
        else:
            direita -= 1

if __name__ == "__main__":
    main()
