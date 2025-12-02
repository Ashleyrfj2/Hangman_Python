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
lives = 9
letters_guessed = [ ]
guessed = False


print("Let's play Hangman!")
print("The word to guess has", len(selected_word), "letters.")


while lives > 0 and not end_of_game:
    print("")
    user_input = input("Guess a letter: ").lower()
    if user_input in letters_guessed:
        print("")
        print("You've already guessed that letter. Try again.")
        print("")
    elif user_input not in selected_word:
        letters_guessed.append(user_input)
        print("")
        print(f"You guessed {user_input}, that's not in the word. You lose a life.")
        lives -= 1
        print(f"Lives: {lives}.")
        print("")
    elif user_input in selected_word:
        letters_guessed.append(user_input)
        print("")
        print(f"Good job! {user_input} is in the word.")
        print("")
        for position in range(len(selected_word)):
            letter = selected_word[position]
            if letter == user_input:
                display[position] = letter
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        guessed = True
        break

        
print("")

if guessed:
    print("-----------------------------------------" )
    print("You got it, I let you win though.")
else:
    print("-------------LOSER--------------" )
    print("The word was:", selected_word)
    print("Epic fail!")