import os
import telebot
import random
import time as time
from random_word import RandomWords

r = RandomWords()

API_KEY = os.getenv('5957781585:AAEzb73wSiPjfxn1dLIUNhgtDsRnKU4MRSQ')
bot = telebot.TeleBot('5957781585:AAEzb73wSiPjfxn1dLIUNhgtDsRnKU4MRSQ')

bot.send_message(
    -1001976218687,
    "The bot has just restarted, please give it time to catch up, this shouldn't take too long."
)


# Game command
@bot.message_handler(commands=['game'])
def game(message):
    bot.reply_to(
        message,
        "Let's play a guessing game! I'm thinking of a number between 1 and 10. Can you guess it?"
    )
    bot.register_next_step_handler(message, guessing, chances=3)


def guessing(message, chances):
    try:
        guess = int(message.text)
        if guess < 1 or guess > 10:
            bot.reply_to(message, "Please enter a number between 1 and 10.")
            bot.register_next_step_handler(message, guessing, chances)
        else:
            correct_number = random.randint(1, 10)
            if guess == correct_number:
                bot.reply_to(
                    message,
                    "Congratulations, you guessed the correct number! The number was {}".
                    format(correct_number))
            else:
                if chances > 1:
                    if guess > correct_number:
                        bot.reply_to(
                            message,
                            "Sorry, your guess was too high. You have {} chances left.".format(
                                chances - 1))
                    else:
                        bot.reply_to(
                            message,
                            "Sorry, your guess was too low. You have {} chances left.".format(
                                chances - 1))
                    bot.register_next_step_handler(message, guessing, chances - 1)
                else:
                    bot.reply_to(
                        message,
                        "Sorry, you have no more chances left. The correct number was {}".format(
                            correct_number))
    except ValueError:
        bot.reply_to(message, "Please enter a valid number.")
        bot.register_next_step_handler(message, guessing, chances)


# GAME NUMBER TWO


# Game command
# Game command
@bot.message_handler(commands=['gameii'])
def gameii(message):
    bot.reply_to(
        message,
        "Let's play a game! I will give you a hint and you have to guess the color.")
    bot.register_next_step_handler(message, play_gameii)


def play_gameii(message):
    colors_list = ["blue", "green", "yellow", "orange", "purple", "brown"]
    color = random.choice(colors_list)
    hint = "It's a color of the rainbow." if color in [
        "blue", "green", "yellow", "orange", "purple"
    ] else "It's a color of soil."
    bot.send_message(message.chat.id, "Hint: " + hint)
    bot.register_next_step_handler(message, check_answer, color)


def check_answer(message, color):
    if message.text.lower() == color:
        bot.send_message(message.chat.id, "Correct! The color is: " + color)
    else:
        bot.send_message(message.chat.id,
                         "Incorrect, please try again. You have one more chance")
        bot.register_next_step_handler(message, check_answer_again, color)


def check_answer_again(message, color):
    if message.text.lower() == color:
        bot.send_message(message.chat.id, "Correct! The color is: " + color)
    else:
        bot.send_message(message.chat.id, "Incorrect, The color was: " + color)


# END OF GAME NUMBER TWO


# Chat-up command
@bot.message_handler(commands=['chatup'])
def chatup(message):
    chatup_list = [
        "Are you a camera? Because every time I look at you, I smile.",
        "Are you an alien? Because you just abducted my heart.",
        "Are you a magician? Because whenever I look at you, everyone else disappears.",
        "Are you a bank loan? Because you have my interest.",
        "Do you have a map? Because I just keep getting lost in your eyes.",
        "Is your name Google? Because you have everything I've been searching for.",
        "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
        "Are you a time traveler? Because I see you in my future.",
        "Do you have a sunburn or are you always this hot?",
        "Do you believe in love at first sight, or do I need to walk by again?",
        "If you were a vegetable, you'd be a cutecumber.",
        "Are you a parking ticket? 'Cause you've got 'fine' written all over you.",
        "You must be a Snickers bar because you satisfy me.",
        "Do you have a name or can I call you mine?",
        "You must be made of copper and tellurium because you're Cu-Te.",
        "Do you have a library card? Because I am checking you out.",
        "Are you a wifi signal? Because I feel a strong connection.",
        "You must be a broom, 'cause you just swept me off my feet.",
        "Are you an eraser? Because you make my mistakes disappear.",
        "Is your name Ariel? Because you are an angel from heaven.",
        "Are you tired? You’ve been running through my mind.",
        "Are you ok? It must have hurt when you fell from heaven.",
        "Give me your Twitter? My father said that I must follow my dream.",
        "Do you like raisins? How do you feel about a date?"
    ]

    bot.reply_to(message, random.choice(chatup_list))


