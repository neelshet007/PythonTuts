# # n=18
# #MAI CHANCES WALA NAHI KAR PAYA KI BATO KITNE CHANCES BACHE HAII
# PAR MAINE ISME EK BAAR WILE LOOP USE KIA ORR IF ELIF ELSE
# print("Hello to guess the number game\nYou will only have 9 chances")
# x1=int(input("Enter the number"))
# while (x1==18):
#     print("You have guess it correctly")
#     x1=x1+1
# if x1>18:
#     print("You have enetered wrong number please decrease the number")
# else:
#     print("You have entered wrong number please decrease your number")
#This is from comment try to understand it depply

#Code with haary website solution

# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n = 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses <= 9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 18:
        print("you enter less number please input greater number.\n")
    elif guess_number > 18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses, "no.of guesses he took to finish.")
        break
    print(9 - number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses > 9):
    print("Game Over")

#1 comment
n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over"

#2 comment
pc = 100
print("please guess a number\n")
k = int(input())
while(True):
    if k>pc:
        print("\n",k,"is too much please reduce a bit\n")
        k= int(input())
        continue
    elif k<pc:
        print("\n",k,"is very low. please raise a little\n")
        k =  int(input())
        continue
    if k==pc:
        print("\n",k,"congrats you entered correct answer\n")
        print("Game over !")
        break
#3 from comment
n= 18
i= 0
while(i<9):
    i=i+1
    print("Enter a number")
    x=int(input())
    if x==n:
        print("Congo!! ur number matched")
        print("number guesses u took",i)
        break
    elif x<18:
        print("Try again with a larger number")
        print("Chances left",9-i)
        continue
    elif x>18:
        print("Try again with a smaller number")
        print("chances left",9-i)
    elif i>9:
        print("OOPS!! U have used all ur chances")
        break
#4 from comment
# x is guess number
i = 1
while (i <= 5):
    x = int(input("Enter your guess,'You can only five guesses'.\n"))
    if x == 18:
        print("Congrats you are won!")
        print("You done it in",i,"time.")
        break
    elif x  ==17:
        print("You are approximately nearest")
    elif x <10 :
        print(" It is too smallest number!")
    elif x >=10:
        print("You are nearest")
    else:
     print("Your answer is greater")
    print("Guesses left",5-i,":")
    i= i + 1
    if i > 5:
        print("Game Over!")
        break
#4 from comment
Print("welcome to guess the number game")
Print("rules\n")
Print("1 number of guesses are equal\n", "2 you will get information about how to guess the number\n",
      "3 no need to be sad the rules are over"\n
","
let
's start the game\n")

n = 56
Print("this is your first guess")
While(number_
of_
guess < 18)
Print("you are going too low")
If(number_of_guess > 18)
Print("you are going too high")
else (number_of_guesses == 18)
Print("congrats you have chosen the correct number")
Print("10-number of guess left")
number
of
guesses = number
of
guesses + 1
If(number_of_guesses > 10)
Print("your game is over"\n
","
you
can
not guess
the
number
")

#6 from comment
# Numer is 6 and Guesses are 5
num = 6;
i = 5;
print("You have 5 choices \n \t \t Your Game Starts Now!");
while (True):
    print("Enter your choice in-between 0 to 20: ");
    a = int(input());
    i = i -1;

    if(a == 6 ):
        print("Congratulation, Your guess is correct \n")
        break;

    elif(a != 6 and (a>8 and a<=10)):
        if (i == 0):
            print("Game Over")
        else:
            print("Your Guess is wrong \n "
                  "Hint: You are near but You should decrease the number by good amount \n");


    elif (a != 6 and (a > 6 and a <= 8)):
        if (i == 0):
            print("Game Over")
        else:
            print("Your Guess is wrong \n "
                  "Hint: You are almost near, decrease the number by small amount \n");

    elif(a != 6 and (a>10 and a<=15)):
        if (i == 0):
            print("Game Over")
        else:
            print("Your Guess is wrong \n "
                  "Hint: Your guess is far but You should decrease the number \n");

    elif(a != 6 and (a>=0 and a<=2)):
        if (i == 0):
            print("Game Over")
        else:
            print("Your Guess is wrong \n "
                  "Hint: Your guess is very far but "
                  "You should increase the number by great amount \n");

    elif(a != 6 and (a>2 and a<=5)):
        if (i == 0):
            print("Game Over")
        else:
            print("Your Guess is wrong \n "
                  "Hint: You are almost near but "
                  "You should increase the number by small amount \n");


    elif (a != 6 and (a > 15 and a <= 20)):
        if (i == 0):
            print("Game Over")
        else:
            print("Your Guess is wrong \n "
                  "Hint: You are very far, decrease the number by huge amount \n");