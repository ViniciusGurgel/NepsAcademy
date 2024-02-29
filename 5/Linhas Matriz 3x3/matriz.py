def main():
    lista = [int(input()) for _ in range(9)]
    for i in range(3):
        print(f'Linha {i}: {sum(lista[i*3:i*3+3])}')

if __name__ == "__main__":
    main()
