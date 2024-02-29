def main():
    risada = input()
    vogais = 'aeiou'
    risada_sem_consoantes = ''.join(letra for letra in risada if letra in vogais)
    
    if risada_sem_consoantes == risada_sem_consoantes[::-1]:
        print("S")
    else:
        print("N")
if __name__ == "__main__":
    main()
