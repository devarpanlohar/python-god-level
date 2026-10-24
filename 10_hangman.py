import random

word_list = [
    "python",
    "monster",
    "tamluk",
    "github",
    "developer",
    "falakata",
    "programming",
]

stages = [
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |

""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |

""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |

""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |

""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |

""",
    """
  +---+
  |   |
  O   |
      |
      |
      |

""",
    """
  +---+
  |   |
      |
      |
      |
      |

""",
]

secret = random.choice(word_list)
print(f"[For debug purpose] selected word is: {secret}")  # For debug
display = ["_"] * len(secret)
guessed = []
lives = 6
round = 0

while True:
    round += 1
    print(f"\n==== {round} try ====")
    print("Guess the word: " + " ".join(display))
    print(f"Lives: {lives} | Guessed: {', '.join(guessed)}")

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input!")
        continue

    if guess in guessed:
        print("Already guessed")
        continue

    guessed.append(guess)

    if guess in secret:
        for i, letter in enumerate(secret):
            if letter == guess:
                display[i] = guess

    else:
        lives -= 1
        print(stages[lives])
        print(f"{guess} not in word")

    if "_" not in display:
        print("You win the game")
        print(f"The word was: {secret}")
        break
    elif lives == 0:
        print(stages[0])
        print("You lost the game")
        print(f"The word was: {secret}")
        break
