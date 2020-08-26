def bracebalance(string):
    stack=[]
    braces = {
                "{":"}",
                "[":"]",
                "(":")"
            }
    for i in string:
        if i in braces:
            stack.append(braces[i])
        else:
            if(len(stack)==0 or stack.pop()!=i):
                return False
    return len(stack)==0
string=input()

if(bracebalance(string)):
    print("valid")
else:
    print("invalid")