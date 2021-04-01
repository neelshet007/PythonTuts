#problem1 python tutorials for absolute beginners  by CODEWITHHARRY
#caution: Time module has used for showing proccess is going on function used is time.sleep(1)
import time #time had been use to show process is going on

x1=int(input("Enter your age or year of birth to know when you will be 100 years old and what will be your age in 2090\n"))
x2=len(str(x1))
#1900 is because  a human cannot live alive till 120 years now year is 2021
if x2==3 and x1>120: print("I don't think so your are alive you are lieing  but see the given information for the official purpose\n")
# elif x2==3 and x1>120: pri
elif x2==1 and x1==0: print("You have not born yet......")
elif x2==4 and x1<1900: print("I don't think so your are alive you are lieing but see the given information for the official purpose\n")

elif x2==4 and x1>2021: print("You have not born yet......but see the given information for the official purpose\n")
else:
    print("Process is going on..Thanks for your patience\n")
if x2 == 4:
    x5 = 2090 - int(x1)
    x6 = int(x1) + 100
    time.sleep(1)
    print(f"Your age in 2090 will be {x5} & in {x6} you will be of 100 years\n")

elif x2 == 2:
    x9 = 60 + int(x1)
    x7=100- int(x1)
    x10=2021+ int(x7)
    time.sleep(1)
elif x2 == 3:
    x9 = 60 + int(x1)
    x7 = int(x1)-100
    x10 = 2021 + int(x7)
    time.sleep(1)
    print(f"Your age in 2090 will be {x9} & in {x10} you will be of 100 years\n")
print("Thank you for using our services.Hope you love it.If you have got any other technical error please contact us")

