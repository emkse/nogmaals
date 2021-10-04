import random
#Emre Kose
ronde = 1 
punten = 0 
raden = -1

print("Raad het getal tussen 1 en 1000") 
while ronde <= 20: 
    print("Ronde " + str(ronde))
    getal = random.randint(1,1000)
    kans = 1  
    while getal != raden:
        raden = int(input(str(kans) + ": "))
        if raden < getal:
            print("Hoger")
            if (getal - raden) <= 20:
                print("Je bent heel warm")
            elif (getal - raden) <= 50:
                print("Je bent warm")
        elif raden > getal:
            print("Lager")
            if (raden - getal) <= 20: 
                print("Je bent heel warm")
            elif (raden - getal) <= 50:
                print("Je bent warm")
        else: 
            print("Correct")
            punten = punten + 1
        kans = kans + 1
        if kans > 10:
            break
    print("Het getal was " + str(getal))
    if ronde >= 20:
        break  
    print("Aantal punten: " + str(punten))
    print("Nog een keer getal raden? Ja/Nee")
    antwoord = input("")
    if not (antwoord == "Ja" or antwoord == "ja"):
        break
    ronde = ronde + 1
print("Einde")
print("Uw eindscore is " + str(punten))
