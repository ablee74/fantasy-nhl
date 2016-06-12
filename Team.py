#Team Class

#Team
#City
#List of Players

class Team:
    """Represents an NHL team of players"""
    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        self.roster = []
        self.forward = []
        self.defense = []

class Lineup:
    """Represents a lineup of an NHL Team"""
    def __init__(self, playerList, fwd):
        assert((fwd and len(playerList) == 3) or
               (not fwd and len(playerList) == 2))
        self.playerList = list(playerList)
        self.fwd = fwd
        self.score = 0    # NEED TO UPDATE - REFINE TEAM SCORING SYSTEM
        


