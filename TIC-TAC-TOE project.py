board = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "}


def space_is_empty(position):
    return board[position] == " "


def checkDraw():
    return all(board[key] != " " for key in board)


def checkForWin(mark):
    return (
            (board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark)
    )


def insertLetter(letter, position):
    if space_is_empty(position):
        board[position] = letter
        if checkForWin(letter):
            if letter == bot:
                print("Bot wins!")
            else:
                print("Player wins!")
            return True
        if checkDraw():
            print("Draw!")
            return True


def comp_move():
    bestScore = -1000
    bestMove = None
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    buttons[bestMove - 1]['text'] = bot
    insertLetter(bot, bestMove)


def minimax(isMaximizing):
    if checkForWin(bot):
        return 1
    elif checkForWin(player_letter):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(False)
                board[key] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player_letter
                score = minimax(True)
                board[key] = ' '
                bestScore = min(score, bestScore)
        return bestScore


import tkinter as tk
from tkinter import messagebox

player_letter = messagebox.askquestion("Enter yes for 'X' no for 'O'", "Choose X or O")
bot = None

if player_letter == "yes":
    player_letter = "X"
    bot = "O"
elif player_letter == "no":
    player_letter = "O"
    bot = "X"


def buttonClick(button):
    if buttons[button]['text'] == "" and not checkForWin('X') and not checkForWin('O'):
        buttons[button]['text'] = player_letter
        insertLetter(player_letter, button + 1)
        if checkForWin(player_letter):
            messagebox.showinfo("Result", "Player wins!")
            resetGame()
        elif checkDraw():
            messagebox.showinfo("Result", "It's a draw!")
            resetGame()
        else:
            comp_move()
            if checkForWin(bot):
                messagebox.showinfo("Result", "Bot wins!")
                resetGame()
            elif checkDraw():
                messagebox.showinfo("Result", "It's a draw!")
                resetGame()


def resetGame():
    global board
    for i in range(9):
        buttons[i]['text'] = ""
        board[i + 1] = ' '



root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=('Arial', 20), width=4, height=2, command=lambda i=i: buttonClick(i))
    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)j
root.mainloop()
