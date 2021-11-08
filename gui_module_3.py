from module2moderatie import *
from tkinter import *
from post_to_twitter import post_to_twitter
from PIL import ImageTk,Image
from read_from_twitter import grabtweets
from weather_api_importer import *

root = Tk()

def clicked_yes():
    yeslabel = Label(master=root, text='clicked yes')
    yeslabel.pack()

def twitterscreen():
    time = ''
    if time == 1:
        text = 'latest tweet here'
    else:
        text = 'weather'

    return text


root.title('Twitter zuil notificatiescherm')


# Logo image placement:
ns_logo = ImageTk.PhotoImage(Image.open("640px-Logo_NS.jpg"))
logo_label = Label(image=ns_logo)
logo_label.pack(pady=15, padx=15)

# first message
label = Label(master=root,text='Welkom bij de NS Twitterzuil',height=2,bg='blue',fg='yellow',font= 'Times 32')
label.pack(pady=10, padx=17)

# second message
label2 = Label(master=root,text=twitterscreen(),height=2,bg='blue',fg='white')
label2.pack(pady=10, padx=17)

# third message
label3 = Label(master=root,text=grabtweets(),height=2,bg='blue',fg='white')
label3.pack(pady=10, padx=17)
# gonna have to be a selective grab from DB

# fourth message weather
label3 = Label(master=root,text=weatherget(),height=2,bg='blue',fg='white')
label3.config(height=8, width=70)
label3.pack(pady=50, padx=50)
# gonna have to be a selective grab from DB


buttonYes = Button(master=root, text="Yes", command=clicked_yes)
buttonYes.pack(padx=10,pady=10)

#weerbericht:
# weerbericht bij geen nieuwe tweets na ? minuten
# --- This is my weather importing tool, Will try to add this to the homescreen of module 3
from pprint import pprint
import requests
# pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={API key}
# r = requests.get(
#     'http://api.openweathermap.org/data/2.5/weather?q=Amsterdam&APPID=bec405355763e158b82e587d6f63b06b')  # .format(Amsterdam))
# pprint(r.json())


# post nieuwe tweets uit goedgekeurde tweets


root.mainloop()