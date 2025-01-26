number = input()
names = []

if (2<=int(number)<=20):
    for i in range(int(number)):
        name = input()
        if (2<=len(name)<=12) and name.isupper():
            names.append(name)
    
    if (len(names)>=1):
        if names == sorted(names):
            print('INCREASING')
        elif names == sorted(names, reverse=True):
            print('DECREASING')
        else:
            print('NEITHER')