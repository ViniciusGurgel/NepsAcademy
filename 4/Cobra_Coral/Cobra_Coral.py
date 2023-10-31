def main():
    lista = list(map(int,input().split()))
    if lista[0] == lista[2] or lista[1] == lista[3]:
        print("V")
    else:
        print("F")

if __name__ == "__main__":
    main()
