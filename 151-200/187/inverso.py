def main():
    lista = []
    for i in range(10):
        lista.append(input())
    for i in lista[::-1]:
        print(i)
        
if __name__ == "__main__":
    main()
