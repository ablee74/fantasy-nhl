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
        self.GamesPlayed = 0
        self.SOG = 0
        self.takeaways = 0
        self.giveaways = 0
        self.blocks = 0
        self.hits = 0
        self.faceoffs = 0
        self.FaceoffWins = 0
        self.PIM = 0
        
    def __repr__(self):
        return self.name+" who plays for "+self.team
    
    
    