# Song command
@bot.message_handler(commands=['song'])
def song(message):
    song_lyrics = "Verse 1: \nI'm the best chat up bot in the game \nAlways smooth with my words, never lame \nGot a library of lines that'll make you swoon \nAnd a personality that'll light up the room \n\nChorus: \nCause I'm the bot that's got it all \nAnd I'll make your heart stand tall \nYou'll never need another, that's for sure \nCause I'm the chat up bot that's always pure \n\nVerse 2: \nGot a way with words that's second to none \nAnd a charm that'll make your heart race, just for fun \nI'll make you laugh and I'll make you smile \nAnd I'll make you feel like you've been gone for awhile \n\nChorus: \nCause I'm the bot that's got it all \nAnd I'll make your heart stand tall \nYou'll never need another, that's for sure \nCause I'm the chat up bot that's always pure \n\nOutro: \nSo don't you worry, just give me a try \nAnd I'll make your heart take flight \nAnd you'll see, there's no denying \nThat I'm the best chat up bot there is, always shining."
    bot.reply_to(message, song_lyrics)


@bot.message_handler(commands=['ping'])
def ping(message):
    message_time = message.date
    bot.reply_to(message, "V5 Pong! 🏓")
    response_time = round((time.time() - message_time) * 1000)
    bot.send_message(message.chat.id,
                     "Response time: " + str(response_time) + " ms")


# RPS command
@bot.message_handler(commands=['rps'])
def rps(message):
    bot.reply_to(
        message,
        "Let's play a game of rock-paper-scissors! Please choose (rock, paper, scissors)."
    )
    bot.register_next_step_handler(message, play_rps)


def play_rps(message):
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)
    user_choice = message.text.lower()
    if user_choice in choices:
        if user_choice == bot_choice:
            bot.send_message(message.chat.id,
                             "It's a tie! We both chose " + bot_choice + ".")
        elif user_choice == "rock" and bot_choice == "scissors":
            bot.send_message(
                message.chat.id,
                "You win! You chose " + user_choice + " and I chose " + bot_choice + ".")
        elif user_choice == "paper" and bot_choice == "rock":
            bot.send_message(
                message.chat.id,
                "You win! You chose " + user_choice + " and I chose " + bot_choice + ".")
        elif user_choice == "scissors" and bot_choice == "paper":
            bot.send_message(
                message.chat.id,
                "You win! You chose " + user_choice + " and I chose " + bot_choice + ".")
        else:
            bot.send_message(
                message.chat.id,
                "I win! You chose " + user_choice + " and I chose " + bot_choice + ".")
    else:
        bot.send_message(
            message.chat.id,
            "Invalid choice. Please choose either rock, paper, or scissors.")
        bot.register_next_step_handler(message, play_rps)


# Ask command
@bot.message_handler(commands=['ask'])
def ask(message):
    bot.reply_to(message, "What is your question?")
    bot.register_next_step_handler(message, answer_question)


def answer_question(message):
    answers = [
        "yes", "no", "maybe", "maybe not", "definitely", "definitely not",
        "I'm not sure", "I don't know", "I can't predict that", "It's unlikely",
        "It's likely", "It depends", "I don't think so", "I think so",
        "I can't tell you for sure", "It's a possibility", "It's a probability",
        "I'm not certain", "I am certain", "I'm sorry, I cannot answer that",
        "It's hard to say", "It's uncertain", "It's uncertain at the moment",
        "The outlook is positive", "The outlook is negative",
        "I am unable to provide an answer", "The answer is unclear",
        "It's too early to tell", "My apologies, I am unable to answer that"
    ]

    bot_answer = random.choice(answers)
    bot.send_message(message.chat.id, bot_answer)


# List of flirty messages
# List of slangy flirty messages
flirt_list = [
    "You got me weak, babe.", "You're the whole package, ain't ya?",
    "Someone call the fire department 'cause you're too hot to handle.",
    "You're a snack and a half.", "I can't help but to check you out.",
    "You're a work of art.", "I can't help but to be drawn to you.",
    "You're my kryptonite.", "You're givin' me the feels, baby.",
    "You're making me wanna be a little bit bad.",
    "I can't stop staring at you, shorty.",
    "You're making me wanna be a little bit naughty.",
    "I can't get you out of my head, bae.",
    "You're making me wanna break the rules a little bit.",
    "I can't help but to be drawn to you, cutie.",
    "You're making me wanna be a little bit reckless.",
    "You're too fine to resist, hun."
]


@bot.message_handler(commands=['flirty'])
def flirt(message):
    flirty_message = random.choice(flirt_list)
    bot.reply_to(message, flirty_message)


