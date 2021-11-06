# m= [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
# i=0
# while i<len(m):
#     j=0
#     sum=0
#     while j<len(m):
#         sum=sum+m[i][j]
#         j+=1
#     print(sum)
#     # i+=1    
#     a=0
#     suma=0
#     while a<len(m):
#         suma=suma+m[a][i]
#         a+=1
#     print(suma)
#     i+=1    
# p=0
# for i in range (len(m)):
#     for c in range(len(m[i])):
#         if i==c:
#             p=p+m[i][c]
# print("diagolous",p)
# s=0
# for i in range(len(m)):
#     for c in range(len(m[i])):
#         if i+c==len(m[i])-1:
#             s=s+m[i][c]
# print("diagnolous",s)


students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
print (len(students))
print (len(marks))
length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
counter = 0
while counter < length:
    print (students[counter] + str(marks[counter]))
    counter+=1