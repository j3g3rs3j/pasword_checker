def password_checker(password, secure_threshold=10**12):
    # possible characters
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ"
    digits = "0123456789"
    special = "!@#¤%&/()=?`£$€{[+"

    possible_characters = 0

    found = {
        "letters": False,
        "digits": False,
        "special": False
    }

    # Identify character sets used in the password
    for c in password:
        if c in letters:
            if not found["letters"]:
                possible_characters += len(letters)
                found["letters"] = True

        if c in digits:
            if not found["digits"]:
                possible_characters += len(digits)
                found["digits"] = True
        if c in special:
            if not found["digits"]:
                possible_characters += len(digits)
                found["digits"] = True

    # number of possible combinations
    total_combinations = possible_characters ** len(password)

    if total_combinations >= secure_threshold:
        return f"Your password is secure it has {total_combinations} possible combinations."
    else:
        return f"Your password is NOT secure it only has {total_combinations} possible combinations."

# example usage
print(password_checker("test123?"))