a=int(input("enter the deepu age: "))
b=int(input("Enter the madhu age: "))
c=int(input("enter the kajal age: "))
if b<a and c<a:
    print("a is oldest",a)
    if b<c:
        print("b is youngest",b)
    else:
        print("c is youngest",c)    
elif a<b and c<b:
    print("b is oldest",b)
    if a<c:
        print("a is youngest",a)
    else:
        print("c is youngest",c)    
else:
    print("c is oldest",c)
    if a<b:
        print("a is youngest",a)
    else:
        print("b is youngest",b)    