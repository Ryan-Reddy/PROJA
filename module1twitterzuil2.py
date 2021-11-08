#Start Module1:




def nieuw_bericht(klant_naam, station, bericht):
    if len(bericht) > 140:
        return "Uw bericht is " + str(len(bericht) - 140) + " tekens te lang!"
    else:
        if len(klant_naam) == 0:
            klant_naam = "Anoniem"
        tweets = open("tweets.txt", "a")
        tweets.write(str(klant_naam+" schreef: " + bericht +" op station: " + station + "\n"))
        tweets.close()
        return "Uw bericht is in ontvangst genomen."


#
# station = input("Op welk station bent u? ")
# klant_naam = input("Uw naam: (optioneel) ")
# bericht = input("Typ uw bericht, maximaal 140 tekens: ")

# print(nieuw_bericht(klant_naam, station, bericht))