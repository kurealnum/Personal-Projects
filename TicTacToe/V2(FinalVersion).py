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
winner = ""
class main:



        #takes args won, easy, and board size. won and easy are bools, and board_size should be a number between 3 and 10 (it gets messy once you get past that) 
        def __init__(self, won: bool, easy: bool, board_size: int, player: str, bot: str) -> None:
            #won stays false until someone wins
            self.won = won
            #easy will be used in the future to determine the bot difficulty
            self.easy = easy
            #a board size of 3 would make a 3x3 board
            self.board_size = board_size
            #player and bot is any 2 symbols to represent the player and the bot on the board; strings of course.
            self.player = player
            self.bot = bot
            #the numbers that go across the top (row)
            self.horizontal_list = [i+1 for i in range(self.board_size)]
            #the numbers that go down the side (column)
            self.vertical_list = [chr(i+65) for i in range(self.board_size)]
            #number of X's/O's needed to win, used primarily in check_for_win
            #turned into a string on variable declaration for ease of use
            self.x_winning_score = ''.join(["X" for i in range(len(self.horizontal_list))])
            self.o_winning_score = ''.join(["O" for i in range(len(self.horizontal_list))])
            #the board map itself
            self.board_map = [["." for i in range(len(self.horizontal_list))]for j in range(len(self.vertical_list))]


            
        #prints the board
        def print_board(self):
            print("", end='   ')
            for horiz_count in range(len(self.horizontal_list)):
                print(self.horizontal_list[horiz_count], end=' ')

            print("")
            for vert_count in range(len(self.vertical_list)):
                print(self.vertical_list[vert_count], end=' |')

                for i in range(len(self.board_map)):
                    print(self.board_map[vert_count][i], end='|')

                print("")



        def check_for_win(self):
            #check if this section of the list is just periods
            for i in range(len(self.horizontal_list)):
                temp_list = []
                possible_winner_list = []
                temp_str = ''.join(self.board_map[i])
                if self.player or self.bot in temp_str:
                    pass
                else:
                    continue
                
                #this part of the loop actually checks the vertical part of the list for matches,
                #not the horizontal. idk why I did it that way, makes more sense to me though
                #should be the same value either way 
                for h in range(len(self.horizontal_list)):
                    temp_list.append(self.board_map[h][i])

                if ''.join(temp_list) == self.x_winning_score:
                    possible_winner_list.append(self.player)
                
                if ''.join(temp_list) == self.o_winning_score:
                    possible_winner_list.append(self.bot)
                

            #checks for horizontal wins
            for j in range(len(self.vertical_list)):
                    if ''.join(self.board_map[j]) == self.x_winning_score:
                        possible_winner_list.append(self.player)

                    if ''.join(self.board_map[j]) == self.o_winning_score:
                        possible_winner_list.append(self.bot)    

            #physically long asf list, but it's just two values, those being each diagonal
            diag_solutions_list = [self.board_map[0][0] + self.board_map[1][1] + self.board_map[2][2], self.board_map[0][2] + self.board_map[1][1] + self.board_map[2][0]]

            for k in range(len(diag_solutions_list)):
                if diag_solutions_list[k] == self.x_winning_score:
                    possible_winner_list.append(self.player)

                if diag_solutions_list[k] == self.o_winning_score:
                    possible_winner_list.append(self.bot)


            try:
                if len(possible_winner_list) > 1:
                    return (True, "Tie")

                elif ''.join(possible_winner_list) == self.player:
                    return (True, self.player)

                elif ''.join(possible_winner_list) == self.bot:
                    return (True, self.bot)

            except:
                return (False, "")

            #ok don't forget to add this to default to if no conditions are met you've done this twice today
            return (False, "")
                


        def easy_robots_turn(self):
            #we have 0 and 0 in here because we need to pick an random even number later on
            easy_temp_list = []

            for i in range(len(self.horizontal_list)):
                for j in range(len(self.vertical_list)):
                    if self.player in self.board_map[i][j] or self.bot in self.board_map[i][j]:
                        continue
                    else:
                        easy_temp_list.append(i),easy_temp_list.append(j)

            #yes, we have to do some pretty funky stuff with the random function to make it work
            even_random_number = random.randint(0,(len(easy_temp_list))/2)*2
            
            try:
                self.board_map[easy_temp_list[even_random_number]][easy_temp_list[even_random_number+1]] = self.bot
            
            except:
                self.board_map[easy_temp_list[even_random_number-2]][easy_temp_list[even_random_number-1]] = self.bot

            print("The easy robot just took its turn! Let's see what the board looks like now.\n")



        def hard_robots_turn(self):
            #maybe one day in the future this will practically be an AI that plays tic tac toe
            #i'm too stupid as of 12/22/22 to do it tho so :shrug:
            pass



        def main_process(self):

            print("")
            mn.print_board()
            print(f"\nHere's your starting board. You can call a position by saying \"A1\", or \"B3\".\nYour tac will be placed in that location. You are X, and your goal is to get {len(mn.horizontal_list)} X's in a row.\n")

            while self.won != True:
                user_input = input("\nEnter a location on the grid that exists (A1, B2, C3, ect.): ")

                #try to index the list, and if that doesn't work, throw an error and prompt the user again
                try:
                    letter_index_num = ord(user_input[0].upper()) - 65
                    num_index_num = int(user_input[1]) - 1
                    #we use this to be able to turn the first letter of the users input into a number that we can index the list with
                    if self.board_map[letter_index_num][num_index_num] == self.player or self.board_map[letter_index_num][num_index_num] == self.bot:
                        print("You entered a tac where one already exists!")
                        continue
                    #actually placing the "tac"
                    self.board_map[letter_index_num][num_index_num] = self.player        
                    print("")

                except:
                    print("You entered the wrong type of input.\nRemember, it must be a capital letter, then a number.\n")
                    continue
                if self.easy == True:
                    mn.easy_robots_turn()
                else:
                    mn.hard_robots_turn()

                print("Here's the current board!\n")
                mn.print_board()
                print("")
               
                #here's where we change the winner and won variable, using the check_for_win func
                self.won, winner = mn.check_for_win()

                #check if anyone won
                if self.won == True:
                    if winner == "Tie":
                        print("You tied with the bot!\n")
                        input("Enter any key to quit")
                    elif winner == self.player:
                        print(f"{self.player} won!\n(That means you!)\n")
                        input("Enter any key to quit")
                    elif winner == self.bot:
                        print(f"{self.bot} won!\n(You lost)\n")
                        input("Enter any key to quit")



mn = main(False, True, 3, "X", "O")   
mn.main_process()
