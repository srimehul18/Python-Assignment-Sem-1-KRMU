import datetime                                                         #imports datetime for log purposes

print('Hi')
print('If you are here, then you must be health conscious — you are in the right place.')                   #introductory messages
print('This tool will help you monitor your calories.')
print("===============================================")
print(" Welcome to the Daily Calorie Tracker CLI  ")
print("===============================================")
print("Track your meals, calculate your total calories,")
print("and check if you’re within your daily calorie goal!\n")

meal_names = []                                      #creates empty lists 
calorie_values = []

while True:                                         #runs a while loop for exception handling to prevent illeagle inputs
    try:
        num_meals = int(input("How many meals do you want to enter? "))
        if num_meals < 0:
            print("Please enter a non-negative number.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter an integer.")


for i in range(num_meals):                      #prints and prompts the user to ask for meals
    print(f"\nMeal {i + 1}:")
    meal = input("Enter meal name: ").strip() or f"Meal_{i+1}"   #for clean output and prompt
    try:
        calories = float(input("Enter calories for this meal: "))
    except ValueError:                                            #again to prevent andy illeagel inputs
        print("Invalid calorie input! Please enter a number. Setting calories = 0.0 for this meal.")
        calories = 0.0

    meal_names.append(meal)                                       #appends the list and updates it
    calorie_values.append(calories)


total_calories = sum(calorie_values)                            #takes the total sum of calories
average_calories = total_calories / len(calorie_values) if calorie_values else 0.0             #calcilates the average calories

try:
    daily_limit = float(input("\nEnter your daily calorie limit: "))        #exception handling ans prompts the user to input their daily calorie goal
except ValueError:
    print("Invalid input! Setting limit to 2000 calories by default.")      #to prevent any illeagel input
    daily_limit = 2000.0

print("\n----------------------------------------------")
if total_calories > daily_limit:                                         
    print(f"WARNING: You've exceeded your daily limit by {total_calories - daily_limit:.2f} calories!")   #warns the user about excessive caloure intake
else:
    print(f"Great job! You’re within your daily calorie goal by {daily_limit - total_calories:.2f} calories.")  
print("----------------------------------------------\n")

print("Your Calorie Summary:\n")
print(f"{'Meal Name':<20}\t{'Calories'}")
print("----------------------------------------------")

for meal, cal in zip(meal_names, calorie_values):                         #combines all the values in a list and for clean output
    print(f"{meal:<20}\t{cal:.2f}")

print("----------------------------------------------")
print(f"Total:\t\t\t{total_calories:.2f}")
print(f"Average:\t\t{average_calories:.2f}\n")

save = input("Would you like to save this session to a file? (yes/no): ").strip().lower()         #asks if you want to save the log in a txt file

if save == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")          #for proper formatting in date and time
    filename = f"calorie_log_{timestamp}.txt"

    with open(filename, "w") as f:                                       #write the file
        f.write("Daily Calorie Tracker CLI - Session Log\n")
        f.write(f"Date: {datetime.datetime.now()}\n")
        f.write("----------------------------------------------\n")
        for meal, cal in zip(meal_names, calorie_values):
            f.write(f"{meal:<20}\t{cal:.2f}\n")
        f.write("----------------------------------------------\n")       #for clean output
        f.write(f"Total: {total_calories:.2f}\n")
        f.write(f"Average: {average_calories:.2f}\n")
        f.write(f"Daily Limit: {daily_limit:.2f}\n")
        if total_calories > daily_limit:
            f.write(f"Exceeded by {total_calories - daily_limit:.2f} calories\n")
        else:
            f.write(f"Within limit by {daily_limit - total_calories:.2f} calories\n")
        f.write("----------------------------------------------\n")
        f.write("End of Session\n")

    print(f"\nSession saved successfully as '{filename}'")
else:
    print("\nSession not saved. Have a healthy day!")

print ('Thankyou!')                     #Thanks the user for using the software        
