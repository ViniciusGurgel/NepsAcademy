def main():
    C = int(input())
    lista = list(map(int,input().split()))
    lista = list(dict.fromkeys(lista))
    print(len(lista)*2)
    
if __name__ == "__main__":
    main()
