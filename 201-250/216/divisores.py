def main():
    A = int(input())
    lista = [n for n in range(1,A) if A % n == 0]
    lista.append(A)
    print(' '.join(map(str,lista)))

if __name__ == "__main__":
    main()
