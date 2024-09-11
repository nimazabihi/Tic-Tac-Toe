import tkinter as tk
from tkinter.messagebox import showinfo
window = tk.Tk()
window.title("Tic Tac Toe")

global turn, result, player_points
turn = "X"
result = ["", "", "", "", "", "", "", "", ""]
player_points = [0, 0]

def clicked(btn):
     global turn
     btn = int(btn)
     if result[btn] == "":
          if turn == "X":
               result[btn] = "X"
               buttons[btn]["bg"] = "red"
               buttons[btn]["fg"] = "white"
               buttons[btn]["text"] = "X"
               buttons[btn]["state"] = tk.DISABLED
               turn = "O"
          else:
               result[btn] = "O"
               buttons[btn]["bg"] = "blue"
               buttons[btn]["fg"] = "white"
               buttons[btn]["text"] = "O"
               buttons[btn]["state"] = tk.DISABLED
               turn = "X"  
     rule()           
               
def rule():
     if (result[0] == result[1] == result[2] and result[0] != ""):
          show_winner(result[0])     
     elif (result[3] == result[4] == result[5] and result[3] != ""):
          show_winner(result[3])
     elif (result[6] == result[7] == result[8] and result[6] != ""):
          show_winner(result[6])
     elif (result[0] == result[3] == result[6] and result[0] != ""):
          show_winner(result[0])   
     elif (result[1] == result[4] == result[7] and result[1] != ""):
          show_winner(result[1])
     elif (result[2] == result[5] == result[8] and result[2] != ""):
          show_winner(result[2])
     elif (result[0] == result[4] == result[8] and result[4]):
          show_winner(result[0])
     elif (result[2] == result[4] == result[6] and result[2] != ""):
          show_winner(result[2])    
     else:
          draw()                                        

def show_winner(winner):
     if winner == "X":
          player_points[0] +=1   
          showinfo("End Of Game", "Player Number 1 Was Won") 
          restart()
     else:
          player_points[1] +=1
          showinfo("End Of Game", "Player Number 2 Was Won") 
          restart()
          
def restart():
     global result, turn
     result = ["", "", "", "", "", "", "", "", ""]   
     turn = "X"
     points()
     board()    
     
def draw():
     if "" not in result:
          showinfo("End Of Game", "The Game Was Draw")          
          restart()  
     
def points():
     global points
     board_frame = tk.Frame(window)
     board_frame.grid(row=0)
     label_player_one = tk.Label(board_frame, text="Player 1", font=("Aviny", 16), padx=10)
     label_player_two = tk.Label(board_frame, text="Player 2", font=("Aviny", 16), padx=10)
     label_player_one.grid(row=0, column=0)
     label_player_two.grid(row=0, column=2)
     point_frame = tk.Frame(window)
     point_frame.grid(row=1)
     player_one_point = tk.Label(point_frame, text=player_points[0], padx=20, font=("Lalezar", 18))
     player_two_point = tk.Label(point_frame, text=player_points[1], padx=20, font=("Lalezar", 18))
     player_one_point.grid(row=0, column=0)
     player_two_point.grid(row=0, column=1)
     
def board():
     global buttons
     buttons = []
     counter = 0
     board_frame = tk.Frame(window)
     board_frame.grid(row=2)
     for row in range(1, 4):
          for column in range(1, 4):
               index = counter
               buttons.append(index)
               buttons[index] = tk.Button(board_frame, command=lambda x=f"{index}":clicked(x)) 
               buttons[index].config(width=10, height=4, font=("None", 18, "bold"))
               buttons[index].grid(row=row, column=column)
               counter += 1
points()
board()     
window.mainloop()