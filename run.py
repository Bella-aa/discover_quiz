#---------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num -1]:
            print(i)

            guess = input("Enter (A, B, C, D):")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key),guess)
            question_num +=1

 display_score(correct_guesses, guesses)
#----------------

def check_answer(answer, guess):
   if answer == guess
   print("CORRECT!")
   return 1

   else:
       print("WRONG")
       return 0
#-----------------

def display_score(correct_guesses, guesses):
    print("---------------------------")
    print("RESULTS")
    print("---------------------------")
    PRINT("Answers:", end = "")
    
    for i in questions:
        print(questions.get(i), end = "")
      print()  
#-----------------

def play_again():
    pass
#------------------

questions = {
    "Which waterfall is called the smoke that thunders?:":"A",
    "Which is the biggest waterfall in the world?:":"C",
    "Which mountain has the tallest peak on Earth and measures 8 848.86m tall?:":"B",
    "Where is the Grand Canyon located?:":"D",
    "The Great Barrier Reef is the largest Coral reef located in which country?:":"B",
}

options = [
    ["A. Victoria Falls", "B. Niagra Falls", "C. Iguazu Falls", "D. Angel Falls",]
    ["A. Iguazu Falls", "B. Niagra Falls", "C. Victoria Falls", "D. Angel Falls", ]
    ["A. Mount Denali", "B. Mount Everest", "C. Mount Makalu", "D. Mount Kilimanjaro", ]
    ["A. Peru", "B. Norway", "C. Ireland", "D. Unites States", ]
    ["A. United Kingdom", "B. Australia", "C. France", "D. Botswana", ]
]

new_game()

