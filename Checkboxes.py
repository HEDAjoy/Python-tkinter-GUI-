from tkinter import *

def display():
    if(x.get()==1)&(y.get()==0):
        print('I like Python')
    elif(x.get()==0)&(y.get()==1):
        print('I like Java')
    elif(x.get()==1)&(y.get()==1):
        print('I like both Python and Java')
    else:
        print('I do not like either')

window = Tk()
window.geometry("420x420")
x = IntVar()
y = IntVar()

checkbox = Checkbutton(window,text='Python',variable=x,onvalue=1,offvalue=0,command=display)
checkbox.pack()
checkbox.config(font=('Arial',20))
checkbox.config(fg='#0000FF')
checkbox.config(bg='#000000')
checkbox.config(activeforeground='#0000FF')
checkbox.config(activebackground='#000000')
photo = PhotoImage(file='logo.png')
checkbox.config(image=photo,compound='left')
checkbox.config(padx=25,pady=25,width=250,height=50)
checkbox.config(anchor='w')

checkbox2 = Checkbutton(window,text='Java',variable=y,onvalue=1,offvalue=0,command=display)
checkbox2.pack()
checkbox2.config(font=('Arial',20))
checkbox2.config(fg='#0000FF')
checkbox2.config(bg='#000000')
checkbox2.config(activeforeground='#0000FF')
checkbox2.config(activebackground='#000000')
photo2 = PhotoImage(file='logo.png')
checkbox2.config(image=photo2,compound='left')
checkbox2.config(padx=25,pady=25,width=250,height=50)
checkbox2.config(anchor='w')#makes them align to relative cardinal direction(west)

window.mainloop()