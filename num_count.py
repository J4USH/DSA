zero=0
P_v=0
N_v=0
while (True):
    a=int(input())
    if(a>0):
        P_v+=1
    elif(a==0):
        zero+=1
    elif(a==-1):
        break
    else:
        N_v+=1
print(f"The No of zeros are {zero} , the no of positive no are {P_v} and the no of negative no are {N_v}")
        
    


