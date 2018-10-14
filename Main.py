"""
Authors: George Engel, Cory Johns, Justin Keeling 
"""

running = True
output_file = open('output.txt', 'w+')


def read_in_maze(string):
    global running

    def __build_maze(file):
        """
        Builds a 2D array from the input file
        :param file: containing the board in text form
        """
        nonlocal maze_xy
        # open file, make a 2d list of each letter
        # with covers try-catch business, '__' prefix is 'private' sort of
        with open(file) as __f:
            for __line in __f:
                # build up a row, then add it to the maze
                __x_tmp = []
                for __char in __line:
                    # don't add newline chars
                    if __char != '\n':
                        __x_tmp.append(__char)
                maze_xy.append(__x_tmp)
        # convert into nodes
        return

    # the maze will go here, overwrites for each run
    maze_xy = []

    # maze txt files must be in the same directory with the given names
    if string == '5':
        __build_maze("assignment-resources/5x5maze.txt")
    elif string == '7':
        __build_maze("assignment-resources/7x7maze.txt")
    elif string == '8':
        __build_maze("assignment-resources/8x8maze.txt")
    elif string == '9':
        __build_maze("assignment-resources/9x9maze.txt")
    elif string == '10':
        __build_maze("assignment-resources/10x10maze.txt")
    elif string == '12':
        __build_maze("assignment-resources/12x12maze.txt")
    elif string == '14':
        __build_maze("assignment-resources/14x14maze.txt")
    else:
        print("Maze not found")


    print(maze_xy)


input_list = ["5", "7", "8", "9", "10", "12", "14"]
index = 0
while running:
    # inp = "" + input("Enter the maze type you would like to run, Enter N where N is the size of the maze or Enter Q to quit: ")
    print("Automatic running enabled: ", input_list[index])
    inp = input_list[index]

    read_in_maze(inp)

    index += 1

output_file.close()
