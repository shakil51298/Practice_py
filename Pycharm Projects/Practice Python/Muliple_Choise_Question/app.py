from QuestionClass import Questions

# questions data
question_prompts =[
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "what color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

#  making quesitons list.....
questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "a"),
    Questions(question_prompts[2], "b"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.question)
        if answer == question.answer:
            score += 1
    print("You got " + str(score)+ "/" + str(len(questions)) +" correct!")
run_test(questions) 
