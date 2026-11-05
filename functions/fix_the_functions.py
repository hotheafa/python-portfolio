# fix_the_functions.py


def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)


def lock_minutes(failed, minutes = 15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        total = failed * minutes
        #semantic: missing return statement for the calculated total minutes inside the if block
        return total
    return 0


def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes (failed)
    return f"{username}: {failed} failed, locked {minutes} min"

#runtime: called print_header before its definition
print_header()
# runtime: fixed unexpected keyword argument 'user' by using positional arguments
print(login_line("sara",4))
## semantic: missing print function call to display omar's login line
print(login_line("omar", 1))