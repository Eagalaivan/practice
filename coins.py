def coinsfinder(n):
    five = two = one = 0
    temp = n
    while temp % 5 != 0:
        temp -= 1
    five = (temp//5) - 1
    temp = n - (5*five)
    if temp % 2 == 0:
        one = 2
    else:
        one = 1
    temp -= one
    two = temp//2
    print((five+two+one),five,two,one)
    # print("totalcoins",five+two+one)
    # print("5 coin(s)",five)
    # print("2 coin(s)",two)
    # print("1 coin(s)",one)
n=int(input())
coinsfinder(n)