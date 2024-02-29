def main():
    A = int(input())
    soma = 1
    for n in range(1,A+1):
        soma *= n
    print(soma)
    
if __name__ == "__main__":
    main()
