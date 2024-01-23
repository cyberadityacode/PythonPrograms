# Guess the Random Word
import random

def shuffle_word(word):
    """Shuffle the letters of a word."""
    char_list = list(word)
    random.shuffle(char_list)
    return ''.join(char_list)

def guess_word(guess_user_word, pick_word):
    """Check if the user's guess is correct."""
    return guess_user_word.lower() == pick_word.lower()

def display_round_result(is_correct):
    """Display the result of each round."""
    if is_correct:
        print("Correct!\n")
    else:
        print("Incorrect.\n")

def play_round(word_list):
    """Play a single round of the word-guessing game."""
    pick_word = random.choice(word_list)
    shuffled_word = shuffle_word(pick_word)
    
    print("Shuffled word:", shuffled_word)
    
    try:
        guess_user_word = input("Guess this word: ").strip()
        if not guess_user_word:
            raise ValueError("Enter non empty word")
            
    except ValueError as e:
        print(e)

    is_correct = guess_word(guess_user_word, pick_word)
    display_round_result(is_correct)

    return is_correct, pick_word

def main():
    word_list = ["impeccable", "amazing", "vocabulary", "professional", "improvement"]
    max_attempts = 3
    count_score = 0

    for attempt in range(max_attempts):
        is_correct, picked_word  = play_round(word_list)
        if is_correct:
            count_score += 1

    print("Your score is", count_score)

if __name__ == "__main__":
    main()
