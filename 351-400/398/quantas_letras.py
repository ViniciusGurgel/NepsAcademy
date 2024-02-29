def main():
    S = input()
    char = input()
    count = 0
    for letra in S:
        if letra == char:
            count += 1
    print(count)
if __name__ == "__main__":
    main()
