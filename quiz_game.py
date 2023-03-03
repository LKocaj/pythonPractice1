print("Welcome to my quiz")

playing = input("Do you want to play? ") #Asking question

if playing != "yes": # If the answer is anything != but yes, it will quit the program
    quit()

print("Okay! Lets play :)") #If the game doesnt quit - it'll continue on and print this message

answer = input("What does CPU stand for? ") #if You pressed yes then it'll trigger this statement
if answer == "central processing unit":
    print('Correct!')