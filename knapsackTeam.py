#Knapsack approach
# We're going to figure out how to get the highest FFPG with $200
# Each player will be a list of the format [str,str,float,int] which is
# [name, position, FFPG, price]

import random

players02212016 = [
    ['Henrik Lundqvist','G',13.0,41],
    ['Semyon Varlamov','G',12.5,38],
    ['Cam Ward','G', 9.8,36],
    ['Ryan Miller','G',11.3,36],
    ['John Gibson','G',11.3,32],
    ['Andrei Vasilevskiy','G',9.7,30],
    ['Jonas Hiller','G',10.1,30],
    ['Jimmy Howard','G',9.5,25],
    ['Ryan Getzlaf','C',8.3,30],
    ['Pavel Datsyuk','C',8.2,29],
    ['Derek Stepan', 'C',6.9,25],
    ['Steven Stamkos','C',7.8,25],
    ['Henrick Zetterberg','C',6.8,23],
    ['Derick Brassard','C',6.9,23],
    ['Ryan Kesler','C',6.3,23],
    ['Sean Monahan','C',6.8,22],
    ['JT Miller','C',4.9,20],
    ['Nathan MacKinnon','C',7.1,20],
    ['Jordan Staal','C',5.1,19],
    ['Rickard Rakell','C',4.5,19],
    ['Matt Duchene','C',6.9,19],
    ['Sam Bennett', 'C',4.4,18],
    ['Tyler Johnson','C',7.5,17],
    ['Michael Backlund','C',5.2,17],
    ['Andrej Nestrasil','C',4.0,16],
    ['Elias Lindholm','C',4.5,16],
    ['Carl Soderberg','C',5.6,16],
    ['Henrik Sedin','C',6.0,16],
    ['Darren Helm','C',4.3,15],
    ['Victor Rask','C',4.8,15],
    ['Valtteri Filppula','C',3.8,14],
    ['Brad Richards','C',5.3,13],
    ['Andrew Cogliano','C',4.0,13],
    ['Mike Santorelli','C',3.8,13],
    ['Bo Horvat','C',3.7,13],
    ['Riley Sheahan','C',3.5,12],
    ['Andreas Athanasiou', 'C',2.7,12],
    ['Luke Glendening','C',3.2,12],
    ['Dominic Moore','C',3.1,12],
    ['Oscar Lindberg','C',4.7,12],
    ['Brian Boyle', 'C', 3.6,12],
    ['Jonathan Marchessault', 'C', 4.0,12],
    ['Cedric Paquette','C',3.0,12],
    ['Jay McClement','C',2.0,12],
    ['Eric Staal', 'C', 6.1,12],
    ['Riley Nash', 'C', 3.4,12],
    ['Brad Malone', 'C',1.8,12],
    ['Matt Stajan', 'C',2.6,12],
    ['Joe Colborne','C',3.7,12],
    ['Markus Granlund','C',3.3,12],
    ['Josh Jooris','C',3.4,12],
    ['Nate Thompson','C',2.8,12],
    ['Harry Zolnierczyk','C',-0.3,12],
    ['Ryan Garbutt','C',3.6,12],
    ['Mikhail Grigorenko','C',3.0,12],
    ['Alex Friesen','C',-3.0,12],
    ['Jared McCann','C',3.2,12],
    ['Corey Perry','W',8.0,27],
    ['Mats Zuccarello','W',6.4,26],
    ['Daniel Sedin','W',7.9,26],
    ['Johnny Daudreau', 'W',7.3,25],
    ['Nikita Kucherov', 'W',7.6,23],
    ['Jarome Iginla', 'W',6.1,21],
    ['Gabriel Landeskog','W',6.8,21],
    ['David Perron','W',4.7,20],
    ['Jakob Silfvberg','W',5.7,20],
    ['Jeff Skinner','W',5.4,19],
    ['Justin Abdelkader','W',5.5,18],
    ['Chris Kreider','W',5.5,17],
    ['Jiri Hudler', 'W',6.3,17],
    ['Ryan Callahan','W',5.7,16],
    ['JT Brown','W',3.3,16],
    ['Gustav Nyquist','W',5.5,15],
    ['Kevin Hayes','W',4.6,15],
    ['Alex Killorn','W',5.2,15],
    ['Blake Comeau','W',4.8,15],
    ['Jannik Hansen','W',4.7,15],
    ['Tomas Tatar','W',6.0,14],
    ['Ondrej Palat','W',6.4,14],
    ['Kris Versteeg','W',5.3,14],
    ['Michael Frolik','W',5.5,14],
    ['Sven Baertschi','W',3.5,14],
    ['Teemu Pulkkinen','W',4.3,12],
    ['Tomas Jurco','W',2.6,12],
    ['Daniel Paille','W',2.0,12],
    ['Tanner Glass','W',1.3,12],
    ['Viktor Stlberg','W',3.8,12],
    ['Jesper Fast','W',3.2,12],
    ['Erik Condra','W',3.5,12],
    ['Joel Vermin','W',1.5,12],
    ['Nathan Gerbe','W',3.9,12],
    ['Chris Terry','W', 2.7,12],
    ['Joakim Nordstrom','W',2.5,12],
    ['Phillip Di Giuseppe','W',3.9,12],
    ['David Jones','W',3.8,12],
    ['Brandon Bollig','W',1.5,12],
    ['Michael Ferland','W',3.1,12],
    ['Lance Bouma','W',4.1,12],
    ['Patrick Maroon','W',3.5,12],
    ['Nick Ritchie','W',2.6,12],
    ['Alex Tanguay','W',4.5,12],
    ['Jack Skille', 'W',2.8,12],
    ['Cody McLeod', 'W',2.4,12],
    ['Chris Wagner','W',2.0,12],
    ['Andreas Martinsen','W',2.3,12],
    ['Radim Vrbata','W',6.6,12],
    ['Alexandre Burrows','W',4.3,12],
    ['Adam Cracknell','W',2.1,12],
    ['Derek Dorsett', 'W',2.6,12],
    ['Emerson Etem', 'W', 3.1,12],
    ['Jake Virtanen','W', 3.0,12],
    ['Victor Hedman','D', 7.3,25],
    ['Mark Giordano','D', 8.4,23],
    ['Sami Vatanen', 'D', 6.7,22],
    ['Dougie Hamilton','D',5.9,21],
    ['Erik Johnson', 'D',7.2,20],
    ['Keith Yandle', 'D',6.1,19],
    ['Dan Girardi','D',5.3,19],
    ['TJ Brodie','D',6.5,19],
    ['Cam Fowler','D',5.0,18],
    ['Hampus Lindholm','D',5.1,18],
    ['Tyson Barrie', 'D', 6.1, 18],
    ['Francois Beauchemin','D',6.4,17],
    ['Mike Green', 'D', 5.7,15],
    ['Danny DeKyser','D',4.1,14],
    ['Dan Boyle', 'D', 5.1, 14],
    ['Anton Stralman','D',5.4,14],
    ['Jaccob Slavin', 'D',4.6,14],
    ['Christopher Tanev','D',4.6,14],
    ['Ben Hutton','D',3.7,14],
    ['Kevin Klein','D',5.1,13],
    ['John-Michael Liles','D',4.0,13],
    ['Brett Pesce','D',4.0,13],
    ['Kevin Bieksa','D',4.0,13],
    ['Simon Despres','D',4.4,13],
    ['Kyle Quincey', 'D',3.7,12],
    ['Jakub Kindi', 'D', 3.9,12],
    ['Brendan Smith','D',2.9,12],
    ['Xavier Ouellet','D',2.9,12],
    ['Alexey Marchenko','D',2.4,12],
    ['Marc Staal', 'D', 3.7,12],
    ['Dylan McIlrath', 'D', 3.3,12],
    ['Braydon Coburn', 'D', 3.3,12],
    ['Matthew Carle', 'D', 3.3,12],
    ['Nikita Nesterov','D',3.2,12],
    ['Slater Koekkoek','D',2.0,12],
    ['Andrej Sustr', 'D',2.7,12],
    ['Ron Hainsey', 'D', 3.2,12],
    ['Michal Jordan','D',2.7,12],
    ['Noah Hanifin','D',3.7,12],
    ['Deryk Engelland','D',2.9,12],
    ['Jakub Nakladal','D',2.5,12],
    ['Josh Manson','D',3.0,12],
    ['Andrew Bodnarchuk','D',0.9,12],
    ['Nick Holden','D',3.6,12],
    ['Zach Redmond','D',3.8,12],
    ['Chris Bigras','D',1.6,12],
    ['Dan Hamhuis','D',3.8,12],
    ['Luca Sbisa','D',3.2,12],
    ['Yannick Weber','D',3.7,12],
    ['Matt Bartkowski','D',2.0,12],
    ['Alex Biega','D',2.2,12]
    ]


