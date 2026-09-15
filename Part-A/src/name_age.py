"""Ask for a user's name and age and calculate the birth year.
Input:
    Name as a string entered by the user.
    Age as an integer entered by the user. 
    

Process:
Calculate birth year by subtracting age from the current year.

Output:
Display the user's name and calculated birth year on the screen.

Typical usage example:
    What is your name? Armani
    How old are you? 21
    Hello Armani! You were born in 2005.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    birth_year = CURRENT_YEAR - age
    
    # Output personalized message with user's name and birth year.
    print(f"Hello {name}! You were born in {birth_year}.")

# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===

