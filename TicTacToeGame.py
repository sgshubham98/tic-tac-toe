from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

activePlayer = 1
shakti = [] 
rishabh = []

root = Tk()
root.title("Tic Tac Toe : Player 1")

button1 = ttk.Button(root, text = '')
button1.grid(row = 0, column = 0, sticky = 'snew', ipadx = 40, ipady = 40)
button1.config(command = lambda: ButtonClick(1))

button2 = ttk.Button(root, text = '')
button2.grid(row = 0, column = 1, sticky = 'snew', ipadx = 40, ipady = 40)
button2.config(command = lambda: ButtonClick(2))

button3 = ttk.Button(root, text = '')
button3.grid(row = 0, column = 2, sticky = 'snew', ipadx = 40, ipady = 40)
button3.config(command = lambda: ButtonClick(3))

button4 = ttk.Button(root, text = '')
button4.grid(row = 1, column = 0, sticky = 'snew', ipadx = 40, ipady = 40)
button4.config(command = lambda: ButtonClick(4))

button5 = ttk.Button(root, text = '')
button5.grid(row = 1, column = 1, sticky = 'snew', ipadx = 40, ipady = 40)
button5.config(command = lambda: ButtonClick(5))

button6 = ttk.Button(root, text = '')
button6.grid(row = 1, column = 2, sticky = 'snew', ipadx = 40, ipady = 40)
button6.config(command = lambda: ButtonClick(6))

button7 = ttk.Button(root, text = '')
button7.grid(row = 2, column = 0, sticky = 'snew', ipadx = 40, ipady = 40)
button7.config(command = lambda: ButtonClick(7))

button8 = ttk.Button(root, text = '')
button8.grid(row = 2, column = 1, sticky = 'snew', ipadx = 40, ipady = 40)
button8.config(command = lambda: ButtonClick(8))

button9 = ttk.Button(root, text = '')
button9.grid(row = 2, column = 2, sticky = 'snew', ipadx = 40, ipady = 40)
button9.config(command = lambda: ButtonClick(9))

def ButtonClick(id):
   global activePlayer
   global shakti
   global rishabh

   if(activePlayer == 1):
      setLayout(id, "X")
      shakti.append(id)
      root.title("Tic Tac Toe : Player 2")
      activePlayer = 2
      print("P1:{}".format(shakti))
      autoPlay()

   elif(activePlayer == 2):
      setLayout(id, "O")
      rishabh.append(id)
      root.title("Tic Tac Toe : Player 1")
      activePlayer = 1
      print("P2:{}".format(rishabh))

   checkWinner()


def setLayout(id, PlayerSymbol):
   if id==1:
      button1.config(text=PlayerSymbol)
      button1.state(['disabled'])

   elif id==2:
      button2.config(text=PlayerSymbol)
      button2.state(['disabled'])
   
   elif id==3:
      button3.config(text=PlayerSymbol)
      button3.state(['disabled'])

   elif id==4:
      button4.config(text=PlayerSymbol)
      button4.state(['disabled'])

   elif id==5:
      button5.config(text=PlayerSymbol)
      button5.state(['disabled'])
   
   elif id==6:
      button6.config(text=PlayerSymbol)
      button6.state(['disabled'])

   elif id==7:
      button7.config(text=PlayerSymbol)
      button7.state(['disabled'])

   elif id==8:
      button8.config(text=PlayerSymbol)
      button8.state(['disabled'])

   elif id==9:
      button9.config(text=PlayerSymbol)
      button9.state(['disabled'])

def checkWinner():
   winner = -1
   if((1 in shakti) and (2 in shakti) and (3 in shakti)):
      winner=1
   if((1 in rishabh) and (2 in rishabh) and (3 in rishabh)):
      winner=2
   if((4 in shakti) and (5 in shakti) and (6 in shakti)):
      winner=1
   if((4 in rishabh) and (5 in rishabh) and (6 in rishabh)):
      winner=2
   if((7 in shakti) and (8 in shakti) and (9 in shakti)):
      winner=1
   if((7 in rishabh) and (8 in rishabh) and (9 in rishabh)):
      winner=2    
   if((1 in shakti) and (4 in shakti) and (7 in shakti)):
      winner=1
   if((1 in rishabh) and (4 in rishabh) and (7 in rishabh)):
      winner=2
   if((2 in shakti) and (5 in shakti) and (8 in shakti)):
      winner=1
   if((2 in rishabh) and (5 in rishabh) and (8 in rishabh)):
      winner=2
   if((3 in shakti) and (6 in shakti) and (9 in shakti)):
      winner=1
   if((3 in rishabh) and (6 in rishabh) and (9 in rishabh)):
      winner=2
   if((1 in shakti) and (5 in shakti) and (9 in shakti)):
   	  winner=1
   if((1 in rishabh) and (5 in rishabh) and (9 in rishabh)):
      winner=2
   if((3 in shakti) and (5 in shakti) and (7 in shakti)):
      winner=1
   if((3 in rishabh) and (5 in rishabh) and (7 in rishabh)):
      winner=2   

   if winner==1:
      messagebox.showinfo(title="Congratulations!!",message = "Player 1 Wins!")
      exit()

   elif winner==2:
      messagebox.showinfo(title="Congratulations!!",message = "Player 2 Wins!")
      exit()

def autoPlay():
	global shakti
	global rishabh
	emptyCells = []
	for  cell in range(9):
		if(not((cell+1 in shakti) or (cell+1 in rishabh))):
			emptyCells.append(cell+1)
	randIndex = randint(0, len(emptyCells)-1)
	ButtonClick(emptyCells[randIndex])

root.mainloop()
