x = int(input("첫 번째 정수를 입력하세요 > "))
y = int(input("두 번째 정수를 입력하세요 > "))

if x == y:
    print(False)
elif x > y:
    print(x)
else:
    print(y)