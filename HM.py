import random
from Hangman_Art import stages, logo
from Hangman_Words import word_List

# Write Code 💻
print("\n" + logo + "\n")
name = input("\n\nKaede : What's Your Name -> ")
random_Word = random.choice(word_List)
word_Length = len(random_Word)
end_Of_Game = False
lives_Count = len(stages) - 1

display_Board = []

for letter in range(word_Length):
    display_Board.append("_")

while not end_Of_Game:
    guess = input(f"\n\nKaede : What's Your Guess?\n\n\nKaede : A Word That Contains {len(random_Word)} Characters.\n\n\n{name} : ").lower()
    print("\n")
    for i in range(word_Length):
        if random_Word[i] == guess:
            display_Board[i] = random_Word[i]
    print(' '.join(display_Board))
    print("\n")

    if guess not in random_Word:
        lives_Count -= 1
        if lives_Count != 0:
            print(f"Kaede : You Lose A Life, You have {lives_Count} Lives Remaining.")
        print(f"{stages[lives_Count]}")

        if lives_Count == 0:
            end_Of_Game = True
            print("\nKaede : You Lost.\n\n")
            print(f"Kaede : The Word Is {random_Word}.\n")

    if "_" not in display_Board:
        end_Of_Game = True
        print("Kaede : You Won!\n\n")
        print(f"Kaede : The Word Is {random_Word}.\n")
