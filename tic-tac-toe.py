def game():
    length = 3
    depth = 3
    i = 0
    map = []
    for i in range (length):
        map[i][i] = ""
    player = "x"
    computer = "o"
    while True:
        # print the map here
        while True:
            print("Welcome to the game! In this game, you will be playing against a computer!")
            row = int(input(f"Player {player}, enter the row (0, 1, or 2): "))
            column = int(input(f"Player {player}, enter the column (0, 1, or 2): "))
            if row > 2 and column >2:
                print(f"Invalid input. Try again.")
            if map[row][column] == "":
                map[row][column] = player
                break
            else:
                print(f"Invalid input. Try again.")
           



