import random
def game(comp, user):
    if comp == user:
        return 0
    if comp == 3 and user == 2:
        return -1  
    if comp == 1 and user == 3:
        return -1
    if comp == 2 and user == 1:
        return -1
    else:
        return 1
while True:
    try:
        user1 = int(input("Difficulty Level=> 1 for Easy, 2 for Medium, 3 for Hard: "))
        if user1 not in [1, 2, 3]:
            print("Please enter only 1, 2, or 3 for difficulty level.")
            
            continue
        user = int(input("Your Move=> 1 for Stone, 2 for Paper, 3 for Scissor: "))
        
        if user1 == 3:
            rand = random.random()
            if rand < 0.8:
                #loosing chances 80%
                winning_move = {1: 2, 2: 3, 3: 1}
                comp = winning_move[user]
            else:
                comp = random.randint(1, 3)
                
                rand = random.random()
                
        if user1 == 2:
            rand = random.random()
            if rand < 0.5:
                #loosing chances 50%
                winning_move = {1: 2, 2: 3, 3: 1}
                comp = winning_move[user]
            else:
                comp = random.randint(1, 3)
                
                rand = random.random()
                
        if user1 == 1:
            rand = random.random()
            if rand < 0.2:
                #loosing chances 20%
                winning_move = {1: 2, 2: 3, 3: 1}
                comp = winning_move[user]
            else:
                comp = random.randint(1, 3)

        
        if user not in [1,2,3]:
            print("\nType only 1 or 2 or 3\nCHOICE IS YOURS!!!\n")
            continue
        
    except ValueError:
        print("\nInvalid input! Please enter only 1 or 2 or 3\n")
        continue



    score = game(comp, user)
    options = {1:"Stone",2: "Paper",3: "Scissor"}           #if we don't putting 1:,2:,3: then they take stone = 0 (default) instead of 1
    
    print(f"\nYou: {options[user]}")
    print(f"Computer: {options[comp]}")

    if (score == 0):
        print("Its Draw!!!")

    elif (score == -1):
        print("You Loose!!!")

    else:
        print("You Won!!!")
            
    again = input("Do you want to play further? (y/n): ").lower()
    if again == "y":
        continue
    else:
        break