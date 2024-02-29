def main():
    A = int(input())
    B = int(input())
    lista = list(range(min(A,B),max(A,B)+1))
    print(" ".join(map(str,lista)))
    
if __name__ == "__main__":
    main()
