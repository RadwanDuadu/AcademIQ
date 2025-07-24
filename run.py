import random
import time
import colorama
from colorama import Fore

from questions import (
    geographyQuestions,
    historyQuestions,
    chemistryQuestions,
    biologyQuestions,
    physicsQuestions,
)

colorama.init(autoreset=True)  # Initialize colorama to auto-reset colors
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


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    print("\033c")


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
            clear()
            print(f"{Fore.CYAN}Your choice {Fore.YELLOW}'{choice}'{Fore.CYAN},"
                  " Please enter a valid number.\n")
            continue

        index = int(choice) - 1
        if 0 <= index < len(topics):
            chosen_topic = topics[index]
            return chosen_topic
        else:
            clear()
            print(f"{Fore.CYAN}Your choice {Fore.YELLOW}'{choice}'{Fore.CYAN},"
                  "Invalid choice. Please try again.\n")


def quiz_banner():
    """
    Displays the ASCII art banner for the quiz game.

    This function prints a stylized banner to the terminal
    to give the application a more polished and engaging look.
    It's typically called at the start of the game or after major sections
    like finishing the quiz or restarting.

    The ASCII art represents the title or branding of the quiz game.
    """
    banner = r"""
    _                 _                ___ ___
   / \   ___ __ _  __| | ___ _ __ ___ |_ _/ _ \
  / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \ | | | | |
 / ___ \ (_| (_| | (_| |  __/ | | | | || | |_| |
/_/   \_\___\__,_|\__,_|\___|_| |_| |_|___\__\_\

A fun and educational multiple-choice quiz to test your knowledge.
    """
    print(banner)


def input_validation(input_func, question):
    '''
    Validates user input against a list of valid inputs.
    Repeats the prompt until a valid input is received.
    '''
    while True:
        raw_input = input_func("\nYour answer (1-4): \n").strip()

        try:
            user_choice = int(raw_input)
            if 1 <= user_choice <= len(question["options"]):
                return user_choice
            else:
                clear()
                print(
                    f"{Fore.CYAN}Your choice {Fore.YELLOW}'{user_choice}'"
                    f"{Fore.CYAN}, ❗ Please enter a number between 1-4.\n"
                      )
        except ValueError:
            clear()
            print(f"{Fore.CYAN}Your choice {Fore.YELLOW}'{raw_input}'"
                  f"{Fore.CYAN},❗ Invalid, Please enter number between 1-4.\n")

        # Re-display the question and options after error
        print(f"\n{question['question']}")
        for idx, opt in enumerate(question["options"], 1):
            print(f"{idx}. {opt}")


def score_tracker(selected_option, question):
    '''
    Display feedback of answered question.
    Track correct and incorrect answers and total score.
    '''
    global correct_answers, incorrect_answers, total_questions
    # Increment game state counters
    total_questions += 1
    if selected_option.lower() == question["answer"].lower():
        correct_answers += 1
        print(f"{Fore.GREEN} ✅ Correct!\n")
        time.sleep(0.9)  # Pause for a moment before next question
    else:
        incorrect_answers += 1
        print(f"{Fore.RED} ❌ Incorrect! The correct answer was: "
              f"{Fore.YELLOW}{question['answer']}\n")
        time.sleep(2)  # Pause for a moment before next question


def reset_game():
    '''
    Resets the game state counters to zero.
    This is called at the end of each game to prepare for a new round.
    '''
    global correct_answers, incorrect_answers, total_questions

    # Clear the terminal for a fresh start
    clear()
    # Input validation loop
    while True:
        prompt = "Do you want to play again? (yes/no): "
        restart = input(prompt).strip().lower()
        if restart in ['yes', 'no']:
            break
        else:
            clear()
            print(f"{Fore.CYAN} Your choice {Fore.YELLOW}'{restart}'"
                  f"{Fore.CYAN},❗ Invalid input. Please type 'yes' or 'no'.")

    if restart == 'yes':
        correct_answers = 0
        incorrect_answers = 0
        total_questions = 0
        run_game()
    else:
        print(f"{Fore.YELLOW} Goodbye! Thanks for playing!\n")


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

    clear()  # Clears screen after choosing topic

    # randomly select questions and shuffle options
    selected_questions = get_random_questions_with_shuffled_options(
        questionSets[chosen_topic]
    )

    # loop over selected questions
    for i, q in enumerate(selected_questions, 1):
        clear()
        print(f"\nQuestion {i}: {q['question']} \n")

        # Display options with numbers
        for idx, opt in enumerate(q["options"], 1):
            print(f"{idx}. {opt}")

        # Input loop to ensure valid selection
        user_choice = input_validation(input, q)

        selected_option = q["options"][user_choice - 1]

        # Increment game state counters
        score_tracker(selected_option, q)

    clear()
    # Summary of results
    print("\n🎉 Quiz complete!\n")
    print(f"{Fore.YELLOW} Score: {correct_answers} correct,"
          f"{Fore.RED} {incorrect_answers} incorrect"
          f"{Fore.YELLOW}, out of {total_questions} total.\n")

    prompt = "Press Enter if you want to Continue \n"
    input(prompt)
    # Reset game state for next playthrough
    print("Thank you for playing! You can restart the game to try another "
          "topic or exit.")
    reset_game()


if __name__ == "__main__":
    clear()
    quiz_banner()
    run_game()
