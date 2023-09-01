x=int(input("enter the height that should be between 1 and 8\n"))
while x<1 or x>8:
    print ("please enter another number within the required range\n") 
    x=input (" ") 



for i in range(1,int(x)+ 1):
    print((" " * (8 - i)) + ("#" * i) +"  "+("#" * i) )         

