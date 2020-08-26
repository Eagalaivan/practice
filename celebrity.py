def eliminate_non_celebrities(matrix):
    possible_celeb = 0
    n = len(matrix)
    for p in range(1, n):
        if (matrix[possible_celeb][p]
            or not matrix[p][possible_celeb]):
            possible_celeb = p
    return possible_celeb
def check_if_celebrity(possible_celeb, matrix):
    for i in range(n):
        if matrix[possible_celeb][i]==1:
            return False
    for i in range(n):
        if matrix[i][possible_celeb]==0:
            if i != possible_celeb:
                return False
    return True
n = int(input('Number of people: '))
m=[]
a=[]
for i in range(n):
    a=list(map(int,input().split()))
    m.append(a)
possible_celeb = eliminate_non_celebrities(m)
 
if check_if_celebrity(possible_celeb, m):
    print('{} is the celebrity.'.format(possible_celeb))
else:
    print('There is no celebrity.')