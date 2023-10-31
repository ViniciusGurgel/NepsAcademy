def main():
    A = int(input())
    lista = []
    for i in range(1,11):
        lista.append(A+i)
    print(" ".join(map(str,lista)))
if __name__ == "__main__":
    main()
