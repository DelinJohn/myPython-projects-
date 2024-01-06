# create a custom exception class and raise this exception when user press one in the menu and handles this exception. 
class InvalidChoiceError(Exception):
    pass

pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}

def display_menu():
    print("            MENU ")
    for i, recipe in enumerate(recipes, start=1):
        print(f"{i}. {recipe}")
    print("__________________________")

def cook_recipe(recipe_name):
    global pantry
    try:
        if recipe_name in recipes:
            ingredients = recipes[recipe_name]
            for ingredient in ingredients:
                if ingredient in pantry and pantry[ingredient] > 0:
                    pantry[ingredient] -= 1
                else:
                    raise ValueError(f"Not enough {ingredient} in the pantry!")
            print(f"Successfully cooked {recipe_name}!")
            return True
        else:
            raise ValueError("Recipe not found!")
    except ValueError as e:
        print(f"Error: {e}")
        return False

while True:
        display_menu()
        choice = input("Enter the number of the recipe you want to cook (or 'q' to quit): ")

        if choice.lower() == 'q':
            break

        try:
            choice = int(choice)
            if choice == 1:
                raise InvalidChoiceError("Invalid choice: 'one' is not allowed.")
            elif 1 < choice <= len(recipes):
                recipe_name = list(recipes.keys())[choice - 1]
                if cook_recipe(recipe_name):
                    print("Pantry after cooking:")
                    print(pantry)
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
        except InvalidChoiceError as e:
            print(f"Error: {e}")

