from random import *
import ast 


class Questionnaire:

    #propriétés du questionnaires
    # theme = None
    # nb_questions = 0
    
    def __init__(self, theme, nb_questions):
        #on va initialiser des trucs mais je sais pas encore quoi
        self.theme = theme
        self.nb_questions = nb_questions
        self.file_path = "/home/luca/Projet/FlashCard/" + theme
        quest = self.get_questionsfromfile(self.file_path)
        self.ask_questions(quest)


    def show_properties(self):
        print("Le theme est " + self.theme)
        print("Le nb de question est " + str(self.nb_questions))


    def getrandom_questions(self, qlist):
        # alea = randint(0,len(qlist))
        alea = sample(range(len(qlist)), self.nb_questions)
        # print(alea)
        # shuffle(alea)
        print(alea)
        return alea

    def show_question(self, index,qlist):
        print(qlist[index][0])
        print("1: " + qlist[index][1])
        print("2: " + qlist[index][2])
        print("3: " + qlist[index][3])
        print("4: " + qlist[index][4])

    def reveal_answer(self, index, qlist, answer):
        if qlist[index][-1] == qlist[index][answer]:
            print("Correct, la réponse est bien")
        else:
            print("Incorrect, la réponse était:")

        print(qlist[index][-1])

    def ask_questions(self, qlist):
        order_list = self.getrandom_questions(qlist)
        for x in order_list:
            self.show_question(x,qlist)
            answer = int(input("Votre réponse:"))
            self.reveal_answer(x, qlist, answer)

    def get_questionsfromfile(self, file):
        # new_list = []
        with open(file, "r") as q:
            lines = q.readlines()
        
        # for elem in lines:
        #     temp = elem.split(', ')
        #     new_list.append((temp))
        new_list = [list(ast.literal_eval(x)) for x in lines]
        return new_list