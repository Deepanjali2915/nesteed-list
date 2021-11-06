# i=51
# while i<61:
#     z=i-50
#     print(z,"=",z**2)
#     i+=1
    







# row=int(input("Enter the row:"))
# i=0
# k=1
# while i<row:
#     j=0
#     while j<row:
#         print(k,end=' ')
#         print(k)
#         k+=4
#         j+=1
#     print()
#     i+=1

# print(False and 42)
# print(True and 42)


# star=int(input("Enter the number"))
# i=0
# while i<star-i:
#     j=8
#     while j>i:
#         print(i,end='')
#         j+=1
#     print()
#     i-=1    
# i=0
# while i<10:
#     print(i)
#     i+=1



# year=int(input("Enter the year:"))
# salary=int(input("Enter the salary:"))
# persent=salary/100*5
# totalsalary=salary+persent
# if year>=5:
#     print(totalsalary)
# else:
#     print(salary)    

# row=int(input("Enter the number:"))
# i=0
# k=1
# while i<row+1:
#     j=0
#     while j<=i:
#         j+=1
#         print(k,end='')
#         k+=1
#     print(" ")
#     i+=1  



# num=int(input("Enter the number:"))
# i=0
# fac=1
# if fac<0:
#     print("Does not allow negative number")
# elif fac==0:
#     print("fac 0 is 1")
# else:
#     while i<=num+1:
#         fac=fac*i
#         fac+=1
#     print(fac,num) 
#     i+=1       




a=[]
size=int(input("Enter the number: "))
# for i in range(size):
i=0
# val=0
sum=0
while i<size:
    val=int(input("Enter number:"))
    a.append(val)
# for i in range(size):
    sum=sum+a[i]
    i+=1
print(sum)    
