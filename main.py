

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Hyderabad", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2. Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "3. Which data type stores True or False values?",
        "options": ["A. int", "B. bool", "C. str", "D. float"],
        "answer": "B"
    },
    {
        "question": "4. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
        
    },
    {
        "question": "5. Which loop is used to repeat a block of code?",
        "options": ["A. if", "B. while", "C. switch", "D. case"],
        "answer": "B"
    }
]

def run_quiz():
    print("=" * 40)
    print("      WELCOME TO PYTHON QUIZ")
    print("=" * 40)

    name = input("Enter your name: ")
    print(f"\nHello, {name}! Best of luck.\n")

    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! Correct answer is {q['answer']}.\n")

    total = len(questions)
    percentage = (score / total) * 100

    print("=" * 40)
    print("           QUIZ RESULT")
    print("=" * 40)
    print(f"Name       : {name}")
    print(f"Score      : {score}/{total}")
    print(f"Percentage : {percentage:.2f}%")

    if percentage >= 80:
        print("Grade      : A")
    elif percentage >= 60:
        print("Grade      : B")
    elif percentage >= 40:
        print("Grade      : C")
    else:
        print("Grade      : Fail")

    # Save score
    with open("scores.txt", "a") as file:
        file.write(f"{name} - {score}/{total} - {percentage:.2f}%\n")

    print("\nYour score has been saved to scores.txt")

# Restart option
while True:
    run_quiz()
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice != "yes":
        print("\nThank you for playing!")
        break