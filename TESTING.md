# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | [questions.py](https://github.com/RadwanDuadu/AcademIQ/blob/main/questions.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/AcademIQ/main/questions.py) | ![screenshot](documentation/validation/py--questions.png) | No Errors |
|  | [run.py](https://github.com/RadwanDuadu/AcademIQ/blob/main/run.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RadwanDuadu/AcademIQ/main/run.py) | ![screenshot](documentation/validation/py--run.png) | No Errors |


## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- |
| ![screenshot](documentation/responsiveness/mobile-terminal.png) | ![screenshot](documentation/responsiveness/tablet-terminal.png) | ![screenshot](documentation/responsiveness/desktop-terminal.png) | Mobile issues: `overflow-x`, doesn't work on iPhones, but does work on Android with some limitations |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- |
| ![screenshot](documentation/browsers/chrome-terminal.png) | ![screenshot](documentation/browsers/firefox-terminal.png) | ![screenshot](documentation/browsers/safari-terminal.png) | Chrome: work as expected. Firefox: emojis get cut-off. Safari: some limitations. |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Mobile | Desktop |
| --- | --- |
| ![screenshot](documentation/lighthouse/mobile-terminal.png) | ![screenshot](documentation/lighthouse/desktop-terminal.png) |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| **Feature**   | **Expectation**   | **Test**    | **Result**    | **Screenshot**    |
| ------------- | ------------------| ----------- | --------------| ----------------- |
| Topic Selection Validation   | The game should only allow users to choose from available topics using a valid number. | Entered invalid input such as letters and out-of-range numbers.                 | Program displayed error messages and re-prompted until valid input was received. | ![screenshot](documentation/defensive/topic-validation.png)    |
| Answer Input Handling        | Only numeric values from 1 to 4 should be accepted during answer selection.            | Entered invalid responses like letters, empty strings, and numbers outside 1–4. | The program rejected invalid input and prompted again without crashing.          | ![screenshot](documentation/defensive/answer-input.png)        |
| Score Calculation Safety     | The program should not crash due to missing answer fields or incorrect indices.        | Entered random invalid options and forced incorrect questions.                  | Program handled all cases gracefully and tracked scores accurately.              | ![screenshot](documentation/defensive/score-feedback.png)      |
| Restart Prompt Handling      | Only “yes” or “no” should be accepted when asking to restart the quiz.                 | Typed “y”, “maybe”, and random strings.                                         | Program rejected invalid input and prompted again clearly.                       | ![screenshot](documentation/defensive/restart-validation.png)  |
| Empty Question Bank Handling | The app should exit gracefully if a topic has no valid questions.                      | Emptied one question bank and ran the game.                                     | Game detected the issue and exited with a friendly error message.                | ![screenshot](documentation/defensive/empty-question-bank.png) |
| Clear Instructions           | The app should provide clear instructions for each step.                               | Ran through the game without reading the source code.                           | All prompts and feedback were understandable without needing documentation.      | ![screenshot](documentation/defensive/usability.png)           |


## User Story Testing

| **Target**     | **Expectation**                                                                 | **Outcome**                                                                                    | **Screenshot**                                      |
| -------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| As a user      | I would like to answer multiple-choice questions using a number between 1 and 4 | so that I can easily select an option without typing the full answer.                          | ![screenshot](documentation/features/input-validation.png) |
| As a user      | I want the quiz to validate my input                                            | so that I don't accidentally crash the program by entering something invalid.                  | ![screenshot](documentation/features/input-validation.png) |
| As a user      | I want the quiz to ignore capitalization when checking my answers               | so that I’m not penalized for formatting.                                                      | ![screenshot](documentation/features/restart-quiz.png) |
| As a user      | I want immediate feedback after each question                                   | so that I know right away whether I was correct or not.                                        | ![screenshot](documentation/features/answer-feedback.png) |
| As a user      | I want to see my total score at the end of the quiz                             | so that I can track how well I performed.                                                      | ![screenshot](documentation/features/score-feedback.png) |
| As a user      | I want the option to restart the quiz without closing the program               | so that I can try different topics easily.                                                     | ![screenshot](documentation/features/restart-quiz.png) |
| As a user      | I want the quiz to only accept “yes” or “no” when asking to restart             | so that I’m not confused by vague input handling.                                              | ![screenshot](documentation/features/restart-validation.png) |
| As a user      | I want to choose from multiple quiz topics                                      | so that I can focus on the subject areas that interest me most.                                | ![screenshot](documentation/features/choose-topic.png) |
| As a user      | I want questions to be randomly selected from the topic I choose                | so that I get a different experience each time I play.                                         | ![screenshot](documentation/features/random-question-selection.png) |


## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3ARadwanDuadu%2FAcademIQ%20label%3Abug&label=bugs)](https://www.github.com/RadwanDuadu/AcademIQ/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/RadwanDuadu/AcademIQ/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/RadwanDuadu/AcademIQ/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

[![GitHub issues](https://img.shields.io/github/issues/RadwanDuadu/AcademIQ)](https://www.github.com/RadwanDuadu/AcademIQ/issues)

Any remaining open issues can be tracked [here](https://www.github.com/RadwanDuadu/AcademIQ/issues).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The `colorama` terminal colors are fainter on Heroku when compared to the IDE locally. | ![screenshot](documentation/issues/colorama.png) |
| Emojis are cut-off when viewing the application from Firefox. | Unable to add screenshot due to timer added to feedback resulting in feedback display for 1-2 seconds |
| The Python terminal doesn't work well with Safari, and sometimes uses cannot type in the application. | ![screenshot](documentation/issues/safari-terminal.png) |
| If a user types `CTRL`+`C` in the terminal on the live site, they can manually stop the application and receive and error. | ![screenshot](documentation/issues/ctrl-c.png) |

> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

