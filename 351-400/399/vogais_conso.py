def main():
    S = input()
    vogais = 'AaEeIiOoUu'
    print('Vogais: '+ ''.join(i for i in S if i in vogais))
    print('Consoantes: '+''.join(_ for _ in S if _ not in vogais))

if __name__ == "__main__":
    main()
