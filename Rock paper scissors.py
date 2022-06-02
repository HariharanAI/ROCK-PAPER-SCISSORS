import random
print("WELCOME TO ROCK, PAPER $ SCISSORS GAME")
while True:
    while True:
       
        print("                                  ")
        player = input("Enter Your Choice : ")

        choices = ["rock","paper","scissors"]
        computer = random.choice(choices)
        print("The choice of the Computer is : ", computer)
        print("                                 ")
        print("---------------------------------")
        if player == "rock":
            if computer == "rock":
                print("|Computer Is Win | ")
                print("------------------")
                break
        if player == "paper":
            if computer == "paper":
                print("|Computer Win |")
                print("--------------")
                break
        if player == "scissors":
            if computer == "scissors":
                print("|Computer Win |")
                print("--------------")
                break
    while True:
        choices = ["rock","paper","scissors"]
        computer = random.choice(choices)
        print("                 ")
        print("NOW YOUR CHOICE ")
        print("                ")
        print("The choice of the Computer is : ",computer)
        print("                                ")
        print("--------------------------------")
        player = input("Enter Your Choice : ")
        #print(player)
        if computer == "rock":
            if player == "rock":
                print("player Is Win ")
                print("--------------")
                break
        if computer == "paper":
            if player == "paper":
                print("player Win")
                print("--------------")
                break
        if computer == "scissors":
            if player == "scissors":
                print("player  Win")
                print("--------------")
                break
            
        
