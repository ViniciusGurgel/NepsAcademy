def main():
    A = int(input())
    lista = []
    for i in range(A):
        number = input()
        lista.extend(int(digits.strip()) for digits in number.strip())
    for n in range(10):
        print(f"{n} - {lista.count(n)}")
if __name__ == "__main__":
    main()
