def main():
    A = int(input())
    B = input()
    C = input()
    acertos = 0
    index = 0
    for char in B:
        if char == C[index]:
            acertos += 1 
        index += 1
    print(acertos)
if __name__ == "__main__":
    main()
