import random

n = int(input("enter no of keys : "))
c = 0
l = []

while c<n:
    num = str(random.randint(0,9))
    let = random.randint(97,122)
    pos = random.randint(0,n)
    cho = random.randint(0,2)
    if cho == 0:
        l.insert(pos, num)
    elif cho == 1:
        l.insert(pos, chr(let))
    else:
        l.insert(pos, "#")
    c+=1

print("your password is == ","".join(l))


