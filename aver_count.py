P_v=0
N_v=0
S_p=0
S_n=0
c=0
while(True):
    a=int(input())
    if(a>=0):
        P_v+=1
        S_p+=a
    elif(a==-1):
        break
    else:
        N_v+=1
        S_n+=a
aver_p=S_p/P_v
aver_n=S_n/N_v
print(f"The average of positive number is {aver_p}\nThe average of Negative Number is {aver_n}")

    


