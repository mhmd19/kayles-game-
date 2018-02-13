import random
tokens=[]
size=random.randint(10,20)
print("size = ",size)
a=0
for i in range (size+1):  
    tokens.append(i)
    print(i,end=",")
arr1=[]
f=True
d=True
while True:    
    while f==True:
        print("\n\n player1 :please , press 1 or 2 to choose number of tokens?")
        x=int(input())
        if x==1:
            print("enter the number")
            y=int(input())
            if y<=size:
                if (y not in arr1):
                    a=a+1
                    arr1.append(y)  
                    tokens[y]="-"
                    print (tokens,end=',')
                    if a==size+1:
                        print("\n  player 1 wins")
                        f=False
                        d=False
                        break
                    else:
                        f=False
                        d=True
                else:
                    print("entered before , try again")
            else:
                print("error , not in the domain , try again")            
        elif x==2:
            print("\n enter the two numbers")
            while f==True:
                z1=int(input())
                z2=int(input())
                if (z1 and z2) <=size:
                    if(z2==z1+1):
                        if z1 not in arr1 and z2 not in arr1:
                            a=a+2
                            arr1.append(z1)
                            arr1.append(z2)
                            tokens[z1]="-"
                            tokens[z2]="-"
                            print (tokens,end=',')
                            if a==size+1:
                                print("\n  player 1 wins")
                                f=False
                                d=False
                                break
                            else:
                                f=False
                                d=True
                        else:
                            print("entered before , try again")
                    else:
                        print("error , please enter two successive numbers")
                        break
                else:
                    print("error : not in the domain try again")
               
        else:
            print("please choose 1 or 2 tokens only")
    while d==True:
        print("\n\n player2 :psress 1 or 2 to choose number of tokens?")
        x1=int(input())
        if x1==1:
            print("enter the number")
            y1=int(input())
            if y1<=size:
                if y1 not in arr1:
                    a=a+1
                    arr1.append(y1)  
                    tokens[y1]="-"
                    print (tokens,end=',')
                    if a==size+1:
                        print("\n  player 2 wins")
                        d=False
                        f=False
                        break
                    else:
                        d=False
                        f=True
                else:
                    print("entered before , try again")
            else:
                print("error , try again")
        elif x1==2:
            print(a)
            print("\n enter the two numbers")
            while True:
                s1=int(input())
                s2=int(input())
                if (s1 and s2) <=size:
                    if(s2==s1+1):
                        if s1 not in arr1 and s2 not in arr1:
                            a=a+2
                            arr1.append(s1)
                            arr1.append(s2)
                            tokens[s1]="-"
                            tokens[s2]="-"
                            print (tokens,end=',')
                            if a==size+1:
                                print("\n  player 2 wins")
                                d=False
                                f=False
                                break
                            else:
                                d=False
                                f=True
                                break
                        else:
                            print("entered before , try again")
                    else:
                        print("error ,please enter two successive numbers")
                        break
                else:
                    print("error : not in the domain , try again")
               
        else:
            print("please choose 1 or 2 tokens only")
    if f==False and d==False:
        break
       
