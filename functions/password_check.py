#password_check.py
# Description: A utility module for validating user passwords against minimum length 
# requirements and ensuring they do not match the username

def long_enough(password, minimum=8):

    """Check if the password meets or exceeds the minimum required length."""
    if len(password) >= minimum:
        return True
    return False

def differs_from_username(password, username):

    """Check if the password is different from the username."""
    if password != username:
        return True
    return False

def password_ok(password, username):

    """Evaluate the password against length and username rules and return acceptance or rejection status."""
    if (long_enough(password, minimum=8) == True) and (differs_from_username(password, username) == True):
        return "Password accepted."
    return "Password rejected."

username = input("Username: ")
password = input("Password: ")

print(password_ok(password, username))