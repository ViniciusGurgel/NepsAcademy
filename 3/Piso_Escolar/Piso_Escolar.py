def main():
    A = int(input())
    B = int(input())
    area = A*B*4 - 1 
    tipo_2 = (A-1)*2 + (B-1)*2
    area -= tipo_2
    print(int((area/2)))
    print(tipo_2)
    
    
if __name__ == "__main__":
    main()
