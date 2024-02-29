def main():
    N, M = map(int, input().split())
    medalhas = {i: [0, 0, 0] for i in range(1, N + 1)}
    for _ in range(M):
        O, P, B = map(int, input().split())
        medalhas[O][0] += 1
        medalhas[P][1] += 1
        medalhas[B][2] += 1
    classificacao = sorted(medalhas.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2], x[0]))
    for pais, _ in classificacao:
        print(pais, end=' ')

if __name__ == "__main__":
    main()
