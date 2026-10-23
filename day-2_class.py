import math 

def calculate_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

total_seconds=int(input("Enter total seconds: "))
hours, minutes, seconds = calculate_time(total_seconds)
print(f"Time: {hours} hours, {minutes} minutes, {seconds} seconds")

def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print(f"Area of the circle: {area}")

def even_or_odd(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"

number = int(input("Number:"))
res=even_or_odd(number)
print(f"The number {number} is {res}.")

def leapyear(year):
    if(year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False

year = int(input("Enter a year:"))
if(leapyear(year)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

def sum(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total

n=int(input("Enter a number:"))
result=sum(n)
print(f"The sum of numbers from 1 to {n} is {result}.")

def vowels(s):
    count=0
    for char in s:
        if char.lower() in 'aeiou':
            count+=1
    return count

s=input("Enter a string:")
print(f"The number of vowels in the string is: {vowels(s)}") 