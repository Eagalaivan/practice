def georock():
    S,R=map(int,input().split())
    count=[]
    samples=list(map(int,input().split()))
    # samples.sort()
    for i in range(R):
        r1,r2=map(int,input().split())
        sum=0
        for j in range(S):
            if(samples[j]>r1 and samples[j]<r2):
                sum+=1
        count.append(sum)
    for i in count:
        print(i,end=" ")
georock()
# def geosum(sample,ranges):
    
#     s=[345, 604, 321, 433, 704, 470, 808, 718, 517, 811]
#     #print(s)
#     count=[0]*ranges
#     temp=0
#     for i in range(0,ranges):
#         r1,r2=300,350
#         for j in range(sample):
#             if(s[i]>=r1 and s[j]<=r2):
#                 count[i]+=1
#     for i in count:
#         print(i)
# sample,ranges= 10,2
# geosum(sample,ranges)