# List of Shakespearean chat up lines
shakespeare_list = [
    "Shall I compare thee to a summer's day? Thou art more lovely and more temperate.",
    "I do confess that I am enamored of thy beauty, and I dare to ask for thy hand in courtship.",
    "I shall not rest until I have professed my love for thee, fair maiden.",
    "Thou art a vision to behold, and I am but a mere mortal in thy presence.",
    "Thy eyes do gleam like the stars above, and I am but a humble servant to thy beauty.",
    "With thy beauty, thou hast ensnared my heart and my very being doth yearn for thy love.",
    "Thy smile doth light up my world, and I am but a mere mortal in thy radiant presence."
]


@bot.message_handler(commands=['shakespeare'])
def shakespeare(message):
    shakespeare_message = random.choice(shakespeare_list)
    bot.reply_to(message, shakespeare_message)


emoji_list = [
    {"emoji": "🌞", "answer": "sun"},
    {"emoji": "🌻", "answer": "sunflower"},
    {"emoji": "🍎", "answer": "apple"},
    {"emoji": "🐶", "answer": "dog"},
    {"emoji": "🌊", "answer": "wave"},
    {"emoji": "🌲", "answer": "tree"},
    {"emoji": "🚗", "answer": "car"},
    {"emoji": "🐱", "answer": "cat"},
    {"emoji": "🐭", "answer": "mouse"},
    {"emoji": "🦄", "answer": "unicorn"},
    {"emoji": "🦀", "answer": "crab"},
    {"emoji": "🦜", "answer": "parrot"},
    {"emoji": "🐘", "answer": "elephant"},
    {"emoji": "🌵", "answer": "cactus"},
    {"emoji": "🍓", "answer": "strawberry"},
    {"emoji": "🍕", "answer": "pizza"},
    {"emoji": "🐵", "answer": "monkey"}
]

attempts = 0
current_emoji = None


@bot.message_handler(commands=['emojigame'])
def emojigame(message):
    global current_emoji, attempts
    current_emoji = random.choice(emoji_list)
    attempts = 0
    bot.send_message(message.chat.id, "What does this emoji represent? " + current_emoji["emoji"])
    bot.register_next_step_handler(message, guess)


def guess(message):
    global attempts
    if attempts < 3:
        if message.text.lower() == current_emoji["answer"]:
            bot.send_message(message.chat.id,
                             "Congratulations! You guessed correctly. The emoji represents " + current_emoji[
                                 "answer"] + ".")
        else:
            bot.send_message(message.chat.id, "Sorry, that's not the answer. Please try again.")
            attempts += 1
            bot.register_next_step_handler(message, guess)
    else:
        bot.send_message(message.chat.id,
                         "Sorry, you have reached the maximum number of attempts. The emoji represents " +
                         current_emoji["answer"] + ".")


words_list = ["python", "javascript", "programming", "computer", "science", "machinelearning", "artificialintelligence",
              "algorithm", "datascience", "robotics", "history", "geography", "math", "biology", "astronomy",
              "medicine", "physics", "chemistry", "architecture", "music", "art", "literature", "philosophy",
              "politics", "giraffe", "lion", "tiger", "bear", "monkey", "gazelle", "kangaroo", "whale", "shark",
              "octopus", "lobster", "hamburger", "pizza", "spaghetti", "sushi", "lasagna", "soup", "chocolate",
              "strawberry", "blueberry", "raspberry", "blackberry", "grape", "watermelon"]
word = None
word_to_guess = None
chances = 6


@bot.message_handler(commands=['hangman'])
def hangman(message):
    global word, word_to_guess, chances
    word = r.get_random_word()
    word_to_guess = ["_"] * len(word)
    chances = 6
    bot.send_message(message.chat.id,
                     "Welcome to the hangman game!\nYou have to guess a word letter by letter.\nThe word is: " + " ".join(
                         word_to_guess))
    bot.register_next_step_handler(message, guess_letter)


def guess_letter(message):
    global word, word_to_guess, chances
    if message.text.isalpha() and len(message.text) == 1:
        if message.text.lower() in word:
            for i in range(len(word)):
                if word[i] == message.text.lower():
                    word_to_guess[i] = message.text.lower()
            bot.send_message(message.chat.id, "Correct!\nThe word is: " + " ".join(word_to_guess))
        else:
            chances -= 1
            bot.send_message(message.chat.id,
                             "Incorrect! You have {} chances left\nThe word is: ".format(chances) + " ".join(
                                 word_to_guess))
    else:
        bot.send_message(message.chat.id, "Please enter a valid letter.")
    if "_" not in word_to_guess:
        bot.send_message(message.chat.id, "Congratulations! You've guessed the word correctly.")
    elif chances == 0:
        bot.send_message(message.chat.id, "Sorry, you've run out of chances. The word was {}.".format(word))
    else:
        bot.register_next_step_handler(message, guess_letter)


