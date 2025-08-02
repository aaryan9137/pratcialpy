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
# if num%2==0:
#     print("The number is even..")
# else:
#     print("The number is odd..")
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

#3b
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

#3c
arr=np.array([10,20,30,40])

alias_arr=arr
copy_arr=arr.copy()

arr[0]=100

print("original Array (after change):",arr)
print("Aliased Aray (after change):",arr)
print("copied Array(no change):",copy_arr)

#4a
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

#4.b
#create a2d array
arr=np.array([[1,2,3],[4,5,6]])
#array attributes
print("array:\n",arr)
print("shape:",arr.shape)
print("dimensions:",arr.ndim)
print("size:",arr.size)
print("array:\n",arr)
#5.a)w.a.function to check th input value is armstong & also write the function for palindrome
def armnum(num):
    sum=0
    temp=num 
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
        if num==sum:
            print(num,"is an armstrong number:")
        else:
            print(num,"is a not armstrong number")
    def palnum(num):
        sum=0
        temp=num
        while num!=
            rem =num%10
            sum=rem+sum*10
            num=num//10
            if temp==sum:
                print(temp,"is a palindrome number")
            else:
                print(temp,"is not a palindrome number")
                
            num=int(input("enter any no:

        
