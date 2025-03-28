from tkinter import *
from tkinter.ttk import Radiobutton

#radi buttons are similar to checkboxes but you can only select one from group

food = ['Pizza','Hotdog','Burgers']

def order():
    if (x.get()==0):
        print('You got pizza')
    elif(x.get()==1):
        print('You got a burger')
    elif (x.get() == 2):
        print('You got a hotdog')
    else:
        print('huh!!')

window = Tk()
pizzaImage = PhotoImage(file='pizza.png')
burgerImage = PhotoImage(file='burger.png')
hotdogImage = PhotoImage(file='hotdog.png')
foodImages = [pizzaImage,burgerImage,hotdogImage]


x = IntVar()
window.geometry('420x420')

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],#adds text to radio buttons
                              variable=x,#groups radiobuttons together if they share same variable
                              value=index,#assigns each radio button a different value
                              #padx=25,
                              #font=('Impact',50)
                              padding=25,
                              image = foodImages[index],
                              compound='right',
                              command=order#set command of button to function
                              )
    radiobutton.pack(anchor=W)



window.mainloop()