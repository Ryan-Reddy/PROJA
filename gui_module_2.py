from tkinter import *
from module2moderatie import *

root = Tk()

def clickedYes():
    print(modNumEntry)
    berichtOK = 'ja'
    modifystatustweet(berichtOK, modNumEntry)

def clickedNo():
    print(modNumEntry)
    berichtOK = 'nee'
    modifystatustweet(berichtOK, modNumEntry)

nxttweet= readnexttweet()

# ----------------------------------------
#           GUI design:



label = Label(master=root,text='Type your moderator ID# here:', height=2)
label.pack()

modNumEntry = Entry(master=root)
modNumEntry.pack()

label = Label(master=root,text='Review the following tweet: ',height=2)
label.pack()

label = Label(master=root,text=nxttweet,height=2, bg='blue', fg='white')
label.pack()

label = Label(master=root,text='Is it ok?',height=2)
label.pack()

buttonYes = Button(master=root, text="Yes", command=clickedYes)
buttonYes.pack(side=LEFT, pady=10)

buttonNo = Button(master=root, text="No", command=clickedNo)
buttonNo.pack(side=RIGHT, pady=10)






root.mainloop()