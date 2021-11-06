# print(4000/100*10)


bs=int(input("Enter the salary: "))
if bs<=10000:
    hra=bs/100*20;ba=bs/100*80
    print(int(bs+hra+ba))
elif bs<=20000:
    hra=bs/100*25;ba=bs/100*90
    print(int(bs+hra+ba))
elif bs>20000:
    hra=bs/100*30;ba=bs/100*95
    print(int(bs+hra+ba))    
else:
    print("invalide")    

# print(100+1234)
