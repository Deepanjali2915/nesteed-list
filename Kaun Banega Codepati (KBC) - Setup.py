ques=["Deepanjali's nick name?","Deepanjali brother's name is?","What is capital of india","Deepanjali mother's name is?"]
option=[["1.Anjali","2.Deepa","3.Deepu","4.Anju"],["1.Bander","2.Mohan","3.Kumar","4.Manjeet"],["1.Goa","2.Delhi","3.Haryana","4.Punjab"],["1.Sangeeta","2.Sundhari","3.Anita","4.Kavita"]]
sol=[3,4,2,1]
i=0
a=0
b=1
count=0
while i <len(ques):
    print(ques[i])
    j=0
    while j<len(option):
        print(option[i][j])
        j+=1
    ans=["3.Depu","4.Anju","1.Bander","4.Manjeet","2.Delhi","3.Haryana","1.Sangeeta","Kavita"]
    lifeline=input("If you want life line 50-50:\n PRESS YES\n PRESS NO")
    if lifeline=="y":
        if count==0:
            print(ans[a+i])
            print(ans[b+i])
            answer=int(input("Enter your answer"))
            if sol[i]==answer:
                print("Your answer correct.....")
                count+=1
                break
            else:
                print("Your answer is wrong")
        else:
            print("Your life line is finished")
            print("Now your lifeline is over so please make up your mind") 
            if sol[i]==a:
                print('right')
            else:
                print("your answerr is wrong")
                break
    elif lifeline=='n':
        user=int(input("Choose the answer by your self"))
        if sol[i]==user:
            print("your answer is correct")
        else:
            print("your answer is wrong")
    else:
         print('Thanks for playing the game.. ')
         break
    a+=1
    b+=1
    i+=1
# print("Thanks for playing game..")    
