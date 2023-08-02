import random
def game():
    length = 3
    depth = 3
    i = 0
    map = []
    # for i in range (length):
    #     map[i][i] = ""
    map = [["" for _ in range(length)] for _ in range(depth)]
    player = "x"
    computer = "o"
    who_is_player = ""
    while True:
        while who_is_player == "":
        # print the map here
            print("Welcome to the game! In this game, you will be playing against a computer!")
            player_name = input(f"May I have your name:" )
            x = str(input(f"Do you want {player_name} to go first or computer go first? "))
            name = {player_name:player, "computer": computer }
            who_is_player = x
        while True:
            if who_is_player == "computer":
                while True:
                    random_row = random.randint(0,2)
                    random_columm =random.randint(0,2)
                    if map[random_row][random_columm] == "":
                        map [random_row][random_columm]= name["who_is_player"]
                        break
                row = int(input(f"Player {who_is_player}, enter the row (0, 1, or 2): "))
                column = int(input(f"Player {who_is_player}, enter the column (0, 1, or 2): "))
                if row > 2 and column >2:
                    print(f"Invalid input. Try again.")
                elif map[row][column] != "":
                    print(f"Invalid input. Try again.")
                    
                else:
                    map[row[column]] == who_is_player
                    break
        
        
        
        
        
        if who_is_player == "x" :
            who_is_player=computer
        else:
            who_is_player="x"
if __name__ == "__main__":
    game()
            
           



