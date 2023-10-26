def main():
    A = int(input())
    lista = [int(n) for n in input().split()]
    consecutive = 0
    max = 0
    for n in range(len(lista)-1):
        if lista[n] == lista[n + 1]:
            consecutive += 1
        else:
            consecutive += 1
            if consecutive > max:
                max = consecutive
            consecutive = 0
    if consecutive > max:
        consecutive += 1
        max = consecutive
    print(max)

if __name__ == "__main__":
    main()

# ------------------------------------------------------------ #
def main():
    _ = input()
    lista = list(map(int, input().split()))
    max_count = 0
    current_count = 1
    
    for i in range(1, len(lista)):
        if lista[i] == lista[i - 1]:
            current_count += 1
        else:
            current_count = 1
        
        max_count = max(max_count, current_count)
    
    print(max_count)

if __name__ == "__main__":
    main()
