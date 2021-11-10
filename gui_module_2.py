from tkinter import *
from module2moderatie import *

root = Tk()

def clickedYes():
    modnum = modNumEntry.get()
    berichtOK = 'ja'
    modifystatustweet(berichtOK, modnum)

def clickedNo():
    modnum = modNumEntry.get()
    berichtOK = 'nee'
    modifystatustweet(berichtOK, modnum)

nxttweet= readnexttweet()

# ----------------------------------------
#           GUI design:



label = Label(master=root,text='Type your moderator NAME here:', height=2)
label.pack()


modNumEntry = Entry(master=root)
modNumEntry.pack()

label = Label(master=root,text='Review the following tweet: ',height=2)
label.pack()

label = Label(master=root,text=nxttweet[0][0],height=2, bg='blue', fg='white')
label.pack()

label = Label(master=root,text='Is it ok?',height=2)
label.pack()

buttonYes = Button(master=root, text="Yes", command=clickedYes)
buttonYes.pack(side=LEFT, pady=10)

buttonNo = Button(master=root, text="No", command=clickedNo)
buttonNo.pack(side=RIGHT, pady=10)

buttontweet = Button(master=root, text="check of er een post klaar ligt voor twitter", command=posttotwitter, bg='red', fg='white')
buttontweet.pack(side=BOTTOM, pady=10)






root.mainloop()