from random import *
import ast 

# questions = []
# questions.append(["Quel département a le numéro 59 ?","Nord","Aisne","Savoie","Pas de calais","Nord"])
# questions.append(["Au Moyen-Âge, comment appelait-on les villages fortifiés ?","Tour","Bastide","Chateau Fort","Rempart","Chateau Fort"])
# questions.append(["Dans quel film un couple en croisière va-t-il recueillir un naufragé qui va les terrifier ?","Calme Blanc","Tempete en mer","Le naufragé","Les disparus","Le naufragé"])
# questions.append(["Quel est le surnom de l'équipe de football d'Allemagne ?","Die Wunderteam","Die Nationalmannschaf","Die FuBballmannschaft","Die Ballspielerteam","Die Nationalmannschaf"])
# questions.append(["Combien de quilles sont alignées sur la dernière rangée au bowling ?","3","4","5","6","4"])

def getrandom_questions(qlist):
    alea = randint(0,len(qlist))
    return alea

def show_question(index,qlist):
    print(qlist[index][0])
    print("1: " + qlist[index][1])
    print("2: " + qlist[index][2])
    print("3: " + qlist[index][3])
    print("4: " + qlist[index][4])

def reveal_answer(index, qlist, answer):
    if qlist[index][-1] == qlist[index][answer]:
        print("Correct, la réponse est bien")
    else:
        print("Incorrect, la réponse était:")

    print(qlist[index][-1])

def ask_questions(qlist):
    i = getrandom_questions(qlist)
    show_question(i,qlist)
    answer = int(input("Votre réponse:"))
    reveal_answer(i,qlist, answer)

def get_questionsfromfile(file):
    # new_list = []
    with open(file, "r") as q:
        lines = q.readlines()
    
    # for elem in lines:
    #     temp = elem.split(', ')
    #     new_list.append((temp))
    new_list = [list(ast.literal_eval(x)) for x in lines]
    return new_list
        
        
        

questions = get_questionsfromfile("/home/luca/Projet/FlashCard/fichier_questions")
ask_questions(questions)