def main():
    A = int(input())
    fila = list(map(int,input().split()))
    C = int(input())
    D = list(map(int,input().split()))
    for n in D:
        fila.remove(n)
    print(' '.join(map(str,fila)))
    
    
if __name__ == "__main__":
    main()
