import math
def solutionbank():
    bank=[0,0,0]
    l=0
    principal=float(input('principal'))
    tenure=float(input('tenure'))
    for i in range(2):
        slabs1=int(input('slab'))
        sum=0.0
        for j in range(0,slabs1):
            years,monthlyinterestrate=map(float,input('year,monthrate').split())
            #monthlyinterestrate=float(input('rate'))
            po=pow((1+monthlyinterestrate),(years*12))
            emi = principal*monthlyinterestrate/(1-1/po)
            sum+=emi
        bank[i+1]=sum
    print(bank)
    if(bank[1]<bank[2]):
        print("Bank A")
    else:
        print("Bank B")
solutionbank()
# EMI = loanAmount * monthlyInterestRate / ( 1 – 1 / (1 +
# monthlyInterestRate)^(numberOfYears * 12))
# import math
# def solutionbank():
#     bank=[0]*3
#     principal=10000
#     tenure=20
#     all_sum=0.0
#     for i in range(2):
#         slabs=int(input("slabs"))
#         for i in range(slabs):
#             years,rateofinterest=map(float,input().split())
#             po=pow((1+rateofinterest),years*12)
#             emi=(principal*rateofinterest)/(1-(1/po))
#             all_sum+=emi
#         bank[i]=all_sum
#     print(bank)
#     if(bank[1]<bank[2]):
#         print("Bank A")
#     else:
#         print("Bank B")
# solutionbank()