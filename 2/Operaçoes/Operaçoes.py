def main():
    A = input()
    B , C = map(float,input().split())
    print( '{:.2f}'.format(B*C) if A == 'M' else '{:.2f}'.format(B/C))
    
if __name__ == "__main__":
    main()
