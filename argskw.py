# def function_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)

def funargs(normal,*argsrohan,**kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would like to introduce some of our hereos")
    for key,value in kwargsbala.items():
        print(f"{key} is a {value}")

# function_name_print("Harry","Rohan", "Skillf","Hammad","Shivam")

har=["Harry","Rohan","Skillf","Hammd",
     "Shivam","The programmer"]
normal="T am a normal Argument and the students are:"
kw= {"Rohan":"Monitor", "Harry":"fitness instructor",
     "The Programmer":"Coordinator","Shivam":"Cook"}
funargs(normal,*har,**kw)