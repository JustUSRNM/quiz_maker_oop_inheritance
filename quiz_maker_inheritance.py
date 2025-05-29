import json
# creating a class for making a question
class question_making:
    def __init__(self):
        self.problem = ''
        self.answer = None
        self.choices = {}
    def user_inputs(self):
        # input the question
        self.problem = input("Enter the question\n")
        # input the choices
        for option in ['option_a', 'option_b', 'option_c', 'option_d']:
            self.choices[option] = input(f"Enter the answer for {option}\n")
        # input the correct answer
        self.answer = input("Enter the correct answer for this question\n")
        while self.answer not in self.choices.values():
            self.answer = input("Your correct answer is not in the choices you have given\nThe correct anwers must be one of your choices\nenter the correct answer again\n")
    # save inputted data to a dictionary
    def dictionary(self):
        return {"question" : self.problem, "choices" : self.choices, "answer" : self.answer}
# creating a class for the running the quiz maker
class quiz_maker:
    # initialize the question data as dictionary
    def __init__(self):
        self.question_data = []
    # add the question data to the dictionary
    def adding_questions (self, question_obj):
        self.question_data.append(question_obj)
    def cycle(self):
        while True:
            question = question_making()
            question.user_inputs()
            self.adding_questions(question)
        # ask if user wants to make more questions
            continue_input = input('Add another question? (y/n)\n')
            if continue_input.lower() == 'n':
                break
    # function to save the quiz data
    def saving(self, filename):
        file_data = [items.dictionary() for items in self.question_data]
        with open(filename, "w") as json_file:
            json.dump(file_data, json_file, indent=4)
# running the program
# saving the data to a text file

test = quiz_maker()
test.cycle()