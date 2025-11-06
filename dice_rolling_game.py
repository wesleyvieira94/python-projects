import random
while True:
    input_choice = input("Roll the dice? (y/n): ").lower()
    if input_choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled: {die1} and {die2}")
    elif input_choice == 'n':
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")
