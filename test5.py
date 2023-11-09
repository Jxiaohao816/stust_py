def fc(a,b):
    square = a ** b
    def infc(a,b):
        return a+b
    add = infc(a,b)
    return add+5
print(fc(5,10))