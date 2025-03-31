from tkinter import *
#a list box is a listing of selectable items in It's own container.

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print('You have ordered: ')
    #print(listbox.get(listbox.curselection()))
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia',35),
                  width=12,
                  selectmode=MULTIPLE
                  )


listbox.pack()

listbox.insert(1,'Pizza')
listbox.insert(2,'Burger')
listbox.insert(3,'HotDog')
listbox.insert(4,'Chapati')
listbox.insert(5,'Salad')

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

submitbutton = Button(window,
                      text='Submit',
                      command=submit,
                      )


addbutton = Button(window,
                      text='Add',
                      command=add,
                      )
addbutton.pack()
submitbutton.pack()

deletebutton = Button(window,
                      text='Delete',
                      command=delete)
deletebutton.pack()


window.mainloop()
