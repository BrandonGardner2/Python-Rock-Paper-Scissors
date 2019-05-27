#import modules
import random

#file i/o functions
def load_results():
    text_file = open("history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history

def save_results(w, t, l):
    text_file = open("history.txt", "w")
    text_file.write(str(w) + "," + str(t) + "," + str(l))
    text_file.close()
    


#welcome message
results = load_results()
if len(results) == 3:
    wins = int(results[0]) or 0
    ties = int(results[1]) or 0
    losses = int(results[2]) or 0
else:
    wins = 0
    ties = 0
    losses = 0
print("Welcome to Rock, PAper, Scissors!")
print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
print("Please choose to continue...")

#initialize user and computer choices
computer = random.randint(1, 3)
user = int(input("[1] Rock [2] Paper [3] Scissors [9] Quit\n"))

#gameplay loop
while not user == 9:
    #user chooses ROCK
    if user == 1:
        if computer == 1:
            print("The computer also chose rock...tie!")
            ties += 1
        elif computer == 2:
            print("The computer chose paper...loss!")
            losses += 1
        elif computer == 3:
            print("The computer chose scissors...win!")
            wins += 1

    #user chooses PAPER
    elif user == 2:
        if computer == 1:
            print("The computer chose rock...win!")
            wins += 1
        elif computer == 2:
            print("The computer also chose paper...tie!")
            ties += 1
        elif computer == 3:
            print("The computer chose scissors...loss!")
            losses += 1

    #user chooses SCISSORS
    elif user == 3:
        if computer == 1:
            print("The computer chose rock...loss!")
            losses += 1
        elif computer == 2:
            print("The computer chose paper...win!")
            wins += 1
        elif computer == 3:
            print("The computer also chose scissors...tie!")
            tie += 1

    else:
        print("Please enter a valid choice of 1, 2, 3 or 9")

    #print stats
    print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

    #prompt next selection
    print("Please choose again to continue...")
    computer = random.randint(1, 3)
    user = int(input("[1] Rock [2] Paper [3] Scissors [9] Quit\n"))

#game over save results
save_results(wins, ties, losses)
