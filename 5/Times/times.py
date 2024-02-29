def formar_times(T, alunos):
    alunos.sort(key=lambda x: x[1], reverse=True)
    times = [[] for _ in range(T)]
    for i, aluno in enumerate(alunos):
        times[i % T].append(aluno[0])
    return times

def main():
    N,T = map(int,input().split())
    alunos = []
    for _ in range(N):
        name , skill = input().split()
        alunos.append((name,int(skill)))
    times = formar_times(T, alunos)
    for i, time in enumerate(times, 1):
        print("Time", i)
        for jogador in sorted(time):
            print(jogador)
        print()
    
if __name__ == "__main__":
    main()
