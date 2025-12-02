import random

hangman_list = [
    "astronomy",
    "backpacks",
    "butterfly",
    "celebrate",
    "dandelion",
    "elevation",
    "fantastic",
    "gargoyle",
    "happiness",
    "invisible",
    "jubilance",
    "knowledge",
    "lighthouse",
    "magnitude",
    "notoriety",
    "overgrown",
    "pineapple",
    "quenching",
    "radiation",
    "sandstorm",
    "treasure",
    "umbrella",
    "volunteer",
    "wanderers",
    "zephyrion"
]

selected_word = random.choice(hangman_list)
display = ["_" for _ in range(len(selected_word))] #Puts _ for the length of the selected word which is chsen randomly from the list 
end_of_game = False
lives = 8
letters_guessed = [ ]
guessed = False


print("Let's play Hangman!")
print("The word to guess has", len(selected_word), "letters.")


while lives > 0 and not end_of_game:
    user_input = input("Guess a letter: ").lower()
    if user_input in letters_guessed:
        print("You've already guessed that letter. Try again.")
    elif user_input not in selected_word:
        letters_guessed.append(user_input)
        print(f"You guessed {user_input}, that's not in the word. You lose a life.")
        lives -= 1
        print(f"Lives: {lives}.")
    elif user_input in selected_word:
        letters_guessed.append(user_input)
        print(f"Good job! {user_input} is in the word.")
        for position in range(len(selected_word)):
            letter = selected_word[position]
            if letter == user_input:
                display[position] = letter
    print(f"{' '.join(display)}")
else:
    if "_" not in display:
        end_of_game = True
        guessed = True
        

print("The word was:", selected_word)
if guessed:
    print("I let you win")
else:
    print("Epic fail!")