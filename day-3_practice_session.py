import random 
#Safe calculator 

def safe_cal():
	print("Welcome to the safe calculator")
	num=int(input("Enter the first number:"))
	num1=int(input("Enter the second number:"))
	operator=input("Enter a operator (+,-,*,/,//,**)")
	if operator == '+':
		print(f"The addition of {num} and {num1} is :",(num+num1))
	elif operator == '-':
		print(f"The subtraction of {num} and {num1} is :",(num-num1))
	elif operator == '*':
		print(f"The multiplication of {num} and {num1} is :",(num*num1))
	elif operator == '/':
		if num1 != 0:
			print(f"The division of {num} and {num1} is :",(num/num1))
		else:
			print("Error: Division by zero")
	elif operator == '//':
		if num1!=0:
			print(f"The floor division of {num} and {num1} is :",(num//num1))
		else:
			print("Error: division by zero")
	elif operator == '**':
		print(f"The {num} power {num1} is :",(num**num1))
	else:
		print("Invalid Arthimatic operator")

safe_cal()

#Grade Classifier

def grade_classifier():
	print("Welcome to the grade classifier")
	marks=float(input("Enter the marks:"))
	grade=marks/20
	if grade>0 and grade<20:
		if grade>=16:
			print("Very Good")
		elif grade>=14 and grade<16:
			print("Good")
		elif grade>=12 and grade<14:
			print("Fairly Good")
		elif grade>=10 and grade<12:
			print("Pass")
		else:
			print("Fail")
	else:
		print("Please enter the valid marks")

grade_classifier()

#Guessing Game

def guess_game():
	print("Welcome to the guessing game")
	secert=random.randint(1,100)
	input1=int(input("Guess the number from 1 to 100: "))
	attempt=0
	flag=False
	while(attempt<7):
		if(input1<secert):
			print("Too Low")
			pass
		elif(input1>secert):
			print("Too High")
			pass
		elif(input1==secert):
			print(f"WOW you found in {attempt} attempts")
			flag=True
			break
		attempt+=1
		if(attempt<7):
			input1=int(input("Guess the number from 1 to 100: "))

	if flag!=True: 
		print("HUH...Your attempts are completed")
		print(f"The secret number was {secert}")

guess_game()

#with For loop 
def loopf():
	print("Welcome to the for loop")
	total=0
	for i in range(1,10):
		if(i%2==0):
			total+=i
	print(total)

loopf()

#with while Loop
def loopw():
	print("Welcome to the while loop")
	num=int(input("Enter the number:"))
	ans=0
	while(num>0):
		ans=num%10
		num=num//10
	print(ans)

loopw()

#Using break and continue statements 
def bc():
	print("Welcome to the break and continue statements")
	num=int(input("enter the number from:"))
	for i in range(0,num):
		if(i%2==0):
			print(i)
			continue
		else:
			print("It's not a even number")
			break
bc()
	
	
	

#enumerate concept practice

def best_scores():
	print("Welcome to the best scores")
	scores=[10,17,12,18,19]
	ans=-1
	curr_pos=0
	for pos,score in enumerate(scores,start=1):
		if score>ans:
			ans=score
			curr_pos=pos
	print(f"Best: {ans} (student #{curr_pos})")

best_scores()

#Zip concept practice

def marks():
	print("Welcome to the marks")
	answers=['b','d','c','a']
	correct=['a','d','c','b']
	score=0
	for given,corr in zip(answers,correct):
		if given==corr:
			score+=1
	print(f"score:{score}/4")

marks()
			
	
	




