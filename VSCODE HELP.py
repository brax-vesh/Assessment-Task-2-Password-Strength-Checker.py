# Simple text adventure game to demonstrate program tracing

def start_adventure():
    print("You are in a dark forest. You see a path to the left and a path to the right.")
    choice = input("Which path do you choose? (left/right): ")
    if choice == "left":
        encounter_dragon()
    elif choice == "right":
        find_treasure()
    else:
        print("Invalid choice! The game will restart.")
        start_adventure()

def encounter_dragon():
    print("You encounter a dragon!")
    choice = input("Do you fight or run? (fight/run): ")
    if choice == "fight":
        print("You bravely fight the dragon and win!")
        end_adventure("victory")
    elif choice == "run":
        print("You run away safely.")
        end_adventure("safe")
    else:
        print("Invalid choice! The dragon eats you.")
        end_adventure("defeat")

def find_treasure():
    print("You find a treasure chest!")
    choice = input("Do you open it or leave it? (open/leave): ")
    if choice == "open":
        print("You find a heap of gold!")
        end_adventure("rich")
    elif choice == "leave":
        print("You leave the treasure and walk away.")
        end_adventure("safe")
    else:
        print("Invalid choice! The chest disappears.")
        end_adventure("mystery")

def end_adventure(outcome):
    if outcome == "victory":
        print("Congratulations! You are victorious!")
    elif outcome == "safe":
        print("You are safe and sound.")
    elif outcome == "rich":
        print("You are now rich!")
    elif outcome == "defeat":
        print("You were defeated by the dragon.")
    elif outcome == "mystery":
        print("The mystery of the chest remains unsolved.")
    print("The adventure ends here.")

if __name__ == "__main__":
    start_adventure()