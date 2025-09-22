##########################ppppppp##################
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

https://drive.google.com/file/d/1qpZLI5zJJxKTbHrFD7eR6FMEBml5ATQo/view?usp=drivesdk            
https://drive.google.com/file/d/1Ve8Eb90_9aH4fdkgICMnbH9NnSmLPzQ7/view?usp=drivesdk

###########ddddddddddddddddd###########################  


#1.a insert an element at a specific position in an array 
from array import array
arr=array('i',[10,20,30,40,50])
elem=int(input("enter element to insert:"))
pos=int(input("enter position(0-based index):"))
arr.insert(pos,elem)
print("Array adt insertion :",arr.tolist())      
        
1.b) Delete an element from a specific position in an array.
from array import array
#Create an integer array
arr= array('I', [10, 20, 30, 40, 50])
# Input position to delete
pos = int(input("Enter position to delete (0-based index): "))
# Check if position is valid
if 0 <= pos < len(arr):
    arr.pop(pos) # Remove element at position
    print("Array after deletion:", arr.tolist()) 
else:
        print("Invalid position!")

1.c)Search for an element in an array (linear search).
from array import array
#Create an array
arr = array('i', [15, 25, 35, 45, 55])
# Input element to search
key=int(input("Enter element to search: "))
# Linear search
found = False
for i in range(len(arr)):
    if arr[i] == key:
        print(f"Element found at position (i)")
        found = True
        break
        if not found:
            print("Element not found")
#2.a create a singly linked list.

head = { 'data':10, 'next': None }
Second = {'data': 20, 'next': None }
third = {'data': 30 ,'next': None }
head ['next'] = Second

Second ['next'] = third
temp= head

print("Linked List!", end = " ")

while temp is not None:
    print (temp['data'], end="=>")
    temp = temp ['next']
    print("None")
    
#2.b)Insert a Note at the beginning end and at the given position in a linked list
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to print linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # if list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insert at given position (1-based index)
    def insert_at_position(self, data, position):
        if position <= 0:
            print("Invalid Position!")
            return

        new_node = Node(data)

        # Insert at beginning
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse to position
        current = self.head
        for i in range(position - 2):
            if current is None:
                print("Position out of range!")
                return
            current = current.next

        if current is None:
            print("Position out of range!")
            return

        new_node.next = current.next
        current.next = new_node


# ------------------------------
# Example usage
ll = LinkedList()

ll.insert_at_beginning(10)   # 10
ll.insert_at_end(20)         # 10 -> 20
ll.insert_at_end(30)         # 10 -> 20 -> 30
ll.insert_at_position(15, 2) # 10 -> 15 -> 20 -> 30
ll.insert_at_position(5, 1)  # 5 -> 10 -> 15 -> 20 -> 30
ll.insert_at_position(40, 6) # 5 -> 10 -> 15 -> 20 -> 30 -> 40

ll.display()

#2.c)Delete a note from a given position in linkef list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert node at end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Function to delete node at a given position
    def delete_at_position(self, position):
        if self.head is None:  # empty list
            return

        temp = self.head

        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find the previous node of the node to be deleted
        for i in range(position - 1):
            if temp is None or temp.next is None:
                return  # position is greater than number of nodes
            temp = temp.next

        # Node to be deleted is temp.next
        node_to_delete = temp.next
        if node_to_delete is None:
            return

        # Unlink the node from linked list
        temp.next = node_to_delete.next
        node_to_delete = None

    # Function to print linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Original List:")
ll.display()

ll.delete_at_position(2)  # delete node at position 2 (30)
print("After Deleting at Position 2:")
ll.display()
#output:
Original List:
10 -> 20 -> 30 -> 40 -> None
After Deleting at Position 2:
10 -> 20 -> 40 -> None


Q7)Prefix to Postfix
Code:
def is_operator(c):
    return c in "+-*/^"

def prefix_to_postfix(expression):
    stack = []
    for symbol in reversed(expression):
        if is_operator(symbol):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + symbol)
        else:
            stack.append(symbol)
    return stack[-1]

# Example usage
prefix_expr = "*+AB-CD"
postfix_expr = prefix_to_postfix(prefix_expr)
print("Prefix Expression :", prefix_expr)
print("Postfix Expression:", postfix_expr)


Q8)Infix to Postfix
Code:
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expr):
    stack = []
    output = ''
    for char in expr:
        if char.isalnum():
            output += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                output += stack.pop()
            stack.append(char)
    while stack:
        output += stack.pop()
    return output

expr = "A*(B+C)/D"
print("Postfix:", infix_to_postfix(expr))
Q9)Queue
Code:
class Queue:
    def __init__(self, size): 
        self.size = size 
        self.queue = [None] * size  
        self.front = -1 
        self.rear = -1 

   def is_empty(self):
        return self.front == -1   
                          
   def is_full(self):
        return self.rear == self.size – 1 
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        if self.is_empty():
            self.front = 0
       self.rear += 1
      self.queue[self.rear] = item
      print(f"Enqueued: {item}") 
        if self.is_empty():.
            print("Queue is empty. Cannot dequeue.") 
            return None 
        removed_item = self.queue[self.front] 
        print(f"Dequeued: {removed_item}")
        if self.front == self.rear: 
            # Queue becomes empty
            self.front = self.rear = -1 
        else:
            self.front += 1 
        return removed_item

    def peek(self):
    if self.is_empty():
        print("Queue is empty.")
        return None
    return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
          print("Queue contents:", self.queue[self.front:self.rear + 1])
    if __name__ == "__main__":
    q = Queue(5)              
    q.enqueue(10)             
    q.enqueue(20)             
    q.enqueue(30)             
    q.display()               
    q.dequeue()             
    q.display()               
    print("Front item:", q.peek())  





Q10)Binary Search Tree
Code:
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(node, val):
            if not node: return Node(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            elif val > node.val:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)

    def search(self, val):
        def _search(node, val):
            if not node: return False
            if val == node.val: return True
            return _search(node.left, val) if val < node.val else _search(node.right, val)
        return _search(self.root, val)

    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.val, end=' ')
                _inorder(node.right)
        _inorder(self.root)
        print()

# Example usage
bst = BST()
for val in [40, 20, 60, 10, 30, 50, 70]:
    bst.insert(val)

print("Inorder Traversal:")
bst.inorder()

print("Search 30:", "Found" if bst.search(30) else "Not Found")

Q11)Tree Traversal
Code
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal:")
preorder(root)
print("\nInorder traversal:")
inorder(root)
print("\nPostorder traversal:")
postorder(root)

Q12)Bubble Sort Algorithm
Code:
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)

Q13)Insertion Sort Algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [12, 11, 13, 5, 6]
print("Original array:", arr)

insertion_sort(arr)

print("Sorted array:", arr)

Q14)Linear Search Algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [12, 11, 13, 5, 6]
print("Original array:", arr)

insertion_sort(arr)

print("Sorted array:", arr)

Q15)Binary Seacrh Algorithm
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [2, 3, 4, 10, 40]
target = 10

result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")









