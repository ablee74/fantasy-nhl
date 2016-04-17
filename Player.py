#Player Class
#written by Mark Chercoe on 3/20/16
#
# Player
# Goals
# Assists
# TOI
# Shifts
# Games Played
# SOG
# Takeaways
# Giveaways
# Blocks
# Hits
# Faceoffs
# Faceoff wins
# PIM

class Player:
    """Represents an NHL Player"""

    def __init__(self, name, team):
        self.name=name
        self.team=team
        #name and team are strings
        self.goals = 0
        self.assists = 0
        self.TOI = 0
        self.shifts = 0
        self.gamesPlayed = 0
        self.SOG = 0
        self.takeaways = 0
        self.giveaways = 0
        self.blocks = 0
        self.hits = 0
        self.faceoffs = 0
        self.faceoffWins = 0
        self.PIM = 0
        
    def __repr__(self):
        
        s = self.name + "\n"
        s = s + "Team: " + self.team + "\n"
        s = s + "Goals: " + str(self.goals) + "\n"
        s = s + "Assists: " + str(self.assists) + "\n"
        s = s + "TOI: " + str(self.TOI) + "\n"
        s = s + "Shifts: " + str(self.shifts) + "\n"
        s = s + "Games Played: " + str(self.gamesPlayed) + "\n"
        s = s + "SOG: " + str(self.SOG) + "\n"
        s = s + "Takeaways: " + str(self.takeaways) + "\n"
        s = s + "Giveaways: " + str(self.giveaways) + "\n"
        s = s + "Blocked Shots: " + str(self.blocks) + "\n"
        s = s + "Hits: " + str(self.hits) + "\n"
        s = s + "Faceoffs: " + str(self.faceoffs) + "\n"
        s = s + "Faceoff Wins: " + str(self.faceoffWins) + "\n"
        s = s + "PIM: " + str(self.PIM) + "\n"
        
        return s
    
  
    
