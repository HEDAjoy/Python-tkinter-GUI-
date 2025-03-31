from tkinter import *

def submit():
    print('Temp is: '+ str(scale.get()) + ' degrees celcius.')

window = Tk()
hot = PhotoImage(file='fire.png')
hotlabel = Label(image=hot)
hotlabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=500,
              orient=VERTICAL,  # orientation of scale
              font=('Arial', 10),
              tickinterval=10,  # numeric integers on scale 4 value
              showvalue=0,  # Hides current value
              troughcolor='#69FAFF',
              fg='#FF1C00',
              bg='#111111'
              )
scale.set((scale['from']-scale['to']/2)+scale['to'])#sets initial place of scale
scale.pack()
cold = PhotoImage(file='ice.png')
icelabel = Label(image=cold)
icelabel.pack()

button = Button(window,
                text='Submit',
                command=submit,

                )
button.pack()
window.mainloop()