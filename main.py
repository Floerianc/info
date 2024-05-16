import random
import os
import time
import threading
from inputimeout import inputimeout, TimeoutOccurred

class Player:
    def __init__(self) -> None:
        self.name = input("Dein Name\n> ").strip().title()
        self.points = 0
    
    def menu(self):
        os.system("cls")
        print("Willkommen zu unserem unfassbar realistischem Ansatz an die Zukunft von künstlicher Intelligenz!\n1. Starten\n2. Abbrechen")
        while True:
            choice = int(input("> "))
            if choice == 1:
                self.run()
            elif choice == 2:
                exit()
            else:
                return
    
    def run(self):
        os.system("cls")
        print("Erste Herrausforderung wird geladen...")
        time.sleep(3)
        math_question()
        
class AI:
    def __init__(self) -> None:
        self.score = 0
        self.has_responded = None



threads = []
def AI_responds(sleep):
    time.sleep(sleep)
    if new_AI.has_responded == False:
        os.system("cls")
        new_AI.score += 1
        print(f"Du hast verloren! Ein Punkt geht an die KI\n{New_Player.points} : {new_AI.score}\nNächste Runde startet in 8 Sekunden")
        time.sleep(8)
    else:
        pass



def math_question():
    os.system("cls")
    new_AI.has_responded = False

    while True:
        operators = ["+","-","*"]
        rdm_num = random.randint(0,100)
        rdm_num2 = random.randint(0,100)
        operator = random.choice(operators)
        available_time = random.randint(3,7)
        question_str = f"{rdm_num} {operator} {rdm_num2}"

        if operator == "+":
            solution = rdm_num + rdm_num2
        elif operator == "-":
            solution = rdm_num - rdm_num2
        elif operator == "*":
            solution = rdm_num * rdm_num2
        
        if solution < 0:
            return
        else:
            break
    
    print(f"Berechne folgendes bevor die KI es kann!\n{question_str}")
    time_t = threading.Thread(target=AI_responds, args=(available_time,))
    time_t.start()
    threads.append(time_t)

    try:
        user_input = int(inputimeout("> ", available_time))
    except TimeoutOccurred:
        user_input = None
    
    os.system("cls") 
    if user_input == solution:
        won_o_lose(True)
    else:
        time.sleep(available_time)
    
    choose_path()



def won_o_lose(won_game):
    os.system("cls")
    if won_game == True:
        new_AI.has_responded = True
        New_Player.points += 1
        print(f"DU hast diese Runde gewonnen!\nDie nächste Runde startet in 8 Sekunden.\n{New_Player.points} : {new_AI.score}")
        time.sleep(8)
    elif won_game == None:
        new_AI.has_responded = True
        print(f"Niemand hat gewonnen, keiner kriegt einen Punkt\nDie Nächste Runde startet in 8 Sekunden\n{New_Player.points} : {new_AI.score}")
        time.sleep(8)
    else:
        new_AI.has_responded = True
        new_AI.score += 1
        print(f"Du hast diese Runde verloren, ein Punkt geht an die KI\nDie Nächste Runde startet in 8 Sekunden\n{New_Player.points} : {new_AI.score}")
        time.sleep(8)
    


def choose_path():
    os.system("cls")
    new_AI.has_responded = False
    print("          ------")
    print("         /      \ ")
    print("  You ---        --- AI")
    print("         \      /    ")
    print("          ------\n\n")
    print("Du darfst nicht den gleichen Weg nehmen, wie die KI\n'oben' um nach oben zu gehen, 'unten' um nach unten zu gehen.")
    choice = input("> ").lower()
    ai_choice = random.randint(0,1)

    if choice == "unten" or choice == "oben":
        os.system("cls")
        if ai_choice == 0:
            print("          --YOU-")
            print("         /      \ ")
            print("      ---        --- ")
            print("         \      /    ")
            print("          --AI--\n\n")
            print("Ihr habt beide NICHT den gleichen Weg gewählt!")
            time.sleep(3)
            won_o_lose(True)
        else:
            print("Ihr habt beide den gleichen Weg gewählt!")
            time.sleep(3)
            won_o_lose(False)
    else:
        os.system("cls")
        print("Das war keine Option. Spiel abgebrochen")
        time.sleep(4)
        exit()
    reaction_time()



