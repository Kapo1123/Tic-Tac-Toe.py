import random
def show_map(map):
    for line in map :
        print(" | ".join(line))
    print("-"*9)
def check_win(map, x =3, y = 3):
    i=0
    const_three_x = 0
    const_three_y = 0
    # check if player win
    for i in range (x):
        if map[0][i] == "x":

    
        
def game():
    length = 3
    depth = 3
    # i = 0
    # map = []
    # # for i in range (length):
    # #     map[i][i] = ""
    map = [["" for _ in range(length)] for _ in range(depth)]
    # player = "x"
    # computer = "o"
    who_is_player = "" #show whose turn
    player_name =""
    played = False
    while True:
        if who_is_player == "computer":
            who_is_player = player_name
            played = False
        elif who_is_player != "":
            who_is_player= "computer"
            played = False
        show_map(map)
        while who_is_player == "":
            print("Welcome to the game! In this game, you will be playing against a computer!")
            player_name = input(f"May I have your name:" )
            x = str(input(f"Do you want {player_name} to go first or computer go first? "))
            name = {player_name:"x", "computer": "y" }
            who_is_player = x.lower()
        while played == False:
            if who_is_player == "computer":
                while True:
                    random_row = random.randint(0,2)
                    random_columm =random.randint(0,2)
                    if map[random_row][random_columm] == "":
                        map [random_row][random_columm]= name["computer"]
                        played = True
                        break  
            else:
                # de_bug = name[player_name]
                row = int(input(f"Player {player_name}, enter the row (0, 1, or 2): "))
                column = int(input(f"Player {player_name}, enter the column (0, 1, or 2): "))
                if row > 2 or column >2:
                    print(f"Invalid input. Try again.")
                elif map[row][column] != "":
                    print(f"Invalid input. Try again.")
                else:
                    map[row][column] = name[player_name]
                    played = True
                    break
        if check_win(map,length, depth ) == "player":
            print ("Congratulations!! You won")
        elif check_win(map,length, depth ) == "computer":
            print ("Do better next time!")
        elif check_tie(map,length, depth) == True:
            print ("It's a tie ")
if __name__ == "__main__":
    game()
            
           



