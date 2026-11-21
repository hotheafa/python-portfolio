# username_policy.py
# check if a new username follows the policy rules

MIN_LENGTH = 3
MAX_LENGTH = 12


def clean(username):
    """Return username stripped of whitespace and in lowercase."""
    return username.strip().lower()


def bad_character(username):
    """Return the first character not a letter, digit, or _, or ""."""
    for bad in username:
        if not (bad.isalnum() or bad == "_"):
            return bad
    return ""


def policy_problem(username):
    """Return the first policy problem with username, or ""."""
    if len(username) > MAX_LENGTH or MIN_LENGTH > len(username):
        return "length must be 3 to 12."
    elif not (username[0].isalpha()):
        return "it must start with a letter."
    bad = bad_character(username)
    if bad != "":
        return f"the character {bad} is not allowed."
    return ""


username = input("New username: ")
username = clean(username)

if policy_problem(username) == "":
    print(f"Accepted [{username}].")
else:
    print(f"Rejected [{username}]: {policy_problem(username)}")
