def is_magic_square(square):
    n = len(square)
    target_sum = sum(square[0])
    
    for i in range(n):
        if sum(square[i]) != target_sum:
            return False
    
    for j in range(n):
        col_sum = sum(square[i][j] for i in range(n))
        if col_sum != target_sum:
            return False
    
    diagonal_sum = sum(square[i][i] for i in range(n))
    if diagonal_sum != target_sum:
        return False
    
    sec_diagonal_sum = sum(square[i][n - 1 - i] for i in range(n))
    if sec_diagonal_sum != target_sum:
        return False
    
    return True

def main():
    n = int(input())
    square = []
    for _ in range(n):
        row = list(map(int, input().split()))
        square.append(row)
    
    if is_magic_square(square):
        print(sum(square[0]))
    else:
        print(-1)

if __name__ == "__main__":
    main()
