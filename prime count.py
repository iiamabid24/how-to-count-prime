primecount=0
for num in range(142,1295):
    faccount=0
    for div in range(2,num+1):
        if num%div==0:
            faccount+=1
    if faccount==1:
        primecount+=1
        
print(primecount)
        