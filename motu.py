
# tests = int(input())
# for _ in range(tests):
#     n = int(input())
#     a = list(map(int,input().split()))
#     s = 1
#     l = n-1
#     c_first = a[0]/2
#     c_second = 0
#     while s<=l:
#         mid = (l-s)//2 + s
#         first_half = sum(a[s:mid])/2 + c_first
#         second_half = sum(a[mid+1:l+1]) + c_second
#         if first_half == second_half:
#             s = mid+1
#             c_first = first_half + a[mid]/2
#             first_half = c_first
#             if c_second != 0:
#                 second_half = c_second
#             break
#         elif first_half < second_half:
#             c_first = first_half + a[mid]/2
#             first_half = c_first
#             s = mid+1
#         else:
#             c_second = second_half + a[mid]
#             second_half = c_second
#             l = mid-1
#     motu = s
#     patlu = n - motu
#     print(motu, patlu)
#     if motu > patlu:
#         print('Motu')
#     elif motu < patlu:
#         print('Patlu')
#     else:
#         print('Tie')


tests = 1
for _ in range(tests):
    n = 5
    a = [2,6,2,1,7]
    s = 1
    l = n-1
    c_first = a[0]/2
    c_second = 0
    while s<=l:
        mid = (l-s)//2 + s
        first_half = sum(a[s:mid])/2 + c_first
        second_half = sum(a[mid+1:l+1]) + c_second
        if first_half == second_half:
            s = mid+1
            c_first = first_half + a[mid]/2
            first_half = c_first
            if c_second != 0:
                second_half = c_second
            break
        elif first_half < second_half:
            c_first = first_half + a[mid]/2
            first_half = c_first
            s = mid+1
        else:
            c_second = second_half + a[mid]
            second_half = c_second
            l = mid-1
    motu = s
    patlu = n - motu
    print(motu, patlu)
    if motu > patlu:
        print('Motu')
    elif motu < patlu:
        print('Patlu')
    else:
        print('Tie')