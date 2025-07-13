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
    '''
    Randomly selects a specified number of questions from the provided list.
    Each question's options are shuffled before returning.
    '''
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


def reset_game():
    '''
    Resets the game state counters to zero.
    This is called at the end of each game to prepare for a new round.
    '''
    global correct_answers, incorrect_answers, total_questions
    # Input validation loop
    while True:
        restart = input("Do you want to play again? (yes/no): ").strip().lower()
        if restart in ['yes', 'no']:
            break
        else:
            print("❗ Invalid input. Please type 'yes' or 'no'.")

    if restart == 'yes':
        correct_answers = 0
        incorrect_answers = 0
        total_questions = 0
        run_game()
    else:
        print("Goodbye! Thanks for playing!\n")


def run_game():
    '''
    Main function to run the quiz game.
    1. Prompts the user to choose a topic.
    2. Randomly selects questions from the chosen topic.
    3. Displays each question with shuffled options.
    4. Collects user input and checks answers.
    5. Displays the score at the end.
    6. Asks if the user wants to play again.
    '''
    global correct_answers, incorrect_answers, total_questions

    # Choose Quiz Topic
    chosen_topic = topic_choice()

    selected_questions = get_random_questions_with_shuffled_options(questionSets[chosen_topic])
    for i, q in enumerate(selected_questions, 1):
        print(f"\nQuestion {i}: {q['question']}")

        # Display options with numbers
        for idx, opt in enumerate(q["options"], 1):
            print(f"{idx}. {opt}")

        # Input loop to ensure valid selection
        while True:
            try:
                user_choice = int(input("Your answer (1-4): \n").strip())
                if 1 <= user_choice <= len(q["options"]):
                    break
                else:
                    print("❗ Please enter a number between 1 and 4.\n")
            except ValueError:
                print("❗ Invalid input. Please enter a number between 1 and 4.\n")

        selected_option = q["options"][user_choice - 1]

        # Increment game state counters
        total_questions += 1
        if selected_option.lower() == q["answer"].lower():
            correct_answers += 1
            print("✅ Correct!\n")
        else:
            incorrect_answers += 1
            print(f"❌ Incorrect! The correct answer was: {q['answer']}\n")

    # Summary of results
    print("\n🎉 Quiz complete!\n")
    print(f"Score: {correct_answers} correct, {incorrect_answers} incorrect, out of {total_questions} total.\n")

    # Reset game state for next playthrough
    print("Thank you for playing! You can restart the game to try another topic or exit.")
    reset_game()


if __name__ == "__main__":
    run_game()
