questions = [
    {
        "question": "What is the capital city of Australia?",
        "options": ["A: Paris", "B: London", "C: Canberra", "D: Madrid"],
        "answer": "C"
    },

    {
        "question": "Who wrote the famous novel To Kill a Mockingbird",
        "options": ["A: Stephen King", "B: Harper lee", "C: J. K. Rowling", "D: Agatha Christie"],
        "answer": "B"
    },

    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A: La", "B: Hf", "C: Ge", "D: Au"],
        "answer": "D"
    },

    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A: Jupiter", "B: Mars", "C: Tellus", "D: Mercurius"],
        "answer": "B"
    },

    {
        "question": "how tall is mount everest?",
        "options": ["A: 1912", "B: 8488", "C: 8849", "D: 8489"],
        "answer": "D"
    },

    {
        "question": "In which year did the Titanic sink?",
        "options": ["A: 1912", "B: 1895", "C: 1910", "D: 1911"],
        "answer": "A"
    },

    {
        "question": "What is the chemical formula for water?",
        "options": ["A: H", "B: CO2", "C: H2", "D: H20"],
        "answer": "D"
    },

    {
        "question": "Where is the smallest bone i located in the human body",
        "options": ["A: Toe", "B: lil finger", "C: Ear", "D: nose"],
        "answer": "C"
    },

    {
        "question": "What is the largest organ in the human body?",
        "options": ["A: Liver", "B: Skin", "C: Brain", "D: Heart"],
        "answer": "B"
    },
]








# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")

run_quiz(questions)