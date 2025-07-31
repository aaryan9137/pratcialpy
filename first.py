# (A)W .a.p that asks the user to enter their name ,age.print out a message,
# the year that they will tuen 100 y old.
user=input("Enter your name:")
age=int(input("Enter your age: "))
current_year=2025
year_when_100=current_year + (100 -age)
print("hello",user+"!")
print("your age is:",age)
print("you will turn 100 year old in the year:",year_when_100)

#(b)w.a.pto accept a (no)from user &depending on the no is (even)or(odd)&print it.
num=int(input("Enter a number: "))
if num%2==0:
    print("The number is even..")
else:
    print("The number is odd..")
#