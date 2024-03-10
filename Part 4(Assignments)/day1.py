"""Write a code to find the minimum among three given numbers."""
def minimum_of_three(a,b,c):
  if a<=b and a<=c:
    return a
  if b<=a and b<=c:
    return b
  return c

# a = int(input('Enter A:'))
# b = int(input('Enter B:'))
# c = int(input('Enter C:'))
# print('minimum', minimum_of_three(a,b,c))


'''Write a code to check whether a given number is a palindrome.'''
def is_palindrome(s):
  i=0
  j=len(s)-1
  while(i<j):
    if(s[i]!=s[j]):
      return False
    i+=1
    j-=1
  return True

# s = input('Enter string:')
# print(is_palindrome(s))

'''Write a code to find the sum of numbers divisible by 4.The code must allow the user to accept a number and add it to the sum if it is divisible by 4. It should continue accepting numbers as long as the user wants to provide an input and should display the final sum.'''

def divisible_by_4():
  sum = 0
  a = int(input('Enter the number:'))
  while(a%4==0):
    sum+=a
    a = int(input('Enter the number:'))
  return sum

# print('Sum:',divisible_by_4())

'''A three digit number is said to be an “Armstrong number” if the sum of the third power of its individual digits is equal to the number itself.Write a program to check whether a number is armstrong or not'''
def is_armstrong(num):
  n = num
  temp = 0
  while(num>0):
    d = num%10
    temp+=(d**3)
    num//=10
  return n==temp

# num = int(input('Enter a number:'))
# print('Armstrong number:',is_armstrong(num))


'''JIT University offering degree courses to students has decided to provide scholarship based on the following details:
Branch of study    Score (%)   Scholarship %     Remarks
Arts      Score is at least 90    50             The student is eligible only for one scholarship% even if 
both the score conditions are valid for the given 
branch of study. In such cases, students are eligible 
for the highest scholarship% applicable among the two.
Arts
Score is an odd number
5
Engineering
Score is more than 85
50
Engineering
Score is divisible by 7
5

If there are 500 students who have joined the university, write a code to calculate and display the final fees to be paid by each student.
You may accept the branch of study, score and course fee as inputs for each student and calculate the final fees to be paid by each student based on formulae given below:
Scholarship amount=course fee * (scholarship%)
Final fee= course fee - scholarship amount
'''

def calculate_final_fee(branch, score, course_fee):
  scholarship = 0
  if(branch=='Arts'):
    if(score >= 90):
      scholarship = max(50, scholarship)
    if(score%2==1):
      scholarship = max(5, scholarship)
  elif(branch=='Engineering'):
    if(score>85):
      scholarship = max(50, scholarship)
    if(score%7==0):
      scholarship = max(5, scholarship)

  scholarship_amount = course_fee*scholarship/100
  return (course_fee - scholarship_amount)

# branch = input('Enter the branch of study:')
# score = int(input('Enter the score:'))
# course_fee = int(input('Enter the course fee:'))
# print('Final fee:', calculate_final_fee(branch,score, course_fee))


'''The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows:
Rate per Adult: Rs. 37550.0
Rate per Child: 1/3rd of the rate per adult
Service Tax: 7% of the ticket amount (including all passengers)
As it was a holiday season, the airline also offered a 10% discount on the final ticket cost (after inclusion of the service tax).
Find and display the total ticket cost for a group which had adults and children.
'''
def calculate_ticket_fare(adults, children):
  fare = adults*37550.0 + children*37550.0/3
  tax = fare*7/100
  total_fare = fare + tax
  discount = total_fare*10/100
  payable_amount = total_fare - discount
  return payable_amount

# adults = int(input('Enter the count of adults:'))
# children = int(input('Enter the count of children:'))
# print('total fare:', calculate_ticket_fare(adults, children))


'''Write a python program to solve a classic ancient Chinese puzzle.
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?




Sample Input
Expected Output
heads-150 legs-400
100 50
heads-3 legs-11
No solution
heads-3 legs-12
0 3
heads-5 legs-10
5 0

'''
def calculate_animals(heads, legs):
  i,j=0,heads
  while(i<=j):
    mid = (i+j)//2
    total_legs = mid*2 + (heads - mid)*4
    if(total_legs == legs):
      return mid
    if(total_legs < legs):
      j = mid-1
    else:
      i = mid+1
    print(mid, total_legs)
  return -1

# heads = int(input("Enter no. of heads:"))
# legs = int(input("Enter no. of legs:"))
# print("no of chickens:",calculate_animals(heads, legs))


