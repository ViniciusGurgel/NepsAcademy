def main():
    N = int(input())
    D = int(input())
    A = int(input())
    print((N-A)+D if A > D else D-A)

if __name__ == "__main__":
    main()
