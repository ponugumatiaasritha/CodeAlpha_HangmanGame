import random
words = ["python", "computer", "program", "student", "hangman"]
word = random.choice(words)

guessed_letters = []

attempts = 6

print("====== HANGMAN GAME ======")
print("Guess the word one letter at a time!")
print("You have", attempts, "incorrect guesses.\n")

while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)


    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break


    guess = input("Enter a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.\n")
        continue


    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)
    if guess in word:
        print("✅ Correct!\n")
    else:
        attempts -= 1
        print("❌ Wrong!")
        print("Remaining incorrect guesses:", attempts, "\n")
if attempts == 0:
    print("😢 Game Over!")
    print("The correct word was:", word)