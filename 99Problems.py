N = int(input())
match = []
for i in range (-100, 101):
    x = N + i 
    if(str(x)[-2:] == '99' and x > 0):
        match.append((x,abs(i)))
if(len(match) < 2):
    print(match[0][0])
if(len(match) > 1):
    if(match[0][1] == match[1][1]):
        if(match[0][0] > match[1][0]):
            print(match[0][0])
        else:
            print(match[1][0])
if(len(match) > 1):
    if(match[0][1] < match[1][1]):
        print(match[0][0])
    elif(match[0][1] > match[1][1]):
        print(match[1][0])



