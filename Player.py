#Player Class
#written by Mark Chercoe on 3/20/16
#
# Player
# Goals
# Assists
# TOI
#

class Player:
    """Represents an NHL Player"""

    def __init__(self, name, team):
        self.name=name
        self.team=team                  #name and team are strings
        
    def __repr__(self):
        return self.name+" who plays for the "+self.team
    
    
