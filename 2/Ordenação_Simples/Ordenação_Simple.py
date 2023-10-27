def main():
    A = int(input())
    lista = [int(_) for _ in input().split()]
    lista.sort()
    print(" ".join(map(str,lista)))
    
if __name__ == "__main__":
    main()
