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
class quiz_taker(quiz_reader):
    def __init__(self, filename):
        super().__init__(filename)
        self.comparison = {'a': 'option_a', 'b': 'option_b', 'c': 'option_c', 'd': 'option_d'}
        self.question = None
        self.user_answer = None
    # pick a random question
    def random_question(self):
        self.question = random.choice(self.quiz_data)
    # display the question and the choices
    def display_question(self):
        print('Question:', self.question['question'])
        for opt, ans in self.question['choices'].items():
            print(f"{opt[-1].upper()}: {ans}")
    # let the taker answer the question
    def get_answer(self):
        while True:
            user_input = input('Type the letter of the correct answer:\n').lower()
            if user_input in self.comparison:
                return self.question['choices'][self.comparison[user_input]]
            else:
                print('Invalid input. Try again.')
    # check the answer if it is correct
    def check_answer(self, user_answer):
        correct = self.question['answer']
        print('Your answer is:', user_answer)
        print('The correct answer is:', correct)
        # display if they passed or not
        if user_answer == correct:
            print('Congratulations, you got the correct answer!!')
        else:
            print('Bad luck, you chose the wrong answer. Better luck next time.')
    def cycle(self):
        self.random_question()
        self.display_question()
        self.user_attempt = self.get_answer()
        self.check_answer(self.user_attempt)
# running the program
if __name__ == "__main__":
    program_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(program_path, "quiz.json")
    
    quiz = quiz_taker(filename)
    quiz.cycle()