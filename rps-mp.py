##This is my version of a multiplayer rock, paper, scissors, game.

#Imports the "random" module. Used to randomly select a value from a list.
import random

#Imports the "getpass" module. Used to hide user input for certain variables.
import getpass

#Establishes a while loop to restart the program.
while True:

    #Prints a welcome message and question for the user to the terminal.
    print('Welcome to the multiplayer version of Rock, Paper, Scissors. You can have up to 3 players total. Would you like to play? ')
    
    #Requests input from the user to start the game.
    start_game = input('Yes or No: ')

    #Defines an if statement that checks for a certain string, after being capitalized with the .capitalize method, input to the variable.
    if start_game.capitalize() == 'Yes':

        #Prints a string to the terminal. Used to aesthetically separate text.
        print('-------------------------------------------')
        
        #Establishes a while loop. Used to restart the game.
        while True:
            print('How many players do you have? ')

            #Defines a variable to contain input from the user. This input will decide the amount of players for the game.
            player_count = input('Number of Players: ')
            
            #Defines an if statement for if the variable contains a '1' string.
            if player_count == '1':
                print('-------------------------------------------')

                #Prints a string that includes the data provided in the "player_count" variable.
                print('You have chosen ' + player_count + ' ' + 'player. Is that correct? ')
                singleplayer_confirm = input('Yes or No: ')

                if singleplayer_confirm.capitalize() == 'Yes':

                    #Establishes a while loop. Used to restart a singleplayer game.
                    while True:

                    #A set of print statements acting as a read out for a real-life game of RPS.
                        print('-------------------------------------------')
                        print('Alright. Time to play Rock, Paper, Scissors.')
                        print('.')
                        print('.')
                        print('.')
                        print('Rock')
                        print('.')
                        print('.')
                        print('.')
                        print('Paper')
                        print('.')
                        print('.')
                        print('.')
                        print('Scissors')
                        print('.')
                        print('.')
                        print('.')
                        print('SHOOT!')
                        print('-------------------------------------------')
                        
                        #Uses the method .choice() provided by the "random" module to choose a random value from the argument and puts the value in the rps_result variable.
                        rps_result = random.choice(['Rock', 'Paper', 'Scissors'])
                        
                        #Prints the data contained in the rps_result variable with a string.
                        print('The result is: ' + rps_result)

                        print('-------------------------------------------')
                        print('Want to play again?')
                        singleplayer_start_again = input('Yes or No: ')

                        if singleplayer_start_again.capitalize() == 'Yes':

                            print('-------------------------------------------')

                            #Skips all other code left in the loop and initiates the loop.
                            continue

                        #Defines an elif statment for if the user, after the data is capitalized, has provided 'No' to the variable.
                        elif singleplayer_start_again.capitalize() == 'No':

                            #Prints a goodbye message to the user.
                            print('Okay. Goodbye')

                            #Breaks the while loop.
                            exit()

                        #Defines an else statement for any other inputs.
                        else:
                            #Prints a message to the user that tells them their input was invalid.
                            print('Invalid input. Try again.')
                            print('-------------------------------------------')
                            continue

                elif singleplayer_confirm.capitalize() == 'No':
                    print('Input the correct player count.')
                    print('-------------------------------------------')
                    continue

                else:
                    print('Invalid input. Try again.')
                    print('-------------------------------------------')
                    continue

            elif player_count == '2':
                print('-------------------------------------------')
                print('You have chosen ' + player_count + ' ' + 'players. Is that correct? ')
                two_player_confirm = input('Yes or No: ')

                if two_player_confirm.capitalize() == 'Yes':
                    
                    #All the print statements and variables defined or executed here are used to let players choose their player name for the game.
                    print('-------------------------------------------')
                    print('Both players will now input what their Player Name should be.')
                    print('-------------------------------------------')

                    print('Player 1, what would you like your name to be?')
                    two_player_player1_name = input('Player 1 Name: ')
                    print(two_player_player1_name + ' ' + 'is the name you have submitted.')

                    print('-------------------------------------------')
                    print('Player 2, what would you like your name to be?')
                    two_player_player2_name = input('Player 2 Name: ')
                    print(two_player_player2_name + ' ' + 'is the name you have submitted.')

                    print('-------------------------------------------')
                    print(two_player_player1_name + ' ' + 'and ' + two_player_player2_name + ' it is time to play Rock, Player, Scissors.')
                    print('-------------------------------------------')

                    print('Neither ' + two_player_player1_name + ' or ' + two_player_player2_name + ' will be able to see your answers until both of you have submitted your choices.')
                    print('-------------------------------------------')

                    #Establishes a while loop. Used to restart a two-player game.
                    while True:
                        print(two_player_player1_name + ' get ready to make your choice. When you are ready, put your answer in below.')
                        print('-------------------------------------------')

                        #These sets of variables will contain the choices of the players and of the program. The player's choices will be hidden to them until after both are submitted.
                        two_player_player1_choice = getpass.getpass(two_player_player1_name + ' choice: ')
                        two_player_player2_choice = getpass.getpass(two_player_player2_name + ' choice: ')
                        two_player_rng_choice = random.choice(['Rock', 'Paper', 'Scissors'])

                        print('-------------------------------------------')
                        print('All the choices have been submitted. Here is what was chosen: ')
                        print(two_player_player1_name + ' chose: ' + two_player_player1_choice)
                        print(two_player_player2_name + ' chose: ' + two_player_player2_choice)
                        print('Finally, the game chose: ' + two_player_rng_choice)
                        print('-------------------------------------------')
                        
                        #Defines these two variables to contain the 0 integer. They will be used for the scoreboard system.
                        two_player_player1_score = 0
                        two_player_player2_score = 0

                        #The following if/elif/else statements are used to check the choices made by the players and the program. 
                        if two_player_player1_choice.capitalize() == 'Rock':
                            if two_player_player1_choice.capitalize() == two_player_rng_choice:
                                print(two_player_player1_name + ' did not win or lose.')

                                #Defines a variable that will be used to display the amount of points each player has.
                                                                    #This may seem useless, however, if it is not done, the program will consider this variable "undefined".
                                two_player_player1_score_points = two_player_player1_score + 0
                                print('0 points have been awarded to ' + two_player_player1_name)
                                print('-------------------------------------------')
                            
                            elif two_player_player1_choice.capitalize() == 'Rock' and two_player_rng_choice == 'Scissors':
                                print('Rock beats scissors.')
                                print(two_player_player1_name + ' has earned a point.')
                                two_player_player1_score_points = int(two_player_player1_score) + 1
                                print('-------------------------------------------')

                            elif two_player_player1_choice.capitalize() == 'Rock' and two_player_rng_choice == 'Scissors':
                                print('Rock beats scissors.')
                                print(two_player_player1_name + ' has earned a point.')
                                two_player_player1_score_points = int(two_player_player1_score) + 1
                                print('-------------------------------------------')
                        
                            elif two_player_player1_choice.capitalize() == 'Rock' and two_player_rng_choice == 'Paper':
                                print('Paper beats rock.')
                                print(two_player_player1_name + ' has lost a point.')
                                two_player_player1_score_points = int(two_player_player1_score) - 1
                                print('-------------------------------------------')
                            else:
                                print('.')

                        elif two_player_player1_choice.capitalize() == 'Paper':
                            if two_player_player1_choice.capitalize() == two_player_rng_choice:
                                print(two_player_player1_name + ' did not win or lose.')
                                two_player_player1_score_points = two_player_player1_score + 0
                                print('0 points have been awarded to ' + two_player_player1_name)
                                print('-------------------------------------------')
                            
                            elif two_player_player1_choice.capitalize() == 'Paper' and two_player_rng_choice == 'Rock':
                                print('Paper beats rock.')
                                print(two_player_player1_name + ' has earned a point.')
                                two_player_player1_score_points = int(two_player_player1_score) + 1
                                print('-------------------------------------------')

                            elif two_player_player1_choice.capitalize() == 'Paper' and two_player_rng_choice == 'Scissors':
                                print('Scissors beats paper.')
                                print(two_player_player1_name + ' has lost a point.')
                                two_player_player1_score_points = int(two_player_player1_score) - 1
                                print('-------------------------------------------')
                            else:
                                print('.')

                        elif two_player_player1_choice.capitalize() == 'Scissors':
                            if two_player_player1_choice.capitalize() == two_player_rng_choice:
                                print(two_player_player1_name + ' did not win or lose.')
                                two_player_player1_score_points = two_player_player1_score + 0
                                print('0 points have been awarded to ' + two_player_player1_name)
                                print('-------------------------------------------')
                            
                            elif two_player_player1_choice.capitalize() == 'Scissors' and two_player_rng_choice == 'Paper':
                                print('Scissors beats paper.')
                                print(two_player_player1_name + ' has earned a point.')
                                two_player_player1_score_points = int(two_player_player1_score) + 1
                                print('-------------------------------------------')

                            elif two_player_player1_choice.capitalize() == 'Scissors' and two_player_rng_choice == 'Rock':
                                print('Scissors beats paper.')
                                print(two_player_player1_name + ' has lost a point.')
                                two_player_player1_score_points = int(two_player_player1_score) - 1
                                print('-------------------------------------------')
                            else:
                                print('.')                        
                        else:
                            print('An invalid input was made. Try again.')
                            print('-------------------------------------------')
                            continue
                            
                        if two_player_player2_choice.capitalize() == 'Rock':
                            if two_player_player2_choice.capitalize() == two_player_rng_choice:
                                print(two_player_player2_name + ' did not win or lose.')
                                two_player_player2_score_points = two_player_player2_score + 0
                                print('0 points have been awarded to ' + two_player_player2_name)
                                print('-------------------------------------------')

                            elif two_player_player2_choice.capitalize() == 'Rock' and two_player_rng_choice == 'Scissors':
                                print('Rock beats scissors.')
                                print(two_player_player2_name + ' has earned a point.')
                                two_player_player2_score_points = int(two_player_player2_score) + 1
                                print('-------------------------------------------')
                            
                            elif two_player_player2_choice.capitalize() == 'Rock' and two_player_rng_choice == 'Paper':
                                print('Paper beats rock.')
                                print(two_player_player2_name + ' has lost a point.')
                                two_player_player2_score_points = int(two_player_player2_score) - 1
                                print('-------------------------------------------')

                        elif two_player_player2_choice.capitalize() == 'Paper':
                            if two_player_player2_choice.capitalize() == two_player_rng_choice:
                                print(two_player_player2_name + ' did not win or lose.')
                                two_player_player2_score_points = two_player_player2_score + 0
                                print('0 points have been awarded to ' + two_player_player2_name)
                                print('-------------------------------------------')
                            
                            elif two_player_player2_choice.capitalize() == 'Paper' and two_player_rng_choice == 'Rock':
                                print('Paper beats rock.')
                                print(two_player_player2_name + ' has earned a point.')
                                two_player_player2_score_points = int(two_player_player2_score) + 1
                                print('-------------------------------------------')
                            
                            elif two_player_player2_choice.capitalize() == 'Paper' and two_player_rng_choice == 'Scissors':
                                print('Scissors beats paper.')
                                print(two_player_player2_name + ' has lost a point.')
                                two_player_player2_score_points = int(two_player_player2_score) - 1
                                print('-------------------------------------------')
                        
                        elif two_player_player2_choice.capitalize() == 'Scissors':
                            if two_player_player2_choice.capitalize() == two_player_rng_choice:
                                print(two_player_player2_name + ' did not win or lose.')
                                two_player_player2_score_points = two_player_player2_score + 0
                                print('0 points have been awarded to ' + two_player_player2_name)
                                print('-------------------------------------------')
                            
                            elif two_player_player2_choice.capitalize() == 'Scissors' and two_player_rng_choice == 'Paper':
                                print('Scissors beats paper.')
                                print(two_player_player2_name + ' has earned a point.')
                                two_player_player2_score_points = int(two_player_player2_score) + 1
                                print('-------------------------------------------')
                            
                            elif two_player_player2_choice.capitalize() == 'Scissors' and two_player_rng_choice == 'Rock':
                                print('Rock beats scissors.')
                                print(two_player_player2_name + ' has lost a point.')
                                two_player_player2_score_points = int(two_player_player2_score) - 1
                                print('-------------------------------------------')
                    else:
                        print('An invalid input was made. Try again.')
                        print('-------------------------------------------')
                        continue

                    #This is a set of print statements to display the scoreboard with the active values in the variables we used for keeping up with the player's scores.
                    print('The results are in:')
                    print('-------------------------------------------')
                                                           #Converts the variable to a string since it currently contains an integer which would cause errors.
                    print(two_player_player1_name + ': ' + str(two_player_player1_score_points))
                    print(two_player_player2_name + ': ' + str(two_player_player2_score_points))
                    print('-------------------------------------------')

                    #Establishes a while loop. Used to either restart the two-player game or terminate the program based on user input.
                    while True:
                        print('Would you like to play again? ')
                        two_player_start_again = input('Yes or No: ')

                        if two_player_start_again.capitalize() == 'Yes':
                            break

                        elif two_player_start_again.capitalize() == 'No':
                            print('Okay. Goodbye')
                            exit()

                        else:
                            print('Invalid input. Try again')
                            continue
                    continue

                if two_player_confirm.capitalize() == 'No':
                    print('Input the correct player count.')
                    print('-------------------------------------------')
                    continue

                else:
                    print('Invalid input was entered. Try again.')
                    print('-------------------------------------------')
                    continue

            elif player_count == '3':
                print('-------------------------------------------')
                print('You have chosen ' + player_count + ' ' + 'players. Is that correct? ')
                three_player_confirm = input('Yes or No: ')

                if three_player_confirm.capitalize() == 'Yes':
                    print('All players will now input what their Player Name should be.')
                    print('-------------------------------------------')

                    print('Player 1, what would you like your name to be?')
                    three_player_player1_name = input('Player 1 Name: ')
                    print(three_player_player1_name + ' ' + 'is the name you have submitted.')
                    print('-------------------------------------------')

                    print('Player 2, what would you like your name to be?')
                    three_player_player2_name = input('Player 2 Name: ')
                    print(three_player_player2_name + ' ' + 'is the name you have submitted.')
                    print('-------------------------------------------')

                    print('Player 3, what would you like your name to be?')
                    three_player_player3_name = input('Player 3 Name: ')
                    print(three_player_player3_name + ' ' + 'is the name you have submitted.')
                    print('-------------------------------------------')

                    print(three_player_player1_name + ', ' + three_player_player2_name + ', and' + three_player_player3_name + ' it is time to play Rock, Player, Scissors.')
                    print('-------------------------------------------')
                    print('None of you will be able to see your answers until all of you have submitted your choices.')
                    print('-------------------------------------------')

                elif three_player_confirm.capitalize() == 'No':
                    print('Input the correct player count.')
                    print('-------------------------------------------')
                    continue

                else:
                    print('Invalid input. Try again.')
                    print('-------------------------------------------')
                    continue
                
                #Establishes a while loop. Used to restart a three-player game.       
                while True:
                    print(three_player_player1_name + ' get ready to make your choice. When you are ready, put your answer in below.')
                    print('-------------------------------------------')

                    three_player_player1_choice = getpass.getpass(three_player_player1_name + ' choice: ')
                    three_player_player2_choice = getpass.getpass(three_player_player2_name + ' choice: ')
                    three_player_player3_choice = getpass.getpass(three_player_player3_name + ' choice: ')
                    three_player_rng_choice = random.choice(['Rock', 'Paper', 'Scissors'])

                    print('-------------------------------------------')
                    print('All the choices have been submitted. Here is what was chosen: ')
                    print(three_player_player1_name + ' chose: ' + three_player_player1_choice)
                    print(three_player_player2_name + ' chose: ' + three_player_player2_choice)
                    print(three_player_player3_name + ' chose: ' + three_player_player3_choice)
                    print('Finally, the game chose: ' + three_player_rng_choice)
                    print('-------------------------------------------')

                    three_player_player1_score = 0
                    three_player_player2_score = 0
                    three_player_player3_score = 0

                    if three_player_player1_choice.capitalize() == 'Rock':
                        if three_player_player1_choice.capitalize() == three_player_rng_choice:
                            print(three_player_player1_name + ' did not win or lose.')
                            print('0 points have been awarded to ' + three_player_player1_name)
                            three_player_player1_score_points = three_player_player1_score + 0
                            print('-------------------------------------------')
                            
                        elif three_player_player1_choice.capitalize() == 'Rock' and three_player_rng_choice == 'Scissors':
                            print('Rock beats scissors.')
                            print(three_player_player1_name + ' has earned a point.')
                            three_player_player1_score_points = int(three_player_player1_score) + 1
                            print('-------------------------------------------')

                        elif three_player_player1_choice.capitalize() == 'Rock' and three_player_rng_choice == 'Paper':
                            print('Paper beats rock.')
                            print(three_player_player1_name + ' has lost a point.')
                            three_player_player1_score_points = int(three_player_player1_score) - 1
                            print('-------------------------------------------')

                    elif three_player_player1_choice.capitalize() == 'Paper':
                        if three_player_player1_choice.capitalize() == three_player_rng_choice:
                            print(three_player_player1_name + ' did not win or lose.')
                            print('0 points have been awarded to ' + three_player_player1_name)
                            three_player_player_score_points = three_player_player1_score + 0
                            print('-------------------------------------------')
                        
                        elif three_player_player1_choice.capitalize() == 'Paper' and three_player_rng_choice == 'Rock':
                            print('Paper beats rock.')
                            print(three_player_player1_name + ' has earned a point.')
                            three_player_player1_score_points = int(three_player_player1_score) + 1
                            print('-------------------------------------------')
                        
                        elif three_player_player1_choice.capitalize() == 'Paper' and three_player_rng_choice == 'Scissors':
                            print('Scissors beats paper.')
                            print(three_player_player1_name + ' has lost a point.')
                            three_player_player1_score_points = int(three_player_player1_score) - 1
                            print('-------------------------------------------')

                    elif three_player_player1_choice.capitalize() == 'Scissors':
                        if three_player_player1_choice.capitalize() == three_player_rng_choice:
                            print(three_player_player1_name + ' did not win or lose.')
                            print('0 points have been awarded to ' + three_player_player1_name)
                            three_player_player1_score_points = three_player_player1_score + 0
                            print('-------------------------------------------')
                        
                        elif three_player_player1_choice.capitalize() == 'Scissors' and three_player_rng_choice == 'Paper':
                            print('Scissors beats paper.')
                            print(three_player_player1_name + ' has earned a point.')
                            three_player_player1_score_points = int(three_player_player1_score) + 1
                            print('-------------------------------------------')
                        
                        elif three_player_player1_choice.capitalize() == 'Scissors' and three_player_rng_choice == 'Rock':
                            print('Scissors beats paper.')
                            print(three_player_player1_name + ' has lost a point.')
                            three_player_player1_score_points = int(three_player_player1_score) - 1
                            print('-------------------------------------------')
                    else:
                        print('An invalid input was made. Try again.')
                        print('-------------------------------------------')
                        continue

                    if three_player_player2_choice.capitalize() == 'Rock':
                        if three_player_player2_choice.capitalize() == three_player_rng_choice:
                            print(three_player_player2_name + ' did not win or lose.')
                            print('0 points have been awarded to ' + three_player_player2_name)
                            three_player_player2_score_points = three_player_player2_score + 0
                            print('-------------------------------------------')

                        elif three_player_player2_choice.capitalize() == 'Rock' and three_player_rng_choice == 'Scissors':
                            print('Rock beats scissors.')
                            print(three_player_player2_name + ' has earned a point.')
                            three_player_player2_score_points = int(three_player_player2_score) + 1
                            print('-------------------------------------------')
                        
                        elif three_player_player2_choice.capitalize() == 'Rock' and three_player_rng_choice == 'Paper':
                                print('Paper beats rock.')
                                print(three_player_player2_name + ' has lost a point.')
                                three_player_player2_score_points = int(three_player_player2_score) - 1
                                print('-------------------------------------------')
                    
                    elif three_player_player2_choice.capitalize() == 'Paper':
                        if three_player_player2_choice.capitalize() == three_player_rng_choice:
                            print(three_player_player2_name + ' did not win or lose.')
                            print('0 points have been awarded to ' + three_player_player2_name)
                            three_player_player2_score_points = three_player_player2_score + 0
                            print('-------------------------------------------')
                        
                        elif three_player_player2_choice.capitalize() == 'Paper' and three_player_rng_choice == 'Rock':
                            print('Paper beats rock.')
                            print(three_player_player2_name + ' has earned a point.')
                            three_player_player2_score_points = int(three_player_player2_score) + 1
                            print('-------------------------------------------')
                        
                        elif three_player_player2_choice.capitalize() == 'Paper' and three_player_rng_choice == 'Scissors':
                            print('Scissors beats paper.')
                            print(three_player_player3_name + ' has lost a point.')
                            three_player_player3_score_points = int(three_player_player3_score) - 1
                            print('-------------------------------------------')
                    
                    elif three_player_player2_choice.capitalize() == 'Scissors':
                        if three_player_player2_choice.capitalize() == three_player_rng_choice:
                            print(three_player_player2_name + ' did not win or lose.')
                            print('0 points have been awarded to ' + three_player_player2_name)
                            three_player_player2_score_points = three_player_player2_score + 0
                            print('-------------------------------------------')

                        elif three_player_player2_choice.capitalize() == 'Scissors' and three_player_rng_choice == 'Paper':
                            print('Scissors beats paper.')
                            print(three_player_player2_name + ' has earned a point.')
                            three_player_player2_score_points = int(three_player_player2_score) + 1
                            print('-------------------------------------------')

                        elif three_player_player2_choice.capitalize() == 'Scissors' and three_player_rng_choice == 'Rock':
                            print('Rock beats scissors.')
                            print(three_player_player2_name + ' has lost a point.')
                            three_player_player2_score_points = int(three_player_player2_score) - 1
                            print('-------------------------------------------')
                    else:
                        print('An invalid input was made. Try again.')
                        print('-------------------------------------------')
                        continue
                    
                    if three_player_player3_choice.capitalize() == 'Rock':
                        if three_player_player3_choice.capitalize() == three_player_rng_choice:
                            print(three_player_player3_name + ' did not win or lose.')
                            print('0 points have been awarded to ' + three_player_player3_name)
                            three_player_player3_score_points = three_player_player3_score + 0
                            print('-------------------------------------------')

                        elif three_player_player3_choice.capitalize() == 'Rock' and three_player_rng_choice == 'Scissors':
                            print('Rock beats scissors.')
                            print(three_player_player3_name + ' has earned a point.')
                            three_player_player3_score_points = int(three_player_player3_score) + 1
                            print('-------------------------------------------')

                        elif three_player_player3_choice.capitalize() == 'Rock' and three_player_rng_choice == 'Paper':
                                print('Paper beats rock.')
                                print(three_player_player3_name + ' has lost a point.')
                                three_player_player3_score_points = int(three_player_player3_score) - 1
                                print('-------------------------------------------')

                    elif three_player_player3_choice.capitalize() == 'Paper':
                        if three_player_player3_choice.capitalize() == three_player_rng_choice:
                            print(three_player_player3_name + ' did not win or lose.')
                            print('0 points have been awarded to ' + three_player_player3_name)
                            three_player_player3_score_points = three_player_player3_score + 0
                            print('-------------------------------------------')
                        
                        elif three_player_player3_choice.capitalize() == 'Paper' and three_player_rng_choice == 'Rock':
                            print('Paper beats rock.')
                            print(three_player_player3_name + ' has earned a point.')
                            three_player_player3_score_points = int(three_player_player3_score) + 1
                            print('-------------------------------------------')
                        
                        elif three_player_player3_choice.capitalize() == 'Paper' and three_player_rng_choice == 'Scissors':
                            print('Scissors beats paper.')
                            print(three_player_player3_name + ' has lost a point.')
                            three_player_player3_score_points = int(three_player_player3_score) - 1
                            print('-------------------------------------------')
                    
                    elif three_player_player3_choice.capitalize() == 'Scissors':
                        if three_player_player3_choice.capitalize() == three_player_rng_choice:
                            print(three_player_player3_name + ' did not win or lose.')
                            print('0 points have been awarded to ' + three_player_player3_name)
                            three_player_player3_score_points = three_player_player3_score + 0
                            print('-------------------------------------------')
                        
                        elif three_player_player3_choice.capitalize() == 'Scissors' and three_player_rng_choice == 'Paper':
                            print('Scissors beats paper.')
                            print(three_player_player3_name + ' has earned a point.')
                            three_player_player3_score_points = int(three_player_player3_score) + 1
                            print('-------------------------------------------')
                        
                        elif three_player_player3_choice.capitalize() == 'Scissors' and three_player_rng_choice == 'Rock':
                            print('Rock beats scissors.')
                            print(three_player_player3_name + ' has lost a point.')
                            three_player_player3_score_points = int(three_player_player3_score) - 1
                            print('-------------------------------------------')
                    else:
                        print('An invalid input was made. Try again.')
                        print('-------------------------------------------')
                        continue

                    print(three_player_player1_name + ': ' + str(three_player_player1_score_points))
                    print(three_player_player2_name + ': ' + str(three_player_player2_score_points))
                    print(three_player_player3_name + ': ' + str(three_player_player3_score_points))

                    while True:
                        print('Would you like to play again? ')
                        three_player_start_again = input('Yes or No: ')

                        if three_player_start_again.capitalize() == 'Yes':
                            break

                        elif three_player_start_again.capitalize() == 'No':
                            print('Okay. Goodbye')
                            exit()

                        else:
                            print('Invalid input. Try again')
                            print('-------------------------------------------')
                            continue 
                    continue           
            else:
                print('Make sure to enter a maximum of 3 total players.')
                print('-------------------------------------------')
                continue

    elif start_game.capitalize() == 'No':
        print('Okay. Goodbye now.')
        
        #Stops executing the current while loop and moves on to any code left outside of that loop.
        break

    else:
        print('Invalid input. Try again.')
        print('-------------------------------------------')
        continue