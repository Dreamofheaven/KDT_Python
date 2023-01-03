x = int(input("첫 번째 정수를 입력하세요 > "))
y = int(input("두 번째 정수를 입력하세요 > "))

if x == y:
    print(False)
elif x > y:
    for i in range(x-1, y, -1):
        print(i, end = " ")
elif x < y:
    for i in range(y-1, x, -1):
        print(i, end = " ")
