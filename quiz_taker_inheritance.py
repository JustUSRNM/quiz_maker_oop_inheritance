# import the essential modules
import json
import random
import os
# create a class for loading the quiz.json file
class quiz_reader:
    def __init__(self, filename):
        self.filename = filename
        self.quiz_data = self.load_quiz()

    def load_quiz(self):
        with open(self.filename, 'r') as file:
            return json.load(file)
# create the class for the flow of the program 
    # pick a random question
    # display the question and the choices
    # let the taker answer the question
    # check the answer if it is correct
    # display if they passed or not
# running the program