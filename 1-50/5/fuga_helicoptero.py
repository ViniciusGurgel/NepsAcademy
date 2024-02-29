def main():
    H, P, F ,D = map(int,input().split())
    lista = ["H" if i == H else "P" if i == P else "F" if i == F else 0 for i in range(17)]
    lista_aux = lista[F+1:]
    lista_aux2 = lista[:F]
    lista_final = lista_aux + lista + lista_aux2
    for i,v in enumerate(lista_final):
        if v == 'F':
            index = i
    if D == -1:
        for i in range(len(lista_final[:index]),D,D):
            if lista_final[i] == 'H':
                print('S')
                break
            elif lista_final[i] == 'P':
                print('N')
                break
    if D == 1:
        for i in range(0,len(lista_final[index:]),D):
            if lista_final[i] == 'H':
                print('S')
                break
            elif lista_final[i] == 'P':
                print('N')
                break
    
        

if __name__ == "__main__":
    main()
