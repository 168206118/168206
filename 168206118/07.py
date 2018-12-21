flag =0

for xt in ['A','B','C','D']:
    if(xt!='A')+(xt=='D')+(xt=='B')+(xt!='D')==1:
        print(xt,"shi xiao tou")
        flag=1
if flag==1 :
        if xt=='A':
                print("shuo zhen hua de shi D ")
        if xt=='B':
                print("shuo jia hua de shi B")
        if xt=='C':
                print("shuo zhen hua de shi A")
        if xt=='D':
                print("shuo jia hua de shi D")                
