def fc(x):
    if x:
        return x+fc(x-1)
    else:
        return 0
print(fc(10))
