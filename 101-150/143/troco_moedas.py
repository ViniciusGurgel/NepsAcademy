def main():
    C = int(input())
    lista = [100,50,25,10,5,1]
    contador = 0
    lista_moedas = []
    for n in lista:
        restante = C // n
        contador += restante
        lista_moedas.append(restante)
        C = C % n
    print(contador)
    for i in lista_moedas:
        print(i)
if __name__ == "__main__":
    main()
