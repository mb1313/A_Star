class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):

    # Create Start Node

    startNode = Node(None, start)
    endNode = Node(None, end)

    startNode.g = startNode.h = startNode.f = 0
    endNode.g = endNode.h = endNode.f = 0

    # Create open and closed lists

    openList = []
    closedList = []

    # Add start node to open list

    openList.append(startNode)

    #Create iteration limit to ensure no infinite loops
    totalCount = 0
    maxCount = (len(maze) // 2) ** 10

    while len(openList) > 0:

        #increase count by 1
        totalCount += 1
        if totalCount >= maxCount:
            print("giving up - too many iterations")
            return []

        # Get current node
        currentNode = openList[0]
        currentIndex = 0

        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index

        # Pop from open list, add to closed list
        openList.pop(currentIndex)
        closedList.append(currentNode)

        # Found EndNode
        if (currentNode == endNode):
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            #Returns reversed path
            return path[::-1]

        # Get Children of currentNode
        children = []
        positions = [(0, 1), (0, -1), (1, 0), (1, 1),
                    (1, -1), (-1, 0), (-1, 0), (-1, -1)]

        for newPosition in positions:

            # Get Child
            nodePosition = (
                currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

            # Confirm child is in range
            if nodePosition[0] > (len(maze) - 1) or nodePosition[0] < 0 or nodePosition[1] > (len(maze[len(maze) - 1]) - 1) or nodePosition[1] < 0:
                continue

            # Confirm tile is walkable
            if maze[nodePosition[0]][nodePosition[1]] != 0:
                continue

            # Create new Child Node
            newNode = Node(currentNode, nodePosition)
            children.append(newNode)

        # Loop through children
        for child in children:

            # child on closed list
            if closedChild(child, closedList):
                continue

            # Create g, h, f values
            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) **
                       2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g + child.h

            # child on open list
            if openChild(child, openList):
                continue

            # add child to open list
            openList.append(child)

# Function for idenitfying if child is in closed list


def closedChild(child, list):
    for item in list:
        if child == item:
            return True

# Function for identifying if child is on open list


def openChild(child, list):
    for item in list:
        if child == item and child.g > item.g:
            return True


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)

if __name__ == '__main__':
    main()
