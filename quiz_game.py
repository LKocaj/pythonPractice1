print("Welcome to my quiz")

playing = input("Do you want to play? ") #Asking question

if playing != "yes": # If the answer is anything != but yes, it will quit the program
    quit()

print("Okay! Lets play :)") # If the game doesnt quit - it'll continue on and print this message

answer = input("What does CPU stand for? ") # You answered yes then it'll trigger this statement
if answer.lower == "central processing unit": # .lower makes anything you type lowercase to match the if statement
    print('Correct!')
else: 
    print("Incorrect!")

answer = input("What does RAM stand for? ") # You answered yes then it'll trigger this statement
if answer.lower == "random access memory":
    print('Correct!')
else: 
    print("Incorrect!")

answer = input("What does PSU stand for? ") 
if answer.lower == "power supply unit":
    print('Correct!')
else: 
    print("Incorrect!")

