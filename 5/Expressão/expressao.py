def expressao(string):
    lista_aux = []
    matching = {'{': '}', '[': ']', '(': ')'}
    for char in string:
        if char in '{[(':
            lista_aux.append(char)
        elif char in ']})':
            if not lista_aux or matching[lista_aux.pop()] != char:
                return False
    return not lista_aux

def main():
    lista = []
    for _ in range(int(input())):
        lista.append(input())
    for i in lista:
        if expressao(i):
            print("S")
        else:
            print("N")
if __name__ == "__main__":
    main()
