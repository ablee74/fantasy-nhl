#Hockey Graph
#Represents a hockey game as a flow chart (Markov Chain). This flow chart will
# be represented as a directional graph (the kind with nodes and edges, search
# 'graph theory').
#For now, this does not simulate anything. We're going to use this to lay out
# and visualize the structure of the Markov Chain.

#To get a graph object, we'll need the networkx package.
# Open up the Command Prompt in the start menu
# Type in the command 'cd ../../Python27' This will Change your Directory to the
#  Python directory
# Type in the command 'python -m pip install networkx'

#Bring in the networkx package. Any function taken from this package must be
# proceeded by nx.
import networkx as nx
#We'll also need matplotlib to display the graphs. You should already have this
import matplotlib.pyplot as plt

#First, run the sample function. Doing so, will execute a script that will
# create a graph representing our SimpleSim. You will be editing a similar
# script that creates a graph representing a hockey match in much more detail.

def sample():
    '''This function is a script that creates a graph representing the
    SimpleSim version of a hockey match'''
    #Create a directional graph
    G = nx.DiGraph()
    
    #Create our nodes (stages of the game), represented by strings    
    f = 'faceoff'    
    t1 = 'team1 has the puck'    
    t2 = 'team2 has the puck'    
    g1 = 'team1 scores'
    g2 = 'team2 scores'
    myNodes = [f,t1,t2,g1,g2]

    G.add_nodes_from(myNodes)

    #Create our edges (transitions between stages). Each edge is represented by
    # a tuple: (start,destination)
    G.add_edge(f,t1) #faceoff results in team1 getting the puck
    G.add_edge(f,t2) #faceoff results in team2 getting the puck
    G.add_edge(t1,t2) #team2 takes puck from team1
    G.add_edge(t2,t1) #team1 takes puck from team2
    G.add_edge(t1,g1) #team1 shoots and scores
    G.add_edge(t2,g2) #team2 shoots and scores
    G.add_edge(g1,f) #after scoring, reset to faceoff
    G.add_edge(g2,f) #after scoring, reset to faceoff

    #display the graph
    reprGraph(G)

def reprGraph(graph):
    '''takes a graph and draws/displays it for the user'''
    pos = nx.spring_layout(graph)
    nodes = nx.draw_networkx_nodes(graph,
                                   pos,
                                   graph.nodes(),
                                   node_color='r')
    edges = nx.draw_networkx_edges(graph,
                                   pos,
                                   graph.edges(),
                                   edge_color = 'r')
    #drawing labels requires a dictionary. This is kind of silly
    # for us since our nodes are already strings, but bear with
    # me
    labelsDict = {}
    for x in graph.nodes():
        labelsDict[x]=x
    labels = nx.draw_networkx_labels(graph,
                                     pos,
                                     labelsDict)
    plt.show([nodes,edges,labels])
    
#Now we're going to create the graph that describes a hockey match in much more
# detail. When you're ready, uncomment the code below the horizontal line. To do
# this, highlight the code and hit Alt+4 (Format >> Uncomment Region)
#As you work, you can see what you have so far by compiling (f5). Since this
# script isn't contained inside a function, it will run automatically once you
# compile

##############################################################################

MC = nx.DiGraph() #MC is short for Markov Chain

#Create our nodes (stages of the game), represented by strings

#Add new stages and change the existing stages
#example: if a defender blocks a shot, will they most likely have possession of
#         the puck? instead of D2aBlocks, should there just be D2aHasPuck?
#Some places to start:
#  RW1 should be able to shoot
#  team2 should be able to pass and shoot
#  various forms of gva/tka between the two teams
#  penalties

faceoff = 'faceoff'
MC.add_node(faceoff)
RW1HasPuck = 'RW 1 has puck'
MC.add_node(RW1HasPuck)
LW1HasPuck = 'LW 1 has puck'
MC.add_node(LW1HasPuck)
D1LHasPuck = 'Def1-L has puck'
MC.add_node(D1LHasPuck)
D1RHasPuck = 'Def1-R has puck'
MC.add_node(D1RHasPuck)
RW2HasPuck = 'RW 2 has puck'
MC.add_node(RW2HasPuck)
LW2HasPuck = 'LW 2 has puck'
MC.add_node(LW2HasPuck)
C2HasPuck = 'Center 2 has puck'
MC.add_node(C2HasPuck)
D2LHasPuck = 'Def2-L has puck'
MC.add_node(D2LHasPuck)
D2RHasPuck = 'Def2-R has puck'
MC.add_node(D2RHasPuck)
LW1Shoots = 'LW1 shoots'
MC.add_node(LW1Shoots)
C1HasPuck = 'Center1 has puck'
MC.add_node(C1HasPuck)
C1Shoots = 'Center1 shoots'
MC.add_node(C1Shoots)
D2LBlocks = 'Def2-L blocks shot'
MC.add_node(D2LBlocks)
D2RBlocks = 'Def2-R blocks shot'
MC.add_node(D2RBlocks)
G1Saves = 'Goalie1 makes a save'
MC.add_node(G1Saves)
G2Saves = 'Goalie2 makes a save'
MC.add_node(G2Saves)
score1 = 'team1 scores'
MC.add_node(score1)

#Create our edges (transitions between stages)

#Faceoff results in LW1 getting the puck
MC.add_edge(faceoff,LW1HasPuck)
#LW1 passes to Center1
MC.add_edge(LW1HasPuck,C1HasPuck)
#Center1 passes to LW1
MC.add_edge(C1HasPuck,LW1HasPuck)

#LW1 shoots
MC.add_edge(LW1HasPuck,LW1Shoots)
#Def2-L blocks LW1's shot
MC.add_edge(LW1Shoots,D2LBlocks)
#Def2-R blocks LW1's shot
MC.add_edge(LW1Shoots,D2RBlocks)
#Goalie2 blocks LW1's shot
MC.add_edge(LW1Shoots,G2Saves)
#LW1 scores a goal
MC.add_edge(LW1Shoots,score1)

#C1 shoots
MC.add_edge(C1HasPuck,C1Shoots)
#Def2-L blocks C1's shot
MC.add_edge(C1Shoots,D2LBlocks)
#Def2-R blocks C1's shot
MC.add_edge(C1Shoots,D2RBlocks)
#Goalie2 blocks C1's shot
MC.add_edge(C1Shoots,G2Saves)
#C1 scores a goal
MC.add_edge(C1Shoots,score1)

reprGraph(MC)

