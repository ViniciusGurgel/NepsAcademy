def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    if B == C:
        if B+C == D:
            if A == B+C+D:
                print("S")
            else:
                print("N")
        else:
            print("N")
    else:
        print("N")
        
    
if __name__ == "__main__":
    main()