#filter functions

def posFilter(player, pos):
    """returns true if the player plays position pos"""
    return player[1] == pos

def priceFilter(player, price):
    """returns true if the player is within budget"""
    return player[3] <= price

def ffpgFilter(player, ffpg):
    """returns true if the player is better than ffpg"""
    return player[2] >= ffpg

def bestPlayer(playerList):
    """returns the player with the highest ffpg"""
    assert(playerList != [])
    bestSoFar = ['fake','fake',-10,100]
    for i in range(len(playerList)):
        if playerList[i][2]>bestSoFar[2]:
            bestSoFar = playerList[i]
    return bestSoFar

def makeTeam(playerList, spotsL, money):
    """Randomly creates a valid fantasy hockey team: spotsL is a list of open
    positions of the form [G, C, W, D] and will normally be [2, 2, 3, 2], money
    is the funds available to buy players"""
    myTeam=[]
    posL = ['G','C','W','D']

    finished = False
    attempt = 0
    while not finished:
        budget = money

        for i in range(len(posL)):
            # we randomly choose players for position i
            tempPosition = filter(lambda x: posFilter(x,posL[i]),playerList)
            potentialPositions = []
            for j in range(spotsL[i]):
                p = random.choice(tempPosition)
                tempPosition.remove(p)
                potentialPositions.append(p)
            for j in range(len(potentialPositions)):
                #Look for better deals: lower prices and higher ffpg
                betterPlayers = filter(lambda x: \
                                       ffpgFilter(x,potentialPositions[j][2]),
                                       filter(lambda y: \
                                              priceFilter(y, \
                                                    potentialPositions[j][3]),
                                              tempPosition))
                #If we find a better deal, make the switch
                if betterPlayers != []:
                    bestDeal = bestPlayer(betterPlayers)
                    tempPosition.append(potentialPositions[j])
                    potentialPositions[j]=bestDeal
                    tempPosition.remove(bestDeal)
            #pay for the players
            for p in potentialPositions:
                budget -= p[3]
            #make sure there's enough to fill out the rest of the team
                #This will also check that we aren't in debt : budget < 0
            if budget < 12*sum(spotsL[i+1:]):
                break
            # add players to your roster
            myTeam += potentialPositions
        #If you have filled the spots and you're not in debt then we have a team
        if len(myTeam)==sum(spotsL) and budget >= 0:
            finished = True
        attempt+=1
    return myTeam

def evaluate(team):
    """returns the total FFPG of the team"""
    ffpg=0
    spent=0
    for p in team:
        ffpg += p[2]
        spent += p[3]
    return [ffpg,spent]

def optimize(playerList,spotsL,money, threshold1,threshold2):
    """Tries to find the best possible fantasy team, currently done by randomly
    generating teams and printing the ones higher than a threshold"""
    bestSoFar=[0,money]
    bestTeam=[]
    while bestSoFar[0] <= threshold1:
        team = makeTeam(playerList,spotsL, money)
        x=evaluate(team)
        if x[0]>bestSoFar[0] or (x[0]==bestSoFar[0] and x[1]<bestSoFar[1]):
            bestSoFar=x
            bestTeam=team
            print 'subpar:', bestSoFar
            if bestSoFar[0]>threshold2:
                print bestSoFar
                for p in bestTeam:
                    print p
                print
    return bestTeam, bestSoFar
        
                    




