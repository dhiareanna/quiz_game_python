import random

quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Rome"],
        "answer": "A"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "Who developed Python Programming Language?",
        "options": ["A. Dennis Ritchie", "B. Bjarne Stroustrup", "C. Guido van Rossum", "D. James Gosling"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /* */", "D. <!-- -->"],
        "answer": "B"
    }
]

def start_quiz():
    print("🎯 Welcome to the Python Quiz Game!")
    name = input("Enter your name: ").title()
    print(f"\nHi {name}! Let's test your knowledge.\n")
    
    score = 0
    random.shuffle(quiz) 

    for q in quiz:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    print(f"🏁 Quiz Over, {name}! You scored {score}/{len(quiz)}.")
    
    if score == len(quiz):
        print("🌟 Excellent! You nailed it all!")
    elif score >= 3:
        print("👍 Good job! Keep improving your knowledge.")
    else:
        print("📚 Don’t worry — every mistake is a step toward learning!")

start_quiz()