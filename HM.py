import random
from Hangman_Art import stages, logo
from Hangman_Words import word_List

# Write Code 💻
print(logo)
random_Word = random.choice(word_List)
word_Length = len(random_Word)
end_Of_Game = False
lives_Count = len(stages) - 1

display = []

for letter in range(word_Length):
    display.append("_")

while not end_Of_Game:
    guess = input(f"Kaede : What's Your Guess?\n\n{' '.join(display)}\n\n\n")
    print("\n\n")
    for i in range(word_Length):
        if random_Word[i] == guess.lower():
            display[i] = random_Word[i]
    print(' '.join(display))
    print("\n")

    if guess not in random_Word:
        lives_Count -= 1
        print(f"\n\nKaede : You Lose A Life, You have {lives_Count} Lives.")
        print(f"{stages[lives_Count]}")

        if lives_Count == 0:
            end_Of_Game = True
            print("Kaede : You Lost. \n\n")
            print(f"Kaede : The Word Is {random_Word}")

    if "_" not in display:
        end_Of_Game = True
        print("Kaede : You Won! \n\n")
