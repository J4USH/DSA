import math
a=input()
b=int(a)
s=0
c=len(a)
while(b>0):
    d=b%10
    s+=int(math.pow(d,c))
    b=int(b/10)
a=int(a)
if(s==a):
    print(f"The Number {a} is an Armstrong Number")