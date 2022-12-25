import random
'''
Board should look something like this:

    1   2   3       each one of these is tabbed out
A | 0 | 0 | 0 |

B | 0 | 0 | 0 |

C | 0 | 0 | 0 |     space between each of these (not a tab)

Have a default print every time you print the board (that being the 1-3 and the A-C)
Then go through and print where the x's and o'x need to go
Also change the 0 out for something else
'''
won = False
easy = True
winner = ""
horizontal_list = ["1", "2", "3"] 
vertical_list = ["A", "B", "C"]
board_map = [["." for i in range(len(horizontal_list))]for j in range(len(vertical_list))]
#could potentially ask the user for size of the board and populate the list as prompted

print("")

#print the current state of the board
def print_board():
    print("", end='   ')
    for horiz_count in range(len(horizontal_list)):
        print(horizontal_list[horiz_count], end=' ')

    print("")
    for vert_count in range(len(vertical_list)):
        print(vertical_list[vert_count], end=' |')

        for i in range(len(board_map)):
            print(board_map[vert_count][i], end='|')

        print("")


def check_for_win():
    #check if this section of the list is just periods
    for i in range(len(horizontal_list)):
        temp_list = []
        temp_str = ''.join(board_map[i])
        if "X" or "O" in temp_str:
            pass
        else:
            continue
        
        #this part of the loop actually checks the vertical part of the list for matches,
        #not the horizontal. idk why I did it that way, makes more sense to me though
        #should be the same value either way 
        for h in range(len(horizontal_list)):
            temp_list.append(board_map[h][i])

        if ''.join(temp_list) == "XXX":
            return (True, "X")
        
        elif ''.join(temp_list) == "OOO":
            return (True, "O")

    #checks for horizontal wins
    for j in range(len(vertical_list)):
            if ''.join(board_map[j]) == "XXX":
                return (True, "X")

            elif ''.join(board_map[j]) == "OOO":
                return (True, "O")    

    #physically long asf list, but it's just two values, those being each diagonal
    diag_solutions_list = [board_map[0][0] + board_map[1][1] + board_map[2][2], board_map[0][2] + board_map[1][1] + board_map[2][0]]

    for k in range(len(diag_solutions_list)):
        if diag_solutions_list[k] == "XXX":
            return (True, "X")

        elif diag_solutions_list[k] == "OOO":
            return (False, "O")

    return (False, "")


#looks at every open spot and places an O at random
def easy_robots_turn():
    #we have 0 and 0 in here because we need to pick an random even number later on
    easy_temp_list = [0,0]

    for i in range(len(horizontal_list)):
        for j in range(len(vertical_list)):
            if "X" in board_map[i][j] or "O" in board_map[i][j]:
                continue
            else:
                easy_temp_list.append(i),easy_temp_list.append(j)

    #yes, we have to do some pretty funky stuff with the random function to make it work
    even_random_number = random.randint(1,(len(easy_temp_list))/2)*2
    
    try:
        board_map[easy_temp_list[even_random_number]][easy_temp_list[even_random_number+1]] = "O"
    
    except:
        board_map[easy_temp_list[even_random_number-2]][easy_temp_list[even_random_number-1]] = "O"

    print("The easy robot just took its turn! Let's see what the board looks like now.\n")
     

#puts an O where it is most needed; if there's only one x on the board, it puts it next to it
#if there's multiple, find the most needed. that means if there's a hole in the middle of 2 x's
#or if there's 2 x's right next to eachother
def hard_robots_turn():
    #check for all possible places, then check for optimal ones
    hard_temp_list = []

    #all valid spots to place an O
    for i in range(len(horizontal_list)):
        for j in range(len(vertical_list)):
            if "X" in board_map[i][j] or "O" in board_map[i][j]:
                continue
            else:
                hard_temp_list.append(i),hard_temp_list.append(j)


print_board()
print("\nHere's your starting board. You can call a position by saying \"A1\", or \"B3\".\nYour tac will be placed in that location. You are X, and your goal is to get 3 X's in a row.\n")

#main process
while won != True:
    user_input = input("\nEnter a location on the grid that exists (A1, B2, C3, ect.): ")

    #try to index the list, and if that doesn't work, throw an error and prompt the user again
    try:
        letter_index_num = ord(user_input[0].upper()) - 65
        num_index_num = int(user_input[1]) - 1
        #we use this to be able to turn the first letter of the users input into a number that we can index the list with
        if board_map[letter_index_num][num_index_num] == "X" or board_map[letter_index_num][num_index_num] == "O":
            print("You entered a tac where one already exists!")
            continue

        #actually placing the "tac"
        board_map[letter_index_num][num_index_num] = "X"        

        print("")

    except:
        print("You entered the wrong type of input.\nRemember, it must be a capital letter, then a number.\n")
        continue

    if easy == True:
        easy_robots_turn()
    else:
        hard_robots_turn()

    print("Here's the current board!\n")
    print_board()
    print("")

    won, winner = check_for_win()
    if won == True:
        if winner == "X":
            print("X won!\n(That means you!)\n")
            break
        elif winner == "O":
            print("O won!\n(You lost)\n")

    
    


        
