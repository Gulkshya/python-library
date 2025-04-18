questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "What is 9 + 10?",
        "options": ["A. 19", "B. 21", "C. 18", "D. 20"],
        "answer": "A"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong answer.")

print(f"\nYour final score is {score}/{len(questions)}.")
