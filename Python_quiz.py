score = 0
print("SIMPLE QUIZ")
print("Write your answers using A, B, C ,D")
question_1 = input('''
Question 1:
What is the capital of France?
A) London
B) Paris
C) Berlin
D) Madrid
Your answer: ''').upper()
if question_1 == "B":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")
    
question_2 = input('''
Question 2:
Which planet is known as the Red Planet?
A) Earth
B) Mars
C) Jupiter
D) Venus
Your answer: ''').upper()
if question_2 == "B":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")
    
question_3 = input('''
Question 3:
Which language is used to create web pages?
A) Python
B) C++
C) HTML
D) Java
Your answer: ''').upper()
if question_3 == "C":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")
    
question_4 = input('''
Question 4:
What is 5 + 7?
A) 12
B) 11
C) 10
D) 13
Your answer: ''').upper()
if question_4 == "A":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")
    
question_5 = input('''
Question 5:
Which animal is known as the "King of the Jungle"?
A) Tiger
B) Elephant
C) Lion
D) Giraffe
Your answer: ''').upper()
if question_5 == "C":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer")
    
print(f"Your score is {score}/5")
