# x = 'harsh'
# x.count('h')
x2=input("Enter customer name")
sum=0
while(True):
    user_Input=input("ENter the product name")
    userInput=input("ENter the price\n")
    if(userInput != 'q'):
        sum=sum + int(userInput)

    else:
        x1=f"Customer name who shopped at your store is {x2}.He shopped {user_Input} products..And customer shopped for totoal of ruppes{sum}..Thanks for shopping"

        print(x1)
        break


