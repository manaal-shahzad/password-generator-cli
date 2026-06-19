import string
import random

# Function to get a valid yes/no response from the user
def get_yes_no(prompt):
    answer = ""

    # Keep asking until the user enters either "yes" or "no"
    while answer != "yes" and answer != "no":
        answer = input(prompt)
        answer = answer.lower()  # Convert input to lowercase for consistency

        if answer != "yes" and answer != "no":
            print("Error! Answer with yes/no.")

    # Return True for yes and False for no
    if answer == "yes":
        return True
    else:
        return False


# Function to evaluate the strength of a password
def strength_checker(pwd):
    score = 0

    # Check whether the password contains different character types
    has_lower = any(p.islower() for p in pwd)
    has_upper = any(p.isupper() for p in pwd)
    has_number = any(p.isdigit() for p in pwd)
    has_symbol = any(p in string.punctuation for p in pwd)

    # Award points based on password length
    if len(pwd) >= 8:
        score += 1
    if len(pwd) >= 12:
        score += 1
    if len(pwd) >= 16:
        score += 1

    # Award points for character variety
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_number:
        score += 1
    if has_symbol:
        score += 1

    # Bonus point if all four character types are present
    if has_lower and has_upper and has_number and has_symbol:
        score += 1

    # Common weak passwords/words that reduce security
    weak_words = ["password", "admin", "letmein", "qwerty", "123456"]

    # Deduct points if a weak word is found
    for word in weak_words:
        if word in pwd.lower():
            score -= 2
            break  # Penalize only once

    # Deduct a point if three consecutive identical characters exist
    # Example: aaa, 111, $$$
    for i in range(len(pwd) - 2):
        if pwd[i] == pwd[i + 1] == pwd[i + 2]:
            score -= 1
            break

    # Deduct a point for predictable number sequences
    sequences = ["012", "123", "234", "345", "456", "567", "678", "789"]

    for seq in sequences:
        if seq in pwd:
            score -= 1
            break

    # Ensure score never becomes negative
    score = max(0, score)

    # Return strength category based on final score
    if score >= 0 and score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    elif score == 5 or score == 6:
        return "Strong"
    elif score == 7:
        return "Very Strong"
    else:
        return "Excellent"


def main():

    # Display welcome banner
    print("----------Welcome!----------")

    # Main loop to allow multiple password generation sessions
    while True:

        # Get a valid password length between 8 and 64
        length = 0
        while length < 8 or length > 64:
            try:
                length = int(
                    input("Enter desired password length (must be between 8 and 64): ")
                )

                if length < 8 or length > 64:
                    print("Length of password must be between 8 and 64!")

            except ValueError:
                print("That is not a valid integer! Please try again.")

        # Ask user what character types should be included
        contain_uppercase = get_yes_no(
            "Should the password contain uppercase letters? (yes/no): "
        )
        contain_number = get_yes_no(
            "Should the password contain numbers? (yes/no): "
        )
        contain_symbol = get_yes_no(
            "Should the password contain symbols? (yes/no): "
        )

        # Start with lowercase letters as the default character pool
        pool = string.ascii_lowercase

        # Add selected character types to the pool
        if contain_uppercase:
            pool += string.ascii_uppercase

        if contain_number:
            pool += string.digits

        if contain_symbol:
            pool += string.punctuation

        # Get the number of passwords to generate (1–10)
        no_of_passwords = 0

        while no_of_passwords < 1 or no_of_passwords > 10:
            try:
                no_of_passwords = int(
                    input("Enter number of passwords to be generated: ")
                )

                if no_of_passwords < 1 or no_of_passwords > 10:
                    print("Error! Number must be between 1-10.")

            except ValueError:
                print("That is not a valid integer! Please try again.")

        # Generate and display the requested number of passwords
        for i in range(no_of_passwords):

            password = ""

            # Build password one character at a time
            for _ in range(length):
                password += random.choice(pool)

            # Display generated password along with its strength rating
            print(
                f"Password #{i + 1}: {password} - Strength: {strength_checker(password)}"
            )

        # Ask user whether they want to generate more passwords
        again = get_yes_no("Do you want to generate more passwords?: ")

        # Exit the loop if the user answers "no"
        if not again:
            break


# Program entry point
if __name__ == "__main__":
    main()