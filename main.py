from cProfile import label
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')

# Disable all buttons
def disableButtons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# Check to see if someone won
def checkWin():
    global winner
    winner = False

    if b1['text'] == b2['text'] == b3['text'] and not b1['text'] == ' ':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', b1['text'] + ' wins!')
        disableButtons()
    elif b4['text'] == b5['text'] == b6['text'] and not b4['text'] == ' ':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', b4['text'] + ' wins!')
        disableButtons()
    elif b7['text'] == b8['text'] == b9['text'] and not b7['text'] == ' ':
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', b4['text'] + ' wins!')
        disableButtons()
    elif b1['text'] == b4['text'] == b7['text'] and not b1['text'] == ' ':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', b1['text'] + ' wins!')
        disableButtons()
    elif b2['text'] == b5['text'] == b8['text'] and not b2['text'] == ' ':
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', b2['text'] + ' wins!')
        disableButtons()
    elif b3['text'] == b6['text'] == b9['text'] and not b3['text'] == ' ':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', b3['text'] + ' wins!')
        disableButtons()
    elif b1['text'] == b5['text'] == b9['text'] and not b1['text'] == ' ':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', b1['text'] + ' wins!')
        disableButtons()
    elif b3['text'] == b5['text'] == b7['text'] and not b3['text'] == ' ':
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', b3['text'] + ' wins!')
        disableButtons()
    
    # check if tie
    if count == 9 and winner == False:
        messagebox.showinfo('Tic Tac Toe', 'Tie')
        disableButtons()

# Button clicked function
def bClick(b):
    global clicked, count

    if b['text'] == ' ' and clicked == True:
        # X is clicking the button
        b['text'] = 'X'
        clicked = False
        count += 1
        checkWin()
    elif b['text'] == ' ' and clicked == False:
        # O is clicking the button
        b['text'] = 'O'
        clicked = True
        count  += 1
        checkWin()
    else: # trying to fill a spot that's taken
        messagebox.showerror('Tic Tac Toe', 'Spot is taken.\nTry Again...')

# Reset the board
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    # Build buttons (9)
    b1 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: bClick(b1))
    b2 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: bClick(b2))
    b3 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: bClick(b3))

    b4 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: bClick(b4))
    b5 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: bClick(b5))
    b6 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: bClick(b6))

    b7 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: bClick(b7))
    b8 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: bClick(b8))
    b9 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: bClick(b9))

    # Grid buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

# create menu
myMenu = Menu(root)
root.config(menu=myMenu)

# create Options menu
optionsMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label='Options', menu=optionsMenu)
optionsMenu.add_command(label='Reset Board', command=reset)

reset() 
root.mainloop()