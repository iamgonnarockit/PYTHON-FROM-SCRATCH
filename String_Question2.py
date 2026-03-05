#Password Validator: Create a simple password validator that checks for minimum length, 
# and the presence of at least one uppercase letter, one lowercase letter, and one special character.
def is_valid_password(password):
    # define special characters you want to allow
    special_chars = "!@#$%^&*()-_+=[]{}|;:'\",.<>?/~`"

    # check minimum length
    if len(password) < 8:
        return False

    # check uppercase
    has_upper = any(c.isupper() for c in password)
    # check lowercase
    has_lower = any(c.islower() for c in password)
    # check special character
    has_special = any(c in special_chars for c in password)

    # return True only if all conditions pass
    return has_upper and has_lower and has_special

# Example usage
pw = input("Enter a password: ")
if is_valid_password(pw):
    print("✅ Password is valid!")
else:
    print("❌ Password is invalid!")