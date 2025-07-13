import random
from questions import (
    geographyQuestions,
    historyQuestions,
    chemistryQuestions,
    biologyQuestions,
    physicsQuestions,
)


# --- Question sets ---
questionSets = {
    "geography": geographyQuestions,
    "history": historyQuestions,
    "physics": physicsQuestions,
    "biology": biologyQuestions,
    "chemistry": chemistryQuestions
}

# --- Game State ---
correct_answers = 0
incorrect_answers = 0
total_questions = 0


def get_random_questions_with_shuffled_options(questions, count=10):
    selected = random.sample(questions, min(count, len(questions)))
    for q in selected:
        random.shuffle(q["options"])
    return selected


def topic_choice():
    '''
    1.Displays topic options with number values.
    2.Prompts the user to input the number corresponding to their topic.
    3.Loops until a valid input is given.
    '''
    topics = list(questionSets.keys())

    while True:
        print("Choose a topic:\n")
        for i, topic in enumerate(topics, 1):
            print(f"{i}. {topic.capitalize()}")

        choice = input("Enter the number of your chosen topic: \n").strip()

        if not choice.isdigit():
            print("Please enter a valid number.\n")
            continue

        index = int(choice) - 1
        if 0 <= index < len(topics):
            chosen_topic = topics[index]
            return chosen_topic
        else:
            print("Invalid choice. Please try again.\n")


def run_game():
    global correct_answers, incorrect_answers, total_questions

    chosen_topic = topic_choice()

    selected_questions = get_random_questions_with_shuffled_options(questionSets[chosen_topic])

    for i, q in enumerate(selected_questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for opt in q["options"]:
            print(opt)

        user_input = input("Your answer (just the text, e.g., 'Paris'): ").strip()

        total_questions += 1
        if user_input.lower() == q["answer"].lower():
            correct_answers += 1
            print("✅ Correct!")
        else:
            incorrect_answers += 1
            print(f"❌ Incorrect! The correct answer was: {q['answer']}")

    print("\n🎉 Quiz complete!")
    print(f"Score: {correct_answers} correct, {incorrect_answers} incorrect, out of {total_questions} total.")


if __name__ == "__main__":
    run_game()
