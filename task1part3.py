x=int(input("enter the amount of money\n"))
x1=x//200
x=x-(200*x1)
x2=x//100
x=x-(100*x2)
x3=x//50
x=x-(50*x3)
x4=x//20
x=x-(20*x4)
x5=x//10
x=x-(10*x5)
x6=x//5
x=x-(5*x6)
if(x1):
    print(str(x1)+"*200  L.E +" )
if(x2):
    print(str(x2)+"*100  L.E +" )    
if(x3):
    print(str(x3)+"*50  L.E +" )
if(x4):
    print(str(x4)+"*20  L.E +" ) 
if(x5):
    print(str(x5)+"*10 L.E +" )
if(x6):
    print(str(x6)+"*5  L.E +" )
if(x):
    print(str(x)+" L.E" )        

