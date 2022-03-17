from tkinter import *

# key down function (for submit button)
def click():
    entered_text = textentry.get() # collect from text box
    output.delete(0.0, END) # from 1st line and 1st character to end of the text box
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = 'sorry that word is not in the dictionary.'
    output.insert(END, definition)

window = Tk() # initialize window
window.title("My First GUI") # set title of window
window.configure(background='black') # set background to black

# create photo
photo1 = PhotoImage(file='python.gif')
Label(window, image=photo1, bg='black').grid(row=0, column=0, sticky=E)

# create label
Label(window, text='Enter a word to get the definition', bg='black', fg='white', font='none 12 bold').grid(row=1, column=0, sticky=W)
Label(window, text='\nDefinition:', bg='black', fg='white', font='none 12 bold').grid(row=4, column=0, sticky=W)

# text entry box
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky=W)

# submit button
Button(window, text='SUBMIT', width=6, command=click).grid(row=3, column=0, sticky=W)

# text box
output = Text(window, width=75, height=6, wrap=WORD, background='white')
output.grid(row=5, column=0, columnspan=2, sticky=W)

# the dictionary
my_compdictionary = {
    'algorithm' : 'Step by step instructions to complete a task',
    'bug' : 'piece of code that causes a program to fail'
}

# exit label
Label(window, text='click to exit:', bg='black', fg='white', font='none 12 bold').grid(row=6, column=0, sticky=W)

# exit button
def close_window():
    window.destroy()
    exit()
Button(window, width=14, command=close_window, text='Exit').grid(row=7, column=0, sticky=W)


# run the main loop - MUST BE AT THE END
window.mainloop()