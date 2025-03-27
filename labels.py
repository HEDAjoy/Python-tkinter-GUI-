from tkinter import *

#label = an area widget that holds text and/or an image within window.

window = Tk()
window.geometry('420x420')

photo = PhotoImage(file='logo.png')

label = Label(window,
              text='Hello world',
              font=('Arial',40,"bold"),
              fg='green',
              bg='black',#fg is text color bg is background color
              relief=RAISED,#relief sets the border style
              bd=10,#bd sets border width
              padx=20,
              pady=20,#padx is padding.
              image=photo,
              compound='bottom')#compound sets where image should be to the text
label.pack()
#displays label on window
#label.place(x=0,y=0)#places widget at top left corner

window.mainloop()