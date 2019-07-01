
"""guess.py: This initiates the word guess game.
@ author: Harmeet Singh
@ ID: 40053592
"""

from stringDatabase import StringDatabase
from game import Game

#Guess class is responsible for maintaining gameplay session record.
"""Guess class is responsible for maintaining gameplay session record."""
class Guess:

    database = StringDatabase()
    noOfPlays = []

    """Function responsible for starting game session."""
    def start_game(self):
        flag = 1
        num_of_game = 1
        print('** The great guessing game **')
        print('')
        while flag and num_of_game<=100:
            gamePlayed = Game()
            gamePlayed.select_word()

            print()
            currentGuess = '____'
            choiceInput = ''
            ptr = 1

            gamePlayed.word = gamePlayed.word
            while ptr:
                print('Your Current Guess : ', currentGuess)
                print()
                print('g = guess, t = tell me, l for a letter, and q to quit')
                choiceInput = input()
                if choiceInput=='q' or choiceInput=='Q':
                    ptr = 0
                    flag = 0
                    gamePlayed.status = 'Gave Up'
                    self.noOfPlays.append(gamePlayed)
                elif choiceInput =='t' or choiceInput == 'T':

                    gamePlayed.evaluate_negative_score(gamePlayed, currentGuess)
                    ptr = 0
                    gamePlayed.status = 'Gave Up'
                    self.noOfPlays.append(gamePlayed)
                    print('The correct word is : ', gamePlayed.word)
                    print()
                elif choiceInput=='g' or choiceInput=='G':
                    userGuess = input('Enter your Guess: ')
                    if userGuess == gamePlayed.word:
                        ptr = 0
                        gamePlayed.score_evaluation(gamePlayed, currentGuess)
                        gamePlayed.status = 'Success'
                        self.noOfPlays.append(gamePlayed)
                        print('Wow! You got it right : ', gamePlayed.word)
                        print()
                    else:
                        ptr = 1
                        gamePlayed.badGuess += 1
                        print('Sorry! Your guess is incorrect.Try again!.')
                        print()
                elif choiceInput=='l' or choiceInput=='L':
                    gamePlayed.numOfRounds += 1
                    userLetter = input('Enter a letter: ')
                    if gamePlayed.word.count(userLetter)>0:
                        count = gamePlayed.word.count(userLetter)
                        print('Well.. you got', count, ' letters')
                        print()
                        tempString = ''
                        for i in range(len(gamePlayed.word)):
                            if gamePlayed.word[i] == userLetter:
                                tempString += userLetter
                            else:
                                tempString += currentGuess[i]
                        currentGuess = tempString
                        if currentGuess == gamePlayed.word:
                            ptr = 0
                            gamePlayed.score_evaluation(gamePlayed, currentGuess)
                            gamePlayed.status = 'Success'
                            self.noOfPlays.append(gamePlayed)
                            print('Great!You guessed it right. Word is : ', gamePlayed.word)
                            print()
                    else:
                        gamePlayed.missedLetters += 1
                        print('No such letter found. Please try again!!!')
                        print()
                else:
                    print('Incorrect input!! Re-enter choice from the  menu.')
                    print()
                num_of_game += 1

        print('Game\tWord\tStatus \tBad Guesses\tMissed Letters\tScore')
        print('----\t----\t------ \t-----------\t--------------\t-----')
        itr = 1
        totalScore = 0.00
        for g in self.noOfPlays:
            string_to_print = ''
            spaces_for_game = 4-len(str(abs(itr)))
            spaces_for_bad_guesses  = 11-len(str(abs(g.badGuess)))
            spaces_for_missed_letter = 14-len(str(abs(g.missedLetters)))
            string_to_print = str(abs(itr)) + " "*spaces_for_game + "\t"
            string_to_print += g.word + "\t"
            string_to_print += g.status + "\t"
            string_to_print += str(abs(g.badGuess)) + " "*spaces_for_bad_guesses + "\t"
            string_to_print += str(abs(g.missedLetters)) + " "*spaces_for_missed_letter + "\t"
            string_to_print += str((round(g.score, 2)))
            print(string_to_print)#output menu table
            #print(itr, " "*spaces_for_game, "\t", g.word, "\t", g.status, "\t", g.badGuess, " "*spaces_for_bad_guesses, "\t", g.missedLetters , " "*spaces_for_missed_letter, "\t", round(g.score,2))
            #print(itr, '\t', g.word, g.status, '\t', g.badGuess, '\t',g.missedLetters, '\t',  g.score)
            print()
            itr += 1
            totalScore += g.score

        print("Final Score : ", round(totalScore, 2))
        print()



guessObj = Guess()
guessObj.start_game()



