print("Welcome to my quiz")

playing = input("Do you want to play? ") #Asking question

if playing != "yes": # If the answer is anything != but yes, it will quit the program
    quit()

print("Okay! Lets play :)") # If the game doesnt quit - it'll continue on and print this message
score = 0

answer = input("What does CPU stand for? ") # You answered yes then it'll trigger this statement
if answer.lower() == "central processing unit": # .lower makes anything you type lowercase to match the if statement
    print('Correct!')
    score += 1 # Adds 1 to score if correctly answered
else: 
    print("Incorrect!")

answer = input("What does GPU stand for? ") 
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

answer = input("What does RAM stand for? ") 
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

answer = input("What does PSU stand for? ") 
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

print("You got " + str(score) + " questions correct!") # Score at end