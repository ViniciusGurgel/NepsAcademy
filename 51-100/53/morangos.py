def main():
    C1 = int(input())
    L1 = int(input())
    C2 = int(input())
    L2 = int(input())
    print(C1*L1 if C1*L1>C2*L2 else C2*L2)

if __name__ == "__main__":
    main()
