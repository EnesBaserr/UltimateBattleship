
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    p1placing = True
    #to control the placement phase loop for player 1
    p2placing = False
    ##to control the placement phase loop for player 2
    p1shooting = False
    occu = False
    #to control the placement loop in case error
    occu2= False
    #to control the placement loop in case error

    lst_1=[['-'for i in range(board_size)] for j in range(board_size)]
    lst_2 = [['-'for i in range(board_size)] for j in range(board_size)]
    my_list = [lst_1, lst_2]
    #board for placement of player 1
    lst_3 = [['-' for i in range(board_size)] for j in range(board_size)]
    lst_4 = [['-'for i in range(board_size)] for j in range(board_size)]

    my_list2 = [lst_3, lst_4]
    #board for placement of player 2

    ship_list = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    shiplist2 = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    #list of ship names for both loops.

    ship_size = {'carrier': 5, 'battleship': 4, 'cruiser': 3, 'submarine': 3, 'destroyer': 2}
    #to determine the length of ships.
    frag = True
    #to iterate main loop.
    while frag:
        if p1placing:
            print_3d_list(my_list)
            print_ships_to_be_placed()

            for shipss in ship_list:
                print_single_element(shipss)
            print_empty_line()
            print_player_turn_to_place(1)
            print_to_place_ships()

            input_list = input().split()
            shipname = input_list[0].capitalize()
            if len(input_list) < 4:
                print_incorrect_input_format()


            elif not input_list[1].isdecimal() or not input_list[
                2].isdecimal():
                print_incorrect_input_format()
            elif int(input_list[1]) > 10 or int(input_list[2]) > 10 or int(input_list[1]) < 1:
                print_incorrect_coordinates()
            elif shipname.lower() not in ship_size.keys():
                print_incorrect_ship_name()

            elif input_list[3].lower() != 'h' and input_list[3].lower() != 'v':
                print_incorrect_orientation()
            elif shipname not in ship_list:
                print_ship_is_already_placed(shipname)
            elif (input_list[3].lower() == 'h') and (int(input_list[1]) + ship_size[input_list[0].lower()] > 11):
                print_ship_cannot_be_placed_outside(input_list[0].capitalize())
            elif (input_list[3].lower() == 'v') and (int(input_list[2]) + ship_size[input_list[0].lower()] > 11):
                print_ship_cannot_be_placed_outside(input_list[0].capitalize())
            else:
                for i in range(ship_size[input_list[0].lower()]):
                    if input_list[3].lower() == 'h':
                        if my_list[0][int(input_list[2]) - 1][int(input_list[1]) - 1 + i] == '#':
                            occu = True
                            break
                            #to break for loop and continue with occupied place error
                    if input_list[3].lower() == 'v':
                        if my_list[0][int(input_list[2]) - 1 + i][int(input_list[1]) - 1] == '#':
                            occu = True
                            break
                            #to break for loop and continue with occupied place error
                if occu:
                    print_ship_cannot_be_placed_occupied(input_list[0].capitalize())
                    occu = False
                    continue
                    #return input loop.
                else:
                    for i in range(ship_size[input_list[0].lower()]):
                        if input_list[3].lower() == 'h':
                            my_list[0][int(input_list[2]) - 1][int(input_list[1]) - 1 + i] = '#'
                        if input_list[3].lower() == 'v':
                            my_list[0][int(input_list[2]) - 1 + i][int(input_list[1]) - 1] = '#'
                ship_list.remove(shipname)
                # reduce ship names to be placed step by step
                if len(ship_list) == 0:
                    a = ""
                    print_3d_list(my_list)
                    while a.lower() != 'y' and a.lower() != 'n':
                        print_confirm_placement()
                        a = input()
                        if a.lower() == 'y':
                            p1placing = False
                            p2placing = True
                            # to continue with second placement phase.
                        elif a.lower() == 'n':
                            ship_list = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
                            lst_1 = [['-' for i in range(board_size)] for j in range(board_size)]
                            lst_2 = [['-' for i in range(board_size)] for j in range(board_size)]
                            my_list = [lst_1, lst_2]
                            #to clear board for player 1 in case not confirming the placement.
        if p2placing:
            print_3d_list(my_list2)
            print_ships_to_be_placed()

            for shipss in shiplist2:
                print_single_element(shipss)
            print_empty_line()
            print_player_turn_to_place(2)
            print_to_place_ships()

            input_list = input().split()
            shipname = input_list[0].capitalize()
            if len(input_list) < 4:
                print_incorrect_input_format()

            elif not input_list[1].isdecimal() or not input_list[
                2].isdecimal():  # or input_list[1]!="10"and input_list[2]!='10':
                print_incorrect_input_format()
            elif int(input_list[1]) > 10 or int(input_list[2]) > 10 or int(input_list[1]) < 1:
                print_incorrect_coordinates()
            elif shipname.lower() not in ship_size.keys():
                print_incorrect_ship_name()

            elif input_list[3].lower() != 'h' and input_list[3].lower() != 'v':
                print_incorrect_orientation()
            elif shipname not in shiplist2:
                print_ship_is_already_placed(shipname)
            elif (input_list[3].lower() == 'h') and (int(input_list[1]) + ship_size[input_list[0].lower()] > 11):
                print_ship_cannot_be_placed_outside(input_list[0].capitalize())
            elif (input_list[3].lower() == 'v') and (int(input_list[2]) + ship_size[input_list[0].lower()] > 11):
                print_ship_cannot_be_placed_outside(input_list[0].capitalize())
            else:
                for i in range(ship_size[input_list[0].lower()]):
                    if input_list[3].lower() == 'h':
                        if my_list2[1][int(input_list[2]) - 1][int(input_list[1]) - 1 + i] == '#':
                            occu = True
                            break
                            # to break for loop and continue with occupied place error
                    if input_list[3].lower() == 'v':
                        if my_list2[1][int(input_list[2]) - 1 + i][int(input_list[1]) - 1] == '#':
                            occu = True
                            break
                            # to break for loop and continue with occupied place error
                if occu:
                    print_ship_cannot_be_placed_occupied(input_list[0].capitalize())
                    occu = False
                    continue
                    # return input loop.
                else:
                    for i in range(ship_size[input_list[0].lower()]):
                        if input_list[3].lower() == 'h':
                            my_list2[1][int(input_list[2]) - 1][int(input_list[1]) - 1 + i] = '#'

                        if input_list[3].lower() == 'v':
                            my_list2[1][int(input_list[2]) - 1 + i][int(input_list[1]) - 1] = '#'
                    shiplist2.remove(shipname)
                    # reduce ship names to be placed step by step
                if len(shiplist2) == 0:
                    a = ""
                    print_3d_list(my_list2)
                    while a.lower() != 'y' and a.lower() != 'n':
                        print_confirm_placement()
                        a = input()
                        if a.lower() == 'y':
                            p2placing = False
                            p1shooting = True
                            #to continue with shooting phase.
                            frag = False
                            #to break main loop.

                        elif a.lower() == 'n':
                            shiplist2 = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
                            lst_3 = [['-' for i in range(board_size)] for j in range(board_size)]
                            lst_4 = [['-' for i in range(board_size)] for j in range(board_size)]
                            my_list2 = [lst_3, lst_4]



    frag2 = True
    p2shooting=False
    count2 = 0
    count1 = 0
    #counters to determine who the winner is.


    while frag2:
        if p1shooting:
            print_3d_list(my_list)
            print_player_turn_to_strike(1)
            print_choose_target_coordinates()
            input_strike=input().split()

            if len(input_strike) < 2:
                print_incorrect_input_format()
                continue
            elif not input_strike[0].isdecimal() or not input_strike[1].isdecimal():
                print_incorrect_input_format()
                continue
            elif int(input_strike[0])>10 or int(input_strike[1])>10 or int(input_strike[0])<0 or int(input_strike[1])<0:
                print_incorrect_coordinates()
            elif my_list2[1][int(input_strike[1]) - 1][int(input_strike[0]) - 1] == '!':
                print_tile_already_struck()
            elif my_list2[1][int(input_strike[1]) - 1][int(input_strike[0]) - 1] == 'O':
                print_tile_already_struck()
            else:

                if my_list2[1][int(input_strike[1])-1][int(input_strike[0])-1] == '#':
                    print_hit()
                    my_list[1][int(input_strike[1])-1][int(input_strike[0])-1] = '!'
                    my_list2[1][int(input_strike[1]) - 1][int(input_strike[0]) - 1] = '!'
                    count1 = count1 + 1
                    if count1 == 17:
                        print_3d_list(my_list)
                        print_player_won(1)
                        frag2 = False
                        #to finish the game.
                else:
                    my_list[1][int(input_strike[1]) - 1][int(input_strike[0]) - 1] = 'O'
                    my_list2[1][int(input_strike[1]) - 1][int(input_strike[0]) - 1] = 'O'
                    print_miss()
                    minflag=True
                    while minflag :
                        print_type_done_to_yield(2)
                        b=input()
                        if b.lower()=='done':
                            minflag=False
                            #to iterate input loop.
                        else:
                            continue

                    p2shooting=True
                    p1shooting=False
                    #continue with second shooting phase.

        if p2shooting:
            print_3d_list(my_list2)
            print_player_turn_to_strike(2)
            print_choose_target_coordinates()
            input_strike = input().split()

            if len(input_strike) < 2:
                print_incorrect_input_format()
                continue
            elif not input_strike[0].isdecimal() or not input_strike[1].isdecimal():
                print_incorrect_input_format()
                continue
            elif int(input_strike[0]) > 10 or int(input_strike[1]) > 10 or int(input_strike[0]) < 0 or int(
                    input_strike[1]) < 0:
                print_incorrect_coordinates()
            elif my_list[0][int(input_strike[1]) - 1][int(input_strike[0]) - 1] == '!':
                print_tile_already_struck()
            elif my_list[0][int(input_strike[1]) - 1][int(input_strike[0]) - 1] == 'O':
                print_tile_already_struck()
            else:
                if my_list[0][int(input_strike[1]) - 1][int(input_strike[0]) - 1] == '#':
                    print_hit()
                    my_list2[0][int(input_strike[1]) - 1][int(input_strike[0]) - 1] = '!'
                    my_list[0][int(input_strike[1]) - 1][int(input_strike[0]) - 1] = '!'
                    count2 = count2 + 1
                    if count2 == 17:
                        print_3d_list(my_list2)
                        print_player_won(2)
                        frag2 = False
                else:
                    my_list2[0][int(input_strike[1]) - 1][int(input_strike[0]) - 1] = 'O'
                    my_list[0][int(input_strike[1]) - 1][int(input_strike[0]) - 1] = 'O'
                    print_miss()
                    minflag = True
                    while minflag:
                        print_type_done_to_yield(1)
                        b = input()
                        if b.lower() == 'done':
                            minflag = False
                        else:
                            continue
                    p2shooting = False
                    p1shooting = True

    print_thanks_for_playing()
















































































































# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()