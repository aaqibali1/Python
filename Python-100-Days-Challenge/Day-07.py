import random

def choose_word():
    words = ["python", "hangman", "programming", "challenge", "developer", "software"]
    return random.choice(words)

def display(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    return display_word

def hangman():
    print("🎉 Welcome to Hangman! 🎉")
    word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of incorrect guesses allowed

    while attempts > 0:
        print("\nWord:", display(word, guessed_letters))
        print(f"Remaining Attempts: {attempts}")
        print("Guessed Letters:", " ".join(guessed_letters))
        
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter!")
            continue
        
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("✅ Good guess!")
        else:
            print("❌ Wrong guess!")
            attempts -= 1
        
        # Check if the word is completely guessed
        if "_" not in display(word, guessed_letters):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n💀 Game Over! The word was:", word)

# Run the game
hangman()
