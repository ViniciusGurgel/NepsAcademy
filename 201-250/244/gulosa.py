def main():
    C = int(input())
    lista = [100,50,25,10,5,1]
    contador = 0
    for n in lista:
        restante = C // n
        contador += restante
        C %= n
    print(contador)
if __name__ == "__main__":
    main()
