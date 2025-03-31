from tkinter import *
from tkinter import messagebox #import messagebox library

def click():
    #messagebox.showinfo(title='This is an info message box',message='You are a great creator')
    #messagebox.showwarning(title='WARNING!!',message='VIRUS detected')
    #messagebox.showerror(title='ERROR!!',message='Something went wrong!')
    #if messagebox.askokcancel(title='ASK OK CANCEL',message='Do you wanna do it??'):
        #print("You did the thing.")
    #else:
        #print('You cancelled.')
    #if messagebox.askretrycancel(title='askretrycancel!',message='Retry or Cancel'):
       # print('You can retry')
    #else:
        #print('You cancelled')

    #if messagebox.askyesno(title="YES or NO",message='Do you love me?'):
        #print('Aww me too!!')
    #else:
        #print('FUCK YOU!')

    #answer = messagebox.askquestion(title='Ask smth',message="Do you like movies??")
    #if answer == 'yes':
           # print('Me too!!')
    #else:
            #print('Why not?')

    answer = messagebox.askyesnocancel(title="YEs No CANCEL",message=('Do you code??'))
    if (answer == True):
        print("YAYYY")
    elif (answer == False):
        print('Tou a bitch!')
    else:
        print('WDYM?')

window = Tk()

button = Button(window,command=click,text='Click Me!!')
button.pack()

window.mainloop()