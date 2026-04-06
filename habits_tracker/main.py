from datetime import datetime

habits = [
    "Practice coding (30 min)",
    "Practice French",
    "Drink 1.5L water",
    "Sleep before 23:00",
    "Physical activity",
    "Walk 5000 steps"
]

def show_habits():
    print("\nYour habits:")
    for i, habit in enumerate(habits, 1):
        print(f"{i}. {habit}")

def mark_done():
    show_habits()
    
    try:
        choice = int(input("Choose a habit number: "))
        
        if 1 <= choice <= len(habits):
            selected = habits[choice - 1]

            if "Physical activity" in selected:
                try:
                    minutes = int(input("How many minutes of activity? "))
                    selected = f"Physical activity ({minutes} min)"
                except ValueError:
                    print("Invalid input for minutes")
                    return

            date = datetime.now().strftime("%Y-%m-%d")

            # 🔍 Check if already done today
            try:
                with open("progress.txt", "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        if date in line and selected in line:
                            print("⚠️ You already completed this habit today!")
                            return
            except FileNotFoundError:
                pass  # file doesn't exist yet, it's fine

            # ✅ Save if not duplicate
            with open("progress.txt", "a") as file:
                file.write(f"{date} - {selected}\n")

            print("✅ Saved!")

        else:
            print("Invalid number")

    except ValueError:
        print("Please enter a number")

def main():
    while True:
        print("\n1. Show habits")
        print("2. Mark habit as done")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_habits()
        elif choice == "2":
            mark_done()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice")

main()
