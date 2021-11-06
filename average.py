from typing import Counter


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0; count=0
sum1=0; counta=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        count+=1
    else:
        sum1=sum1+elements[i]
        counta+=1
    i+=1
print(sum,"even",count)
print(sum1,"odd",counta)            
print("Average, even=",sum/count)
print("Average ,odd=",sum1/counta) 