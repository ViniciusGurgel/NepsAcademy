def main():
    jogadores = ["A","B","C"]
    B = input()
    lista = [int(n) for n in B.split()]
    if lista.count(1) == 1:
        index = lista.index(1)
        print(jogadores[index])
    elif lista.count(0) == 1:
        index = lista.index(0)
        print(jogadores[index])
    else:
        print("*")
if __name__ == "__main__":
    main()
