def main():
    P, R = map(int, input().split())
    print("C" if P == 0 else ("B" if R == 0 else "A"))

if __name__ == "__main__":
    main()
