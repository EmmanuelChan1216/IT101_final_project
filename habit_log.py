#HABIT LOG SYSTEM
#Python program to track daily habits
#------------------------------------------------------------#

#PSEUDOCODE
#1.) Create empty lists to hold habits and completed habits
#2.) Show a menu with 5 options
#3.) Ask the user to pick an option (1-5)
#4.) Run the matching function
#5.) Loop back to the menu until the user quits

#The Setup
#PSEUDOCODE: Create two empty lists
#1.) one to store all habit names
#2.) one to store habits completed today

habits    = []   #it stores all habit names
done_today = []  #it stores habits marked as done today

#Function - Show the menu
#PSEUDOCODE:
#1.) Print a title
#2.) Print each numbered option

def show_menu():
    print("\n_____________________________")
    print("       HABIT LOG MENU         ")
    print("_______________________________")
    print("1.) Add a new habit")
    print("2.) Mark a habit as done today")
    print("3.) View all habits")
    print("4.) Reset today's log/habits")
    print("5.) Quit!!!")
    print("_______________________________")

#Function: Add a habit 
#Ask the user to type a habit name
#If name is empty it will show error
#If name already exists it will show warning
#Otherwise it will add name to habits list

def add_habit():
    name = input("Enter habit name: ").strip()

    if name == "":
        print("Habit name cannot be empty")
    elif name in habits:
        print(f"'{name}' already exists in your list")
    else:
        habits.append(name)
        print(f"Habit '{name}' has been added")

#Function: Mark a habit as done
#If no habits it will show a message and stop
#Loop through habits and print them with a number
#Ask user to enter the number of the habit they finished
#Check that the if the input is a valid number
#Check that the number is inside the list range
#if already done it will say so
#Otherwise, add to done_today list

def mark_done():
    if len(habits) == 0:
        print("No habits found! :< Add one first! (option 1)")
        return

    print("\nYour habits:")
    for i in range(len(habits)):
        #Check if habit is in done list then show checkmark
        if habits[i] in done_today:
            status = "✓"
        else:
            status = " "
        print(f"  {i + 1}. [{status}] {habits[i]}")

    choice = input("\nEnter habit number to mark done: ").strip()

    #Check if the input is a digit
    if not choice.isdigit():
        print("Please enter a number!")
        return

    index = int(choice) - 1  #it would convert to 0 based index for ease of use for users

    #Check the number is within range
    if index < 0 or index >= len(habits):
        print("Invalid number! Try again")
    elif habits[index] in done_today:
        print(f"'{habits[index]}' Is already marked done today!")
    else:
        done_today.append(habits[index])
        print(f"'{habits[index]}' marked as done!")

#FUNCTION: View all habits
#If no habits it will say so and stop
#Loop through habits list
#If habit is in done_today then label it Done
#Otherwise, label it Not done
#Print total progress at the end
def view_habits():
    if len(habits) == 0:
        print("No habits found. add one first (option 1)")
        return

    print("\n____________________________")
    print("      TODAY'S HABIT LOG       ")
    print("____________________________")

    done_count = 0  #the couter for the completed habits

    for i in range(len(habits)):
        if habits[i] in done_today:
            status = "✓ Done     "
            done_count = done_count + 1
        else:
            status = "✗ Not done "
        print(f"  {i + 1}. {status} │ {habits[i]}")

    print("──────────────────────────────")
    print(f"  Progress: {done_count} / {len(habits)} habits done today!")
    print("______________________________")

#Function: Reset the log for today
#Clear the done_today list so all habits show as not done

def reset_log():
    done_today.clear()
    print("The log Today has been reset")

#Main loop
#Print an welcome message
#Set running = True
# While running is True:
#   Show the menu
#   Ask the user for their choice
#   If choice is 1 then call add_habit()
#   If choice is 2 then call mark_done()
#   If choice is 3 then call view_habits()
#   If choice is 4 then call reset_log()
#   If choice is 5 then set running = False (it woudl exit loop)
#Otherwise, show the "invalid" message

print("Welcome to your Habit Log System! :3")

running = True  #this controls the loop

while running:
    show_menu()
    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "1":
        add_habit()
    elif choice == "2":
        mark_done()
    elif choice == "3":
        view_habits()
    elif choice == "4":
        reset_log()
    elif choice == "5":
        print("\n Goodbye! See you next time! >:3")
        running = False
    else:
        print("Invalid choice. Please enter a number between 1 and 5")
