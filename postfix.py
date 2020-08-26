class postfix:
    def __init__(self,capacity):
        self.capacity = capacity
        self.top = -1
        self.array = []
        self.result = []
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array.pop()
    def peek(self):
        return self.array[-1]

    def isOperand(self):
        if self.isalpha():
            self.result.append()
    def push(self,operator):
        self.top+=1
        self.array.append(operator)
    def postfixexecu(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                v1= self.pop()
                v2= self.pop()
                self.push(str(eval(v2 + i +v1)))
        return int(self.pop())
class InfixConversion: 
    def __init__(self, capacity): 
        self.top = -1 
        self.capacity = capacity 
        self.array = [] 
        self.output = [] 
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def peek(self): 
        return self.array[-1] 
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "$"
    def push(self, op): 
        self.top += 1
        self.array.append(op)  
    def isOperand(self, ch): 
        return ch.isalpha() 
    def notGreater(self, i): 
        try: 
            a = self.precedence[i] 
            b = self.precedence[self.peek()] 
            return True if a  <= b else False
        except KeyError:  
            return False
    def infixToPostfix(self, exp): 
        for i in exp: 
            if self.isOperand(i): 
                self.output.append(i) 
            elif i  == '(': 
                self.push(i) 
            elif i == ')': 
                while( (not self.isEmpty()) and self.peek() != '('): 
                    a = self.pop() 
                    self.output.append(a) 
                if (not self.isEmpty() and self.peek() != '('): 
                    return -1
                else: 
                    self.pop() 
            else: 
                while(not self.isEmpty() and self.notGreater(i)): 
                    self.output.append(self.pop()) 
                self.push(i) 
        while not self.isEmpty(): 
            self.output.append(self.pop()) 
  
        print ("".join(self.output)) 
iexp = "a+b*(c^d-e)-i"
obj = InfixConversion(len(iexp)) 
obj.infixToPostfix(iexp) 
pexp = "53*4-"
obj = postfix(len(pexp))
print(obj.postfixexecu(pexp))