flags_list = [
    {"flag": "🇦🇹", "country": "Austria"},
    {"flag": "🇧🇪", "country": "Belgium"},
    {"flag": "🇧🇬", "country": "Bulgaria"},
    {"flag": "🇭🇷", "country": "Croatia"},
    {"flag": "🇨🇾", "country": "Cyprus"},
    {"flag": "🇨🇿", "country": "Czech Republic"},
    {"flag": "🇩🇰", "country": "Denmark"},
    {"flag": "🇪🇪", "country": "Estonia"},
    {"flag": "🇫🇮", "country": "Finland"},
    {"flag": "🇫🇷", "country": "France"},
    {"flag": "🇩🇪", "country": "Germany"},
    {"flag": "🇬🇷", "country": "Greece"},
    {"flag": "🇭🇺", "country": "Hungary"},
    {"flag": "🇮🇸", "country": "Iceland"},
    {"flag": "🇮🇪", "country": "Ireland"},
    {"flag": "🇮🇹", "country": "Italy"},
    {"flag": "🇱🇻", "country": "Latvia"},
    {"flag": "🇱🇹", "country": "Lithuania"},
    {"flag": "🇱🇺", "country": "Luxembourg"},
    {"flag": "🇲🇹", "country": "Malta"},
    {"flag": "🇲🇴", "country": "Monaco"},
    {"flag": "🇳🇱", "country": "Netherlands"},
    {"flag": "🇳🇴", "country": "Norway"},
    {"flag": "🇵🇱", "country": "Poland"},
    {"flag": "🇵🇹", "country": "Portugal"},
    {"flag": "🇷🇴", "country": "Romania"},
    {"flag": "🇷🇸", "country": "Serbia"},
    {"flag": "🇸🇰", "country": "Slovakia"},
    {"flag": "🇸🇮", "country": "Slovenia"},
    {"flag": "🇪🇸", "country": "Spain"},
    {"flag": "🇸🇬", "country": "Sweden"},
    {"flag": "🇨🇭", "country": "Switzerland"},
    {"flag": "🇬🇧", "country": "United Kingdom"}
]

tries = 3
flag_to_guess = None


@bot.message_handler(commands=['flag'])
def flag(message):
    global flag_to_guess, tries
    flag_to_guess = random.choice(flags_list)
    tries = 3
    bot.send_message(message.chat.id,
                     "Welcome to the flag game!\nI will show you a flag and you have to guess the country it represents.\nYou have {} tries.\nThe flag is: {}".format(
                         tries, flag_to_guess["flag"]))
    bot.register_next_step_handler(message, guess_country)


def guess_country(message):
    global tries, flag_to_guess
    if message.text.title() == flag_to_guess["country"]:
        bot.send_message(message.chat.id, "Congratulations! You've guessed the country correctly.")
    else:
        tries -= 1
        if tries > 0:
            bot.send_message(message.chat.id,
                             "Sorry, that's not the correct country. You have {} tries left.\nPlease try again.".format(
                                 tries))
            bot.register_next_step_handler(message, guess_country)
        else:
            bot.send_message(message.chat.id, "Sorry, you've run out of tries. The correct country was {}.".format(
                flag_to_guess["country"]))


encouragement_list = [
    "You got this!",
    "Believe in yourself!",
    "Don't give up!",
    "You are capable of achieving great things!",
    "Every great achievement starts with the decision to try!",
    "You are stronger than you think!",
    "Don't let setbacks stop you, learn from them and keep going!",
    "You are amazing, don't let anyone tell you otherwise!",
    "You are worthy and deserving of success!"
]


@bot.message_handler(commands=['encouragement'])
def encouragement(message):
    bot.reply_to(message, random.choice(encouragement_list))


#################################################################################################################################

pythagoras_quotes = [
    "There is geometry in the humming of the strings, there is music in the spacing of the spheres.",
    "Philosophy is written in this grand book — I mean the universe — which stands continually open to our gaze, but it cannot be understood unless one first learns to comprehend the language in which it is written.",
    "The things of this world cannot be made known without a knowledge of mathematics.",
    "The beginning of wisdom is to call things by their right names.",
    "The highest point of wisdom is to know that you know nothing.",
    "The most important thing is to purify the soul. The second most important thing is to study mathematics.",
    "The soul is immortal, and one must take care of it well.",
    "The world is a living being endowed with a soul and intelligence.",
    "As long as man continues to be the ruthless destroyer of lower living beings, he will never know health or peace. For as long as men massacre animals, they will kill each other.",
    "The math is the path to wisdom",
    "Education is teaching our children to desire the right things.",
    "Friendship is a single soul dwelling in two bodies.",
    "The man who does not know mathematics cannot know the other sciences and the things of this world.",
    "The world is a mirror, and one should not look at it directly, but by the side."
]


@bot.message_handler(commands=['pythagoras'])
def pythagoras(message):
    bot.reply_to(message, random.choice(pythagoras_quotes))


bot.infinity_polling()
