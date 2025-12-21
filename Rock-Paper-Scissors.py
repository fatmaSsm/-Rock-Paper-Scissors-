import random

""" COLORS """
RESET = "\033[0m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
""" ------- """

choices = {
    1: "✊",
    2: "✋",
    3: "✌️"
}

print(BLUE + "╔═════════════════════╗")
print("║" + RESET + WHITE + " Rock Paper Scissors " +RESET + BLUE + "║")
print("╚═════════════════════╝")

while True:
    print(BLUE + "╔═════════════════════╗")
    print("║" + RESET + WHITE + " 1) ✊"+RESET + BLUE + "               ║")
    print("║" + RESET + WHITE + " 2) ✋"+RESET + BLUE + "               ║")
    print("║" + RESET + WHITE + " 3) ✌️"+RESET + BLUE + "                ║")
    print("║" + RESET + WHITE + " 0) Exit"+RESET + BLUE + "             ║")
    print("╚═════════════════════╝"+ RESET)
    try:
        player_choice = int(input(MAGENTA + "\nPick a number: " + RESET))

        if player_choice == 0:
            print(CYAN + "\nGame Over.🪄" + RESET)
            break

        if player_choice not in choices:
            print("Invalid Choice! Please Select 1, 2 or 3.")
            continue

        cpu_choice = random.randint(1, 3)

        print(f"\nYou Chose: {choices[player_choice]}")
        print(f"CPU Chose: {choices[cpu_choice]}")

        if player_choice == cpu_choice:
            print(YELLOW + "It's a tie!" + RESET)
        elif (
            (player_choice == 1 and cpu_choice == 3) or
            (player_choice == 2 and cpu_choice == 1) or
            (player_choice == 3 and cpu_choice == 2)
        ):
            print(GREEN + "You Win!" + RESET)
        else:
            print(RED + "You lose!" + RESET)

    except ValueError:
        print("Please Enter a Valid Number!")
