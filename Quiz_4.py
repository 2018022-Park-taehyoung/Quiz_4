number = int(input("몇 단까지 출력할까요?"))
def gugu(end):
    for x in range(1,end+1):
        print("------- [" + str(x) + "단] -------")
        for y in range(1, end+1):
            print(x, "X", y, "=", x*y)
gugu(number)
