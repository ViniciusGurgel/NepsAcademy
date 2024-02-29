def main():
    count_2, count_3,count_4 = 0 , 0 , 0
    for _ in range(int(input())):
        number = int(input())
        if number % 2 == 0:
            count_2 += 1
        if number % 3 == 0:
            count_3 += 1
        if number % 4 == 0:
            count_4 += 1
    print(count_2)
    print(count_3)
    print(count_4)

if __name__ == "__main__":
    main()
