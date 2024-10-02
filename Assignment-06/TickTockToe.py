import random
from colorama import Fore
import time

start_time = time.time()


# show game board after player move
def show_player(game_board: list, row: int, col: int, symbol: str, pos: bool):
    game_board[row][col] = symbol
    for r in game_board:
        for item in r:
            if item == "X":
                print(Fore.RED, item, end="    ")
            elif item == "O":
                print(Fore.BLUE, item, end="    ")
            else:
                print(Fore.YELLOW, item, end="    ")
        print("")

        # d = "   ".join(r)
        # if pos == True:
        #    print(d)


# show winner
def show_winner(game_board: list, winner_symbol: str):
    winner = ""
    for row in game_board:
        s = "".join(row)
        if s == winner_symbol * 3:
            winner = winner_symbol

    if winner == "":
        col1 = game_board[0][0] + game_board[1][0] + game_board[2][0]
        col2 = game_board[0][1] + game_board[1][1] + game_board[2][1]
        col3 = game_board[0][2] + game_board[1][2] + game_board[2][2]
        if (
            col1 == winner_symbol * 3
            or col2 == winner_symbol * 3
            or col3 == winner_symbol * 3
        ):
            winner = winner_symbol

    if winner == "":
        d1 = game_board[0][0] + game_board[1][1] + game_board[2][2]
        d2 = game_board[0][2] + game_board[1][1] + game_board[2][0]
        if d1 == winner_symbol * 3 or d2 == winner_symbol * 3:
            winner = winner_symbol

    return winner


# game board
game_board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

# reset game board
show_player(game_board=game_board, row=0, col=0, symbol="-", pos=False)

# turn sum
turn_sum = 0

# select game mode
print(Fore.WHITE, "Select game mode... ")
print(Fore.WHITE, "1 : 👤 vs 💻")
print(Fore.WHITE, "2 : 👤 vs 🧞")
game_mode = int(input("Enter 1 or 2 : "))

# loop
while True:
    symbol_1 = "X"
    symbol_2 = "O"

    while True:
        print(Fore.WHITE, "======= 👤 =======")

        row = int(input("Enter Rows: "))
        col = int(input("Enter Cols: "))

        if game_board[row][col] == "-":
            game_board[row][col] = "X"
            turn_sum += 1
            break
        else:
            print(Fore.WHITE, "⛔")

    show_player(game_board=game_board, row=row, col=col, symbol=symbol_1, pos=True)

    winner_pos = show_winner(game_board=game_board, winner_symbol=symbol_1)
    if winner_pos == symbol_1:
        print(Fore.WHITE, "🎉 🎉 🎉 👤 Win 🎉 🎉 🎉")
        break

    if winner_pos == "" and turn_sum == 9:
        print(Fore.WHITE, "😒 😒 😒 DRAW 😒 😒 😒")
        break

    while True:
        if game_mode == 1:
            print(Fore.WHITE, "======= 💻 =======")
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                turn_sum += 1
                break
            else:
                continue

        elif game_mode == 2:
            print(Fore.WHITE, "======= 🧞‍♂️ =======")
            row = int(input("Enter Rows: "))
            col = int(input("Enter Cols: "))

            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                turn_sum += 1
                break
            else:
                print(Fore.WHITE, "⛔")

    show_player(game_board=game_board, row=row, col=col, symbol=symbol_2, pos=True)
    winner_pos = show_winner(game_board=game_board, winner_symbol=symbol_2)
    if winner_pos == symbol_2:
        if game_mode == 1:
            print(Fore.WHITE, "🎉 🎉 🎉 💻 Win 🎉 🎉 🎉")
        else:
            print(Fore.WHITE, "🎉 🎉 🎉 🧞‍♂️ Win 🎉 🎉 🎉")
        break

    if winner_pos == "" and turn_sum == 9:
        print(Fore.WHITE, "😒 😒 😒 DRAW 😒 😒 😒")
        break

end_time = time.time()
total = round(end_time - start_time)

print(Fore.GREEN, "Total Time Spend: ", total, "s")
