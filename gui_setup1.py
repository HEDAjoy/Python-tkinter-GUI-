from tkinter import *

#widgets = GUI elements:buttons,textboxes,labels,images
#windows = serves as container to hold widgets.

#This is for creating WINDOW.

window = Tk()#instantiate an instance of a window
window.geometry("420x420")#sets size of window
window.title("HEDAjoy")#changes title of window

logo = PhotoImage(file='logo.png')#places image on window after converting it to photo
window.iconphoto(True,logo)
window.config(background='#5cfcff')

window.mainloop() # place window on computer screen and listen for events
