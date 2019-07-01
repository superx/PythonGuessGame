
"""stringDatabase.py: Maintains all the input and output.
@ author: Harmeet Singh
@ ID: 40053592
"""
import random


class StringDatabase:


#Function which returns random word from input file.
    def randomisedWord(self):


        #print("lets start")
        # Entering the data file
        four_letter = open("four_letters.txt", "r")

        if four_letter.mode == 'r':
            self.File_letter = four_letter.read().replace("\n", " ").split(" ")

        #print(File_letter)

        randWord = random.choice(self.File_letter)
        return randWord
#Function which returns frequency associated to a character.
    def letter_frequency(self,ch):

        letterFrequency = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'r': 5.99, 'h': 6.09, 'd': 4.25, 'l': 4.03, 'u': 2.76, 'c': 2.78, 'm': 2.41, 'f': 2.23, 'y': 1.97, 'w': 2.36, 'g': 2.02, 'p': 1.93, 'b': 1.49, 'v': 0.98, 'k': 0.77, 'x': 0.15, 'q': 0.10,'j': 0.15, 'z': 0.07}
        return letterFrequency.get(ch)
