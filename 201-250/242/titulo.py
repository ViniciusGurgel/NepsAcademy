def main():
    A = input()
    string = ''
    for letter in range(len(A)):
        if letter == 0:
            string += A[letter].upper()
        elif A[letter-1] == ' ':
            string += A[letter].upper()
        else:
            string += A[letter].lower()
    print(string)
    
if __name__ == "__main__":
    main()
