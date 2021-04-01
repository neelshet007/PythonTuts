"""
Iterable- __inter__()or__getitem__
Itreayor-  __next__()
Itreation-

"""

def gen(n):
    for i in range(n):
       yield i

g=gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in  g:
#     print(i)

h=546546
ier= iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)
number=int(input("Enter the number"))

if number == 0:
    return 1
elif number==1:
    return 1
else:
    def factorial(number)
            return number*number-1....1