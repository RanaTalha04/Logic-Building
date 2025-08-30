quiz = {
    1: {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    2: {
        "question": "Which data type is immutable in Python?",
        "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
        "answer": "C"
    },
    3: {
        "question": "Who developed the theory of relativity?",
        "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
        "answer": "B"
    },
    4: {
        "question": "What does HTML stand for?",
        "options": ["A. Hyper Trainer Marking Language", "B. Hyper Text Markup Language", "C. Hyper Text Marketing Language", "D. Hyper Tool Multi Language"],
        "answer": "B"
    },
    5: {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    6: {
        "question": "In Python, what is the output of 2 ** 3?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 12"],
        "answer": "B"
    },
    7: {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Helium"],
        "answer": "B"
    },
    8: {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. def", "B. func", "C. function", "D. lambda"],
        "answer": "A"
    },
    9: {
        "question": "Who was the first man to walk on the moon?",
        "options": ["A. Neil Armstrong", "B. Yuri Gagarin", "C. Buzz Aldrin", "D. Michael Collins"],
        "answer": "A"
    },
    10: {
        "question": "Which of these is a Python web framework?",
        "options": ["A. Django", "B. Laravel", "C. Spring", "D. Angular"],
        "answer": "A"
    }
}


score = 0
print("📘 Welcome to the Quiz App!")
print("Answer by typing A, B, C, or D\n")

for key, value in quiz.items():
    print(f"Question: {key}: {value['question']}\n")
    for option in value["options"]:
        print(option, end=" ")
    answer = input("\nEnter your answer: ").upper()
    
    if answer == value['answer']:
        print("✅ Correct")
        score += 1
        print()
    else:
        print(f"❌ Wrong answer. Correct answer{value['answer']}")
        print()

print("🎯 Quiz Finished!")
print(f"Your final score: {score}/{len(quiz)}")
