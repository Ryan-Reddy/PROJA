from module2moderatie import *
from tkinter import *
from PIL import Image, ImageTk
from read_from_twitter import grabtweets
from weather_api_importer import *
from geopylocation import *
from clock import *

root = Tk()
root.title('Twitter zuil notificatiescherm')


stad = welke_stad()

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

def grabfromtwitter():
    'YES'

# ????????????????????? Volgens mij is deze module plots kapot gegaan oid HELAAS GEEN LOGO..............:
# Logo image placement:
# pilimage = Image.Open("40px-Logo_NS.jpg")
# ns_logo = ImageTk.PhotoImage(pilimage)
# logo_label = Label(image=ns_logo)
# logo_label.pack(pady=15, padx=15)

# first message
label = Label(master=root,text='Welkom bij de NS Twitterzuil',height=2,bg='blue',fg='yellow',font= 'Times 32')
label.pack(pady=10, padx=17)

# first message
label = Label(master=root,text='in de stad: {}, postcode: {}'.format(stad[0],stad[1]),height=2,bg='blue',fg='yellow',font= 'Times 32')
label.pack(pady=10, padx=17)

label3 = Label(master=root,text='Laatste tweet: ',height=2,bg='blue',fg='white')
label3.pack(pady=10, padx=17)

# second message
label3 = Label(master=root,text=grabtweets(),height=2,bg='blue',fg='white')
label3.pack(pady=10, padx=17)

# third message
label2 = Label(master=root,text=twitterscreen(),height=2,bg='blue',fg='white')
label2.pack(pady=10, padx=17)

# gonna have to be a selective grab from DB
label3 = Label(master=root,text='Weersvoorspelling het komende uur: ',height=2,bg='blue',fg='white')
label3.pack(pady=1, padx=1)


# fourth message weather
label3 = Label(master=root,text=weatherget(),height=2,bg='blue',fg='white')
label3.config(height=8, width=70)
label3.pack(pady=50, padx=50)

# clock:
label = Label(master=root,text='in de stad: {}, postcode: {}'.format(stad[0],stad[1]),height=2,bg='blue',fg='yellow',font= 'Times 32')
label.pack(pady=10, padx=17)


buttonYes = Button(master=root, text="Yes", command=clicked_yes)
buttonYes.pack(padx=10,pady=10)

#weerbericht:
# weerbericht bij geen nieuwe tweets na ? minuten
# --- This is my weather importing tool, Will try to add this to the homescreen of module 3
from pprint import pprint
import requests
# pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={API key}
# r = requests.get(
# pprint(r.json())


# post nieuwe tweets uit goedgekeurde tweets


root.mainloop()