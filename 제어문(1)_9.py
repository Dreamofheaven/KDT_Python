num = int(input("정수를 입력하세요 > "))

if num < 1: 
    print(False)
else:
    for i in range(1, num):
        if i % 2 != 0:
            print(i)
    