# name of student: Emre 
# number of student: 99069595
# purpose of program: een programma dat helpt wisselgeld terug te geven met de juiste hoeveelheid munten van bepaalde soort.
# function of program: rekent uit hoeveel je wisselgeld is 
# structure of program: compact

toPay = int(float(input('Amount to pay: '))* 100) # er wordt hier gevraagd hoeveel je moet betalen
paid = int(float(input('Paid amount: ')) * 100) # er wordt hier uitgeprint hoeveel je hebt betaald
change = paid - toPay # de bedrag die je terug krijgt

if change > 0: # als change groter is dan 0
  coinValue = 500 # dan is coin value 500
  
  while change > 0 and coinValue > 0: # terwijl change is 0 en coinvalue ook 0 is 
    nrCoins = change // coinValue # deze functie  zorgt dat als je 2 getallen deelt en het komt niet precies uit, dat hij de getallen achter de komma wegwerkt en altijd omlaag afrond

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: Deze if statement zit in de while lus dus hij rolt deze statement totdat hij op nul springt
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')