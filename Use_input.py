from tkinter import *

#entry widget is a text box that accepts a single line of user input
def submit():
    username = entry.get()#retrives text written and puts it in variable username
    print('Hello ' + username)

def delete():
    entry.delete(0,END)#this deletes line of text

def backspace():
    entry.delete(len(entry.get())-1, END)#This deletes last character

window = Tk()
window.geometry('420x420')

submit = Button(window,text='Submit',command=submit)
submit.pack(side = RIGHT)

delete = Button(window,text='Delete',command=delete)
delete.pack(side = RIGHT)

backspace = Button(window,text='backspace',command=backspace)
backspace.pack(side = RIGHT)

entry = Entry()
entry.config(font=('Ink Free',50))
entry.config(bg='#111111')
entry.config(fg='white')
#entry.insert(0,'spongebob')#default text
#entry.config(state=DISABLED)#disables the text box(ACTIVE/DISABLED
entry.config(width=10)
#entry.config(show='*')#hide all characters within text box with the character set in show.
entry.pack()


window.mainloop()