# a=int(input("Enter the number:"))
# if a>0:
#     print("positive number")
# elif a<0:
#     print("negative")    
# else:
#     print("zero")    

# a=int(input("enter the number"))
# if a%5==0 and a%11==0:
#     print("correct")
# elif a%5==0:
#     print("divisible by 5")
# elif a%11==0:
#     print("divisible by 11")
# else:
#     print("not disible by both")            

# a=4+4j
# b=3+5j
# print(a*b)

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# i=0
# while i<len(places):
#     i+=1
#     print(places[-i])
    # i+=1

# a = 7 + 7j
# b = 5 - 5j
# print(a+b)

# a=input("Enter the Alphabet")
# if a>="a" and a<="z":
#     print("Lower")
# elif a>="A"and a<="Z":
#     print("upper")    
# else:
#     print("not a alphabet")    


# n=1234
# a=n%10
# b=(n//10)%10
# c=(n//100)%10
# d=(n//1000)%10
# reverse=(a*1000)+(b*100)+(c*10)+(d*1)
# if reverse>1000:
#     print(reverse)
# else:
#     print("invalid")    
# # print(a,b,c,d)

n=1234
a=n%10
b=(n//10)%10
print(b)

name=str(input("Enter the name"))
if str("ly") in name:
    print(name,"\bing")
elif "ing" in name:
    print(name,"\bly")
else:
    print(name,"\blying")    
