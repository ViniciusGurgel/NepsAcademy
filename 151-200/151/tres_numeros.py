def main():
    lista = [int(input()) for _ in range(3)]
    lista_aux = sorted(lista)
    for i in lista_aux:
        print(i)

if __name__ == "__main__":
    main()
