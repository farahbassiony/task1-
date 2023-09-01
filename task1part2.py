text= input("enter a text\n")
letters=0
words=1
sentences=0
for i in text:
    if i.isalpha():
        letters+=1
    elif i==" ":
        words+=1
    elif i=="." or i=="?" or i=="!":
        sentences+=1
l=letters/words*100
s= sentences/words*100
result=(0.0588*l)-(0.296*s)-15.8
approx=int(result)
if approx<1:
    print("before grade 1")
elif approx >1 and approx<16:
    print("grade "+ str(approx))
elif approx >16:
    print("grade 16+")    

                 
