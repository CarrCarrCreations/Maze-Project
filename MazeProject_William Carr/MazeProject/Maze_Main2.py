from aiSearch import *
import Maze

class MazeGraphNode(GraphNode):
    def __init__(self, row, col):
        # This creates the graph node containing starting position
        # and the direction for this node to be drawn in
        GraphNode.__init__(self)
        self.row = row
        self.col = col
        self.move_d = ""

    def prettyPrint(self):
        print "row, col"
        print str(self.row), str(self.col)
        # draws the node on the maze
        maze.moveTurtleToCell(self.move_d)


    def __eq__(self, other):
        if self.row == other.row and self.col == other.col:
            return True
        return False

class MazeSearch(AStarSearch):
    def __init__(self, graphSearch):
        AStarSearch.__init__(self, graphSearch, True)
        # save the goal state
        self.goalState = MazeGraphNode(27, 27)

    def goalTest(self, graphNode):
        # Returns true if we reached a goal state
        if graphNode.row == self.goalState.row and graphNode.col == self.goalState.col:
            return True
        return False

    def wallTest(self, node):
        # create an object of the class Cell, with the nodes coord.
        walls = Maze.Cell(node.row, node.col, maze)
        # returns a tuple of True or false for the walls of the cell
        is_wall = walls.cellWalls()
        return is_wall

    def expand(self, graphNode):
        # Empty list of next possible states to return
        nextStateList = []
        # create a copy of the graphNode's row and col values to manipulate
        row = graphNode.row
        col = graphNode.col
        # check to see where the walls are around the graphNode Location
        walls = self.wallTest(graphNode)
        # series of If statements to check if there is a wall in that direction.
        # If there is not a wall, (False), then change the coords and save the
        # direction to be drawn on the map
        # north. Gain access to the first wall value in the tuple.
        if walls[0]is False:
            # make the new node with the new direction
            newNode = MazeGraphNode(row + 1, col)
            # save the direction of this move to the node
            # so prettyPrint can later draw the path
            newNode.move_d = "north"
            # append this node to the list to be returned
            nextStateList.append(newNode)
        # east
        if walls[1] is False:
            newNode2 = MazeGraphNode(row, col + 1)
            newNode2.move_d = "east"
            nextStateList.append(newNode2)
        # south
        if walls[2] is False:
            newNode3 = MazeGraphNode(row - 1, col)
            newNode3.move_d = "south"
            nextStateList.append(newNode3)
        # west
        if walls[3] is False:
            newNode4 = MazeGraphNode(row, col - 1)
            newNode4.move_d = "west"
            nextStateList.append(newNode4)

        # return the list of next states so the search can decide which moves
        # are valid to do next
        return nextStateList

    def heuristic(self, graphNode):
        # Manhattan distance is the heuristic to be used
        # rowValue is the difference between the graphNode Row value and the goalState Row value
        rowValue = abs(self.goalState.row - graphNode.row)
        # ColValue is the difference between the graphNode Col value and the goalState Col value
        colValue = abs(self.goalState.col - graphNode.col)
        # add rowValue and colValue to get the Manhattan distance
        hVal = rowValue + colValue
        # return the heuristic value
        return hVal

    def cost(self, graphNode1, graphNode2):
        # returns the length of a cell's side
        return Maze.Cell.SIDE

# creates the graph used for this instance
maze = Maze.create_maze()
# sets undirected graph search to true
MazePuzzle = MazeSearch(True)
# create the starting node at row 0, col 0
startNode = MazeGraphNode(0, 0)
# put the turtle in the maze at the correct starting point
maze.putTurtleInCell(startNode.row, startNode.col)
# start the search
MazePuzzle.search(startNode)
