# # 1(A)W .a.p that asks the user to enter their name ,age.print out a message,
# # the year that they will tuen 100 y old.
# user=input("Enter your name:")
# age=int(input("Enter your age: "))
# current_year=2025
# year_when_100=current_year + (100 -age)
# print("hello",user+"!")
# print("your age is:",age)
# print("you will turn 100 year old in the year:",year_when_100)

# #(b)w.a.pto accept a (no)from user &depending on the no is (even)or(odd)&print it.
# num=int(input("Enter a number to check if it is even or odd: "))
 if num%2==0:
     print("The number is even..")
 else:
   print("The number is odd..")
# #2.(a) w.a.p to generate thr fibonacci series
num=int(input("\n enter the range number:"))
a=0
b=1
for n in range(0,num):
     if(n<=1):
         c=n
     else:
         c=a+b
         a=b
         b=c

         print(c)
# b.w.a.p to accept a no from the user display sum of its digits
num=int(input("enter a number:"))
sum_digits=0
while num>0:
    digit=num%10
    sum_digits+=digit
    num=num//10
    print("sum of digit is:",sum_digits)
     o/t:516     
#3(a)w.a.p to perform basic operation,indexing & slicing on arrays
import numpy as np

arr=np.array([10,20,30,40,50])
print("original Array:",arr)
print("Array +5:",arr+5)
print(" Array*2:",arr*2)
print("sum od all element:",arr.sum())

print("first element:",arr[0])
print("last element:",arr[-1])

#slicing
print("element from index 1 to 3:",arr[1:4])
print("element from index start to index 2:",arr[:3])
print("element from index 2 to end:",arr[2:])

#3b)w.a p to implement mathematical function on aarays
arr=np.array([5,10,15,20,25])
print("original Array:",arr)
#mathemathicl function
print("sum of elements:",np.sum(arr))
print("mean (average):",np.mean(arr))
print("max value:",np.max(arr))
print("minimum value:",np.min(arr))
print("square root of each element:",np.sqrt(arr))
print("stander deviation:",np.std(arr))
print("product of all elements:",np.prod(arr))

#3c)w.a.p to perform array aliasing & copying.
arr=np.array([10,20,30,40])
alias_arr=arr
copy_arr=arr.copy()
arr[0]=100
print("original Array (after change):",arr)
print("Aliased Aray (after change):",arr)
print("copied Array(no change):",copy_arr)

#4a)w.a.p to perform slicing,basic & advanced indexing on numpy array.
arr=np.array([ [10,20,30],[40,50,60],[70,80,90]])
#basic indexing
print("element at(1,2):",arr[1,2])
#slicing 
print("sliced (col 1):",arr[:1])

#advanced indexing
rows=[0,2]
cols=[1,2]
print("advance indexing(0,1) & (2,2):",arr[rows,cols])

print("element >50 :",arr[arr>50])

#4b)W.a.p to analyze dimensions & attributes of arrays.
import numpy as np
#create a2d array
arr=np.array([[1,2,3],[4,5,6]])
#array attributes
print("array:\n",arr)
print("shape:",arr.shape)
print("dimensions:",arr.ndim)
print("size:",arr.size)
print("array:\n",arr)
#5.a)w.a.function to check th input value is armstong & also write the function for palindrome a palindrome number")

def armnum(num):
    sum=0
    temp=num 
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
        if num==sum:
            print(num,"is an armstrong number")
        else:
            print(num,"is a not armstrong number")
    def palnum(num):
        sum=0
        temp=num
        while num!=0:
            rem =num%10
            sum=rem+sum*10
            num=num//10
            if temp==sum:
                print(temp,"is a palindrome number")
            else:
                print(temp,"is not a palindrome number")
                
            num=int(input("enter any no:"))
            armnum(num)
            palnum(num)
#b.w.a recursive function to print the factorial for a given number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
number = int(input("Enter a number: "))
result = factorial(number)
print(f"Factorial of {number} is {result}")     
#(c).W. a lambda function that checks whether a given string starts w specific character.
 starts_with = lambda s, ch: s.startswith(ch)
# Example usage
text = input("Enter a string: ")
char = input("Enter a character: ")
print("Starts with", char + ":", starts_with(text, char))
#(6).W.a.p to compute number of characters & words in a string.

# Input string
text = input("Enter a string: ")
# Count characters (excluding spaces)
char_count = len(text.replace("", ""))
# Count words
word_count = len(text.split())
# Output
print("Characters (no spaces):", char_count)
print("Words:", word_count)
#8(a)w.a.p to accept and pass radius to a function that returns are:& circumference (using tuple).
import math
#Function to calculate area and circumference
def circle_details(r):
    area= math.pi*r*r
    circ=2*math.pi*r
    return (area, circ) # Returning as tuple
#Accept radius from user
radius= float(input("Enter radius: "))
# Call function
result = circle_details(radius)
# Display results
print("Area:", result[0])
print("Circumference:", result[1])
o/t:8
201
50
7.a)W.a.p that takes two lists & returns True if they have at least one common member.
# Input lists
list1= input("Enter first list (comma-separated): ").split(".")
list2= input("Enter second list (comma-separated): ").split(".")
#Remove spaces
list1=[x.strip() for x in list1]
list2=[x.strip() for x in list2]
#Check for common element
def has_common(lst1, Ist2):
return any(item in Ist2 for item in Ist1)
#Output
print("Common element exists:", has common(list1, list2))
Output:
Enter : apple, banana, mango
Enter: mango, orange
Common: True
17)Write a python program to generate first n prime numbers.
Code
# Function to check if a number is prime
def is_prime(num):
    # 0 and 1 are not prime numbers
    if num < 2:
        return False
    # Check if num is divisible by any number from 2 to num - 1
    for i in range(2, num):
        if num % i == 0:  # If divisible, it's not prime
            return False
    # If no divisors found, it's a prime number
    return True
# Function to generate the first n prime numbers
def generate_primes(n):
    primes = []     # List to store prime numbers
    number = 2      # Start checking from number 2 (first prime)
    # Keep finding primes until we have n of them
    while len(primes) < n:
        if is_prime(number):         # Check if the current number is prime
            primes.append(number)    # If it is, add it to the list
        number += 1                  # Move to the next number
    return primes  # Return the list of primes
# Ask the user how many primes they want
n = int(input("Enter how many prime numbers you want: "))
# Call the function to generate primes
prime_list = generate_primes(n)
# Print the list of prime numbers
print("First", n, "prime numbers are:", prime_list)
Q18) Write a python program to find the maximum,minimum and average of elements in a list
Code:
# Ask the user to enter numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")
# Split the input string into individual strings and convert them to integers
numbers = list(map(int, user_input.split()))
# Check if the list is not empty
if len(numbers) == 0:
    print("No numbers entered.")
else:
    # Find the maximum value using the built-in max() function
    maximum = max(numbers)
    # Find the minimum value using the built-in min() function
    minimum = min(numbers)
    # Calculate the average by dividing the sum of elements by the number of elements
    average = sum(numbers) / len(numbers)
    # Print the results
    print("Maximum number:", maximum)
    print("Minimum number:", minimum)
    print("Average:", average)

               

        





