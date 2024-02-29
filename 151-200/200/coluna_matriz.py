def main():
    lista = [(int(input()), int(input()), int(input())) for _ in range(3)]
    for i in range(3):
        print(f'Coluna {i}: {lista[0][i] + lista[1][i] + lista[2][i]}')
if __name__ == "__main__":
    main()
