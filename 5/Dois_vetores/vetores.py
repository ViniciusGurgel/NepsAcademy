def main():
    lista = [int(input()) for _ in range(10)]
    num_par = []
    num_impar = []
    for num in lista:
        if num % 2 == 0:
            num_par.append(str(num))
        else:
            num_impar.append(str(num))
    print(' '.join(num_par))
    print(' '.join(num_impar))

if __name__ == "__main__":
    main()
