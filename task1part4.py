def luhn(card):
    def digits_of(n):
       return [int(d) for d in str(n)] 
    digits=digits_of(card) 
    odd=digits[-1::-2]
    even=digits[-2::-2] 
    check=0
    check+=sum(odd)
    for i in even:
        check+=sum(digits_of(i)*2) 
    return check % 10
card=input("enter the card number\n")
length = len(card)
visa= card
mas= card
ae= card
while int(visa)>=10:
    visa=int(visa)/10
while int(ae)>=10**13:
    ae=int(ae)//10**13
while int(mas)>=10**14:
    mas=int(mas)//10**14

if luhn(card)==0:
    if visa==4 and (length==13 or length==16):
        print("visa") 
    elif length ==15 and (ae==34 or ae==37):
        print("american express")
    elif length ==16 and (51<=mas<=55):
        print("mastercard")
    else:
        print("the card is invalid")     
else:
    print("invalid")            
