def ehprimo(A):
    if A <= 1:
        return False
    for n in range(2,A):
        if A % n == 0:
            return False
    return True
def main():
    A = int(input())
    print("S" if ehprimo(A) else "N")
    
if __name__ == "__main__":
    main()
