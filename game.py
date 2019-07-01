"""game.py: Calculates the final score for the gaming session.
@ author: Harmeet Singh
@ ID: 40053592
"""

from stringDatabase import StringDatabase

#Initializing all game related attributes and calculating final score.
"""Score is calculated by using bad guesses and number of guesses and dividing these from the remaining unguessed letters where each letter is assigned a frequency."""
class Game:

    word = ''
    status = ''
    badGuess = 0
    missedLetters = 0
    score = 0.00
    numOfRounds = 0

    db1 = StringDatabase()

#Function is responsible for calculating final score.
    def score_evaluation(self, game, currentGuess):#score_evaluation
        score = 0.00
        for i in range(len(game.word)):
            if currentGuess[i] == '_':
                score += self.db1.letter_frequency(game.word[i])
        if game.numOfRounds > 0:
            score = score / game.numOfRounds
        score = score * (1 - game.badGuess / 10)
        self.score = score

#This function calculates negative score for specific point in game.
    def evaluate_negative_score(self, game, currentGuess):
        score = 0.00
        for i in range(len(game.word)):
            if currentGuess[i] == '_':
                score += self.db1.letter_frequency(game.word[i])
        if game.numOfRounds > 0:
            score = score / game.numOfRounds
        score = 0-score * (1 - game.badGuess / 10)
        self.score = score

#This function returns random four letter word.
    def select_word(self):
        self.word = self.db1.randomisedWord()
