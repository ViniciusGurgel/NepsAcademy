def main():
    A = int(input())
    B = int(input())
    C = int(input())
    print(B if A == C else C if A == B else A)

if __name__ == "__main__":
    main()
