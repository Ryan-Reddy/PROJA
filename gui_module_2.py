from tkinter import *
from module2moderatie import *

root = Tk()

def clickedYes():
    berichtOK = 'ja'
    print(tweet_keuren(berichtOK))
def clickedNo():
    berichtOK = 'nee'
    print(tweet_keuren(berichtOK))

# ----------------------------------------
def tweet():
    message = messageEntry.get()
    user = userEntry.get()
    location = locationEntry.get()
    twitty = nieuw_bericht(user, location, message)
    label["text"] = "{}".format(twitty)

def clicked():
    tweet()
    bericht = 'Bedankt voor uw bericht!'
    showinfo(title='Ontvangen!', message=bericht)
# ----------------------------------------


nxttweet= readnexttweet()

label = Label(master=root,text='Review the following tweet',height=2)
label.pack()

label = Label(master=root,text=nxttweet,height=2)
label.pack()

label = Label(master=root,text='Is it ok?',height=2)
label.pack()

buttonYes = Button(master=root, text="Yes", command=clickedYes)
buttonYes.pack(side=LEFT, pady=10)

buttonNo = Button(master=root, text="No", command=clickedNo)
buttonNo.pack(side=RIGHT, pady=10)






root.mainloop()