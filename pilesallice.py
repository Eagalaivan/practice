

player1 = 1
player2 = 2
def calculateMex(set_):
    Mex = 0
    while Mex in set_:
        Mex+=1
    return Mex
def calculateGrundy(n, Grundy):
    Grundy[0] = 0
    Grundy[1] = 1
    Grundy[2] = 2
    Grundy[3] = 3
    if Grundy[n]!=-1:
        return Grundy[n]
    set_ = []
    for i in range(1,4):
        set_.append(calculateGrundy(n-i, Grundy))
    Grundy[n] = calculateMex(set_)
    return Grundy[n]
def declareWinner(start,piles,Grundy,n):
    xorValue = Grundy[piles[0]]
    for i in range(1,n-1+1):
        xorValue=xorValue ^ Grundy[piles[i]]
    if xorValue!=0:
        if(start==player1):
            print("player1 wins")
        else:
            print("player2 wins")
    else:
        if(start==player1):
            print("player2 wins")
        else:
            print("player1 wins")
n=int(input())
piles=list(map(int,input().split()))
maximum=max(piles)
Grundy =[-1]*(maximum+1)
for i in range(1,n-1+1):
    Grundy[i] = calculateGrundy(piles[i],Grundy)
declareWinner(player1,piles,Grundy,n)