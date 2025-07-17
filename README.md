# [AcademIQ](https://academ-iq-b9bb24eb3c99.herokuapp.com)

Developer: Radwan Duadu ([RadwanDuadu](https://www.github.com/RadwanDuadu))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/RadwanDuadu/AcademIQ)](https://www.github.com/RadwanDuadu/AcademIQ/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/RadwanDuadu/AcademIQ)](https://www.github.com/RadwanDuadu/AcademIQ/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/RadwanDuadu/AcademIQ)](https://www.github.com/RadwanDuadu/AcademIQ)

AcademIQ is a terminal-based quiz application built with Python, designed to make learning interactive and engaging. It covers five key academic subjects — Geography, History, Biology, Chemistry, and Physics — offering users a selection of randomized multiple-choice questions. The game provides immediate feedback on answers, tracks performance, and allows users to replay with different topics, making it ideal for revision, exam prep, or general knowledge testing.

Targeted at students, educators, and lifelong learners, AcademIQ delivers a lightweight and accessible learning tool that works directly from the command line. With robust input validation, a replayable structure, and a focus on ease-of-use, the application is perfect for anyone seeking to improve subject knowledge in a fun and self-paced way.

![screenshot](documentation/mockup.png)

source: [AcademIQ amiresponsive](https://ui.dev/amiresponsive?url=https://academ-iq-b9bb24eb3c99.herokuapp.com)

> [!IMPORTANT]
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "Love Sandwiches".

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**
- Provide users with a simple and interactive way to test their knowledge across multiple academic subjects.
- Help users identify strengths and areas for improvement through engaging quiz sessions.

**Primary User Needs**
- Select a topic and complete a short, randomized quiz with immediate feedback.
- View a summary of correct and incorrect answers at the end of each session.
- Replay quizzes on different topics to reinforce learning.

**Business Goals**
- Offer a reliable, user-friendly educational tool that promotes self-assessment and continuous learning.
- Support students, educators, and independent learners in strengthening their academic knowledge efficiently.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**
- Input system for selecting a quiz topic from multiple academic categories.
- Randomized display of multiple-choice questions with numbered answer options.
- Score tracking for correct and incorrect answers during a single quiz session.
- End-of-quiz summary displaying total questions attempted, number correct, and incorrect.
- Option to restart the quiz and choose a new topic for repeated learning.

#### 3. Structure

**Information Architecture**
- **Hierarchy**:
  - Topic selection and quiz initiation as the primary focus for ease of access.

**User Flow**
1. User opens the app → selects a quiz topic from the available list.
2. User answers a series of randomized multiple-choice questions.
3. User receives immediate feedback after each question (correct/incorrect).
4. User completes the quiz → views a summary of their score and performance.
5. User chooses to replay with a new topic or exit the application.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- No visual design elements as this project is completed using the commandline. 

## Wireframes

To follow best practice, a flowchart was created to showcase the progression of the Python app.
I've used [Lucidchart](https://www.lucidchart.com/pages/examples/flowchart-maker) to design my app flowchart.

![screenshot](documentation/flowchart.png)

## User Stories

| **Target** | **Expectation**                                                                 | **Outcome**                                                                   |
| ---------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| As a user  | I would like to answer multiple-choice questions using a number between 1 and 4 | so that I can easily select an option without typing the full answer.         |
| As a user  | I want the quiz to validate my input                                            | so that I don't accidentally crash the program by entering something invalid. |
| As a user  | I want the quiz to ignore capitalization when checking my answers               | so that I’m not penalized for formatting.                                     |
| As a user  | I want immediate feedback after each question                                   | so that I know right away whether I was correct or not.                       |
| As a user  | I want to see my total score at the end of the quiz                             | so that I can track how well I performed.                                     |
| As a user  | I want the option to restart the quiz without closing the program               | so that I can try different topics easily.                                    |
| As a user  | I want the quiz to only accept “yes” or “no” when asking to restart             | so that I’m not confused by vague input handling.                             |
| As a user  | I want to choose from multiple quiz topics                                      | so that I can focus on the subject areas that interest me most.               |
| As a user  | I want questions to be randomly selected from the topic I choose                | so that I get a different experience each time I play.                        |
| As a developer | I want to deploy the quiz application on Heroku            | so that users can access and play the game online without needing to install anything locally. |
| As a developer | I want to validate the Python code using tools like CI Python Linter | so that I can ensure code quality, readability, and consistency with PEP 8 standards.          |

## Features

### Existing Features

| **Feature**                | **Notes**                                                                                                              | **Screenshot**                                               |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Multiple-Choice Questions  | Each question is presented with 4 answer choices, and users respond by entering a number (1–4).                        | ![screenshot](documentation/features/multiple-choice-questions.png)    |
| Input Validation (Answers) | The quiz validates user input to ensure only numbers between 1 and 4 are accepted to prevent invalid entries.          | ![screenshot](documentation/features/input-validation.png)   |
| Case-Insensitive Answers   | User answers are checked without considering case, ensuring fairness regardless of capitalization.                     | ![screenshot](documentation/features/case-insensitive.png)   |
| Answer Feedback            | The quiz provides immediate feedback after each question—indicating correct or incorrect and showing the right answer. | ![screenshot](documentation/features/answer-feedback.png)           |
| Score Tracking             | Tracks total, correct, and incorrect answers throughout the session, showing a final summary.                          | ![screenshot](documentation/features/score-feedback.png)     |
| Restart Quiz Option        | At the end of the quiz, users can restart without needing to manually rerun the application.                           | ![screenshot](documentation/features/restart-quiz.png)     |
| Restart Input Validation   | Only accepts “yes” or “no” inputs when asking users if they want to restart the quiz.                                  | ![screenshot](documentation/features/restart-validation.png) |
| Topic Selection            | Users can choose from five available topics before the quiz starts (e.g., Geography, History, etc.).                   | ![screenshot](documentation/features/choose-topic.png)    |
| Random Question Selection  | The quiz randomly selects and shuffles questions from the chosen topic to offer a unique experience each time.         | ![screenshot](documentation/features/random-question-selection.png)   |

### Future Features

| **Feature**                         | **Description**                                                                                                                                                    |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **User-Contributed Questions**      | Allow users to input their own multiple-choice questions, including four options and the correct answer, which are then validated and added to the relevant topic. |
| **High Score Tracking**             | Track and display the user’s highest score across all sessions, providing motivation to improve and recognize personal achievements.                               |
| **Timed Quiz Mode**                 | Introduce an optional mode where each question must be answered within a set time limit, increasing challenge and simulating time-pressured conditions.            |
| **Detailed Quiz Summary**           | Display a complete breakdown of all quiz questions, showing which were answered correctly and incorrectly, along with the correct answers for review.              |
| **Custom Question Count Selection** | Allow users to choose how many questions they wish to answer before starting the quiz, enabling flexible gameplay sessions of varying lengths.                     |


## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Lucidchart-grey?logo=lucid&logoColor=F97B2C)](https://www.lucidchart.com) | Flow diagrams for mapping the app's logic. |

## Database Design

### Data Model

#### Flowchart

To follow best practice, a flowchart was created for the app's logic, and mapped out using a free version of [Lucidchart](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning). The flowchart below represents the main process of this Python program. It shows the entire cycle of the application.

![screenshot](documentation/flowchart.png)

```mermaid
flowchart TD
    A([Start]) --> B[Import quiz questions and set score values to zero]
    B --> C[Request topic choice]
    C --> D{Is the data provided valid?}
    D -- No --> E[Print an error message to terminal to discuss what is wrong with data]
    E --> C
    D -- Yes --> F[Choose user-selected topic]
    F --> G[Select 10 questions from the chosen topic randomly]
    G --> H{Start loop while questions have not all been displayed}
    H --> I[Display question from randomly selected topic]
    I --> J[Display answer options]
    J --> K[Request user to select an answer option]
    K --> L{Is the data provided valid?}
    L -- No --> M[Print an error message to terminal to discuss what is wrong with data]
    M --> K
    L -- Yes --> N[Compare the user input with correct answer]
    N --> O{Is input correct?}
    O -- Yes --> P[Increment correct answer value]
    O -- No --> Q[Increment incorrect answer variable]
    P --> R[Display feedback]
    Q --> R
    R --> S{Have all 10 questions been displayed?}
    S -- No --> H
    S -- Yes --> T[Display score after all questions have been answered]
    T --> U{Request user if they wish to continue the quiz}
    U -- Yes --> C
    U -- No --> V([End])
```

Source: [Mermaid Flowchart for AcademIQ](https://mermaid.live/edit#pako:eNqtVE1z2jAQ_SsanZoZksHhI-BDOw0kgXwnJJ1pDQfFWrAmtuRKcihh-O_VF4xJe-ihPoAl7Xv73u5aa5wKCjjG81ws04xIjZ6GU47M8_VTMtFmY3aADg8_o9NkXJTCnP-s2Lv5AaWZ4AoRTpECjVQqJKA3kpsTpAV6BylmnunUEQySR3Awc1qyFKWZYCmEkIELGa7HBpsBokQTVErxxihQS8rol42PHJpIdCtc_FlyLxnXRgMCKYVEBShFFmDza5AF4yS375SptFIKLTOiETP_UvAFWjKduUxBw5mXWUvz3Vixe-fJIBNCAaoUyEMFOaTa6HI-AvjcBV4kE3eIomatRHMpCmfLWFbAg39pKieKfBUILhzBaO1qjnIhSiOX5VDjycgbIC6M3zxHL2CYjLEyJyugoTgjRzJOhn5_h_USthnRXx2MHfZyhyVcLUEiUbrkIejSBV3tWmkLYivsGW0j9mABdeVQ1__Q3etad2_-a3dvvPJamm13b5OBKEpipteKc44YLyvtKcxYS2_N-gpktw54Zw350BC1tXFX579PxjyVUADXH9j85zKrYYL1hxqE8T9AkpGXfIu7d4jHXd_mAPSFpK_h-MEf-8WjW0zWIztJdor25nR_pLZeJjVdo9rW1t7TLrO_AsjcNMeRf5hcR-89AA3qnhzF83pvntjcdmJl6q8y2-BUcM145ftjr5-g7LkuY1DbC2q_fUrOOJ0dTDlu4IVkFMdaVtDAhZkeYpd4bVFTbIgLmOLYvFIiX6d4yjcGUxL-Q4hiC5OiWmQ4npNcmVVVmumCISMLSYrdLqm0mKx4usMApyAHouIax512z5HieI1_4bjV6x31m51Ws9U5PmlF7Wa3gVc4bnePTjrN5nHU7kadKGpHmwZ-dzKaR72Tdt88vW7UivpRp9_AQJkW8sbf4u4y3_wG8njeSQ)

#### Classes & Functions

The primary functions used on this application are:

- `get_random_questions_with_shuffled_options()`
    - Randomly selects a specified number of questions from the provided list.
- `topic_choice()`
    - Selects the subject based on user input and validates input.
- `reset_game()`
    - Resets the game state to start of user flow. 
- `score_tracker()`
    - Track correct and incorrect answers and total score.
- `input_validation()`
    - Validates user input against a list of valid inputs.
- `run_game()`
    - Main function to run the quiz game.
- `main()`
    - Runs the run_game() function

#### Imports

⚠️ INSTRUCTIONS ⚠️

Use this space to explain your Python imports and packages, with some common examples found below.

⚠️ --- END --- ⚠️

I've used the following Python packages and external imports.

- `gspread`: used with the Google Sheets API
- `google.oauth2.service_account`: used for the Google Sheets API credentials
- `time`: used for adding time delays
- `os`: used for adding a `clear()` function
- `colorama`: used for including color in the terminal
- `random`: used to get a random choice from a list

## Agile Development Process

### GitHub Projects

⚠️ TIP ⚠️

Consider adding screenshots of your Projects Board(s), Issues (open and closed), and Milestone tasks.

⚠️ --- END ---⚠️

[GitHub Projects](https://www.github.com/RadwanDuadu/AcademIQ/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/RadwanDuadu/AcademIQ/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/RadwanDuadu/AcademIQ)](https://www.github.com/RadwanDuadu/AcademIQ/issues) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/RadwanDuadu/AcademIQ)](https://www.github.com/RadwanDuadu/AcademIQ/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser. This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://academ-iq-b9bb24eb3c99.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of **KEY** to `PORT`, and the **VALUE** to `8000` then select **ADD**.
- If using any confidential credentials, such as **CREDS.JSON**, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important; select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: node index.js > Procfile`

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The Python terminal window should now be connected and deployed to Heroku!



### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/RadwanDuadu/AcademIQ).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/RadwanDuadu/AcademIQ.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/RadwanDuadu/AcademIQ)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/RadwanDuadu/AcademIQ).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss any differences between the local version you've developed, and the live deployment site. Generally, there shouldn't be [m]any major differences, so if you honestly cannot find any differences, feel free to use the following example:

⚠️ --- END --- ⚠️

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

⚠️ INSTRUCTIONS ⚠️

In the following sections, you need to reference where you got your content, media, and any extra help. It is common practice to use code from other repositories and tutorials (which is totally acceptable), however, it is important to be very specific about these sources to avoid potential plagiarism.

⚠️ --- END ---⚠️

### Content

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links for any borrowed code snippets, elements, and resources. Ideally, you should provide an actual link to every resource used, not just a generic link to the main site. If you've used multiple components from the same source (such as Bootstrap), then you only need to list it once, but if it's multiple Codepen samples, then you should list each example individually. If you've used AI for some assistance (such as ChatGPT or Perplexity), be sure to mention that as well. A few examples have been provided below to give you some ideas.

Eventually you'll want to learn how to use Git branches. Here's a helpful tutorial called [Learn Git Branching](https://learngitbranching.js.org) to bookmark for later.

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [Love Sandwiches](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Real Python](https://realpython.com/python-quiz-application) | Inspiration for a quiz app |
| [BroCode](https://www.youtube.com/watch?v=ag8NtD1e0Kc) | Inspiration for hangman game |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [Colorama](https://www.youtube.com/watch?v=u51Zjlnui4Y) | Adding color in Python |
| [StackOverflow](https://stackoverflow.com/a/50921841) | Clear screen in Python |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links to any media files borrowed from elsewhere (images, videos, audio, etc.). If you're the owner (or a close acquaintance) of some/all media files, then make sure to specify this information. Let the assessors know that you have explicit rights to use the media files within your project. Ideally, you should provide an actual link to every media file used, not just a generic link to the main site, unless it's AI-generated artwork.

Looking for some media files? Here are some popular sites to use. The list of examples below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links by sending yourself (or Slackbot) the following command: `!freemedia`.

- Images
    - [Pexels](https://www.pexels.com)
    - [Unsplash](https://unsplash.com)
    - [Pixabay](https://pixabay.com)
    - [Lorem Picsum](https://picsum.photos) (placeholder images)
    - [Wallhere](https://wallhere.com) (wallpaper / backgrounds)
    - [This Person Does Not Exist](https://thispersondoesnotexist.com) (reload to get a new person)
- Audio
    - [Audio Micro](https://www.audiomicro.com/free-sound-effects)
    - [Button Clicks](https://www.zapsplat.com/sound-effect-category/button-clicks)
    - [Lasers & Weapons](https://www.zapsplat.com/sound-effect-category/lasers-and-weapons/page/5)
    - [Puzzle Music](https://soundimage.org/puzzle-music)
    - [Camtasia Audio](https://library.techsmith.com/camtasia/assets/Audio)
- Video
    - [Videvo](https://www.videvo.net)
- Image Compression
    - [TinyPNG](https://tinypng.com) (for images <5MB)
    - [CompressPNG](https://compresspng.com) (for images >5MB)

A few examples have been provided below to give you some ideas on how to do your own Media credits.

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [ASCII Art Archive](https://www.asciiart.eu) | Pre-defined ASCII art |
| [TEXT-IMAGE](https://www.text-image.com) | Converting an image to ASCII art |
| [Patorjk](https://patorjk.com/software/taag) | Converting text to ASCII art |

### Acknowledgements

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution and acknowledgement to any supports that helped, encouraged, or supported you throughout the development stages of this project. It's always lovely to appreciate those that help us grow and improve our developer skills. A few examples have been provided below to give you some ideas.

⚠️ --- END ---⚠️

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.

