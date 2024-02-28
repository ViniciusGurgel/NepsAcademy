def main():
    N = int(input())
    a,b = 0,1
    fib = []
    for _ in range(N):
        fib.append(str(a))
        a, b = b, a + b
    print(' '.join(fib))

if __name__ == "__main__":
    main()
