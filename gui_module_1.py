from tkinter import *
from module1twitterzuil2 import *
from tkinter.messagebox import showinfo

# define the functions of the gui screen:
def tweet():
    message = messageEntry.get()
    client = userEntry.get()
    location = locationEntry.get()
    twitty = nieuw_bericht(client, location, message)
    label["text"] = "{}".format(twitty)

def clicked():
    tweet()
    bericht = 'Bedankt voor uw bericht!'
    showinfo(title='Ontvangen!', message=bericht)



root = Tk()

# GUI screen design:
label = Label(master=root,text='Type your message here:',height=2)
label.pack()
messageEntry = Entry(master=root)
messageEntry.pack()

label = Label(master=root,text='Type your name here:',height=2)
label.pack()
userEntry = Entry(master=root)
userEntry.pack()

label = Label(master=root,text='Type your location here:',height=2)
label.pack()
locationEntry = Entry(master=root)
locationEntry.pack()


button = Button(master=root, text="press here", command=clicked)
button.pack()

label = Label(master=root)
label.pack()

root.mainloop()