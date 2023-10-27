def main():
    A = int(input())
    B = int(input())
    resultado = (A*2 + B*3) / 5
    if resultado >= 7:
        print("Aprovado")
    elif resultado < 3:
        print("Reprovado")
    else:
        print("Final")

if __name__ == "__main__":
    main()