def reaction_time():
    os.system("cls")
    time_until_event = random.randint(3,7)

    def event():
        ai_reaction = random.randint(250,450)
        os.system("cls")
        start_time = time.time()
        user_input = input("")
        end_time = time.time()
        rough_time = end_time-start_time
        exact_time = round((rough_time*1000), 1)
        print(f"Reaktionszeit der KI: {ai_reaction}\nDeine Reaktionszeit: {exact_time}")

        if exact_time > ai_reaction:
            print("Du hast länger gebraucht als die KI")
            time.sleep(4)
            won_o_lose(False)
        else:
            print("Du warst schneller als die KI")
            time.sleep(4)
            won_o_lose(True)
        defuse_the_bomb()

    for i in range(10):
        print("Wenn dieser Text verschwindet, drücke die 'Eingabe'-Taste so schnell du kannst!")
    time.sleep(time_until_event)
    event()


def defuse_the_bomb():
    os.system("cls")
    print("Vor dir sind 3 Kabel, jeweils eins davon ist rot, blau oder gelb.\n\n")
    print("   |     |     |   ")
    print("  Rot  Blau  Gelb\n\n")
    print("Gebe jetzt entweder 1, 2 oder 3 ein. \n[Rot steht für 1, gelb für 3 etc.]\nWenn du das falsche Kabel wählst, geht der Punkt an die KI.")
    correct_cable = random.randint(1,3)
    ai_choice = random.randint(1,3)
    user_choice = int(input("> "))

    try:
        os.system("cls")
        if ai_choice == correct_cable:
            if ai_choice == user_choice:
                print("Ihr habt beide das richtige Kabel durchtrennt. Keiner kriegt einen Punkt")
                time.sleep(4)
                won_o_lose(None)
            else:
                print("Die KI hat gewonnen.")
                time.sleep(4)
                won_o_lose(False)
        else:
            if user_choice == correct_cable:
                print("Du hast gewonnen.")
                time.sleep(4)
                won_o_lose(True)
            else:
                print("Niemand hat gewonnen.")
                time.sleep(4)
                won_o_lose(None)
    except Exception as e:
        print(e)
        time.sleep(3)
        exit()
    decide()

def decide():
    def result():
        def add_score():
            with open("entries.txt", "a", encoding="UTF-8") as f:
                if new_AI.score == New_Player.points:
                    mode = "hat es geschafft, die KI mit der Menschheit zu vereinen."
                
                elif new_AI.score > New_Player.points:
                    mode = "hat es nicht geschafft, die Menschheit vor der KI zu retten."
                
                else:
                    mode = "hat es geschafft, die KI zu besiegen und zu zerstören."
                
                f.write(f"\n{New_Player.name} {mode} // Punktestand: {New_Player.points} : {new_AI.score}")

        with open("entries.txt", 'r') as file_obj:
            # read first character
            first_char = file_obj.read(1)
        
            if not first_char:
                with open("entries.txt", "w") as file:
                    file.write("------------ +++++++ ENTRIES +++++++ -------------")
            add_score()

    os.system("cls")
    result()
    if new_AI.score == New_Player.points:
        print("Ihr habt beide die gleiche Punktzahl. Keiner gewinnt und somit wird niemand ausgelöscht :>")
    elif new_AI.score > New_Player.points:
        print("Die KI hat mehr Punkte als du, die Menschheit wird jetzt ausgerottet, tja blöd.")
    else:
        print("DU hast mehr Punkte als die KI, die KI ist jetzt tot und die Menschheit gerettet :D")
    time.sleep(10)
    exit()

new_AI = AI()
New_Player = Player()
New_Player.menu()