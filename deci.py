#without decimals
import math
d_s=0
c=0
a=int(input())
while(a!=0):
    d=a%2
    d_s=d_s+d*math.pow(10,c)
    c+=1
    a=int(a/2)
print(f"The Binary number is {d_s}")
