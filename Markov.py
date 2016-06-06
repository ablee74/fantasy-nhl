#Markov Chain - Stage Class
#

class markovStage:
    """Represents the stages of the game progression"""

    def __init__(self, name):
        self.name = name
        self.destL = []
        self.densityL = []


    def addDest(self, dest, density):
        """Adds info to self to determine which stage to go to next"""
        self.destL.append(dest)
        self.densityL.append(density)


    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other.name
