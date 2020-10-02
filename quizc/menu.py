from json_persistence import MyClass, MyEncoder
from quizc.console.quiz_ui_handler import *


class Menu(object):
    MENU_PROMPT = "> "

    def __init__(self):
        self.car = ""
        self.quiz = None
        self.quiz_answers = None

    def show_main_menu(self):
        print("""
Quizc - A command quiz utility
======================================
1. Create quiz
2. Fill quiz
3. Show quiz
4. Save quiz in JSON file
5. Exit
======================================
        """)

    @property
    def process(self):
        self.show_main_menu()
        option = int(input(self.MENU_PROMPT))
        should_exit = False

        if option == 1:
            self.quiz = QuizUIHandler.create_quiz()
        elif option == 2:
            if self.quiz is None:
                print("No quiz available, you must create first a quiz")
            else:
                self.quiz_answers = QuizUIHandler.fill_quiz(self.quiz)
        elif option == 3:
            if self.quiz_answers is None:
                print("No filled quiz available, you must create first a quiz")
            else:
                QuizUIHandler.show_quiz(self.quiz_answers)
        elif option == 4:
            if self.quiz_answers is None:
                print("No filled quiz available, you must create first a quiz")
            else:
                myClass = MyClass(self.quiz_answers.id, self.quiz_answers)
                json = MyEncoder().encode(myClass)
                f = open("myform.json", "w")
                f.write(json)
                f.close()
        elif option == 5:
            should_exit = True

        return should_exit
