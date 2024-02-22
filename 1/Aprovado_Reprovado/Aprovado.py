A, B = map(float,input().split())
print('Aprovado' if (A+B) / 2 >= 7 else ('Recuperacao' if (A+B) / 2 >= 4 else 'Reprovado'))

