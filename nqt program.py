def first():
    ds=[10.0,20.0,304.0,50.0]
    amt=[]
    # input line by line int and string mixed getinput until n is pressed
    while(True):
        order=int(input())
        quantity=int(input())
        amt.append(ds[order-1]*quantity)
        if input()=='n':
            break
    print(sum(amt)) 
first()
def second():
    order=list(map(int,input().split()))
    quant=list(map(int,input().split()))
    ismember=input()
    menu=[50,100,40,200,300]
    amt=0.0
    for i in range(3):
        amt+=menu[i] * quant[i]
    if ismember=='y' and amt>1000:
        amt-=(amt*15)/100
        print(amt)
    elif ismember=='n' and amt>1000:
        amt-=(amt*10)/100
        print(amt)
    elif ismember=='y' and amt<1000:
        amt-=(amt*5)/100
        print(amt)
 second()

# third problem

def third():
    inp=input()
    softtoys=['GIANT-TEDDY-BEAR','GIRAFFE','CAT',
              'MEGABEAR','DOG','LION','BILLY-BEAR',
              'BESTY-BEAR','MONKEY','BOBBY-BEAR',
              'BUNNY-RABBIT','BENJAMIN-BEAR',
              'KUNG-FU-PANDA','BROWN BEAR',
              'PINK-BEAR','BABY-ELEPHANT',
              'BLUE-FISH','HIPPO','CUTE-PIG',
              'PIKACHU','DOREMON','TORTISE',
              'CATERPILLAR','CANDY-DOLL']
   
    print(softtoys.pop(softtoys.index(inp)))
    print(softtoys)
third()

def fourth():
    choice=int(input())
    tv=[10000,7000,6000]
    if choice < 1 or choice  > 3:
        print("INVALID INPUT")
    schoice=input()
    cashtopay=tv[choice-1]
    if schoice=="yes" or schoice=='Yes':
        tchoice=input()
    else:
        print(cashtopay)
    if schoice=='yes' and tchoice=='working':
        cashtopay-=(cashtopay*20)/100
        print(cashtopay)
    elif schoice=='yes' and tchoice=='notworking':
        cashtopay-=(cashtopay*2)/100
        print(cashtopay)
fourth()
    