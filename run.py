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
