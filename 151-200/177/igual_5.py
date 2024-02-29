def main():
    count = 0
    lista = [int(input()) for _ in range(3)]
    for i in lista:
        if i % 2 == 0 or i % 5 == 0:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
