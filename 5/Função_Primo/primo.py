def eh_primo(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

x = int(input())
if eh_primo(x):
    print('S')
else:
    print('N')


