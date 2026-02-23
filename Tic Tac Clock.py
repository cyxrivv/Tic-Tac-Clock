import tkinter
import webbrowser

def set_tile(row, column):
    global current_player

    if (game_over):
        return

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = current_player

    if current_player == playero:
        current_player = playerx
    else:
        current_player = playero

    label["text"] = current_player+"'s turn'"

    check_win()



def check_win():
    global turns, game_over
    turns += 1


    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text = board[row][0]["text"]+" is the gae!!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground = color_yellow, background = color_lightgray)
            webbrowser.open("https://youtu.be/OxstMK_Gkzw?si=LEeEM5_mzOVaFoga")
            game_over = True
            return

    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text = board[0][column]["text"]+" is the gae!!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground = color_yellow, background = color_lightgray)
            webbrowser.open("https://youtu.be/OxstMK_Gkzw?si=LEeEM5_mzOVaFoga")
            game_over = True
            return

    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
       and board[0][0]["text"] != ""):
        label.config(text = board[0][0]["text"]+" is the gae!!", foreground=color_yellow)
        
        for i in range(3):
            board[i][i].config(foreground = color_yellow, background = color_lightgray)
        webbrowser.open("https://youtu.be/OxstMK_Gkzw?si=LEeEM5_mzOVaFoga")
        game_over = True
        return

    if(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
       and board[0][2]["text"] != ""):
        label.config(text = board[0][2]["text"]+" is the gae!!", foreground=color_yellow)
        board[0][2].config(foreground = color_yellow, background = color_lightgray)
        board[1][1].config(foreground = color_yellow, background = color_lightgray)
        board[2][0].config(foreground = color_yellow, background = color_lightgray)
        webbrowser.open("https://youtu.be/OxstMK_Gkzw?si=LEeEM5_mzOVaFoga")
        game_over = True
        return

    if (turns == 9):
        game_over = True
        label.config(text = "T I E !", foreground=color_yellow)
        webbrowser.open("https://youtu.be/dQw4w9WgXcQ?si=UHJL76xW8zo29k0y")



def new_game():
    global turns, game_over

    turns = 0
    game_over = False
    
    label.config(text = current_player+"'s turn! ", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text = "", foreground = color_pink, background = color_gray)



playerx = 'X'
playero = 'Clock'
current_player = playerx

board = [ ['0', '0', '0'],
          ['0', '0', '0'],
          ['0', '0', '0'] ]

color_red = '#ff0000'
color_yellow = '#ffff00'
color_lightgray = '#d3d3d3'
color_darkgray = '#a9a9a9' 
color_gray = '#343434'
color_pink = '#ff69b4'

turns = 0
game_over = False



window = tkinter.Tk()
window.title('Tic Tac Clock')
window.resizable(False, False)

frame = tkinter.Frame(window) 
label = tkinter.Label(frame, text=current_player+"'s turn", font=('Consolas', 20), background=color_darkgray, 
                      foreground = "white")

label.grid(row = 0, column = 0, columnspan=3, sticky='we')
frame.pack()




for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text = '', font = ('Consolas', 50, "bold"),
                                            background=color_gray, foreground=color_pink, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)





button = tkinter.Button(frame, text='Reset', font=('Consolas', 20), background=color_gray,
                              foreground=color_lightgray, command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky='we')


window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_height/2))
window_y = int((screen_height/2) - (screen_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()