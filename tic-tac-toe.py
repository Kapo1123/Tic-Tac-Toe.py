import random
def show_map(map):
        for line in map :
            print(" | ".join(line))
        print("-"*9)
def check_win(map, x =3, y = 3):
        row_number=0
        column_number =0
        const_three_x_horizontal = 0
        const_three_x_vertical =0
        const_three_y_horizontal = 0
        const_three_y_vertical =0
        # check if player win
        #first way to win for player
        if map[0][0] == map[1][1] == map[2][2] and (map[0][0] == "x" or map[0][0] == "o"):
            return "player" if map[0][0] == "x" else "computer"
        if map[0][2] == map[1][1] == map[2][0] and (map[0][2] == "x" or map[0][2] == "o"):
            return "player" if map[0][2] == "x" else "computer"
        for row_number in range (x):
            const_three_x_horizontal = 0
            const_three_x_vertical = 0 
            const_three_y_horizontal = 0
            const_three_y_vertical =0
            for column_number in range (y):
                if map[row_number][column_number] == "x":
                    const_three_x_horizontal +=1
                elif map[row_number][column_number] == "y":
                    const_three_y_horizontal +=1
                if map[column_number][row_number] == "x":
                    const_three_x_vertical +=1
                elif map[column_number][row_number] == "y":
                    const_three_y_vertical +=1
                if const_three_x_vertical ==3 or const_three_x_horizontal ==3:
                    return "player"
                elif const_three_y_vertical ==3  or const_three_y_horizontal ==3:
                    return "computer"
        #check computer
        
def check_tie(map, x =3, y = 3):
        row_number=0
        column_number =0
        for row_number in range (x):
            for column_number in range (y):
                if map[row_number][column_number]== "":
                    return False
        return True

                
        
            
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
        player_name = ""
        played = False
        while True:
            if who_is_player == "computer":
                who_is_player = player_name
                played = False
            elif who_is_player != "":
                who_is_player= "computer"
                played = False
            show_map(map)
            answer = check_win(map,length, depth )           
            if answer == "player":
                print ("Congratulations!! You won")
                still_play =input(f"Do you still want to play? Y/N : ").lower()
                if still_play == "n":
                    break
                if still_play == "y":
                    game()
                
            elif answer == "computer":
                print ("Do better next time!")
                still_play =input(f"Do you still want to play? Y/N : ")
                if still_play == "N":
                    break
                if still_play == "Y":
                    game()
            if check_tie(map,length, depth ) == True:
                print ("It's a tie!")
                still_play =input(f"Do you still want to play? Y/N : ")
                if still_play == "N":
                    break
                if still_play == "Y":
                    game()
            
            while who_is_player == "":
                print("Welcome to the game! In this game, you will be playing against a computer!")
                player_name = input(f"May I have your name:" )
                x = str(input(f"Do you want {player_name} to go first or computer go first? "))
                name = {player_name:"x", "computer": "o" }
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
            # answer = check_win(map,length, depth )           
            # if answer == "player":
            #     print ("Congratulations!! You won")
            # elif answer == "computer":
            #     print ("Do better next time!")
            # elif check_tie(map,length, depth) == True:
            #     print ("It's a tie ")
if __name__ == "__main__":
        game()
                
            



